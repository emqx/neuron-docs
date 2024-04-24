# BACnet/IP

BACnet（Building Automation and Control Networks）是一种用于智能建筑的通信协议，它是由国际标准化组织（ISO）、美国国家标准协会（ANSI）和美国采暖、制冷与空调工程师学会（ASHRAE）定义的通信协议。BACnet 是专门为智能建筑及控制系统设计的通信协议，可用于暖通空调系统（HVAC）、照明控制、门禁系统、火警侦测系统以及其相关设备。其优点在于可降低维护系统所需成本，并且安装比一般工业通信协议更为简易。此外，BACnet 还提供了五种业界常用的标准协议，可以防止设备和系统供应商的垄断，从而增加未来系统的扩展性和兼容性。BACnet 协议支持多种通信方式，包括串口、IP、Ethernet、ZigBee 等。

Neuron 支持 BACnet IP 协议，可以通过 UDP 协议与 BACnet 设备进行通讯。

## 添加插件

在 **配置 -> 南向设备**，点击**添加设备**来创建设备节点，输入插件名称，插件类型选择 **BACnet/IP** 启用插件。

## 设备配置

点击插件卡片或插件列，进入**设备配置**页。配置 Neuron 与设备建立连接所需的参数，下表为插件相关的配置项。

| 字段      | 说明                            |
|--------- | ------------------------------ |
| **设备 IP 地址** | BACnet 设备的 IP                |
| **设备端口** | BACnet 设备的端口号，默认为 47808 |

## 设置组和点位

完成插件的添加和配置后，要建立设备与 Neuron 之间的通信，首先为南向驱动程序添加组和点位。

完成设备配置后，在**南向设备**页，点击设备卡片/设备列进入**组列表**页。点击**创建**来创建组，设定组名称以及采集间隔。完成组的创建后，点击组名称进入**点位列表**页，添加需要采集的设备点位，包括点位地址，点位属性，数据类型等。

公共配置项部分可参考[连接南向设备](../south-devices.md)，本页将介绍支持的数据类型和地址格式部分。

### 数据类型

* FLOAT
* BIT
* INT8
* UINT8
* UINT16
* BOOL
* STRING

### 地址格式

> AREA ADDRESS(.PROPERTY_ID)


支持区域

| 区域 | 地址范围     | 属性  | 数据类型 | 备注       |
| ---- | ------------ | ----- | -------- | ---------- |
| AI   | 0 - 0x3fffff | 读    | float    | 模拟输入   |
| AO   | 0 - 0x3fffff | 读/写 | float    | 模拟输出   |
| AV   | 0 - 0x3fffff | 读/写 | float    | 模拟量     |
| BI   | 0 - 0x3fffff | 读    | bit      | 二进制输入 |
| BO   | 0 - 0x3fffff | 读/写 | bit      | 二进制输出 |
| BV   | 0 - 0x3fffff | 读/写 | bit      | 二进制值   |
| MSI  | 0 - 0x3fffff | 读    | uint8    | 多状态输入 |
| MSO  | 0 - 0x3fffff | 读/写 | uint8    | 多状态输出 |
| MSV  | 0 - 0x3fffff | 读/写 | uint8    | 多状态值   |
| DEV  | 0 - 0x3fffff | 读    |          | 设备       |
| ACC  | 0 - 0x3fffff | 读/写 | uint8    | 累加器     |


目前支持标准属性和自定义属性

标准属性

