# OPC UA 连接策略

## 客户端登录方式

* 匿名方式
  
    OPC UA 服务端需要开启匿名登录选项。

    Neuron OPC UA 模块无需设置用户名/密码和证书/密钥。

* 用户名/密码方式 

    OPC UA 服务端已经创建好具备访问权限的用户名/密码。

    Neuron OPC UA 模块填写对应的用户名/密码，无需添加证书/密钥。

* 证书/密钥 + 匿名方式

    OPC UA 服务端开启合适的安全设置，添加客户端证书到信任列表，并且开启匿名登录。

    Neuron OPC UA 模块添加对应的客户端证书/密钥，无需填写用户名/密码。

* 证书/密钥 + 用户名/密码方式

    OPC UA 服务端已经创建好具备访问权限的用户名/密码，开启合适的安全设置，并添加客户端证书到信任列表。

    Neuron OPC UA 模块添加对应的用户名/密码，添加对应的客户端证书/密钥。

## 安全模式与安全策略

当使用证书认证方式连接 OPC UA 服务器时，需要在 Neuron 中配置**安全模式（Security Mode）**，并确保服务器端启用了匹配的**安全策略（Security Policy）**。

### 安全模式（Security Mode）

安全模式决定了 OPC UA 消息在传输过程中是否受到密码学保护：

| 安全模式         | 说明                                                 |
| ---------------- | ---------------------------------------------------- |
| **None**         | 无安全保护，消息以明文传输。                         |
| **Sign**         | 消息经过数字签名以确保完整性，但内容不加密。         |
| **Sign&Encrypt** | 消息同时进行签名和加密，提供完整性和机密性双重保护。 |

:::tip
生产环境中推荐使用 **Sign&Encrypt**，防止数据篡改和窃听。如果网络已在传输层做安全加固且对加密开销有顾虑，可考虑使用 **Sign** 模式。
:::

### 安全策略（Security Policy）

安全策略定义了签名和加密所使用的具体密码学算法。当 Neuron 以 **Sign** 或 **Sign&Encrypt** 模式连接服务器时，客户端和服务器会自动协商一个双方都支持的安全策略。以下是常见的安全策略：

| 安全策略                  | 对称加密算法 | 密钥交换算法 | 数字签名算法 | 状态     |
| ------------------------- | ------------ | ------------ | ------------ | -------- |
| **Basic128Rsa15**         | AES-128      | RSA-15       | SHA-1        | 已弃用   |
| **Basic256**              | AES-256      | RSA-OAEP     | SHA-1        | 已弃用   |
| **Basic256Sha256**        | AES-256      | RSA-OAEP     | SHA-256      | 推荐使用 |
| **Aes128_Sha256_RsaOaep** | AES-128      | RSA-OAEP     | SHA-256      | 推荐使用 |

:::tip
- **Basic128Rsa15** 和 **Basic256** 因使用 SHA-1 算法，在 OPC UA 规范中已被标记为弃用，新部署中应避免使用。
- 推荐使用 **Basic256Sha256** 和 **Aes128_Sha256_RsaOaep**。其中 **Basic256Sha256** 使用 AES-256 加密，提供最高的安全强度。
- 服务器必须至少启用一种与客户端兼容的安全策略。如果未找到匹配的策略，连接将失败。
:::

### 安全模式与安全策略的协同工作方式

在 Neuron 中，用户仅选择**安全模式**（`None`/`Sign`/`Sign&Encrypt`），无需也不能选择具体的安全策略。策略选择由OPC UA 驱动自动完成。

**客户端初始化：** Neuron 启动 OPC UA 连接时，会注册驱动支持的所有内置安全策略：
- None
- Basic128Rsa15
- Basic256
- Basic256Sha256
- Aes128Sha256RsaOaep
- Aes256Sha256RsaPss

然后将用户配置的安全模式（`Sign` 或 `Sign&Encrypt`）应用到客户端配置中。

:::tip
如果安全模式选择了 `Sign` 或 `Sign&Encrypt`，但没有上传证书和密钥，Neuron 会使用内置的默认证书和密钥。
:::

**连接协商（首次匹配即选中）：** 连接服务器时，流程如下：

1. Neuron 会获取服务器支持的所有端点列表，包括每个端点的 Security Mode 和 Security Policy。
2. 客户端按服务器返回的顺序逐一遍历端点。
3. 对每个端点检查两个条件：
   - 端点的 `securityMode` 必须与 Neuron 中配置的安全模式一致。
   - 端点的 `securityPolicyUri` 必须在客户端支持的策略列表中。
