# OPC UA 介绍及使用

## 模块描述

OPC UA 是一种面向工业自动化的机器到机器通信协议，由 OPC 基金会开发。OPC UA 提供一种标准化的方式，使不同的设备和系统能够互相通信。

opc-ua 模块可用于访问 KEPServerEX、IGS、Prosys Simulation Server、Server_ctt 等 OPCUA 服务器，也可以直接访问一些设备。

## 参数配置

| 字段               | 说明                        |
| ----------------- | --------------------------- |
| **endpoint url**  | 远程访问 PLC 的地址，默认值是`opc.tcp://127.0.0.1:4840/` |
| **username**      | 连接到 PLC 时，使用的用户名     |
| **password**      | 连接到 PLC 时，使用的密码       |
| **cert**          | 提供登录用户认证的证书          |
| **key**           | 私钥文件，用于提供签名和加密传输  |

### 认证方式

* anonymos，需要 OPCUA 服务端开启匿名登录；
* username-password，需要 OPCUA 服务端已经创建好具备访问权限的 username，Neuron 自动会匹配 OPCUA 服务端的安全设置并尝试登录；
* cert-key + anonymos，需要 OPCUA 服务端开启合适的安全设置并设置证书，并且**开启匿名登录**；
* cert-key + username-password，需要 OPCUA 服务端已经创建好具备访问权限的username，并开启合适的安全设置并设置证书；

### 证书要求

OPCUA 可通过用户自签名证书登录到 OPC-UA 服务器，certificate 和 key 必须满足以下条件：

* CERTIFICATE 和 KEYFILE 必须同时设置；
* Certificate 必须以 X.509v3 标准生成；
* Certficate 的 SAN 字段必须包含 `URI:urn:xxx.xxx.xxx`，`xxx` 为自定义部分；
* Certificate 文件和 Key 文件必须使用 DER 格式编码；

:::tip
证书文件可以提前导入到目标服务器中并设置为信任，也可以由 neuron 设置后自动提交再由服务端设置为信任。

老版本的 kepware 或者 IGS 可能需要手动导入证书。
:::

### 证书生成步骤（Windows/Linux/Mac）

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

### 证书转换

可以通过以下步骤和命令将 PEM 证书以及私钥转换为 DER 格式。

第一步，将包括`-----BEGIN CERTIFICATE-----`和`-----END CERTIFICATE-----`的所有内容保存为 1.crt；</br>
第二步，将包括`-----BEGIN PRIVATE KEY-----`和`-----END PRIVATE KEY-----`的所有内容保存为 1.key；</br>
第三步，执行如下命令:

```sh
$ openssl x509 -in 1.crt -outform der -out cert.der   
$ openssl rsa -inform PEM -in 1.key -outform DER -out key.der
```

## 支持的数据类型

* INT8（用于表示 SBYTE 类型）
* INT16
* INT32
* INT64
* UINT8（用于表示 BYTE 类型）
* UINT16
* UINT32（同时用于表示 DATETIME 类型）
* UINT64
* FLOAT
* DOUBLE
* BOOL
* STRING

## 地址格式用法

### 地址格式

> IX!NODEID</span>

**IX** 名字空间索引。

**NODEID** 节点 ID，可以设置为数字形式或者字符串形式。

### 地址示例

| 地址                   | 数据类型 | 说明                                                         |
| ---------------------- | -------- | ------------------------------------------------------------ |
| 0!2258                 | UINT32   | 使用数字类型的 NODEID，获取 OPCUA 服务器的时间戳；NS 为0，NODEID 为2258 |
| 2!Device1.Module1.Tag1 | INT8     | 使用字符串类型的 NODEID，获取类型为 SBYTE 的数据点；NS 为2，NODEID 为 Device1.Module1.Tag1 |

可以使用 UaExpert 软件协助查看所需点位的名字空间和节点 ID 信息。

:::tip
关于命名空间索引和节点 ID 的解释，请参考 OPC UA 标准。

Neuron 设置的数据类型必须与 OPCUA 数据类型相匹配。
:::