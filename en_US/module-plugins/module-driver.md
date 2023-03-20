# Module Setting

This document introduces how to setup parameter and data tag point information in configuration for northbound applications and southbound drivers.

::: tip
uint16 corresponds to the word type. uint32 corresponds to dword type.
:::

## WebSocket

Through this plugin, collected data can be transmitted to WebSocket servers using *ws*/*wss* protocol.

### Parameter Setting

| Parameter           | Description                                                  |
| ------------------- | ------------------------------------------------------------ |
| **format**          | The json format selection of the reported data, required, there are values mode and tags mode, the default is values mode |
| **url**             | WebSocket server address, required. Example: ws://127.0.0.1:8000, wss://example.com |
| **ca**              | ca file, only enabled when using *wss* protocol, in which case it is required       |
| **cert**            | cert file, only enabled when using *wss* protocol, optional                         |
| **key**             | key file, only enabled when using *wss* protocol, optional                          |
| **keypass**         | key file password, only enabled when using *wss* protocol, optional                 |

## File

File plugin is used to read or write files.

### Parameter Setting

| Parameter   | Description                                           |
| ----------- | ----------------------------------------------------- |
| file_length | Set the character length for reading or writing file |

### Support Data Type

* STRING

### Address Format

> FILE PATH</span>

*Example:*

| Address                  | Data Type | Description              |
| ------------------------ | --------- | ----------------------------------------------- |
| /home/root/test/test.txt | string    | Read or write the contents of the test.txt file |

:::tip
The address needs to fill in the GetFullPath.

When writing, the written content will overwrite the previous file content.
:::

## Sparkplug_B

Data collected by Neuron from the device can be transmitted from the edge to the Sparkplug_B application using the Sparkplug_B protocol. Users can also send data modification instructions to Neuron from the application. Sparkplug_B is an application-type protocol that runs on top of MQTT, so the setup in Neuron is similar to the MQTT driver.

### Parameter Setting

| Parameter     | Description                                                  |
| ------------- | ------------------------------------------------------------ |
| **client-id** | MQTT client ID, A unique identifier that can represent the edge end, required |
| **group-id**  | The top-level logical group in Sparkplug_B, which can represent an entity such as a factory or workshop, required |
| **node-id**   | The unique identifier of the edge node in the Sparkplug_B protocol, required |
| **ssl**       | Whether to enable mqtt ssl, default false                    |
| **host**      | MQTT Broker host, required                                   |
| **port**      | MQTT Broker port number, required                            |
| **username**  | Username to use when connecting to the broker, optional      |
| **password**  | The password to use when connecting to the broker, optional  |
| **ca**        | ca file, only enabled when the ssl value is true, in which case it is required |
| **cert**      | cert file, only enabled when the ssl value is true, optional |
| **key**       | key file, only enabled when the ssl value is true, optional  |
| **keypass**   | key file password, only enabled when the ssl value is true, optional |

## Siemens FetchWrite

The s5fetch-write plug-in is used for accessing Siemens PLCs with network expansion module CP443, such as s7-300/400.

### Parameter Setting

| Parameter | Description                  |
| --------- | ---------------------------- |
| **host**  | remote plc ip                |
| **port**  | remote plc port, default 102 |

### Support Data Type

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

### Address Format

> AREA ADDRESS\[.BIT][.LEN]</span>

#### AREA ADDRESS

| AREA | TYPE                                                         | ATTRIBUTE  | REMARK                                 |
| ---- | ------------------------------------------------------------ | ---------- | -------------------------------------- |
| DB   | int16/uint16/bit/int32/uint32/int64/uint64/float/double/string | read       | Data block in main memeory, word       |
| M    | int8/uint8/int16/uint16/bit/int32/uint32/int64/uint64/float/double/string | read/write | Flag area, byte                        |
| I    | int8/uint8/int16/uint16/bit/int32/uint32/int64/uint64/float/double/string | read/write | PII-process image of the inputs, byte  |
| Q    | int8/uint8/int16/uint16/bit/int32/uint32/int64/uint64/float/double/string | read/write | PIQ-process image of the outputs, byte |
| PEPA | int8/uint8/int16/uint16/bit/int32/uint32/int64/uint64/float/double/string | read/write | IO modules, byte                       |
| Z    | int16/uint16/bit/int32/uint32/int64/uint64/float/double/string | read/write | Count cells, word                      |
| T    | int16/uint16/bit/int32/uint32/int64/uint64/float/double/string | read/write | Time cells, word                       |

*Example：*

| Address    | Data Type | Description                   |
| ---------- | --------- | ----------------------------- |
| I0         | int16     | I area, address 0             |
| I1         | uint16    | I area, address 1             |
| Q2         | int16     | Q area, address 2             |
| Q3         | uint16    | Q area，address 3             |
| PEPA4      | int16     | PEPA area, address 4          |
| PEPA5      | int16     | PEPA area, address 5          |
| T6         | int16     | T area, address 6             |
| T7         | int16     | T area, address 7             |
| Z8         | uint16    | Z area, address 8             |
| Z9         | uint16    | Z area, address 9             |
| DB10.DBW10 | int16     | DB area, address 10，start 10 |
| DB12.DBW10 | uint16    | DB area, address 12, start 10 |
| DB10.DBW10 | float     | DB area, address 10, start 10 |
| DB11.DBW10 | double    | DB area, address 11, start 10 |

#### .BIT

Optional, refers to a certain digit of a certain address.

*Example：*

| Address     | Data Type | Description                             |
| ----------- | --------- | --------------------------------------- |
| I0.0        | bit       | I area, address 0, No. 0 bit            |
| I0.1        | bit       | I area, address 0, No, 1 bit            |
| Q1.0        | bit       | Q area, address 1, No. 0 bit            |
| Q1.2        | bit       | Q area, address 1, No. 2 bit            |
| PEPA2.1     | bit       | PEPA area, address 2，No. 1 bit         |
| PEPA2.2     | bit       | PEPA area, address 2，No. 2 bit         |
| T3.3        | bit       | T area, address 3, No. 3 bit            |
| T3.4        | bit       | T area, address 3, No. 4 bit            |
| Z4.5        | bit       | Z area, address 4，No. 5 bit            |
| Z4.6        | bit       | Z area, address 4，No. 6 bit            |
| DB1.DBW10.1 | bit       | DB area, address 1，start 10，No. 1 bit |
| DB2.DBW1.15 | bit       | DB area, address 2，start 10，No. 1 bit |

#### .LEN

When the data type is string type, it is a required item, indicating the length of the string.

*Example：*

| Address      | Data Type | Description                                    |
| ------------ | --------- | ---------------------------------------------- |
| DB1.DBW12.20 | string    | DB area, address 1，start 12，string length 20 |



## HJ212-2017

HJ212-2017 is mainly used to read data that supports the HJ212-2017 standard, this driver only supports active uploading of data by the device.

### Parameter Setting(Ethernet)

| 字段        | 说明                                                         |
| ----------- | ------------------------------------------------------------ |
| **timeout** | 向设备发送请求超时时间                                       |
| **host**    | 当 Neuron 作为客户端使用时，host 指远程设备的 IP。当 Neuron 作为服务端使用时，host 指 Neuron 在本地使用的 IP，默认可填写 0.0.0.0 |
| **port**    | 当 Neuron 作为客户端使用时，post 指远程设备的 TCP 端口。当 Neuron 作为服务端使用时，host 指 Neuron 在本地使用的 TCP 端口，默认为 502 |

### Parameter Setting(Serial)

| 字段        | 说明                             |
| ----------- | -------------------------------- |
| **device**  | 使用串口设备，例如“/dev/ttyUSB0” |
| **stop**    | 停止位，默认值是 1               |
| **parity**  | 校验位，默认值是 2，代表偶校验   |
| **baud**    | 波特率，默认值是 9600            |
| **data**    | 数据位，默认值是 8               |
| **timeout** | 向设备发送请求超时时间           |

### Data Type

* STRING
* DOUBLE
* UINT8
* INT8



### Address Format

#### Pollutant real-time data

> RT!xxxx-[Rtd\][Flag\][SampleTime\][EFlag]</span>

| Address              | Type   | Description                    |
| -------------------- | ------ | ------------------------------ |
| RT!w01018-Rtd        | double | w01018 real-time data          |
| RT!w01018-Flag       | string | w01018 real-time data flag     |
| RT!w01018-SampleTime | string | w01018 real-time sampling time |
| RT!w01018-EFlag      | string | w01018 device flag             |
| RT!w01018-ZsRtd      | double | w01018 real-time zs data       |

#### Pollutant minute data

> MIN!xxxx-[Cou\][Min\][Avg\][Max\][Flag]

| 地址             | 类型   | 说明                    |
| ---------------- | ------ | ----------------------- |
| MIN!w01018-Cou   | double | w01018 cumulative value |
| MIN!w01018-Min   | double | w01018 min value        |
| MIN!w01018-Avg   | double | w01018 average value    |
| MIN!w01018-Max   | double | w01018 max value        |
| MIN!w01018-Flag  | string | w01018 data flag        |
| MIN!w01018-ZsMin | double | w01018 min zs value     |
| MIN!w01018-ZsAvg | double | w01018 average zs value |
| MIN!w01018-ZsMax | double | w01018 max zs value     |

#### Pollutant hour data

> HOUR!xxxx-[Cou\][Min\][Avg\][Max\][Flag]

| 地址              | 类型   | 说明                    |
| ----------------- | ------ | ----------------------- |
| HOUR!w01018-Cou   | double | w01018 cumulative value |
| HOUR!w01018-Min   | double | w01018 min value        |
| HOUR!w01018-Avg   | double | w01018 average value    |
| HOUR!w01018-Max   | double | w01018 max value        |
| HOUR!w01018-Flag  | string | w01018 data flag        |
| HOUR!w01018-ZsMin | double | w01018 min zs value     |
| HOUR!w01018-ZsAvg | double | w01018 average zs value |
| HOUR!w01018-ZsMax | double | w01018 max zs value     |

#### Pollutant day data

> DAY!xxxx-[Cou\][Min\][Avg\][Max\][Flag]

| 地址             | 类型   | 说明                    |
| ---------------- | ------ | ----------------------- |
| DAY!w01018-Cou   | double | w01018 cumulative value |
| DAY!w01018-Min   | double | w01018 min value        |
| DAY!w01018-Avg   | double | w01018 average value    |
| DAY!w01018-Max   | double | w01018 max value        |
| DAY!w01018-Flag  | string | w01018 data flag        |
| DAY!w01018-ZsMin | double | w01018 min zs value     |
| DAY!w01018-ZsAvg | double | w01018 average zs value |
| DAY!w01018-ZsMax | double | w01018 max zs value     |

## IEC61850

The iec61850 plug-in is used to read/write to the IEC61850 server, and currently only supports MMS protocol access.

### Parameter Setting

| Parameter | Description                                   |
| --------- | --------------------------------------------- |
| **host**  | IP of the remote device                       |
| **port**  | The port of the remote device, default is 102 |

### Support Data Type

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

### Address Format

> Logical Devices/Logical Nodes$FC$DO$DA</span>

*Example：*

| Address                               | Data Type | **Description**                                      |
| ------------------------------------- | --------- | ---------------------------------------------------- |
| GenericIO/GGIO1$CF$Mod$ctlModel       | int8      | LD-GenericIO,LN-GGIO1,FC-CF,DO-Mod,DA-ctlModel       |
| GenericIO/GGIO1$CO$SPCSO1$Oper$ctlNum | uint8     | LD-GenericIO,LN-GGIO1,FC-CO,DO-SPCSO1,DA-Oper$ctlNum |
| GenericIO/GGIO1$CF$SPCSO1$ctlModel    | int16     | LD-GenericIO,LN-GGIO1,FC-CF,DO-SPCSO1,DA-ctlModel    |
| GenericIO/GGIO1$CO$SPCSO2$Oper$ctlNum | uint16    | LD-GenericIO,LN-GGIO1,FC-CO,DO-SPCSO2,DA-Oper$ctlNum |
| GenericIO/GGIO1$CF$SPCSO2$ctlModel    | int32     | LD-GenericIO,LN-GGIO1,FC-CF,DO-SPCSO2,DA-ctlModel    |
| GenericIO/GGIO1$ST$SPCSO4$Oper$ctlNum | uint32    | LD-GenericIO,LN-GGIO1,FC-ST,DO-SPCSO4,DA-Oper$ctlNum |
| GenericIO/GGIO1$CF$SPCSO3$ctlModel    | int64     | LD-GenericIO,LN-GGIO1,FC-CF,DO-SPCSO3,DA-ctlModel    |
| GenericIO/GGIO1$ST$SPCSO1$ctlNum      | uint64    | LD-GenericIO,LN-GGIO1,FC-ST,DO-SPCSO1,DA-ctlNum      |
| GenericIO/GGIO1$MX$AnIn1$mag$f        | float     | LD-GenericIO,LN-GGIO1,FC-MX,DO-AnIn1,DA-mag$f        |
| GenericIO/GGIO1$MX$AnIn3$mag$f        | double    | LD-GenericIO,LN-GGIO1,FC-MX,DO-AnIn3,DA-mag$f        |
| GenericIO/GGIO1$CO$SPCSO1$Oper$Test   | bool      | LD-GenericIO,LN-GGIO1,FC-CO,DO-SPCSO1,DA-Oper$Test   |
| GenericIO/LLN0$DC$NamPlt$vendor       | string    | LD-GenericIO,LN-GGIO1,FC-DC,DO-NamPlt,DA-vendor      |
