# Beckhoff ADS

[TwinCAT] 是由 Beckhoff Automation 开发的一种控制技术。它是一种基于软件的控制系统，用于自动化和控制应用。TwinCAT 能够运行在多种平台上并支持多种编程语言。

Neuron Beckhoff ADS 插件使用户可以通过 TCP/IP 连接到 Beckhoff TwinCAT PLC。

## 添加插件

在 **配置 -> 南向设备**，点击**添加设备**来创建设备节点，输入插件名称，插件类型选择 **Beckhoff ADS** 启用插件。

## 设备配置

点击插件卡片或插件列，进入**设备配置**页。配置 Neuron 与设备建立连接所需的参数，下表为插件相关的配置项。

| 字段             | 说明                                         |
| ---------------- | -------------------------------------------- |
| 设备 IP 地址     | 远程设备 IP。                                |
| 设备端口         | 远程设备 TCP 端口（默认 48898）。            |
| 源 AdsAmsNetId   | 运行 Neuron 的设备的 AMS Net ID。            |
| 源 AdsPortNr     | 运行 Neuron 的设备的 AMS Port （默认 851）。 |
| 目标 AdsAmsNetId | 目标 PLC 的 AMS Net ID。                     |
| 目标 AdsPortNr   | 目标 PLC 的 AMS Port（默认 851）。           |

请注意，为了让 Neuron 能与 TwinCAT PLC 正常通信，需要在目标 TwinCAT 软件中添加和设置对应的 ADS 路由。

其中涉及的关键 ADS 概念如下：

| 概念               | 说明                                                         |
| ------------------ | ------------------------------------------------------------ |
| ADS 协议           | [ADS] (Automation Device Specification) 是 TwinCAT 的通讯协议。<br />它使得 TwinCAT 系统能够通过媒介独立的串行或网络连接，实现数据的交换和控制。<br />ADS 旨在为 TwinCAT 系统中控制器与用户界面之间的通信提供标准接口。 |
| AMS Net ID         | [AMS Net ID] 是 TwinCAT 网络中本地计算机的地址。它由6个字节组成，用点分十进制表示（例如： “1.2.3.4.5.6”） 。<br />为避免通信冲突，AMS Net ID 在 TwinCAT 网络中必须是唯一的。<br />默认情况下，TwinCAT 通过在系统的 IP 地址后附加 “.1.1” 来生成 AMS Net ID 。<br />例如，在 IP 地址为 “172.17.213.60” 的系统中， 默认生成的 AMS Net ID 将为 “172.17.213.60.1.1” 。 |
| AMS port           | TwinCAT 网络中的 ADS 设备由 AMS Net ID 和 [AMS port] 标识。<br />每个 TwinCAT 系统通常为特定的目的使用特定的 AMS Port 。<br />例如，Port 801 用于系统通信，Port 851 用于事件通知。 |
| Index group/offset | ADS [index group 和 index offset] 是 TwinCAT ADS 系统服务中用于设备或程序之间进行数据交换的规范。<br />所有的读取和写入操作都通过 index group 和 index offset 在 PLC 上进行。<br />Index offset 是16位的，index offset 是32位的。<br />Index group 用于指定正在访问的数据的类别或类型，而 index offset 指定该类别或类型中的特定数据元素。 |

## 设置组和点位

完成插件的添加和配置后，要建立设备与 Neuron 之间的通信，首先为南向驱动程序添加组和点位。

完成设备配置后，在**南向设备**页，点击设备卡片/设备列进入**组列表**页。点击**创建**来创建组，设定组名称以及采集间隔。完成组的创建后，点击组名称进入**点位列表**页，添加需要采集的设备点位，包括点位地址，点位属性，数据类型等。

公共配置项部分可参考[连接南向设备](../south-devices.md)，本页将介绍支持的数据类型和地址格式部分。

### 数据类型

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

### 地址格式

对 ADS 插件来说，一个点位地址由 INDEX_GROUP 和 INDEX_OFFSET 两个部分组成，分别表示 index group 和 index offset 。

> INDEX_GROUP,INDEX_OFFSET</span>

`INDEX_GROUP` 和 `INDEX_OFFSET` 可以分别使用十进制或十六进制指定。

### 地址示例

| 地址            | 数据类型           | 说明                        |
| --------------- | ------------------ | --------------------------------------------------------- |
| 0x4040,0x7d01c  | bool               | index_group 0x4040, index_offset 0x7d01c                  |
| 16448,51029     | uint8              | index_group 0x4040, index_offset 0x7d01d                  |
| 0x4040,512896.5 | string             | index_group 0x4040, index_offset 0x7d380, 字符串长度为 5  |

## 应用场景

您可通过 Neuron 通过 ADS 协议采集倍福 PLC 上不同地址区域的数据，具体步骤，见[采集 PLC 数据（Beckhoff ADS 协议）](./plc-ads/ads.md)。

## 数据监控

完成点位的配置后，您可点击 **监控** -> **数据监控**查看设备信息以及反控设备，具体可参考[数据监控](../../../usage/monitoring.md)。


[TwinCAT]: https://www.beckhoff.com/en-us/products/automation/twincat/
[ADS]: https://infosys.beckhoff.com/english.php?content=../content/1033/tcadscommon/12440276875.html
[AMS Net ID]: https://infosys.beckhoff.com/english.php?content=../content/1033/tc3_userinterface/3813966475.html
[AMS port]: https://infosys.beckhoff.com/english.php?content=../content/1033/tcplclib_tc2_system/31064331.html
[index group 和 index offset]: https://infosys.beckhoff.com/english.php?content=../content/1033/tcadscommon/12495372427.html
