# Application And Driver Instructions

This document introduces how to setup parameter and data tag point information in configuration for northbound applications and southbound drivers.

**!** uint16 corresponds to the word type. uint32 corresponds to dword type.

## MQTT

The data collected from the device can be transmitted to the mqtt broker through mqtt application, and instructions can be sent to neuron throuth mqtt application.

### Parameter Setting

| Parameter        | Description                                                  |
| ---------------- | ------------------------------------------------------------ |
| **client-id**    | MQTT client ID, required                                     |
| **upload-topic** | Subscription data reporting channel, optional, if not set, the data will be reported under `neuron/{client-id}/upload` |
| **format**       | The json format selection of the reported data, required, there are values mode and tags mode, the default is values mode |
| **ssl**          | Whether to enable mqtt ssl, default false                    |
| **host**         | MQTT Broker host, required                                   |
| **port**         | MQTT Broker port number, required                            |
| **username**     | Username to use when connecting to the broker, optional      |
| **password**     | The password to use when connecting to the broker, optional  |
| **ca**           | ca file, only enabled when the ssl value is true, in which case it is required |
| **cert**         | cert file, only enabled when the ssl value is true, optional |
| **key**          | key file, only enabled when the ssl value is true, optional  |
| **keypass**      | key file password, only enabled when the ssl value is true, optional |

### Error Codes

| 错误码 | 说明                                                         |
| ------ | ------------------------------------------------------------ |
| 4005   | MQTT client creation failed, usually caused by system reasons |
| 4007   | Failed to connect to Broker, possible reasons include connection parameter configuration error or network abnormality (usually temporary) |
| 4010   | Failed to subscribe Topic, usually before the connection is successful, it will be automatically re-subscribed after the connection is successful |
| 4013   | Failed to unsubscribe topic                                  |
| 4014   | Publish fails, usually due to a connection exception. In the current implementation, the failed data will be discarded |
| 4015   | Publish suspended due to user stopping plugin                |
| 4016   | Publish data exceeds buffer length, usually does not happen  |

## eKuiper

