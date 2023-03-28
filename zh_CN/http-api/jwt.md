# 自定义 JWT

在 Neuron 中调用 API 时，需先调用登录接口生成 JWT，再调用其他接口进行 JWT 验证。默认生成的 JWT 过期时间为一小时，可以自己生成 JWT，自定义过期时间。

## 什么是 JWT？

JWT 是一种用于安全传输信息的开放标准（RFC 7519）。JWT 结构包含三个部分，分别是头部（Header）、载荷（Payload）和签名（Signature）。

Neuron 先根据 **iss** 字段查找 neuron 安装目录下的子目录 **certs** 是否包含该名称对应的 .pem 或 .pub 文件，再根据里面的字段进行校验。Neuron 中所需要的 JWT 结构如下：

```json
header
{
    "alg": "RS256",
    "typ": "JWT"
}

payload
{
    "iss": "username",
    "iat": "1679622798",
    "exp": "1679626398",
    "aud": "neuron",
    "bodyEncode": "0"
}
```

### 头部

* 令牌类型（typ）：使用 JWT
* 使用的算法（alg）：使用 RS256

### 载荷

* 签发者（iss）：根据需求自己定义，但要确保与生成的公钥文件名称一致。例如，iss 为 neuron，则需要生成 neuron.pem 的公钥文件。
* 签发时间（iat）：签发时间
* 过期时间（exp）：签发过期时间
* 受众（aud）：neuron，不能修改

## 生成公私钥

签发 JWT 前需要生成一对公私钥，并把生成的公钥 public.pem 放在 Neuron 安装目录下的子目录 **certs** 中。Neuron 自动加载 **certs** 中的文件，根据公钥解码。

:::tip
Docker 以及 deb/rpm 安装包的默认安装路径为 `/opt/neuron`。

公钥文件名称必须要与 JWT 中的签发者保持一致。
:::

使用 OpenSSL 命令行工具生成 RSA 密钥：

```bash
# 生成私钥
$ openssl genrsa -out private.key 2048
# 生成公钥
$ openssl rsa -in private.key -out public.pem -pubout
```

## 如何生成 JWT？

使用 [JWT 官网](https://jwt.io/)工具生成。在 Decoded 中填写：

* Algorithm：RS256
* Header：头部
* Payload：载荷
* Verify Signature：填写公私钥 `-----BEGIN PUBLIC KEY-----` 和 `-----BEGIN RSA PRIVATE KEY-----`。