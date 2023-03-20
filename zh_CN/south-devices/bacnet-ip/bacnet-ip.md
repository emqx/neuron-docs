# BACnet/IP 介绍与使用

## 设备配置

| 字段      | 说明                            |
|--------- | ------------------------------ |
| **host** | BACnet 设备的 IP                |
| **port** | BACnet 设备的端口号，默认为 47808 |

## 支持的数据类型

* FLOAT
* BIT

## 地址格式用法

### 地址格式

> AREA ADDRESS</span>

| 区域  | 地址范围      | 属性    | 数据类型 |  备注        |
| ---- | ------------ | ------ | ------- | ----------- |
| AI   | 0 - 0x3fffff | 读     | float   | 模拟输入      |
| AO   | 0 - 0x3fffff | 读/写  | float   | 模拟输出      |
| AV   | 0 - 0x3fffff | 读/写  | float   | 模拟量        |
| BI   | 0 - 0x3fffff | 读     | bit     | 二进制输入     |
| BO   | 0 - 0x3fffff | 读/写  | bit      | 二进制输出    |
| BV   | 0 - 0x3fffff | 读/写  | bit      | 二进制值      |
| MSI  | 0 - 0x3fffff | 读     | bit      | 多状态输入    |
| MSO  | 0 - 0x3fffff | 读/写  | bit      | 多状态输出    |
| MSV  | 0 - 0x3fffff | 读/写  | bit      | 多状态值     |

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
| MSI10  | bit     | MAI 区域，地址为 10 |
| MSI20  | bit     | MSI 区域，地址为 20 |
| MSI30  | bit     | MSI 区域，地址为 30 |