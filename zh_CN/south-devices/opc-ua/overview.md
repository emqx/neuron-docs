# 概览

OPC UA 是一种面向工业自动化的机器到机器通信协议，由 OPC 基金会开发维护。OPC UA 提供一种标准化的方式， 使不同的设备和系统能够互相通信。

Neuron OPC UA 插件可作为客户端访问 KEPServerEX、Industrial Gateway OPC Server、Prosys Simulation Server、Ignition 等 OPC UA 服务器。 也可以直接访问硬件设备的内置 OPC UA Server， 如：西门子 S7-1200 型 PLC 的内置 Server、 欧姆龙 NJ 系列 PLC 的内置 Server 等。

## 参数

|  参数              | 说明                        |
| ----------------- | --------------------------- |
| **端点 URL**      | 目标 OPC UA Server 的 URL，默认值是`opc.tcp://127.0.0.1:4840/` |
| **用户名**        | 连接目标 OPC UA Server 使用的用户名     |
| **密码**          | 连接目标 OPC UA Server 使用的密码       |
| **证书**          | DER 格式的客户端证书          |
| **密钥**          | DER 格式的客户端密钥   |

## 数据类型

* INT8（用于表示 OPC UA SBYTE 类型）
* INT16
* INT32
* INT64
* UINT8（用于表示 OPC UA BYTE 类型）
* UINT16
* UINT32（同时用于表示 OPC UA DATETIME 类型）
* UINT64
* FLOAT
* DOUBLE
* BOOL
* STRING

## 地址格式

> NS!NODEID

**NS** 名字空间索引。

**NODEID** 节点 ID，可以设置为数字形式或者字符串形式。

## 地址示例

| 地址                   | 数据类型 | 说明                                                         |
| ---------------------- | -------- | ------------------------------------------------------------ |
| 0!2258                 | UINT32   | 使用数字类型的 NODEID，获取 OPC UA 服务器的时间戳；NS 为0，NODEID 为2258 |
| 2!Device1.Module1.Tag1 | INT8     | 使用字符串类型的 NODEID，获取类型为 SBYTE 的数据点；NS 为2，NODEID 为 Device1.Module1.Tag1 |

可以使用 UaExpert 软件协助查看所需点位的名字空间索引和节点 ID 信息。

:::tip
关于命名空间索引和节点 ID 的解释，请参考 OPC UA 标准。

Neuron 设置的数据类型必须与 OPC UA 数据类型相匹配。
:::
