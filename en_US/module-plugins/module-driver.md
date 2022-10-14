# Module Setting

This document introduces how to setup parameter and data tag point information in configuration for northbound applications and southbound drivers.

::: tip
uint16 corresponds to the word type. uint32 corresponds to dword type.
:::

## MQTT

The data collected from the device can be transmitted to the mqtt broker through mqtt application, and instructions can be sent to neuron throuth mqtt application.

### Parameter Setting

| Parameter           | Description                                                  |
| ------------------- | ------------------------------------------------------------ |
| **upload-topic**    | Subscription data reporting channel, required                |
| **heartbeat-topic** | The channel for heartbeat data reporting, required           |
| **format**          | The json format selection of the reported data, required, there are values mode and tags mode, the default is values mode |
| **cache**           | When the MQTT connection is abnormal, the size limit of the upload data cache |
| **ssl**             | Whether to enable mqtt ssl, default false                    |
| **host**            | MQTT Broker host, required                                   |
| **port**            | MQTT Broker port number, required                            |
| **username**        | Username to use when connecting to the broker, optional      |
| **password**        | The password to use when connecting to the broker, optional  |
| **ca**              | ca file, only enabled when the ssl value is true, in which case it is required |
| **cert**            | cert file, only enabled when the ssl value is true, optional |
| **key**             | key file, only enabled when the ssl value is true, optional  |
| **keypass**         | key file password, only enabled when the ssl value is true, optional |

## Modbus

The modbus protocol includes three drivers: modbus RTU, modbus tcp, and modbus RTU over TCP.Except for the device configuration, the three protocols support the same data types and address formats.

### Modbus TCP / Modbus RTU over TCP Parameter Setting

| Parameter     | Description                  |
| ------------- | ---------------------------- |
| **connection mode** | The way the driver connects to the device, the default is client, which means that the neuron driver is used as the client       |
| **host**            | When neuron is used as a client, host means the ip of the remote device. When used as a server, it means the ip used by neuron locally, and 0.0.0.0 can be filled in by default    |
| **port**           | When neuron is used as client, port means the tcp port of the remote device. When used as a server, it means the tcp port used by neuron locally. default 502    |
| **timeout**         | Timeout for sending requests to the device                                   |

### Modbus RTU Parameter Setting

| Parameter   | Description                                         |
| ----------- | --------------------------------------------------- |
| **device**  | Use a serial device, e.g."/dev/ttyUSB0"             |
| **stop**    | stopbits, default 1                                 |
| **parity**  | parity bit, default 2, which means even parity      |
| **baud**    | baudrate, default 9600                              |
| **data**    | bytesize, default 8                                 |
| **timeout**   | Timeout for sending requests to the device        |

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

::: tip
Some device documents use function codes and register addresses to describe instructions. Because register address numbers start from 0, the register address range for each region is 0 to 65535. First, determine the highest digit of the address according to the function code, and add 1 to the register address as the address of Neuron.
:::

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

*Example:*

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

*Example:*

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

| Parameter        | Description                                                  |
| ---------------- | ------------------------------------------------------------ |
| **endpoint url** | The address of the remote access plc, the default value is `opc.tcp://127.0.0.1:4840/` |
| **username**     | The user used when connecting to plc                         |
| **password**     | The password used when connecting to plc                     |
| **cert**         | The certificate to provide login user authentication         |
| **key**          | The private key to provide signature and encrypted transmissions |

Authentication mode:

* anonymos, requires OPCUA server to enable anonymous login;
* username-password, The OPCUA server needs to create a username with access permission. Neuron will automatically match the security Settings of OPCUA server and try to log in.
* cert-key + anonymos, which requires OPCUA server to enable appropriate security settings and set certificates, and **enable anonymous login**;
* cert-key + username-password, the OPCUA server must have created a username with access permission, and enable appropriate security Settings and set the certificate;

### Certificate Setting