Use the eKuiper plugin to stream processing of data collected by Neuron, for detailed usage process,please refer to [Integration of Neuron and eKuiper](https://github.com/lf-edge/ekuiper/blob/master/docs/en_US/tutorials/neuron/neuron_integration_tutorial.md).

## Modbus

The modbus protocol includes three drivers: modbus RTU, modbus tcp, and modbus RTU over TCP.

### Parameter Setting

| Parameter     | Description                  |
| ------------- | ---------------------------- |
| **connection mode** | The way the driver connects to the device, the default is client, which means that the neuron driver is used as the client       |
| **host**            | When neuron is used as a client, host means the ip of the remote device. When used as a server, it means the ip used by neuron locally, and 0.0.0.0 can be filled in by default    |
| **port**           | When neuron is used as client, port means the tcp port of the remote device. When used as a server, it means the tcp port used by neuron locally. default 502    |

### Support Data Type

* INT16
* INT32
* UINT16
* UINT32
* FLOAT
* BIT
* STRING

### Address Format

> SLAVE!ADDRESS\[.BIT][#ENDIAN]\[.LEN\[H]\[L]\[D]\[E]]</span>

#### **SLAVE**

Required, Slave is the slave address or site number.

#### **ADDRESS**

Required,  Address is the register address.The Modbus protocol has four areas, each area has a maximum of 65536 registers, and the address range of each area is shown in the table below. It should be noted that the storage area as large as 65536 is generally not required in practical applications. Generally, PLC manufacturers generally use an address range within 10000. Please pay attention to fill in the correct point address according to the area and function code of the device.

| AREA           | ADDRESS RANGE   | ATTRIBUTE  | REGISTER SIZE | FUNCTION     | DATA TYPE  |
| -------------- | --------------- | ---------- | ------------- | ------------ | ---------- |
| coil           | 000001 ~ 065536 | read/write | 1bit          | 0x1,0x5,0x0f | bit        |
| input          | 100001 ~ 165536 | read       | 1bit          | 0x2          | bit        |
| input register | 300001 ~ 365536 | read       | 16bit         | 0x4          | bit,int16,uint16,int32,uint32,float,string |
| hold register  | 400001 ~ 465536 | read/write | 16bit         | 0x3,0x6,0x10 | bit,int16,uint16,int32,uint32,float,string |

**!** Some device documents use function codes and register addresses to describe instructions. Because register address numbers start from 0, the register address range for each region is 0 to 65535. First, determine the highest digit of the address according to the function code, and add 1 to the register address as the address of Neuron.

example, function is 0x03, and register address is 0, then address used by neuron is 400001. function is 0x02, and register address is 5, then address used by neuron is 100006.

#### **.BIT**

Optional, a bit of a register address, for example:
| Address     | Data Type | Description                                                 |
| ----------- | --------- | --------------------------------------------------- |
| 1!300004.0  | bit     | Refers to station number 1, input area, address 300004, bit 0    |
| 1!400010.4  | bit     | Refers to station number 1, hold register area, address 400010, bit 4    |
| 2!400001.15 | bit     | Refers to station number 2, hold register area, address 400001, bit 15   |

#### **#ENDIAN**

Optional, endianness, applicable to int16/uint16/int32/uint32/float data types, see the table below for details.
| Symbol     | endianness | Data Type | Remark                       |
| ---------- | --------- | ----------------------- | ----- |
| #B         | 2,1       | int16/uint16            |       |
| #L         | 1,2       | int16/uint16            | Leave blank, default byte order |
| #LL        | 1,2,3,4   | int32/uint32/float      | Leave blank, default byte order |
| #LB        | 2,1,4,3   | int32/uint32/float      | |
| #BB        | 3,4,1,2   | int32/uint32/float      | |
| #BL        | 4,3,2,1   | int32/uint32/float      | |

*E.g*
| Address     | Data Type  | Description       |
| ----------- | -------- | --------- |
| 1!300004    | int16    | Refers to station number 1, input area, address 300004, endianness is #L |
| 1!300004#B  | int16    | Refers to station number 1, input area, address 300004, endianness is #B |
| 1!300004#L  | uint16   | Refers to station number 1, input area, address 300004, endianness is #L |
| 1!400004    | int16    | Refers to station number 1, hold register area, address 400004, endianness is #L |
| 1!400004#L  | int16    | Refers to station number 1, hold register area, address 400004, endianness is #L  |
| 1!400004#B  | uint16   | Refers to station number 1, hold register area, address 400004, endianness is #B |
| 1!300004    | int32    | Refers to station number 1, input area, address 300004, endianness is #LL |
| 1!300004#BB | uint32   | Refers to station number 1, input area, address 300004, endianness is #BB |
| 1!300004#LB | uint32   | Refers to station number 1, input area, address 300004, endianness is #LB |
| 1!300004#BL | float    | Refers to station number 1, input area, address 300004, endianness is #BL |
| 1!300004#LL | int32    | Refers to station number 1, input area, address 300004, endianness is #LL |
| 1!400004    | int32    | Refers to station number 1, hold register area, address 400004, endianness is #LL |
| 1!400004#LB | uint32   | Refers to station number 1, hold register area, address 400004, endianness is #LB |
| 1!400004#BB | uint32   | Refers to station number 1, hold register area, address 400004, endianness is #BB |
| 1!400004#LL | int32    | Refers to station number 1, hold register area, address 400004, endianness is #LL |
| 1!400004#BL | float    | Refers to station number 1, hold register area, address 400004, endianness is #BL |

#### .LEN\[H]\[L]\[D]\[E]

When the data type is string type, **.LEN** is a required, indicating the length of bytes that the string needs to occupy. Each register contains **H**, **L**, **D** and **E** four storage methods, as shown in the table below.
| Symbol | Description                                  |
| --- | ------------------------------------- |
| H   | A register stores two bytes, the high byte is in front of the low byte |
| L   | A register stores two bytes, the low byte is in front of the high byte |
| D   | A register stores one byte, and is stored in the low byte      |
| E   | A register stores one byte, and is stored in the high byte      |

*E.g*
| Address     | Data Type | Description |
| ----------- | ------- | --------- |
| 1!300001.10  | String  | Refers to station number is 1, input area, the address is 300001, the string length is 10, and endianness is L, the occupied address is 300001-300005 |
| 1!300001.10H | String  | Refers to station number is 1, input area, the address is 300001, the string length is 10, and endianness is H, the occupied address is 300001-300005 |
| 1!300001.10L | String  |  Refers to station number is 1, input area, the address is 300001, the string length is 10, and endianness is L, the occupied address is 300001-300005 |
| 1!400001.10  | String  | Refers to station number is 1, input area, the address is 400001, the string length is 10, and endianness is L, the occupied address is 400001-400005 |
| 1!400001.10H | String  | Refers to station number is 1, input area, the address is 400001, the string length is 10, and endianness is H, the occupied address is400001 ～ 400005 |
| 1!400001.10L | String  | Refers to station number is 1, input area, the address is 400001, the string length is 10, and endianness is L, the occupied address is 400001-400005  |
| 1!400001.10D | String  | Refers to station number is 1, input area, the address is 400001, the string length is 10, and endianness is D, the occupied address is 400001-400010 |
| 1!400001.10E | String  | Refers to station number is 1, input area, the address is 400001, the string length is 10, and endianness is E, the occupied address is 400001-400010 |

## OPC UA

### Parameter Setting

| Parameter         | Description                      |
| ----------------- | -------------------------------- |
| **endpoint url**  | The address of the remote access plc, the default value is `opc.tcp://127.0.0.1:4840/` |
| **username**      | The user used when connecting to plc                                 |
| **password**      | The password used when connecting to plc                             |
| **cert-file**     | The certificate to provide login user authentication                 |
| **key-file**      | The private key to provide signature and encrypted transmission.s    |

### Support Data Type

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
* STRING

### Addresses Format

> IX!NODEID</span>

**IX** is the namespace index.

**NODEID** is the node id.

*E.g*

* 2!Device1.Module1.Tag1 represents namespace index is 2 and node ID is Device1.Module1.Tag

**!** Please refer to OPC UA standard for the explanation of namespace index and node id.

## Siemens S7 ISOTCP

The s7comm plugin is used for Siemens PLCs with network port, such as s7-200/300/400/1200/1500.

### Parameter Setting

| Parameter         | Description                      |
| ----------------- | -------------------------------- |
| **host** | remote plc ip                 |
| **ip**   | remote plc port, default 102  |
| **rack** | plc rack number, default 0       |
| **slot** | plc cpu slot, default 1          |

**!**  When using the S7COMM plugin to access the S7 1200/1500 PLC,  you need to use Siemens software(TIA16) to make some settings for the PLC.( For detailed settings, please refer to [plc-settings](./plc-settings/siemens-s7-1200-1500.md). )

* The optimized block access must be turned off.
* The access level must be "full" and the "connection mechanism" must allow GET/PUT.

### Support Data Type

* INT16
* UINT16
* INT32
* UINT32
* FLOAT
* DOUBLE
* BIT
* STRING

### Address Format

> AREA ADDRESS\[.BIT][.LEN]</span>

#### AREA ADDRESS

| AREA | DATA TYPE                                         | ATTRIBUTE  | REMARK          |
| ---- | ------------------------------------------------- | ---------- | --------------- |
| I    | int16/uint16/bit                                  | read       | input           |
| O    | int16/uint16/bit                                  | read/write | output          |
| F    | int16/uint16/bit                                  | read/write | flag            |
| T    | int16/uint16/bit                                  | read/write | timer           |
| C    | int16/uint16/bit                                  | read/write | counter         |
| DB   | int16/uint16/bit/int32/uint32/float/double/string | read/write | global DB block |

*E.g*
| Address | Data Type | Description  |
| ------ | ------- | -------- |
| I0         | int16   | I area, address is 0 |
| I1         | uint16  | I area, address is 1 |
| O2         | int16   | O area, address is 2 |
| O3         | uint16  | O area, address is 3 |
| F4         | int16   | F area, address is 0 |
| F5         | int16   | F area, address is 0 |
| T6         | int16   | T area, address is 0 |
| T7         | int16   | T area, address is 0 |
| C8         | uint16  | C area, address is 0 |
| C9         | uint16  | C area, address is 0 |
| DB10.DBW10 | int16   | In a data block of 10 , the starting data word is 10 |
| DB12.DBW10 | uint16  | In a data block of 12 , the starting data word is 10 |
| DB10.DBW10 | float   | In a data block of 10 , the starting data word is 10 |
| DB11.DBW10 | double  | In a data block of 11 , the starting data word is 10 |

#### .BIT

Optional, referring to a bit of an address.

*E.g*

| Address     | Data Type | Description             |
| ----------- | ------- | ------------------------- |
| I0.0        | bit     | I area, address 0, bit 0  |
| I0.1        | bit     | I area, address 0, bit 1  |
| O1.0        | bit     | O area, address 1, bit 0  |
| O1.2        | bit     | O area, address 1, bit 2  |
| F2.1        | bit     | F area, address 2, bit 1  |
| F2.2        | bit     | F area, address 2, bit 2  |
| T3.3        | bit     | T area, address 3, bit 3  |
| T3.4        | bit     | T area, address 3, bit 4  |
| C4.5        | bit     | C area, address 4, bit 5  |
| C4.6        | bit     | C area, address 4, bit 6  |
| DB1.DBW10.1 | bit     | In a data block of 1 , the starting data word is 10, bit 0   |
| DB2.DBW1.15 | bit     | In a data block of 2 , the starting data word is 1, bit 15  |

#### .LEN

When the data type is a string type, it is required and indicates the length of the string.

*E.g*

| Address     | Data Type | Description             |
| ----------- | ------- | ------------------------- |
| DB1.DBW12.20 | string  | In a data block of 1 , the starting data word is 12, string length is 20 |

## OMRON FINS on TCP

The fins plugin is used for Omron PLCs with network port, such as CP2E.

### Parameter Setting

| Parameter         | Description                      |
| ----------------- | -------------------------------- |
| **host**          | remote plc ip                 |
| **port**          | remote plc port, default 9600 ｜

### Support Data Type

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

### Address Format

> AREA ADDRESS\[.BIT]\[.LEN\[H]\[L]]</span>

#### AREA ADDRESS

| AREA | DATA TYPE                                                 | ATTRIBUTE  | REMARK           |
| ---- | --------------------------------------------------------- | ---------- | ---------------- |
| CIO  | All types except uint8/int8                               | read/write | CIO Area         |
| A    | All types except uint8/int8                               | read       | Auxiliary Area   |
| W    | All types except uint8/int8                               | read/write | Work Area        |
| H    | All types except uint8/int8                               | read/write | Holding Area     |
| D    | All types except uint8/int8                               | read/write | Data Memory Area |
| P    | All types except uint8/int8, but bit only supports read   | read/write | PVs              |
| F    | int8/uint8                                                | read       | Completion Flag  |
| EM   | All types except uint8/int8                               | read/write | Extended Memory  |

*E.g*

| Address     | Data Type  | Description          |
| ------- | ------- | --------------- |
| F0      | uint8  | F area, address is 0   |
| F1      | int8   | F area, address is 1   |
| CIO1    | int16  | CIO area, address is 1 |
| CIO2    | uint16 | CIO area, address is 2 |
| A2      | int32  | A area, address is 2   |
| A4      | uint32 | A area, address is 4   |
| W5      | float  | W area, address is 5   |
| W10     | float  | W area, address is 10   |
| H20     | double | H area, address is 20   |
| H30     | uint32 | H area, address is 30   |
| D10     | int32  | D area, address is 10   |
| D20     | float  | D area, address is 20   |
| EM10    | float  | EM area, address is 10   |

#### .BIT

Optional, referring to a bit of an address.

*E.g*
| Address     | Data Type  | Description          |
| ------- | ------- | --------------- |
| CIO0.0   | bit | CIO area, address is 0, bit 0  |
| CIO1.2   | bit | CIO area, address is 1, bit 2  |
| A2.1     | bit | A area, address is 2, bit 1    |
| A2.3     | bit | A area, address is 2, bit 3    |
| W3.4     | bit | W area, address is 3, bit 4    |
| W3.0     | bit | W area, address is 3, bit 0    |
| H4.15    | bit | H area, address is 4, bit 15    |
| H4.10    | bit | H area, address is 4, bit 10    |
| D5.2     | bit | D area, address is 5, bit 2    |
| D5.3     | bit | D area, address is 5, bit 3    |
| EM10.0   | bit | EM area, address is 10, bit 0  |

#### .LEN\[H]\[L]

When the data type is string type, it is a required, **.LEN** indicates the length of the string, including **H** and **L** two endianness, the default is **H** .

*E.g*

| Address   | Data Type  | Description                                             |
| --------- | ------ | ----------------------------------------------------------- |
| CIO0.20   | string | CIO area, address 0, the string length is 20 bytes and the endianness is L  |
| CIO1.20H  | string | CIO area, address 1, the string length is 20 bytes and the endianness is H  |
| A2.10L    | string | A area, address 2, the string length is 10 bytes and the endianness is L  |
| A2.30     | string | A area, address 2, the string length is 30 bytes and the endianness is L  |
| W3.40H    | string | W area, address 3, the string length is 40 bytes and the endianness is H  |
| W3.10     | string | W area, address 3, the string length is 10 bytes and the endianness is L  |
| H4.15L    | string | H area, address 4, the string length is 15 bytes and the endianness is L  |
| H4.10     | string | H area, address 4, the string length is 10 bytes and the endianness is L  |
| D5.20H    | string | D area, address 5, the string length is 20 bytes and the endianness is H  |
| D5.30     | string | D area, address 5, the string length is 30 bytes and the endianness is L  |
| EM10.10   | string | EM area, address 10, the string length is 10 bytes and the endianness is L  |

## Mitsubishi MELSEC-Q E71

The qna3e plugin is used to access Mitsubishi's QnA compatible PLCs via Ethernet, including Q series (MC), iQ-F series (SLMP) and iQ-L series.

### Parameter Setting

| Parameter | Description |
| -------- | -------------------------- |
| **host** | remote plc ip                 |
| **ip**   | remote plc port, default 2000 |

### Support Data Type

* INT16
* UINT16
* INT32
* UINT32
* FLOAT
* DOUBLE
* BIT
* STRING

### Address Format

> AREA ADDRESS\[.BIT]\[.LEN\[H]\[L]]</span>

#### AREA ADDRESS

| AREA | DATA TYPE | ATTRIBUTE  | REMARK                           |
| ---- | --------- | ---------- | -------------------------------- |
| X    | bit       | read/write | Input relay (Q/iQ-F)             |
| DX   | bit       | read/write | (Q/iQ-F)                         |
| Y    | bit       | read/write | Output relay (Q/iQ-F)            |
| DY   | bit       | read/write | (Q/iQ-F)                         |
| B    | bit       | read/write | Link relay (Q/iQ-F)              |
| SB   | bit       | read/write | Link special relay               |
| M    | bit       | read/write | Internal relay (Q/iQ-F)          |
| SM   | bit       | read/write | Special relay (Q/iQ-F)           |
| L    | bit       | read/write | Latch relay (Q/iQ-F)             |
| F    | bit       | read/write | Annunciator (Q/iQ-F)             |
| V    | bit       | read/write | Edge relay (Q/iQ-F)              |
| S    | bit       | read/write | (Q/iQ-F)                         |
| TS   | bit       | read/write | Timer Contact (Q/iQ-F)           |
| TC   | bit       | read/write | Timer Coil (Q/iQ-F)              |
| SS   | bit       | read/write | (Q/iQ-F)                         |
| STS  | bit       | read/write | Retentive timer Contact (Q/iQ-F) |
| SC   | bit       | read/write | (Q/iQ-F)                         |
| CS   | bit       | read/write | Counter Contact (Q/iQ-F)         |
| CC   | bit       | read/write | Counter Coil (Q/iQ-F)            |
| TN   | all       | read/write | Timer Current value (Q/iQ-F)     |
| STN  | all       | read/write | Retentive timer (Q/iQ-F)         |
| SN   | all       | read/write | (Q/iQ-F)                         |
| CN   | all       | read/write | Counter Current value  (Q/iQ-F)  |
| D    | all       | read/write | Data register (Q/iQ-F)           |
| DSH  | --        |            |                                  |
| DSL  | --        |            |                                  |
| SD   | all       | read/write | Specical register (Q/iQ-F)       |
| W    | all       | read/write | Link register (Q/iQ-F)           |
| WSH  | --        |            |                                  |
| WSL  | --        |            |                                  |
| SW   | all       | read/write | Link special register (Q/iQ-F)   |
| R    | all       | read/write | File register (Q/iQ-F)           |
| ZR   | all       | read/write | File register (Q/iQ-F)           |
| RSH  | --        |            |                                  |
| ZRSH | --        |            |                                  |
| RSL  | --        |            |                                  |
| ZRSL | --        |            |                                  |
| Z    | all       | read/write | Index register (Q/iQ-F)          |

*E.g*

| Address     | Data Type  | Description          |
| ------- | ------- | --------------- |
| X0    | bit     | X area, address is 0    |
| X1    | bit     | X area, address is 1    |
| Y0    | bit     | Y area, address is 0    |
| Y1    | bit     | Y area, address is 1    |
| D100  | int16   | D area, address is 100  |
| D1000 | uint16  | D area, address is 1000 |
| D200  | uint32  | D area, address is 200  |
| D10   | float   | D area, address is 10   |
| D20   | double  | D area, address is 20   |

#### .BIT

It can only be used in **non-bit type area**, which means to read the specified bit of the specified address, and the binary bit index range is [0, 15].

| Address | Data Type | Description |
| ------- | --------- | --------- |
| D20.0 | bit | D area, address is 20, bit 0   |
| D20.2 | bit | D area, address is 20, bit 2   |

#### .LEN\[H]\[L]

When the data type is string, **.LEN** indicates the length of the string;   **H** and **L** can be optional to indicate two byte orders, the default is **H** byte order.
*E.g*

| Address     | Data Type  | Description          |
| ------- | ------- | --------------- |
| D1002.16L | string  | D area, address is 1002, string length is 16, endianness is L |
| D1003.16 | string  | D area, address is 1003, string length is 16, endianness is H |

## IEC 60870-5-104

### Parameter Setting

| Parameter   | Description  |
| ------------ | ------------- |
| **host**     | device ip |
| **port**     | device port, default 2404 |
| **ca**       | common address |
| **interval** | station interrogation interval |

### Support Data Type

* uint16
* int16
* float
* bit

### Address Format

> IOA</span>

| IEC 60870-5-104  TYPEID         | NEURON TYPE  |
| ------------------------------- | ------------ |
| M_ME_NB_1、M_ME_TE_1            | uint16/int16 |
| M_ME_NC_1、M_ME_TF_1            | float        |
| M_SP_NA_1、M_SP_TB_1            | bit          |
| M_ME_NA_1、M_ME_TD_1、M_ME_ND_1 | uint16/int16 |

## KNXnet/IP

### Support Data Type

* bit
* bool
* int8
* uint8
* int16
* uint16
* float

### Address Format

Two address formats

* > GROUP_ADDRESS</span>

Represents the KNX group address, which can only be written in Neuron, and KNX devices belonging to this group will react to messages sent to this group.

*E.g*

`0/0/1` is a KNX group address and is write only in Neuron, KNX devices belonging to this group will react to messages sent to this group.

* > GROUP_ADDRESS,INDIVIDUAL_ADDRESS</span>

代表 KNX 组下的设备地址，只能在 Neuron 中读取。

 Represents a KNX individual address that is a member of the group address, and is read only in Neuron.

*E.g*

`0/0/1,1.1.1` represents a KNX individual address `1.1.1` that is a member
  of the group address `0/0/1`, and is read only in Neuron.

## BACnet/IP

### Parameter Setting

| Parameter      | Description                     |
|--------- | ------------------------------------- |
| **host** | BACnet device ip                   |
| **port** | BACnet device port, default 47808  |

### Support Data Type

* float
* bit

### Address Format

> AREA[ADDRESS]</span>

| AREA | ADDRESS RANGE | ATTRIBUTE  | DADA TYPE  | REMARK             |
| ---- | ------------- | ---------- | ------------- | ------------------ |
| AI   | 0 - 0x3fffff  | read       | float     | analog input       |
| AO   | 0 - 0x3fffff  | read/write | float     | analog output      |
| AV   | 0 - 0x3fffff  | read/write | float     | analog value       |
| BI   | 0 - 0x3fffff  | read       | bit       | binary input       |
| BO   | 0 - 0x3fffff  | read/write | bit       | binary output      |
| BV   | 0 - 0x3fffff  | read/write | bit       | binary value       |
| MSI  | 0 - 0x3fffff  | read       | bit       | multi state input  |
| MSO  | 0 - 0x3fffff  | read/write | bit       | multi state output |
| MSV  | 0 - 0x3fffff  | read/write | bit       | multi state value  |

*E.g*

| Address     | Data Type  | Description          |
| ------- | ------- | --------------- |
| AI0    | float   | AI area, address is 0  |
| AI1    | float   | AI area, address is 1  |
| BO10   | float   | BO area, address is 10 |
| BO20   | float   | BO area, address is 20 |
| AV30   | float   | AV area, address is 30 |
| BI0    | bit     | BI area, address is 0  |
| BI1    | bit     | BI area, address is 1  |
| BV3    | bit     | BV area, address is 3  |
| MSI10  | bit     | MAI area, address is 10 |
| MSI20  | bit     | MSI area, address is 20 |
| MSI30  | bit     | MSI area, address is 30 |
