# OMRON FINS on TCP

Omron Fins TCP is a protocol for communication between Omron PLCs and other devices. It is a TCP/IP based protocol. The fins plugin is used for Omron PLCs with network port, such as CP2E.

Neuron supports Fins TCP protocol, which can be used to communicate with Omron PLCs through Fins TCP protocol.

## Parameters

| Parameter         | Description                      |
| ----------------- | -------------------------------- |
| **Equipment Type** | Target PLC Equipment type |
| **PLC IP Address**          | Target PLC IPv4 address|
| **PLC Port**          | Target PLC port, default 9600 |

## Data types

* UINT8
* INT8
* INT16
* UINT16
* INT32
* UINT32
* FLOAT
* INT64
* UINT64
* DOUBLE
* BIT
* STRING

## Address Format

> AREA ADDRESS\[.BIT]\[.LEN\[H]\[L]]

### AREA ADDRESS

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

### .BIT

Optional, referring to a bit of an address.

### .LEN\[H]\[L]

When the data type is string type, it is a required, **.LEN** indicates the length of the string, including **H** and **L** two endianness, the default is **H** .

## Address Examples

| Address   | Data Type  | Description                                             |
| --------- | ------ | ----------------------------------------------------------- |
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