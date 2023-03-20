# OPC UA 介绍及使用

## 模块描述

OPC UA 是一种面向工业自动化的机器到机器通信协议，由 OPC 基金会开发维护。OPC UA 提供一种标准化的方式， 使不同的设备和系统能够互相通信。

OPC UA 模块可用于访问 KEPServerEX、Industrial Gateway OPC Server、Prosys Simulation Server、Ignition 等 OPC UA 服务器， 也可以直接访问硬件设备的内置 OPC UA Server， 如 西门子 S7-1200 型 PLC 的内置 Server。

## 参数配置

| 字段               | 说明                        |
| ----------------- | --------------------------- |
| **端点 URL**      | 必选字段， 目标 OPC UA Server 的 URL，默认值是`opc.tcp://127.0.0.1:4840/` |
| **用户名**        | 可选字段， 连接目标 OPC UA Server 使用的用户名     |
| **密码**          | 可选字段， 连接目标 OPC UA Server 使用的密码       |
| **证书**          | 可选字段， DER 格式的客户端证书          |
| **密钥**          | 可选字段， DER 格式的客户端密钥   |

### OPC UA 服务器认证方式

* 匿名方式：需要 OPCUA 服务端开启匿名登录；
* 用户名/密码方式：需要 OPCUA 服务端已经创建好具备访问权限的用户名，Neuron 自动会匹配 OPC UA 服务端的安全设置并尝试登录；
* 证书/密钥 + 匿名方式：需要 OPCUA 服务端开启合适的安全设置并设置客户端证书，并且**开启匿名登录**；
* 证书/密钥 + 用户名/密码方式：需要 OPC UA 服务端已经创建好具备访问权限的用户名，并开启合适的安全设置并设置客户端证书；

### OPC UA 客户端证书要求

OPC UA 可通过用户自签名证书登录到 OPC UA 服务器，Certificate 和 Key 必须满足以下条件：
* CERTIFICATE 和 KEYFILE 必须同时设置；
* Certificate 必须以 X.509v3 标准生成；
* Certficate 的 SAN 字段必须包含 `URI:urn:xxx.xxx.xxx`，`xxx` 为自定义部分；
* Certificate 文件和 Key 文件必须使用 DER 格式编码；

:::tip
证书文件可以提前导入到目标服务器中并设置为信任，也可以由 Neuron 设置后自动提交再由服务端设置为信任。

老版本的 KepServer 或者 Industrial Gateway OPC Server 可能需要手动导入证书，并设置为信任。
:::

### 客户端证书/密钥生成步骤（Windows/Linux/Mac）

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

### 客户端证书/密钥转换

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
| 0!2258                 | UINT32   | 使用数字类型的 NODEID，获取 OPC UA 服务器的时间戳；NS 为0，NODEID 为2258 |
| 2!Device1.Module1.Tag1 | INT8     | 使用字符串类型的 NODEID，获取类型为 SBYTE 的数据点；NS 为2，NODEID 为 Device1.Module1.Tag1 |

可以使用 UaExpert 软件协助查看所需点位的名字空间和节点 ID 信息。

:::tip
关于命名空间索引和节点 ID 的解释，请参考 OPC UA 标准。

Neuron 设置的数据类型必须与 OPC UA 数据类型相匹配。
:::