4. **第一个同时满足两个条件的端点即被选中**，用于后续连接。

因此，服务器端点的返回顺序实际上决定了策略优先级。例如，假设服务器按以下顺序返回端点：

```
端点1: None,     policy=None              → 安全模式不匹配（None ≠ Sign&Encrypt），跳过
端点2: Sign,     policy=Basic256Sha256    → 安全模式不匹配（Sign ≠ Sign&Encrypt），跳过
端点3: Sign&Encrypt, policy=Aes256Sha256RsaPss → 匹配！选中
端点4: Sign&Encrypt, policy=Aes128Sha256RsaOaep → 不再遍历
```

:::tip
- 如果需要使用特定的安全策略，应在服务器端配置使其端点排在 `GetEndpoints` 返回列表的前面。
- 如果找不到匹配的端点，连接将失败。请确保服务器至少有一个端点的安全模式与 Neuron 配置一致，且其安全策略在 驱动支持列表中。
:::

## 客户端证书要求

OPC UA 可通过用户自签名证书登录到 OPC UA 服务器，Certificate 和 Key 必须满足以下条件：

* CERTIFICATE 和 KEYFILE 必须同时设置；

* Certificate 必须以 X.509v3 标准生成；

* Certficate 的 SAN 字段必须包含 `URI:urn:xxx.xxx.xxx`，`xxx` 为自定义部分；

* Certificate 文件和 Key 文件必须使用 DER 格式编码。

:::tip
证书文件可以提前导入到目标服务器中并设置为信任，也可以由 Neuron 设置后自动提交再由服务端设置为信任。
:::

## 客户端证书/密钥转换

可以通过以下步骤和命令将 PEM 证书以及私钥转换为 DER 格式。

1. 将包括`-----BEGIN CERTIFICATE-----`和`-----END CERTIFICATE-----`的所有内容保存为 1.crt；

2. 将包括`-----BEGIN PRIVATE KEY-----`和`-----END PRIVATE KEY-----`的所有内容保存为 1.key；

3. 执行如下命令:

```sh
$ openssl x509 -in 1.crt -outform der -out cert.der   
$ openssl rsa -inform PEM -in 1.key -outform DER -out key.der
```

## 客户端证书/密钥生成

Windows、Linux 和 Mac OS 系统下的生成方式一致。

```sh
$ openssl req -config localhost.cnf -new -nodes -x509 -sha256 -newkey rsa:2048 -keyout localhost.key -days 365 -subj "/C=DE/O=neuron/CN=NeuronClient@localhost" -out localhost.crt
$ openssl x509 -in localhost.crt -outform der -out client_cert.der
openssl rsa -inform PEM -in localhost.key -outform DER -out client_key.der
$ rm localhost.crt
$ rm localhost.key
```

`-days` 可以根据需要设置数值。

`-config` 指定的 *.cnf 文件可以使用下一节的文件附件 `localhost.cnf` 进行修改，需包含如下配置节：

```sh
[ v3_req ]

# Extensions to add to a certificate request

basicConstraints = CA:FALSE
keyUsage = nonRepudiation, digitalSignature, keyEncipherment
subjectAltName = @alt_names

[ alt_names ]
URI.1 = urn:xxx.xxx.xxx
DNS.1 = localhost
#DNS.2 = localhost
IP.1 = 127.0.0.1
#IP.2 = 0.0.0.0
```

## 服务器端配置

当 Neuron 使用 **Sign** 或 **Sign&Encrypt** 模式时，OPC UA 服务器端必须进行以下配置：
1. 启用所需的安全策略。
2. 信任上传至 Neuron 的客户端证书。

以下以常用的工业 OPC UA 服务器为例，介绍具体配置步骤。

### 通用配置原则

