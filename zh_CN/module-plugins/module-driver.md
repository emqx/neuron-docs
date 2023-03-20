# 模块配置

本节主要介绍了北向应用和南向设备的参数配置，南向设备的点位信息配置规范。

::: tip
uint16 对应 word 类型。uint32 对应 dword 类型。
:::

## WebSocket

使用此插件, 从设备采集到的数据可以通过*ws*/*wss*协议传输到WebSocket服务器上。

### 应用配置

| 字段                | 说明                                                         |
| ------------------- | ------------------------------------------------------------ |
| **format**          | 上报数据的json格式选择，选填，有values模式和tags模式，默认为values模式 |
| **url**             | WebSocket服务地址，必填。例如ws://127.0.0.1:8000, wss://example.com |
| **ca**              | ca文件，只在使用*wss*协议时启用，这种情况下为必填。            |
| **cert**            | cert文件，只在使用*wss*协议时启用，选填。                      |
| **key**             | key文件，只在使用*wss*协议时启用，选填。                       |
| **keypass**         | key文件密码，只有在使用*wss*协议时启用，选填。                 |

## File

File 插件用于读写文件。

### 设备配置

| 字段         | 说明                  |
| ----------- | --------------------- |
| file_length | 设置读写文件内容的字符长度 |

### 支持的数据类型

* STRING

### 地址格式

> FILE PATH</span>

*例子:*

| 地址                      | 数据类型 | 说明                     |
| ------------------------ | ------ | ------------------------ |
| /home/root/test/test.txt | string | 读写 test.txt 文件中的内容 |

:::tip
地址需填写文件的绝对路径。

写操作时，写入的内容将会覆盖之前的文件内容。
:::
## Sparkplug_B

Neuron 从设备采集到的数据可以通过Sparkplug_B协议从边缘端传输到Sparkplug_B应用中，用户也可以从应用程序向 Neuron 发送数据修改指令。Sparkplug_B是运行再MQTT之上的应用型协议，所以在Neuron中的设置与MQTT驱动相似。

### 应用配置

| 字段          | 说明                                                         |
| ------------- | ------------------------------------------------------------ |
| **client-id** | MQTT 客户端 ID，连接的唯一标识，必填                         |
| **group-id**  | Sparkplug_B 协议中的最顶层逻辑分组，可以代表工厂或车间等实体，必填 |
| **node-id**   | Sparkplug_B 协议中的边缘节点唯一标识，必填                   |
| **ssl**       | 是否启用 mqtt ssl，默认 false                                |
| **host**      | MQTT Broker 主机，必填                                       |
| **port**      | MQTT Broker 端口号，必填                                     |
| **username**  | 连接到 Broker 时使用的用户名，可选填                         |
| **password**  | 连接到 Broker 时使用的密码，可选填                           |
| **ca**        | ca 文件，只在 ssl 值为 true 时启用，这种情况下为必填         |
| **cert**      | cert 文件，只在 ssl 值为 true 时启用，可选填                 |
| **key**       | key 文件，只在 ssl 值为 true 时启用，可选填                  |
| **keypass**   | key 文件密码，只有在 ssl 值为 true 时启用，可选填            |

## Siemens FetchWrite

s5fetch-write 插件用于带有网络扩展模块CP443的西门子PLC的访问，如，s7-300/400。

### 设备配置

| 字段     | 说明                        |
| -------- | --------------------------- |
| **host** | 远程 PLC 的 IP              |
| **port** | 远程 PLC 的端口，默认为 102 |

### 支持的数据类型

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

> AREA ADDRESS\[.BIT][.LEN]</span>

#### AREA ADDRESS

| 区域 | 数据类型                                                     | 属性  | 备注                    |
| ---- | ------------------------------------------------------------ | ----- | ----------------------- |
| DB   | int16/uint16/bit/int32/uint32/int64/uint64/float/double/string | 读    | 主存数据块，以words读写 |
| M    | int8/uint8/int16/uint16/bit/int32/uint32/int64/uint64/float/double/string | 读/写 | 标志内存M，以bytes读写  |
| I    | int8/uint8/int16/uint16/bit/int32/uint32/int64/uint64/float/double/string | 读/写 | 输入，以bytes读写       |
| Q    | int8/uint8/int16/uint16/bit/int32/uint32/int64/uint64/float/double/string | 读/写 | 输出，以bytes读写       |
| PEPA | int8/uint8/int16/uint16/bit/int32/uint32/int64/uint64/float/double/string | 读/写 | IO modules，以bytes读写 |
| Z    | int16/uint16/bit/int32/uint32/int64/uint64/float/double/string | 读/写 | 计数器，以words读写     |
| T    | int16/uint16/bit/int32/uint32/int64/uint64/float/double/string | 读/写 | 计时器，以words读写     |

*例子：*

| 地址       | 数据类型 | 说明                         |
| ---------- | -------- | ---------------------------- |
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

#### .BIT

选填，指某一地址的某一位。

*例子：*

| 地址        | 数据类型 | 说明                                 |
| ----------- | -------- | ------------------------------------ |
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

#### .LEN

当数据类型为 string 类型时，是必填项，表示字符串长度。

*例子：*

| 地址         | 数据类型 | 说明                                         |
| ------------ | -------- | -------------------------------------------- |
| DB1.DBW12.20 | string   | 1 数据块中，起始数据字为 12，字符串长度为 20 |



## HJ212-2017

HJ212-2017主要用于采集支持环保HJ212-2017标准的设备数据，此驱动目前只支持设备主动上传数据。

### 以太网连接配置

| 字段        | 说明                                                         |
| ----------- | ------------------------------------------------------------ |
| **timeout** | 向设备发送请求超时时间                                       |
| **host**    | 当 Neuron 作为客户端使用时，host 指远程设备的 IP。当 Neuron 作为服务端使用时，host 指 Neuron 在本地使用的 IP，默认可填写 0.0.0.0 |
| **port**    | 当 Neuron 作为客户端使用时，post 指远程设备的 TCP 端口。当 Neuron 作为服务端使用时，host 指 Neuron 在本地使用的 TCP 端口，默认为 502 |

### 串口连接配置

| 字段        | 说明                             |
| ----------- | -------------------------------- |
| **device**  | 使用串口设备，例如“/dev/ttyUSB0” |
| **stop**    | 停止位，默认值是 1               |
| **parity**  | 校验位，默认值是 2，代表偶校验   |
| **baud**    | 波特率，默认值是 9600            |
| **data**    | 数据位，默认值是 8               |
| **timeout** | 向设备发送请求超时时间           |

### 支持的数据类型

* STRING
* DOUBLE
* UINT8
* INT8



### 地址格式

#### 污染物实时数据

> RT!xxxx-[Rtd\][Flag\][SampleTime\][EFlag]</span>

| 地址                 | 类型   | 说明                         |
| -------------------- | ------ | ---------------------------- |
| RT!w01018-Rtd        | double | 污染物 w01018实时数据        |
| RT!w01018-Flag       | string | 污染物w01018实时数据标志     |
| RT!w01018-SampleTime | string | 污染物w01018实时数据采样时间 |
| RT!w01018-EFlag      | string | 污染物w01018设备标志         |
| RT!w01018-ZsRtd      | double | 污染物w01018实时采样折算数据 |

#### 污染物分钟数据

> MIN!xxxx-[Cou\][Min\][Avg\][Max\][Flag]

| 地址             | 类型   | 说明                       |
| ---------------- | ------ | -------------------------- |
| MIN!w01018-Cou   | double | 污染物w01018分钟累计值     |
| MIN!w01018-Min   | double | 污染物w01018分钟最小值     |
| MIN!w01018-Avg   | double | 污染物w01018分钟平均值     |
| MIN!w01018-Max   | double | 污染物w01018分钟最大值     |
| MIN!w01018-Flag  | string | 污染物w01018分钟数据标志   |
| MIN!w01018-ZsMin | double | 污染物w01018分钟折算最小值 |
| MIN!w01018-ZsAvg | double | 污染物w01018分钟折算平均值 |
| MIN!w01018-ZsMax | double | 污染物w01018分钟折算最大值 |

#### 污染物小时数据

> HOUR!xxxx-[Cou\][Min\][Avg\][Max\][Flag]

| 地址              | 类型   | 说明                       |
| ----------------- | ------ | -------------------------- |
| HOUR!w01018-Cou   | double | 污染物w01018小时累计值     |
| HOUR!w01018-Min   | double | 污染物w01018小时最小值     |
| HOUR!w01018-Avg   | double | 污染物w01018小时平均值     |
| HOUR!w01018-Max   | double | 污染物w01018小时最大值     |
| HOUR!w01018-Flag  | string | 污染物w01018小时数据标志   |
| HOUR!w01018-ZsMin | double | 污染物w01018小时折算最小值 |
| HOUR!w01018-ZsAvg | double | 污染物w01018小时折算平均值 |
| HOUR!w01018-ZsMax | double | 污染物w01018小时折算最大值 |

#### 污染物日数据

> DAY!xxxx-[Cou\][Min\][Avg\][Max\][Flag]

| 地址             | 类型   | 说明                     |
| ---------------- | ------ | ------------------------ |
| DAY!w01018-Cou   | double | 污染物w01018日累计值     |
| DAY!w01018-Min   | double | 污染物w01018日最小值     |
| DAY!w01018-Avg   | double | 污染物w01018日平均值     |
| DAY!w01018-Max   | double | 污染物w01018日最大值     |
| DAY!w01018-Flag  | string | 污染物w01018日数据标志   |
| DAY!w01018-ZsMin | double | 污染物w01018日折算最小值 |
| DAY!w01018-ZsAvg | double | 污染物w01018日折算平均值 |
| DAY!w01018-ZsMax | double | 污染物w01018日折算最大值 |

## IEC61850

iec61850 插件用于对IEC61850服务器的读/写，目前只支持MMS协议的访问。

### 设备配置

| 字段     | 说明                       |
| -------- | -------------------------- |
| **host** | 远程设备的 IP              |
| **port** | 远程设备的端口，默认为 102 |

### 支持的数据类型

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
* BOOL
* STRING

### 地址格式

> Logical Devices/Logical Nodes$FC$DO$DA</span>

*例子：*

| 地址                                  | 数据类型 | 说明                                                 |
| ------------------------------------- | -------- | ---------------------------------------------------- |
| GenericIO/GGIO1$CF$Mod$ctlModel       | int8     | LD-GenericIO,LN-GGIO1,FC-CF,DO-Mod,DA-ctlModel       |
| GenericIO/GGIO1$CO$SPCSO1$Oper$ctlNum | uint8    | LD-GenericIO,LN-GGIO1,FC-CO,DO-SPCSO1,DA-Oper$ctlNum |
| GenericIO/GGIO1$CF$SPCSO1$ctlModel    | int16    | LD-GenericIO,LN-GGIO1,FC-CF,DO-SPCSO1,DA-ctlModel    |
| GenericIO/GGIO1$CO$SPCSO2$Oper$ctlNum | uint16   | LD-GenericIO,LN-GGIO1,FC-CO,DO-SPCSO2,DA-Oper$ctlNum |
| GenericIO/GGIO1$CF$SPCSO2$ctlModel    | int32    | LD-GenericIO,LN-GGIO1,FC-CF,DO-SPCSO2,DA-ctlModel    |
| GenericIO/GGIO1$ST$SPCSO4$Oper$ctlNum | uint32   | LD-GenericIO,LN-GGIO1,FC-ST,DO-SPCSO4,DA-Oper$ctlNum |
| GenericIO/GGIO1$CF$SPCSO3$ctlModel    | int64    | LD-GenericIO,LN-GGIO1,FC-CF,DO-SPCSO3,DA-ctlModel    |
| GenericIO/GGIO1$ST$SPCSO1$ctlNum      | uint64   | LD-GenericIO,LN-GGIO1,FC-ST,DO-SPCSO1,DA-ctlNum      |
| GenericIO/GGIO1$MX$AnIn1$mag$f        | float    | LD-GenericIO,LN-GGIO1,FC-MX,DO-AnIn1,DA-mag$f        |
| GenericIO/GGIO1$MX$AnIn3$mag$f        | double   | LD-GenericIO,LN-GGIO1,FC-MX,DO-AnIn3,DA-mag$f        |
| GenericIO/GGIO1$CO$SPCSO1$Oper$Test   | bool     | LD-GenericIO,LN-GGIO1,FC-CO,DO-SPCSO1,DA-Oper$Test   |
| GenericIO/LLN0$DC$NamPlt$vendor       | string   | LD-GenericIO,LN-GGIO1,FC-DC,DO-NamPlt,DA-vendor      |
