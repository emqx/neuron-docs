# 应用和配置说明

本节主要介绍了北向应用/南向设备的参数配置和点位信息配置规范。

## 类型描述

* 如果你想使用 **word** 类型，请在 Neuron 的数据类型中选择 uint16。
* 如果你想使用 **dword** 类型，请在 Neuron 的数据类型中选择 uint32。

## 通用地址格式选项

每个驱动程序的地址格式所支持的通用选项。

**#** 字节顺序

```
 - B  = 2,1     int16/uint16
 - L  = 1,2     int16/uint16 (默认)
 - LL = 1,2,3,4 int32/uint32/float (默认)
 - LB = 2,1,4,3 int32/uint32/float
 - BB = 3,4,1,2 int32/uint32/float
 - BL = 4,3,2,1 int32/uint32/float
```

**.**  \[bit][len\[H]\[L]\[D]\[E]]  位操作和字符串长度

```
- H = high-to-low endian (default)
- L = low-to-high endian
- D = a high byte is stored in an int16
- E = a low byte is stored in an int16
```

## MQTT

从设备中收集到的数据可以通过 MQTT 应用程序传输到 MQTT 代理，并通过 MQTT 应用程序 向 Neuron 发送指令。

### 参数配置

**client-id** MQTT 的客户端 ID。

**ssl** 是否启用 mqtt ssl，默认 false.

**host** MQTT 代理主机。

**port** MQTT 代理的端口。

**username** 连接到 Broker 时使用的用户名。

**password** 连接到 Broker 时使用的密码。

**ca-path** ca 路径。

**ca-file** ca 文件。

## Modbus

Modbus 协议包括三种协议：Modbus TCP、Modbus RTU 和 Modbus RTU over TCP。

### 支持的数据类型

* INT16
* INT32
* UINT16
* UINT32
* FLOAT
* BIT
* STRING

### 参数设置

**connection mode**：驱动程序连接到设备的方式，默认为客户端，即把 Neuron 作为客户端使用。

**host**：当 Neuron 作为客户端使用时，host 指远程设备的 IP。当 Neuron 作为服务端使用时，host 指 Neuron 在本地使用的 IP，默认可填写 0.0.0.0。

**port**：当 Neuron 作为客户端使用时，post 指远程设备的 TCP 端口。当 Neuron 作为服务端使用时，host 指 Neuron 在本地使用的 TCP 端口，默认为 502。
### 地址格式