1. 使用 OpenSSL **生成客户端证书并上传至 Neuron**（参考[客户端证书/密钥生成](#客户端证书密钥生成)）。
2. 在目标服务器上**启用安全策略** — 至少启用 **Basic256Sha256** 或 **Aes128_Sha256_RsaOaep**。
3. 将客户端证书（DER 格式）**导入服务器**的受信任客户端列表。
4. **重启服务器**或重新初始化 OPC UA 服务以使配置生效。

### 示例：西门子 S7-1200（TIA Portal）

通过 TIA Portal 配置 S7-1200 内置 OPC UA 服务器：

1. 在 TIA Portal 中选择目标 PLC，右键打开 **属性 -> 常规 -> OPC UA -> 服务器**。
2. 在 **安全性 -> 服务器可用的安全策略** 列表中，勾选所需的安全策略：
   - 勾选 **Basic256Sha256**（推荐）或其他需要使用的策略。
3. 在 **受信任的客户端** 区域，配置客户端证书信任：
   - 勾选 **在运行期间自动接受客户端证书**（便于初始调试），或
   - 通过证书管理器手动导入客户端证书。
4. 关闭**访客认证**，如需使用用户名/密码登录，则启用**用户名和密码认证**。
5. 编译并下载硬件配置到 PLC。

更多 S7-1200 配置细节，请参考 [连接西门子 S7-1200](./s71200.md)。

### 示例：KEPServerEX

在 KEPServerEX 中配置 OPC UA 服务器安全策略：

1. 右键单击系统托盘中的 KEPServerEX 图标，选择 **OPC UA 配置 -> 服务器端点**。
2. 双击端点条目（如 `opc.tcp://localhost:49320`）。
3. 在 **安全策略** 区域，勾选所需策略：
   - 勾选 **Basic256Sha256**（推荐）。
4. 点击**确定**保存端点配置。
5. 客户端证书上传至 Neuron 后，右键点击 KEPServerEX 图标，选择 **OPC UA 配置 -> 受信任的客户端**。
6. 点击**导入**，浏览选择 Neuron 客户端证书文件（DER 格式），将其添加到信任列表。
7. 右键点击 KEPServerEX 图标，选择**重新初始化**使配置生效。

更多 KEPServerEX 配置细节，请参考 [连接 KEPServerEX](./kepserverex.md)。

## 文件附件 localhost.cnf

以下为 OpenSSL 配置文件示例，其中定义了用于一些用于生成证书请求、证书签发、时间戳颁发者（TSA）、证书吊销列表（CRL）等操作的参数。

```sh
#
# OpenSSL example configuration file.
# This is mostly being used for generation of certificate requests.
#

# This definition stops the following lines choking if HOME isn't
# defined.
HOME			= .
RANDFILE		= $ENV::HOME/.rnd

# Extra OBJECT IDENTIFIER info:
#oid_file		= $ENV::HOME/.oid
oid_section		= new_oids

# To use this configuration file with the "-extfile" option of the
# "openssl x509" utility, name here the section containing the
# X.509v3 extensions to use:
# extensions		= 
# (Alternatively, use a configuration file that has only
# X.509v3 extensions in its main [= default] section.)

[ new_oids ]

# We can add new OIDs in here for use by 'ca', 'req' and 'ts'.
# Add a simple OID like this:
# testoid1=1.2.3.4
# Or use config file substitution like this:
# testoid2=${testoid1}.5.6

# Policies used by the TSA examples.
tsa_policy1 = 1.2.3.4.1
tsa_policy2 = 1.2.3.4.5.6
tsa_policy3 = 1.2.3.4.5.7

####################################################################
[ ca ]
default_ca	= CA_default		# The default ca section

####################################################################
[ CA_default ]

dir		= ./ca/			# Where everything is kept
certs		= $dir/certs		# Where the issued certs are kept
crl_dir		= $dir/crl		# Where the issued crl are kept
database	= $dir/database.txt	# database index file.
#unique_subject	= no			# Set to 'no' to allow creation of
					# several ctificates with same subject.
new_certs_dir	= $dir/newcerts		# default place for new certs.

certificate	= $dir/ca.crt	 	# The CA certificate
serial		= $dir/serial 		# The current serial number
crlnumber	= $dir/crlnumber	# the current crl number
					# must be commented out to leave a V1 CRL
crl		= $dir/crl.pem 		# The current CRL
private_key	= $dir/ca.key 		# The private key
RANDFILE	= $dir/.rand		# private random number file

x509_extensions	= usr_cert		# The extensions to add to the cert

# Comment out the following two lines for the "traditional"
# (and highly broken) format.
name_opt 	= ca_default		# Subject Name options
cert_opt 	= ca_default		# Certificate field options

# Extension copying option: use with caution.
# copy_extensions = copy

# Extensions to add to a CRL. Note: Netscape communicator chokes on V2 CRLs
# so this is commented out by default to leave a V1 CRL.
# crlnumber must also be commented out to leave a V1 CRL.
crl_extensions	= crl_ext

default_days	= 365			# how long to certify for
default_crl_days= 30			# how long before next CRL
default_md	= default		# use public key default MD
preserve	= no			# keep passed DN ordering

# A few difference way of specifying how similar the request should look
# For type CA, the listed attributes must be the same, and the optional
# and supplied fields are just that :-)
policy		= policy_match

# For the CA policy
[ policy_match ]
countryName		= match
stateOrProvinceName	= match
organizationName	= match
organizationalUnitName	= optional
commonName		= supplied
emailAddress		= optional

# For the 'anything' policy
# At this point in time, you must list all acceptable 'object'
# types.
[ policy_anything ]
countryName		= optional
stateOrProvinceName	= optional
localityName		= optional
organizationName	= optional
organizationalUnitName	= optional
commonName		= supplied
emailAddress		= optional

####################################################################
[ req ]
default_bits		= 2048
default_keyfile 	= privkey.pem
distinguished_name	= req_distinguished_name
attributes		= req_attributes
x509_extensions	= v3_ca	# The extensions to add to the self signed cert

# Passwords for private keys if not present they will be prompted for
# input_password = secret
# output_password = secret

# This sets a mask for permitted string types. There are several options. 
# default: PrintableString, T61String, BMPString.
# pkix	 : PrintableString, BMPString (PKIX recommendation before 2004)
# utf8only: only UTF8Strings (PKIX recommendation after 2004).
# nombstr : PrintableString, T61String (no BMPStrings or UTF8Strings).
# MASK:XXXX a literal mask value.
# WARNING: ancient versions of Netscape crash on BMPStrings or UTF8Strings.
string_mask = utf8only

req_extensions = v3_req # The extensions to add to a certificate request

[ req_distinguished_name ]
countryName			= Country Name (2 letter code)
countryName_default		= AU
countryName_min			= 2
countryName_max			= 2

stateOrProvinceName		= State or Province Name (full name)
stateOrProvinceName_default	= Some-State

localityName			= Locality Name (eg, city)

0.organizationName		= Organization Name (eg, company)
0.organizationName_default	= Internet Widgits Pty Ltd

# we can do this but it is not needed normally :-)
#1.organizationName		= Second Organization Name (eg, company)
#1.organizationName_default	= World Wide Web Pty Ltd

organizationalUnitName		= Organizational Unit Name (eg, section)
#organizationalUnitName_default	=

commonName			= Common Name (e.g. server FQDN or YOUR name)
commonName_max			= 64

emailAddress			= Email Address
emailAddress_max		= 64

# SET-ex3			= SET extension number 3

[ req_attributes ]
challengePassword		= A challenge password
challengePassword_min		= 4
challengePassword_max		= 20

unstructuredName		= An optional company name

[ usr_cert ]

# These extensions are added when 'ca' signs a request.

# This goes against PKIX guidelines but some CAs do it and some software
# requires this to avoid interpreting an end user certificate as a CA.

basicConstraints=CA:FALSE

# Here are some examples of the usage of nsCertType. If it is omitted
# the certificate can be used for anything *except* object signing.

# This is OK for an SSL server.
# nsCertType			= server

# For an object signing certificate this would be used.
# nsCertType = objsign

# For normal client use this is typical
# nsCertType = client, email

# and for everything including object signing:
# nsCertType = client, email, objsign

# This is typical in keyUsage for a client certificate.
# keyUsage = nonRepudiation, digitalSignature, keyEncipherment

# This will be displayed in Netscape's comment listbox.
nsComment			= "OpenSSL Generated Certificate"

# PKIX recommendations harmless if included in all certificates.
subjectKeyIdentifier=hash
authorityKeyIdentifier=keyid,issuer

# This stuff is for subjectAltName and issuerAltname.
# Import the email address.
# subjectAltName=email:copy
# An alternative to produce certificates that aren't
# deprecated according to PKIX.
# subjectAltName=email:move

# Copy subject details
# issuerAltName=issuer:copy

#nsCaRevocationUrl		= http://www.domain.dom/ca-crl.pem
#nsBaseUrl
#nsRevocationUrl
#nsRenewalUrl
#nsCaPolicyUrl
#nsSslServerName

# This is required for TSA certificates.
extendedKeyUsage = critical,timeStamping

[ v3_req ]

# Extensions to add to a certificate request

basicConstraints = CA:FALSE
keyUsage = nonRepudiation, digitalSignature, keyEncipherment
subjectAltName = @alt_names

[ alt_names ]
URI.1 = urn:neuron.client.application
DNS.1 = localhost
#DNS.2 = localhost
IP.1 = 127.0.0.1
#IP.2 = 0.0.0.0

[ v3_ca ]


# Extensions for a typical CA


# PKIX recommendation.

subjectKeyIdentifier=hash

authorityKeyIdentifier=keyid:always,issuer

# This is what PKIX recommends but some broken software chokes on critical
# extensions.
#basicConstraints = critical,CA:true
# So we do this instead.
basicConstraints = CA:false

# Key usage: this is typical for a CA certificate. However since it will
# prevent it being used as an test self-signed certificate it is best
# left out by default.
# keyUsage = cRLSign, keyCertSign

keyUsage = nonRepudiation, digitalSignature, keyEncipherment, dataEncipherment, keyCertSign
extendedKeyUsage = TLS Web Server Authentication, TLS Web Client Authentication

# Some might want this also
# nsCertType = sslCA, emailCA

# Include email address in subject alt name: another PKIX recommendation
# subjectAltName=email:copy
# Copy issuer details
# issuerAltName=issuer:copy

# DER hex encoding of an extension: beware experts only!
# obj=DER:02:03
# Where 'obj' is a standard or added object
# You can even override a supported extension:
# basicConstraints= critical, DER:30:03:01:01:FF

subjectAltName         = @alt_names

[ crl_ext ]

# CRL extensions.
# Only issuerAltName and authorityKeyIdentifier make any sense in a CRL.

# issuerAltName=issuer:copy
authorityKeyIdentifier=keyid:always

[ proxy_cert_ext ]
# These extensions should be added when creating a proxy certificate

# This goes against PKIX guidelines but some CAs do it and some software
# requires this to avoid interpreting an end user certificate as a CA.

basicConstraints=CA:FALSE

# Here are some examples of the usage of nsCertType. If it is omitted
# the certificate can be used for anything *except* object signing.

# This is OK for an SSL server.
# nsCertType			= server

# For an object signing certificate this would be used.
# nsCertType = objsign

# For normal client use this is typical
# nsCertType = client, email

# and for everything including object signing:
# nsCertType = client, email, objsign

# This is typical in keyUsage for a client certificate.
# keyUsage = nonRepudiation, digitalSignature, keyEncipherment

# This will be displayed in Netscape's comment listbox.
nsComment			= "OpenSSL Generated Certificate"

# PKIX recommendations harmless if included in all certificates.
subjectKeyIdentifier=hash
authorityKeyIdentifier=keyid,issuer

# This stuff is for subjectAltName and issuerAltname.
# Import the email address.
# subjectAltName=email:copy
# An alternative to produce certificates that aren't
# deprecated according to PKIX.
# subjectAltName=email:move

# Copy subject details
# issuerAltName=issuer:copy

#nsCaRevocationUrl		= http://www.domain.dom/ca-crl.pem
#nsBaseUrl
#nsRevocationUrl
#nsRenewalUrl
#nsCaPolicyUrl
#nsSslServerName

# This really needs to be in place for it to be a proxy certificate.
proxyCertInfo=critical,language:id-ppl-anyLanguage,pathlen:3,policy:foo

####################################################################
[ tsa ]

default_tsa = tsa_config1	# the default TSA section

[ tsa_config1 ]

# These are used by the TSA reply generation only.
dir		= ./demoCA		# TSA root directory
serial		= $dir/tsaserial	# The current serial number (mandatory)
crypto_device	= builtin		# OpenSSL engine to use for signing
signer_cert	= $dir/tsacert.pem 	# The TSA signing certificate
					# (optional)
certs		= $dir/cacert.pem	# Certificate chain to include in reply
					# (optional)
signer_key	= $dir/private/tsakey.pem # The TSA private key (optional)

default_policy	= tsa_policy1		# Policy if request did not specify it
					# (optional)
other_policies	= tsa_policy2, tsa_policy3	# acceptable policies (optional)
digests		= md5, sha1		# Acceptable message digests (mandatory)
accuracy	= secs:1, millisecs:500, microsecs:100	# (optional)
clock_precision_digits  = 0	# number of digits after dot. (optional)
ordering		= yes	# Is ordering defined for timestamps?
				# (optional, default: no)
tsa_name		= yes	# Must the TSA name be included in the reply?
				# (optional, default: no)
ess_cert_id_chain	= no	# Must the ESS cert id chain be included?
				# (optional, default: no)

```
