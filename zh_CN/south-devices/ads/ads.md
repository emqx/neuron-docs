# 概览

[TwinCAT] 是由 Beckhoff Automation 开发的一种控制技术。
它是一种基于软件的控制系统，用于自动化和控制应用。
TwinCAT 能够运行在多种平台上并支持多种编程语言。

Neuron ADS 插件使用户可以通过 TCP/IP 连接到 Beckhoff TwinCAT PLC 。

## ADS 协议

[ADS] (Automation Device Specification) 是 TwinCAT 的通讯协议。
它使得 TwinCAT 系统能够通过媒介独立的串行或网络连接，实现数据的交换和控制。
ADS 旨在为 TwinCAT 系统中控制器与用户界面之间的通信提供标准接口。

### AMS Net ID

[AMS Net ID] 是 TwinCAT 网络中本地计算机的地址。它由6个字节组成，用点分十进制表示（例如： “1.2.3.4.5.6”） 。
为避免通信冲突，AMS Net ID 在 TwinCAT 网络中必须是唯一的。
默认情况下，TwinCAT 通过在系统的 IP 地址后附加 “.1.1” 来生成 AMS Net ID 。
例如，在IP地址为 “172.17.213.60” 的系统中， 默认生成的 AMS Net ID 将为 “172.17.213.60.1.1” 。

### AMS port

TwinCAT 网络中的 ADS 设备由 AMS Net ID 和 [AMS port] 标识。
每个 TwinCAT 系统通常为特定的目的使用特定的 AMS port 。
例如，port 801 用于系统通信，port 851 用于事件通知。

### Index group/offset

ADS [index group 和 index offset] 是 TwinCAT ADS 系统服务中用于设备或程序之间进行数据交换的规范。
所有的读取和写入操作都通过 index group 和 index offset 在 PLC 上进行。
Index offset 是16位的，index offset 是32位的。
Index group 用于指定正在访问的数据的类别或类型，而 index offset 指定该类别或类型中的特定数据元素。

## 参数设置

| 字段            | 说明                                                         |
| --------------- | ------------------------------------------------------------ |
| host            | 远程设备 IP 。                                               |
| port            | 远程设备 TCP 端口（默认 48898） 。                           |
| src-ams-net-id  | 运行 Neuron 的设备的 AMS Net ID 。                           |
| src-ads-port    | 运行 Neuron 的设备的 AMS Port 。                             |
| dst-ams-net-id  | 目标 PLC 的 AMS Net ID 。                                    |
| dst-ads-port    | 目标 PLC 的 AMS Port 。                                      |

请注意，为了让 Neuron 能与 TwinCAT PLC 正常通信，需要在目标 TwinCAT 软件中添加和设置对应的 ADS 路由。

## 支持的数据类型

* BOOL
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
* STRING

## 地址格式

对 ADS 插件来说，一个点位地址由 INDEX_GROUP 和 INDEX_OFFSET 两个部分组成，分别表示 index group 和 index offset 。

> INDEX_GROUP,INDEX_OFFSET

`INDEX_GROUP` 和 `INDEX_OFFSET` 可以分别使用十进制或十六进制指定。

### 地址示例

| 地址            | 数据类型           | 说明                        |
| --------------- | ------------------ | --------------------------------------------------------- |
| 0x4040,0x7d01c  | bool               | index_group 0x4040, index_offset 0x7d01c                  |
| 16448,51029     | uint8              | index_group 0x4040, index_offset 0x7d01d                  |
| 0x4040,512896.5 | string             | index_group 0x4040, index_offset 0x7d380, 字符串长度为 5  |

[TwinCAT]: https://www.beckhoff.com/en-us/products/automation/twincat/
[ADS]: https://infosys.beckhoff.com/english.php?content=../content/1033/tcadscommon/12440276875.html
[AMS Net ID]: https://infosys.beckhoff.com/english.php?content=../content/1033/tc3_userinterface/3813966475.html
[AMS port]: https://infosys.beckhoff.com/english.php?content=../content/1033/tcplclib_tc2_system/31064331.html
[index group 和 index offset]: https://infosys.beckhoff.com/english.php?content=../content/1033/tcadscommon/12495372427.html