| 属性             | 地址                            | 类型   |
| ---------------- | ------------------------------- | ------ |
| 对象名称         | Object_Name                     | string |
| 对象类型         | Object_Tyep                     | uint8  |
| 描述             | Description                     | string |
| 设备类型         | Device_Type                     | string |
| 状态标志         | Status_Flags                    | string |
| 事件状态         | Event_State                     | uint8  |
| 脱离服务         | Out_Of_Service                  | bool   |
| 更新间隔         | Update_Interval                 | uint8  |
| 最小值           | Min_Pres_Value                  | float  |
| 最大值           | Max_Pres_Value                  | float  |
| 分辨率           | Resolution                      | float  |
| COV增量          | COV_Increment                   | float  |
| 时间延迟         | Time_Delay                      | uint8  |
| 通告类           | Notification_Class              | uint8  |
| 通告类型         | Notify_Type                     | uint8  |
| 单位             | Units                           | uint8  |
| 高阈值           | High_Limit                      | float  |
| 低阈值           | Low_Limit                       | float  |
| 阈值宽度         | Deadband                        | float  |
| 可靠性           | Reliability                     | uint8  |
| 极性             | Polarity                        | uint8  |
| 系统状态         | System_Status                   | uint8  |
| 厂商名           | Vendor_Name                     | string |
| 厂商ID           | Vendor_Identifier               | uint8  |
| 型号名称         | Model_Name                      | string |
| 固件版本         | Firmware_Revision               | string |
| 应用软件版本     | Application_Software_Version    | string |
| 位置             | Location                        | string |
| 协议版本         | Protocol_Version                | uint16 |
| 协议一致类别     | Protocol_Conformance_Class      | uint8  |
| 协议服务支持     | Protocol_Service_Supported      | string |
| 协议对象类型支持 | Protocol_Object_Types_Supported | string |
| 序列号           | Serial_Number                   | string |
| 最大APDU长度支持 | Max_APDU_Length_Accepted        | uint16 |
| 分段支持         | Segmentation_Supported          | uint8  |
| 本地时间         | LOCAL_TIME                      | string |
| 本地日期         | LOCAL_DATE                      | string |
| 时差             | UTC_Offset                      | int8   |
| 夏令时状态       | Daylight_Savings_Status         | bool   |
| APDU分段超时     | APUD_Segment_Timeout            | uint8  |
| APDU超时         | APUD_Timeout                    | uint16 |
| APDU重传次数     | Number_Of_APDU_Retries          | uint8  |
| 最大主节点数     | Max_Master                      | uint8  |
| 最大信息帧数     | Max_Info_Frame                  | uint8  |
| 配置名           | Profile_Name                    | string |
| 频率             | Pulse_Rate                      | uint8  |
| 分频             | Scale                           | float  |
| 预分频           | Prescale                        | float  |
| 原值             | Value_Before_Change             | uint8  |
| 修改时间         | Value_Change_Time               | string |


不指定属性，默认为当前值（Present_Value）属性，DEV 区域除外。

自定义属性

PROPERTY_ID 由两部分组成，一个是 custom 标志，一个是属性的值（int），整体格式为 AREA ADDRESS.custom.id。

支持 Present Value 置零操作，目前支持 AO 和 BO 区域，地址形式为 (AO|BO)xxx.NULL，只支持写操作，根据区域的类型，写入类型的零值即可。

### 地址示例

| 地址                  | 数据属性 | 说明                                    |
| --------------------- | -------- | --------------------------------------- |
| AI0                   | float    | AI 区域，地址为 0                       |
| AI1                   | float    | AI 区域，地址为 1                       |
| AV30                  | float    | AV 区域，地址为 30                      |
| BO10                  | bit      | BO 区域，地址为 10                      |
| BO10.NULL             | bit      | BO 区域，地址为 10，写入NULL值          |
| BO20                  | bit      | BO 区域，地址为 20                      |
| BI0                   | bit      | BI 区域，地址为 0                       |
| BI1                   | bit      | BI 区域，地址为 1                       |
| BV3                   | bit      | BV 区域，地址为 3                       |
| MSI10                 | uint8    | MAI 区域，地址为 10                     |
| MSI20                 | uint8    | MSI 区域，地址为 20                     |
| MSI30                 | uint8    | MSI 区域，地址为 30                     |
| ACC1                  | string   | ACC 区域，地址为 1                      |
| AI0.Object_Name       | string   | AI 区域，地址为 0，属性为对象名         |
| AI0.custom.1234       | ALL      | AI 区域，地址为 0，属性值为1234         |
| DEV400001.Vendor_Name | string   | DEV 区域，地址为 400001，属性值为厂商名 |
