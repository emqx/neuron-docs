# 参数示例

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

    OPC UA 服务端已经创建好具备访问权限的用户名/密码，开启合适的安全设置，并添加客户端证书到信任列表；

    Neuron OPC UA 模块添加对应的用户名/密码，添加对应的客户端证书/密钥。

## 客户端证书要求

OPC UA 可通过用户自签名证书登录到 OPC UA 服务器，Certificate 和 Key 必须满足以下条件：

* CERTIFICATE 和 KEYFILE 必须同时设置；

* Certificate 必须以 X.509v3 标准生成；

* Certficate 的 SAN 字段必须包含 `URI:urn:xxx.xxx.xxx`，`xxx` 为自定义部分；

* Certificate 文件和 Key 文件必须使用 DER 格式编码；

:::tip
证书文件可以提前导入到目标服务器中并设置为信任，也可以由 Neuron 设置后自动提交再由服务端设置为信任。
:::

## 客户端证书/密钥转换

可以通过以下步骤和命令将 PEM 证书以及私钥转换为 DER 格式。

1. 将包括`-----BEGIN CERTIFICATE-----`和`-----END CERTIFICATE-----`的所有内容保存为 1.crt；</br>

2. 将包括`-----BEGIN PRIVATE KEY-----`和`-----END PRIVATE KEY-----`的所有内容保存为 1.key；</br>

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

`-config` 指定的 *.cnf 文件可以使用 [openssl 的模版文件](https://github.com/openssl/openssl/blob/master/apps/openssl.cnf) 进行修改，需包含如下配置节：

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
