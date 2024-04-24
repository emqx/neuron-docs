# Siemens S5 FetchWrite

Fetch/Write 是一种基于 TCP/IP 的通信协议，它允许 PLC 与其他设备（如 SCADA 系统、HMI 设备、其他 PLC 等）进行数据交换。Fetch 操作用于从 PLC 读取数据，而 Write 操作用于向 PLC 写入数据。

Neuron 的 Siemens FetchWrite 插件用于带有网络扩展模块 CP443 的西门子 PLC 的访问，如，s7-300/400。

## 添加插件

在 **配置 -> 南向设备**，点击**添加设备**来创建设备节点，输入插件名称，插件类型选择 **Siemens FetchWrite** 启用插件。

## 设备配置

点击插件卡片或插件列，进入**设备配置**页。配置 Neuron 与设备建立连接所需的参数，下表为插件相关的配置项。

| 字段         | 说明                        |
| ------------ | --------------------------- |
| PLC IP地址   | 远程 PLC 的 IP              |
| **PLC 端口** | 远程 PLC 的端口，默认为 102 |

## 设置组和点位

完成插件的添加和配置后，要建立设备与 Neuron 之间的通信，首先为南向驱动程序添加组和点位。

完成设备配置后，在**南向设备**页，点击设备卡片/设备列进入**组列表**页。点击**创建**来创建组，设定组名称以及采集间隔。完成组的创建后，点击组名称进入**点位列表**页，添加需要采集的设备点位，包括点位地址，点位属性，数据类型等。

公共配置项部分可参考[连接南向设备](../south-devices.md)，本页将介绍支持的数据类型和地址格式部分。

### 数据类型

* INT8
* UINT8
* INT16
* UINT16
* INT32
* UINT32
* INT64
* UINT64
* FLOAT
* DOUBLE
* BIT
* STRING

### 地址格式

> AREA ADDRESS\[.BIT][.LEN]

#### AREA ADDRESS

| 区域 | 数据类型                                                     | 属性  | 备注                    |
| ---- | ------------------------------------------------------------ | ----- | ----------------------- |
| DB   | int16，uint16，bit，int32，uint32，int64，uint64，float，double，string | 读    | 主存数据块，以 words 读写 |
| M    | int8，uint8，int16，uint16，bit，int32，uint32，int64，uint64，float，double，string | 读/写 | 标志内存 M，以 bytes 读写  |
| I    | int8，uint8，int16，uint16，bit，int32，uint32，int64，uint64，float，double，string | 读/写 | 输入，以 bytes 读写       |
| Q    | int8，uint8，int16，uint16，bit，int32，uint32，int64，uint64，float，double，string | 读/写 | 输出，以 bytes 读写       |
| PEPA | int8，uint8，int16，uint16，bit，int32，uint32，int64，uint64，float，double，string | 读/写 | IO modules，以 bytes 读写 |
| Z    | int16，uint16，bit，int32，uint32，int64，uint64，float，double，string | 读/写 | 计数器，以 words 读写     |
| T    | int16，uint16，bit，int32，uint32，int64，uint64，float，double，string | 读/写 | 计时器，以 words 读写     |

#### .BIT

选填，指某一地址的某一位。

#### .LEN

当数据类型为 string 类型时，是必填项，表示字符串长度。

### 地址示例

| 地址         | 数据类型 | 说明                                         |
| ------------ | -------- | -------------------------------------------- |
| I0         | int16    | I 区域，地址为 0             |
| I1         | uint16   | I 区域，地址为 1             |
| Q2         | int16    | Q 区域，地址为 2             |
| Q3         | uint16   | Q 区域，地址为 3             |
| PEPA4      | int16    | PEPA 区域，地址为 4          |
| PEPA5      | int16    | PEPA 区域，地址为 5          |
| T6         | int16    | T 区域，地址为 6             |
| T7         | int16    | T 区域，地址为 7             |
| Z8         | uint16   | Z 区域，地址为 8             |
| Z9         | uint16   | Z 区域，地址为 9             |
| DB10.DBW10 | int16    | 10 数据块中，起始数据字为 10 |
| DB12.DBW10 | uint16   | 12 数据块中，起始数据字为 10 |
| DB10.DBW10 | float    | 10 数据块中，起始数据字为 10 |
| DB11.DBW10 | double   | 11 数据块中，起始数据字为 10 |
| I0.0        | bit      | I 区域，地址为0，第 0 位             |
| I0.1        | bit      | I 区域，地址为0，第 1 位             |
| Q1.0        | bit      | Q 区域，地址为1，第 0 位             |
| Q1.2        | bit      | Q 区域，地址为1，第 2 位             |
| PEPA2.1     | bit      | PEPA 区域，地址为2，第 1 位          |
| PEPA2.2     | bit      | PEPA 区域，地址为2，第 2 位          |
| T3.3        | bit      | T 区域，地址为3，第 3 位             |
| T3.4        | bit      | T 区域，地址为3，第 4 位             |
| Z4.5        | bit      | Z 区域，地址为4，第 5 位             |
| Z4.6        | bit      | Z 区域，地址为4，第 6 位             |
| DB1.DBW10.1 | bit      | 1 数据块中，起始数据字为 10，第 0 位 |
| DB2.DBW1.15 | bit      | 2 数据块中，起始数据字为 1，第 15 位 |
| DB1.DBW12.20 | string   | 1 数据块中，起始数据字为 12，字符串长度为 20 |

## 数据监控

完成点位的配置后，您可点击 **监控** -> **数据监控**查看设备信息以及反控设备，具体可参考[数据监控](../../../admin/monitoring.md)。