OPCUA can login to OPC-UA server by user self-signed certificate, certificate and key must meet the following conditions.

* CERTIFICATE and KEYFILE must be set at the same time
* Certificate must be generated by X.509v3 standard
* The SAN field of the Certficate must contain `URI:urn:xxx.xxx.xxx`, with the "xxx" part being a custom part
* Certificate file and key file must be encoded with DER format

The certificate file can be imported into the target server in advance and set as trust, or it can be set by neuron and submitted automatically and then set as trust by the server.

Certificate generation steps(Windows/Linux/Mac):

```sh
$openssl req -config localhost.cnf -new -nodes -x509 -sha256 -newkey rsa:2048 -keyout localhost.key -days 365 -subj "/C=DE/O=neuron/CN=NeuronClient@localhost" -out localhost.crt
$openssl x509 -in localhost.crt -outform der -out client_cert.der
$openssl rsa -inform PEM -in localhost.key -outform DER -out client_key.der
$rm localhost.crt
$rm localhost.key
```

The *.cnf file specified by `-config` can be modified using the [template file for openssl](https://github.com/openssl/openssl/blob/master/apps/openssl.cnf) to be modified to include the following configuration section:

```sh
[ v3_req ]

# Extensions to add to a certificate request

basicConstraints = CA:FALSE
keyUsage = nonRepudiation, digitalSignature, keyEncipherment
subjectAltName = @alt_names

[ alt_names ]
URI.1 = urn:xxx.xxx.xxx
DNS.1 = localhost
#DNS.2 = localhost
IP.1 = 127.0.0.1
#IP.2 = 0.0.0.0
```

`-days` can set the value as desired.

### Certificate conversion

You can convert PEM certificate and private key to DER format by following steps and commands

1. Save all the contents including "-----BEGIN CERTIFICATE-----" and "-----END CERTIFICATE-----" as 1.crt;
2. Save all the contents including "-----BEGIN PRIVATE KEY-----" and "-----END PRIVATE KEY-----" as 1.key;
3. Execute the following command:

```sh
openssl x509 -in 1.crt -outform der -out cert.der   
openssl rsa -inform PEM -in 1.key -outform DER -out key.der
```

### Support Data Type

* INT8 (OPCUA SBYTE type)
* INT16
* INT32
* INT64
* UINT8 (OPCUA BYTE type)
* UINT16
* UINT32 (also used to represent DATETIME types)
* UINT64
* FLOAT
* DOUBLE
* BOOL
* STRING

### Addresses Format

> IX!NODEID</span>

**IX** is the namespace index.

**NODEID** is the node id.

*Example:*

| Address                | Data Type | Description                                                  |
| ---------------------- | --------- | ------------------------------------------------------------ |
| 0!2258                 | UINT32    | Get the timestamp of the OPCUA server using the NODEID of the numeric type.  NS is 0, and NODEID is 2258 |
| 2!Device1.Module1.Tag1 | INT8      | Get a data point of type SBYTE using a NODEID of type string. NS is 2, and NODEID is Device1.module1.tag1 |

::: tip
Please refer to OPC UA standard for the explanation of namespace index and node id.

The data type set by Neuron must match the OPCUA data type.

:::

## Siemens S7 ISOTCP

The s7comm plugin is used for Siemens PLCs with network port, such as s7-200/300/400/1200/1500.

### Parameter Setting

| Parameter         | Description                      |
| ----------------- | -------------------------------- |
| **host** | remote plc ip                 |
| **port** | remote plc port, default 102  |
| **rack** | plc rack number, default 0       |
| **slot** | plc cpu slot, default 1          |

::: tip
When using the S7COMM plugin to access the S7 1200/1500 PLC,  you need to use Siemens software(TIA16) to make some settings for the PLC.( For detailed settings, please refer to [plc-settings](./plc-settings/siemens-s7-1200-1500.md). )
:::

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
| T    | int16/uint16                                      | read/write | timer           |
| C    | int16/uint16                                      | read/write | counter         |
| DB   | int16/uint16/bit/int32/uint32/float/double/string | read/write | global DB block |

*Example:*

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

*Example:*

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

*Example:*

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
| F    | int8/uint8                                                | read       | Flag Area        |
| EM   | All types except uint8/int8                               | read/write | Extended Memory  |

*Example:*

| Address     | Data Type  | Description          |
| ----------- | ------- | ----------------------- |
| F0          | uint8  | F area, address is 0     |
| F1          | int8   | F area, address is 1     |
| CIO1        | int16  | CIO area, address is 1   |
| CIO2        | uint16 | CIO area, address is 2   |
| A2          | int32  | A area, address is 2     |
| A4          | uint32 | A area, address is 4     |
| W5          | float  | W area, address is 5     |
| W10         | float  | W area, address is 10    |
| H20         | double | H area, address is 20    |
| H30         | uint32 | H area, address is 30    |
| D10         | int32  | D area, address is 10    |
| D20         | float  | D area, address is 20    |
| EM10W100    | float  | EM10 area, address is 100 |

#### .BIT

Optional, referring to a bit of an address.

*Example:*

| Address      | Data Type  | Description                       |
| ------------ | ---------- | --------------------------------- |
| CIO0.0       | bit        | CIO area, address is 0, bit 0     |
| CIO1.2       | bit        | CIO area, address is 1, bit 2     |
| A2.1         | bit        | A area, address is 2, bit 1       |
| A2.3         | bit        | A area, address is 2, bit 3       |
| W3.4         | bit        | W area, address is 3, bit 4       |
| W3.0         | bit        | W area, address is 3, bit 0       |
| H4.15        | bit        | H area, address is 4, bit 15      |
| H4.10        | bit        | H area, address is 4, bit 10      |
| D5.2         | bit        | D area, address is 5, bit 2       |
| D5.3         | bit        | D area, address is 5, bit 3       |
| EM10W100.0   | bit        | EM10 area, address is 100, bit 0  |

#### .LEN\[H]\[L]

When the data type is string type, it is a required, **.LEN** indicates the length of the string, including **H** and **L** two endianness, the default is **H** .

*Example:*

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
| **port** | remote plc port, default 2000 |

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

*Example:*

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

*Example:*

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

*Example:*

`0/0/1` is a KNX group address and is write only in Neuron, KNX devices belonging to this group will react to messages sent to this group.

* > GROUP_ADDRESS,INDIVIDUAL_ADDRESS</span>

Represents a KNX individual address that is a member of the group address, and is read only in Neuron.

*Example:*

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

| AREA | ADDRESS RANGE | ATTRIBUTE  | DATA TYPE  | REMARK             |
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

*Example:*

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

## DL/T645-2007

The dlt645 protocol supports serial and tcp connection.

### Parameter Setting

### 设备配置

#### serival

| Parameter         | Description                                         |
| ----------------- | --------------------------------------------------- |
| **mail address**  | Electricity meter communication address             |
| **timeout**       | Timeout for sending requests to the device          |
| **device**        | Use a serial device, e.g. /dev/ttyUSB0             |
| **stop**          | stopbits, default 1                                 |
| **parity**        | parity bit, default 2, which means even parity      |
| **baud**          | baudrate, default 9600                              |
| **data**          | bytesize, default 8                                 |

#### TCP

| Parameter           | Description         |
| ------------------- | ----------------- |
| **mail address**    | Electricity meter communication address             |
| **timeout**         | Timeout for sending requests to the device    |
| **host**            | When neuron is used as a client, host means the ip of the remote device. When used as a server, it means the ip used by neuron locally, and 0.0.0.0 can be filled in by default    |
| **port**            | When neuron is used as client, port means the tcp port of the remote device. When used as a server, it means the tcp port used by neuron locally     |
| **connection mode** | The way the driver connects to the device, the default is client, which means that the neuron driver is used as the client       |

### Supported data types

* UIN8
* UINT16
* UINT32
* UIN64

### Address format

> DI<sub>3</sub>-DI<sub>2</sub>-DI<sub>1</sub>-DI<sub>0</sub> </span>

DI<sub>3</sub>-DI<sub>2</sub>-DI<sub>1</sub>-DI<sub>0</sub> represents the data identification, and all points only support read attributes, and expressed in hexadecimal.

:::tip
Please refer to the DL/T645-2007 industry standard data coding table for the specific data item name corresponding to the data identifier.

* The data length is 1, and the data type is UINT8;
* The data length is 2, and the data type is UINT16;
* The data length is 3 or 4, and the data type is UINT32;
* The data length is 5 or 6 or 7 or 8, and the data type is UINT64;
* The value of Decimal is determined according to the data format;
:::

| DI<sub>3</sub> | DI<sub>2</sub>    | DI<sub>1</sub>   | DI<sub>0</sub>   | Description                             | Type of data | Decimal value | Example                                                         |
| -------------- | ----------------- | ---------------- | --------------- | -------------------------------- | ------- | --------- | ------------------------------------------------------------ |
| 00    | 00 ~ 0A  | 00 ~ 3F | 00 ~ 0C      | DI<sub>3</sub>= 00, representing the electrical energy</br>DI<sub>0</sub>, representing the settlement date               | UINT64  | 0.01 | 00-00-00-00 Representative (current) combined active total energy</br>00-00-00-01 Representative (last settlement date) combined active total energy |
| 00    | 80~86</br>15~1E</br>94~9A</br>29~32</br>A8~AE</br>3D~46</br>BC~C2 | 00      | 00 ~ 0C   | DI<sub>3</sub>= 00, representing the electrical energy</br>DI<sub>0</sub>, representing the settlement date             | UINT64  | 0.01  | 00-80-00-00 Representative (current) total associated power</br>00-80-00-01 Representative (last 1 settlement date) associated total power</br>00-15-00-01 Representative (last 1 settlement date) A-phase positive Active energy</br>00-15-00-01 represents (last 2 settlement days) A-phase forward active energy</br> 00-29-00-02 represents (last 2 settlement days) B-phase forward active energy |
| 02    | 01 ~ 09   | 01 ~ 03  | 00                   | DI<sub>3</sub>= 02, representing the variable                                 | UINT16</br>UINT32 | 0.1</br>0.01</br>0.001</br>0.0001 | 02-01-01-00 Represents A-phase voltage</br>02-02-01-00 Represents A-phase current |
| 02    | 0A ~ 0B   | 01 ~ 03  | 01 ~15               | DI<sub>2</sub>= 0A, representing the voltage harmonic content</br>DI<sub>2</sub> = 0B, representing the current harmonic content</br>DI<sub>1</sub>, representing A, B, C phase</br> DI~0~, representing the th order of harmonic content | UINT16 |  0.01   | 02-0A-01-01 Represents the 1st harmonic content of A-phase voltage</br>02-0A-02-02 represents the 2nd harmonic content of B-phase voltage</br>02-0B-01-01 represents the 1st harmonic content of A-phase current</br>02-0B-02-02 represents the second harmonic content of phase B current |
| 02    | 80        | 00       | 01 ~ 0A              | DI<sub>3</sub>= 02, representing the variable     | UINT16    | 0.01 | 02-80-00-01 Represents zero line current</br>02-80-00-02 Represents grid frequency     |
| 04    | 00        | 01 ~ 0E  | 01 ~ 0C              | DI<sub>3</sub>= 04, representing the parameter  | UINT8</br>UINT16</br>UINT32</br>UINT64  | 0</br>0.1</br>0.001</br>0.0001 | 04-00-01-01 Represents date and time</br>04-00-01-03 represents maximum demand period</br>04-00-04-01 represents communication address</br>04-00-05-01 represents meter running status word 1 |
| 06    | 00 ~ 06   | 00       | 00 ~ 02              | DI<sub>3</sub>= 06, representing the load record  | UINT8</br>UINT64  | 0    | 06-00-00-00 Represents the oldest recorded block</br>06-06-00-00 represents the earliest recorded block of class 6 loads |

## Sparkplug_B

Data collected by Neuron from the device can be transmitted from the edge to the Sparkplug_B application using the Sparkplug_B protocol. Users can also send data modification instructions to Neuron from the application. Sparkplug_B is an application-type protocol that runs on top of MQTT, so the setup in Neuron is similar to the MQTT driver.

### Parameter Setting

| Parameter     | Description                                                  |
| ------------- | ------------------------------------------------------------ |
| **group-id**  | The top-level logical group in Sparkplug_B, which can represent an entity such as a factory or workshop, required |
| **client-id** | MQTT client ID, A unique identifier that can represent the edge end, required |
| **ssl**       | Whether to enable mqtt ssl, default false                    |
| **host**      | MQTT Broker host, required                                   |
| **port**      | MQTT Broker port number, required                            |
| **username**  | Username to use when connecting to the broker, optional      |
| **password**  | The password to use when connecting to the broker, optional  |
| **ca**        | ca file, only enabled when the ssl value is true, in which case it is required |
| **cert**      | cert file, only enabled when the ssl value is true, optional |
| **key**       | key file, only enabled when the ssl value is true, optional  |
| **keypass**   | key file password, only enabled when the ssl value is true, optional |

## NON A11

The non a11 plugin is used for NON-A11 device.

### Parameter Setting

| Parameter       | Description                                                  |
| --------------- | ------------------------------------------------------------ |
| connection mode | The way the driver connects to the device, the default is client, which means that the neuron driver is used as the client |
| host            | When neuron is used as a client, host means the ip of the remote device. When used as a server, it means the ip used by neuron locally, and 0.0.0.0 can be filled in by default |
| port            | When neuron is used as client, port means the tcp port of the remote device. When used as a server, it means the tcp port used by neuron locally. |
| site            | NON-A11 device site number.                                  |

### Support Data Type

* INT16
* UINT16
* INT32
* UINT32
* FLOAT
* STRING

### Address Format

> COMMAND ! OFFSET[.LEN]</span>

*Example:*

| Address | Data Type          | Description                            |
| ------- | ------------------ | -------------------------------------- |
| 1!10.20 | string             | command 1, offset 10, string length 20 |
| 12!1    | uint16/int16       | command 12, offset 1                   |
| 20!32   | uint32/int32/float | command 20, offset 32                  |

## ADS

The ads plugin is used for Beckhoff ADS/AMS devices.

### Parameter Setting

| Parameter       | Description                                                  |
| --------------- | ------------------------------------------------------------ |
| host            | the IP of the remote device.                                 |
| port            | the TCP port of the remote device (default 48898).           |
| src-ams-net-id  | The AMSNetId of the machine running neuron.                  |
| src-ads-port    | The AMSPort of the machine running neuron.                   |
| dst-ams-net-id  | The AMSNetId of the target PLC.                              |
| dst-ads-port    | The AMSPort of the target PLC.                               |

Note that a ADS route corresponding to the parameter setting should created in the
target TC runtime (PLC), so that neuron could correctly communicate with the PLC.

### Support Data Type

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

### Address Format

> INDEX_GROUP,INDEX_OFFSET</span>

Both `INDEX_GROUP` and `INDEX_OFFSET` could be in decimal or hexadecimal format independently.

*Example:*

| Address         | Data Type          | Description                                               |
| --------------- | ------------------ | --------------------------------------------------------- |
| 0x4040,0x7d01c  | bool               | index_group 0x4040, index_offset 0x7d01c                  |
| 16448,51029     | uint8              | index_group 0x4040, index_offset 0x7d01d                  |
| 0x4040,512896.5 | string             | index_group 0x4040, index_offset 0x7d380, string length 5 |

## OPCDA

Neuron can indirectly access the OPCDA server running on Windows operating system through the external helper program opcshift.exe. opcshift converts the DA protocol to the UA protocol, and then obtains data through Neuron's existing opcua driver. All accessible points of the DA are mapped to the "namespace 1" of the UA, and the IDs of the points remain the same.

### Parameter Setting

Install opcshift and the OPCDA access dependency package opc-core-components-redistributables , open the opcshift.ini file with a text editor, fill in the configuration information, and then run opcshift.exe. Create a new OPCUA node in Neuron, and fill in the corresponding ua.port in opcshift.ini and the IP address of opcshift.

| Parameter    | Description                                                  |
| ------------ | ------------------------------------------------------------ |
| all.log_file | Full path to log file, default is log/opcshift               |
| da.host      | The host name where the DA service is located, the default is localhost |
| da.server    | The name of the DA server, such as "Matrikon.OPC.Simulation.1" |
| ua.port      | The port number of the UA server, the default is 4841        |

### Support Data Type

* INT8（OPCUA SBYTE type）
* INT16
* INT32
* INT64
* UINT8（OPCUA BYTE type）
* UINT16
* UINT32（also used to represent DATETIME types）
* UINT64
* FLOAT
* DOUBLE
* BOOL
* STRING

### Address Format

> IX!NODEID</span>

**IX** Namespace index, IX can only be 1 when accessing opcshift.

**NODEID** Node ID, consistent with the string in the UA server.

*例子：*

| Address                | Data Type | Description                                                  |
| ---------------------- | --------- | ------------------------------------------------------------ |
| 1!Bucket Brigade.UInt2 | UINT16    | Get a datatag of type UINT16; NS is 1, NODEID is Bucket Brigade.UInt2 |



## CNC FANUC FOCAS

### Parameter Setting

| 字段 | 说明       |
| ---- | ---------- |
| host | 设备IP地址 |
| port | 设备端口号 |

### Support Data Type

### Address Format

> C INDEX[!param1]\[!param2]\[!param3]\.[offset]</span>



| Index | Description                      | Param                 | Type   | Example    |
| ----- | -------------------------------- | --------------------- | ------ | ---------- |
| 1     | actual axis feedrate(F)          | 无                    | int64  | C1         |
| 2     | absolute axis position           | param1,param2,offset  | int64  | C2!1!2.2   |
| 3     | machine axis position            | param1,param2,offset  | int64  | C3!1!2.3   |
| 4     | relative axis position           | param1,param2,offset  | int64  | C4!1!2.4   |
| 5     | distance                         | param1,param2,offset  | int64  | C5!1!2.5   |
| 6     | skip position                    | param1,param2,offset  | int64  | C6!1!2.6   |
| 7     | servo delay value                | param1, param2,offset | int64  | C7!1!2.7   |
| 8     | accdec delay value               | param1,param2,offset  | int64  | C8!1!2.8   |
| 9     | actual spindle speed             | 无                    | int64  | C9         |
| 10    | manual overlapped motion value 1 | param1,param2,offset  | int64  | C10!1!2.10 |
| 11    | manual overlapped motion value 2 | param1,param2,offset  | int64  | C11!1!2.11 |
| 12    | serial spindle load info         | param1,offset         | int16  | C12!1.3    |
| 13    | serial spindle max rpm           | param1,offset         | int16  | C13!1.3    |
| 14    | serial spindle gear ration       | param1,offset         | int16  | C14!1.4    |
| 15    | axis name                        | param1                | string | C15        |
| 16    | controlled name                  | param1,param2         | string | C16        |
| 17    | spindle name                     | param1                | string | C17        |
| 18    | order spindle speed              | 无                    | int64  | C18        |
| 19    | order constant spindle speed     | 无                    | int64  | C19        |
| 20    | order maximum spindle speed      | 无                    | int64  | C20        |
