# OPC UA Server

OPC UA（OPC Unified Architecture）是一种平台无关、与厂商无关的工业通信标准，用于在工业自动化系统中进行可靠、安全的数据交换。OPC UA 支持数据建模、事件、历史数据访问和方法调用等丰富功能，适用于从边缘设备到云端的分布式场景。

Neuron 支持将 OPC UA Server 作为北向应用，以便将南向设备的数据通过 OPC UA 服务暴露给上层系统或第三方客户端。通过 OPC UA Server，外部系统可以订阅数据变化、读取实时点位，以及下发控制命令。

## 添加应用

在**数据采集 -> 北向应用**，点击 **添加应用**，选择 **OPC UA Server** 类型来创建一个 OPC UA Server 节点。

## 应用配置

创建 OPC UA Server 应用时，可配置以下字段：

| 字段                         | 说明                                                                                                           |
| ---------------------------- | -------------------------------------------------------------------------------------------------------------- |
| **主机**                     | 指定运行 OPC UA 服务器的计算机，默认 127.0.0.1。                                                               |
| **端口号**                   | 服务器绑定的端口号，默认 4840。                                                                                |
| **安全策略**                 | 支持的安全策略列表，包括 None、Basic256Sha256、Basic256、Basic256Rsa15、Aes128_Sha256_RsaOaep。默认支持 None。 |
| **用户名密码认证**           | 启用用户名和密码认证，支持新增用户，密码更新以及用户删除。                                                     |
| **服务器端证书**             | Server 使用的证书和密钥（PEM）。                                                                               |
| **受信任的证书颁发机构证书** | 支持上传受信任的证书颁发机构的证书（PEM）。                                                                    |
| **受信任的客户端证书**       | 支持上传客户自己生成的证书（PEM）。                                                                            |

### 安全与证书

OPC UA 强烈推荐启用安全策略与消息加密来防止中间人攻击和窃听。配置要点：

- 使用强加密的安全策略（如 Basic256Sha256），客户端启用 SignAndEncrypt 模式。
- 将客户端证书加入 **受信任的客户端证书** 列表以启用双向 TLS。
- 启用用户名密码认证。

当 Neuron 首次启动 OPC UA Server 会生成自签名证书，外部客户端可能需要手动信任该证书（例如在 UA 客户端中将证书导入受信任列表）。
主动上传的客户端证书默认受信任，陌生客户端连接，证书会加入非信任列表，需要在界面进行手动信任操作。

### 命名与映射规则

Neuron 会将南向设备中的点位（tag）映射为 OPC UA 的节点（Node）。映射规则如下：

- 每个南向节点（例如 modbus1）对应一个 OPC UA 对象节点（Object）。
- 组（group）作为子对象组织在南向节点下。
- 点位（tag）映射为变量节点（Variable），变量的 DataType 根据 Neuron 中定义的数据类型映射到 OPC UA 类型（如 Double、Int32、Boolean、String 等）。

所有南向节点都位于 NeuronEX 节点之下。NodeId 遵循 `ns=1;s=[南向设备名称].[组名称].[点位名称]` 规范，例如 `ns=1;s=modbus-tcp-1.group-1.temperature`，ns=1 代表 NeuronEX 的命名空间。

## 数据类型映射


| NeuronEX     | OPC UA        |
| ------------ | ------------- |
| INT8/UINT8   | Sbyte/Byte    |
| INT16/UINT   | Int16/UInt16  |
| INT32/UINT32 | Int32/UInt32  |
| INT64/UINT64 | Int64/UInt64  |
| FLOAT        | Float         |
| DOUBLE       | Double        |
| BIT/BOOL     | Boolean       |
| STRING       | String        |
| BYTES        | ByteString    |
| ARRAY_INT8   | Array Sbyte   |
| ARRAY_UINT8  | Array Byte    |
| ARRAY_INT16  | Array Int16   |
| ARRAY_UINT16 | Array Uint16  |
| ARRAY_INT32  | Array Int32   |
| ARRAY_UINT32 | Array Uint32  |
| ARRAY_INT64  | Array Int64   |
| ARRAY_UINT64 | Array Uint64  |
| ARRAY_FLOAT  | Array Float   |
| ARRAY_DOUBLE | Array Double  |
| ARRAY_BOOL   | Array Boolean |
| Json         | String        |