> SLAVE!ADDRESS\[.BIT][#ENDIAN]\[.LEN\[H]\[L]\[D]\[E]]</span>

**SLAVE** 从机 ID。

**ADDRESS** 寄存器地址。

| 区域           | 地址范围          | 属性        | 寄存器大小     | 功能码        |
| -------------- | --------------- | ---------- | ------------- | ------------ |
| coil           | 000001 ~ 065536 | 读/写       | 1bit          | 0x1,0x5,0x0f |
| input          | 100001 ~ 165536 | 读          | 1bit          | 0x2          |
| input register | 300001 ~ 365536 | 读          | 16bit         | 0x4          |
| hold register  | 400001 ~ 465536 | 读/写       | 16bit         | 0x3,0x6,0x10 |

| 数据类型            | 区域                         | 属性                                               |
| ------------------ | ------------------------ | ------------------------------------------------------- |
| uint16/int16       | 输入寄存器\保持寄存器       | 输入寄存器(读), 保持寄存器(写)                     |
| uint32/int32/float | 输入寄存器\保持寄存器       | 输入寄存器(读), 保持寄存器(写)                     |
| bit                | 所有区域                  | 输入(读), 线圈(读/写), 输入寄存器(读), 保持寄存器(写) |
| string             | 输入寄存器\保持寄存器       | 输入寄存器(读), 保持寄存器(写)                     |

#### **例子**

```
bit:
    1!00001
    1!00007
    1!10001
    1!10005
    1!30004.0
    1!40010.4
    1!40001.15

int16/uint16:
    1!30004(default #L)
    1!30004#B
    1!30004#L
    1!40004(default #L)
    1!40004#L
    1!40004#B

int32/uint32/float:
    1!30004(default #LL)
    1!30004#BB
    1!30004#LB
    1!30004#BL
    1!30004#LL
    1!40004(default #LL)
    1!40004#LB
    1!40004#BB
    1!40004#LL
    1!40004#BL

string:
    1!30001.10(default H)
    1!30001.10H
    1!30001.10L
    1!40001.10(default H)
    1!40001.10H
    1!40001.10L
```

**注意** 一些设备文件使用功能和寄存器地址来描述指令。首先，根据功能确定地址的最高位数，并在寄存器地址上加1，作为 Neuron 的使用地址。

例如，功能码是 0x03，寄存器地址是 0，那么 Neuron 使用的地址是 400001.

## OPC UA

### 支持的数据类型

* BYTE
* INT8
* INT16
* INT32
* INT64
* UINT8
* UINT16
* UINT32
* UINT64
* FLOAT
* DOUBLE
* BOOL
* BIT
* STRING

### 参数配置

**endpoint url** 远程访问 PLC 的地址，默认值是`opc.tcp://127.0.0.1:4840/`。

**username** 连接到 PLC 时，使用的用户名。

**password** 连接到 PLC 时，使用的密码。

**cert-file** 提供登录用户认证的证书。
**key-file** 私钥文件，用于提供签名和加密传输。

### 地址格式

> IX!NODEID</span>

**IX** 命名空间索引。

**NODEID** 节点 ID。

*例子*:

* 2!Device1.Module1.Tag1 指命名空间索引为2，节点 ID 为 Device1.Module1.Tag1。

**注意** 关于命名空间索引和节点 ID 的解释，请参考 OPC UA 标准。

## S7COMM

s7comm 插件用于带有网络端口的西门子PLC，如，s7-200/300/400/1200/1500。

### 支持的数据类型

* INT16
* UINT16
* INT32
* UINT32
* FLOAT
* DOUBLE
* BIT
* STRING

### 参数配置

**host** 远程 PLC 的 IP。

**ip** 远程 PLC 的端口，默认为 102。

**rack** PLC 机架号，默认为 0。

**slot** PLC 插槽号，默认为 1。

### 地址格式

> AREA ADDRESS\[.BIT][.LEN]</span>

| 区域 | 数据类型                                        | 属性  | 备注          |
| ---- | ------------------------------------------------- | ---------- | --------------- |
| I    | int16/uint16/bit                                  | 读       | input           |
| O    | int16/uint16/bit                                  | 读/写 | output          |
| F    | int16/uint16/bit                                  | 读/写 | flag            |
| T    | int16/uint16/bit                                  | 读/写 | timer           |
| C    | int16/uint16/bit                                  | 读/写 | counter         |
| DB   | int16/uint16/bit/int32/uint32/float/double/string | 读/写 | global DB block |

*例子*

```
bit:
    I0.0
    I0.1
    O1.0
    O1.2
    F2.1
    F2.2
    T3.3
    T3.4
    C4.5
    C4.6
    DB1.DBW10.1
    DB2.DBW1.15

int16/uint16:
    I0
    I1
    O2
    O3
    F4
    F5
    T6
    T7
    C8
    C9
    DB10.DBW10
    DB12.DBW10

int32/uint32/float/double:
    DB10.DBW10

string:
    DB1.DBW12.20
```

**注意** 当使用S7COMM插件访问S7 1200/1500 PLC时，你需要使用西门子软件（TIA16）对PLC进行一些设置。

* 优化块访问必须被关闭。
* 访问级别必须是**完全**，**连接机制**必须允许 GET/PUT。

## FINS on TCP

这个插件用于带有网络端口的欧姆龙PLC，如CP2E。

### 支持的数据类型

* UINT8
* INT8
* INT16
* UINT16
* INT32
* UINT32
* FLOAT
* DOUBLE
* BIT
* STRING

### 参数配置

**host** 远程 PLC 的 ID。

**port** 远程 PLC 的端口，默认为 9600.

### 地址格式

> AREA ADDRESS\[.BIT]\[.LEN\[H]\[L]]</span>

| 区域 | 数据类型           | 属性        | 备注           |
| ---- | ---------------- | ---------- | ---------------- |
| CIO  | 所有类型          | 读/写       | CIO Area         |
| A    | 所有类型          | 读          | Auxiliary Area   |
| W    | 所有类型          | 读/写       | Work Area        |
| H    | 所有类型          | 读/写       | Holding Area     |
| D    | 所有类型          | 读/写       | Data Memory Area |
| P    | int16/uint16    | 读/写       | PVs              |
| F    | int8/uint8      | 读          | Completion Flag  |
| EM   | 所有类型          | 读/写      | Extended Memory  |

*例子*

```
bit:
    CIO0.0
    CIO1.2
    A2.1
    A2.3
    W3.4
    W3.0
    H4.15
    H4.10
    D5.2
    D5.3
    EM10W0.0
    
uint8/int8:
   F0
   F1

int16/uint16/int32/uint32/float/double:
    CIO1
    CIO2
    A2
    A4
    W5
    W10
    H20
    H30
    D10
    D20
    EM10W20
 
string:
    CIO0.20
    CIO1.20
    A2.10
    A2.30
    W3.40
    W3.10
    H4.15
    H4.10
    D5.20
    D5.30
    EM10W0.10
```

## QnA3E

qna3e插件用于通过以太网访问三菱的QnA兼容PLC，包括Q系列（MC）、iQ-F系列（SLMP）和iQ-L系列。

### 支持的数据类型

* INT16
* UINT16
* INT32
* UINT32
* FLOAT
* DOUBLE
* BIT
* STRING

### 参数配置

**host** 远程 PLC 的 ID。

**ip** 远程 PLC 的端口号，默认为 2000。

### 地址格式

> AREA ADDRESS\[.BIT]\[.LEN\[H]\[L]]</span>

| 区域 |数据类型 | 属性  | 备注                           |
| ---- | --------- | ---------- | -------------------------------- |
| X    | 所有类型       | 读/写      | Input relay (Q/iQ-F)             |
| DX   | 所有类型       | 读/写 | (Q/iQ-F)                         |
| Y    | 所有类型       | 读/写 | Output relay (Q/iQ-F)            |
| DY   | 所有类型       | 读/写 | (Q/iQ-F)                         |
| B    | 所有类型       | 读/写 | Link relay (Q/iQ-F)              |
| SB   | 所有类型       | 读/写 | Link special relay               |
| M    | 所有类型       | 读/写 | Internal relay (Q/iQ-F)          |
| SM   | 所有类型       | 读/写 | Special relay (Q/iQ-F)           |
| L    | 所有类型       | 读/写 | Latch relay (Q/iQ-F)             |
| F    | 所有类型       | 读/写 | Annunciator (Q/iQ-F)             |
| V    | 所有类型       | 读/写 | Edge relay (Q/iQ-F)              |
| S    | 所有类型       | 读/写 | (Q/iQ-F)                         |
| TS   | 所有类型       | 读/写 | Timer Contact (Q/iQ-F)           |
| TC   | 所有类型       | 读/写 | Timer Coil (Q/iQ-F)              |
| SS   | 所有类型       | 读/写 | (Q/iQ-F)                         |
| STS  | 所有类型       | 读/写 | Retentive timer Contact (Q/iQ-F) |
| SC   | 所有类型       | 读/写 | (Q/iQ-F)                         |
| CS   | 所有类型       | 读/写 | Counter Contact (Q/iQ-F)         |
| CC   | 所有类型       | 读/写 | Counter Coil (Q/iQ-F)            |
| TN   | 所有类型       | 读/写 | Timer Current value (Q/iQ-F)     |
| STN  | 所有类型       | 读/写 | Retentive timer (Q/iQ-F)         |
| SN   | 所有类型       | 读/写 | (Q/iQ-F)                         |
| CN   | 所有类型       | 读/写 | Counter Current value  (Q/iQ-F)  |
| D    | 所有类型       | 读/写 | Data register (Q/iQ-F)           |
| DSH  |           |            |                                  |
| DSL  |           |            |                                  |
| SD   | 所有类型       | 读/写 | Specical register (Q/iQ-F)       |
| W    | 所有类型       | 读/写 | Link register (Q/iQ-F)           |
| WSH  |           |            |                                  |
| WSL  |           |            |                                  |
| SW   | 所有类型       | 读/写 | Link special register (Q/iQ-F)   |
| R    | 所有类型       | 读/写 | File register (Q/iQ-F)           |
| ZR   | 所有类型       | 读/写 | File register (Q/iQ-F)           |
| RSH  |           |            |                                  |
| ZRSH |           |            |                                  |
| RSL  |           |            |                                  |
| ZRSL |           |            |                                  |
| Z    | 所有类型       | 读/写 | Index register (Q/iQ-F)          |

*例子*

```
bit:
    X0
    X1
    Y0
    Y1

int16/uint16/int32/uint32/float/double:
    D100
    D1000
 
string:
    D1002.16
```

## IEC 60870-5-104

### 支持的数据类型

* uint16
* int16
* float
* bit

### 参数配置

**host** : 设备 IP。

**port**: 设备端口号，默认为2404。

**ca**: 公共地址。

**interval**: 站点问询时间间隔。

### 地址格式

> IOA</span>

| IEC 60870-5-104  TYPEID         | Neuron 类型  |
| ------------------------------- | ------------ |
| M_ME_NB_1、M_ME_TE_1            | uint16/int16 |
| M_ME_NC_1、M_ME_TF_1            | float        |
| M_SP_NA_1、M_SP_TB_1            | bit          |
| M_ME_NA_1、M_ME_TD_1、M_ME_ND_1 | uint16/int16 |

## KNXnet/IP

### 支持的数据类型

* bit
* bool
* int8
* uint8
* int16
* uint16
* float

### 参数配置

**host** BACnet 设备的 ID。

**port** BACnet 设备的端口号，默认为 47808.

### 地址格式

> GROUP_ADDRESS | GROUP_ADDRESS,INDIVIDUAL_ADDRESS</span>

| 地址                             | 属性 | 备注                             |
| ----------------------------------- | --------- | ---------------------------------- |
| GROUP_ADDRESS                       | 写     | KNX 组地址                 |
| GROUP_ADDRESS,INDIVIDUAL_ADDRESS    | 读      | KNX individual address under group |

*例子*:

* `0/0/1` 是一个 KNX 组地址，只在 Neuron 中写入，属于这个组的 KNX 设备将对发送的信息做出反应。属于这个组的 KNX 设备将对发送到这个组的信息做出反应。
* `0/0/1,1.1.1` 代表一个 KNX 个人地址 `1.1.1` 是组地址 `0/0/1` 的成员。是组地址 `0/0/1` 的成员，并且在 Neuron 中只读。

## BACnet/IP

### 支持的数据类型

* float
* bit

### 地址格式

> AREA[ADDRESS]</span>

| AREA | ATTRIBUTE  | DADA TYPE | ADDRESS RANGE | REMARK             |
| ---- | ---------- | --------- | ------------- | ------------------ |
| AI   | read       | float     | 0 - 0x3fffff  | analog input       |
| AO   | read/write | float     | 0 - 0x3fffff  | analog output      |
| AV   | read/write | float     | 0 - 0x3fffff  | analog value       |
| BI   | read       | bit       | 0 - 0x3fffff  | binary input       |
| BO   | read/write | bit       | 0 - 0x3fffff  | binary output      |
| BV   | read/write | bit       | 0 - 0x3fffff  | binary value       |
| MSI  | read       | bit       | 0 - 0x3fffff  | multi state input  |
| MSO  | read/write | bit       | 0 - 0x3fffff  | multi state output |
| MSV  | read/write | bit       | 0 - 0x3fffff  | multi state value  |

*例子*

```
float:
 AI0 
 AI1
 BO10
 BO20
 AV30

bit:
 BI0
 BI1
 BV3
 MSI10
 MSI20
 MSI30
```
