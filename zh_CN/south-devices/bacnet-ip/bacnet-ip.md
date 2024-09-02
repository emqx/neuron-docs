# 概览

BACnet（Building Automation and Control Networks）是一种用于智能建筑的通信协议，它是由国际标准化组织（ISO）、美国国家标准协会（ANSI）和美国采暖、制冷与空调工程师学会（ASHRAE）定义的通信协议。BACnet 是专门为智能建筑及控制系统设计的通信协议，可用于暖通空调系统（HVAC）、照明控制、门禁系统、火警侦测系统以及其相关设备。其优点在于可降低维护系统所需成本，并且安装比一般工业通信协议更为简易。此外，BACnet 还提供了五种业界常用的标准协议，可以防止设备和系统供应商的垄断，从而增加未来系统的扩展性和兼容性。BACnet 协议支持多种通信方式，包括串口、IP、Ethernet、ZigBee 等。

Neuron 支持 BACnet IP 协议，可以通过 UDP 协议与 BACnet 设备进行通讯。


## 设备配置

| 字段      | 说明                            |
|--------- | ------------------------------ |
| **host** | BACnet 设备的 IP                |
| **port** | BACnet 设备的端口号，默认为 47808 |

## 支持的数据类型

* FLOAT
* BIT
* UINT8

## 地址格式用法

### 地址格式

> AREA ADDRESS

| 区域  | 地址范围      | 属性    | 数据类型 |  备注        |
| ---- | ------------ | ------ | ------- | ----------- |
| AI   | 0 - 0x3fffff | 读     | float   | 模拟输入      |
| AO   | 0 - 0x3fffff | 读/写  | float   | 模拟输出      |
| AV   | 0 - 0x3fffff | 读/写  | float   | 模拟量        |
| BI   | 0 - 0x3fffff | 读     | bit     | 二进制输入     |
| BO   | 0 - 0x3fffff | 读/写  | bit      | 二进制输出    |
| BV   | 0 - 0x3fffff | 读/写  | bit      | 二进制值      |
| MSI  | 0 - 0x3fffff | 读     | uint8      | 多状态输入    |
| MSO  | 0 - 0x3fffff | 读/写  | uint8      | 多状态输出    |
| MSV  | 0 - 0x3fffff | 读/写  | uint8      | 多状态值     |

### 地址示例

| 地址    | 数据属性 | 说明              |
| ------ | ------- | ---------------- |
| AI0    | float   | AI 区域，地址为 0  |
| AI1    | float   | AI 区域，地址为 1  |
| BO10   | float   | BO 区域，地址为 10 |
| BO20   | float   | BO 区域，地址为 20 |
| AV30   | float   | AV 区域，地址为 30 |
| BI0    | bit     | BI 区域，地址为 0  |
| BI1    | bit     | BI 区域，地址为 1  |
| BV3    | bit     | BV 区域，地址为 3  |
| MSI10  | uint8     | MAI 区域，地址为 10 |
| MSI20  | uint8     | MSI 区域，地址为 20 |
| MSI30  | uint8     | MSI 区域，地址为 30 |