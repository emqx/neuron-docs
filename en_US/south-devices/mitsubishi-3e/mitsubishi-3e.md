# Introduction and Usage of Mitsubishi MELSEC QnA3E

## Module Description

The qna3e plugin is used to access Mitsubishi's QnA compatible PLCs via Ethernet, including Q series (MC), iQ-F series (SLMP) and iQ-L series.

## Parameter Configuration

| Parameter | Description |
| -------- | -------------------------- |
| **host** | remote plc ip                 |
| **port** | remote plc port, default 2000 |

## Support Data Type

* INT16
* UINT16
* INT32
* UINT32
* FLOAT
* DOUBLE
* BIT
* STRING

## Usage of Address Fromat

### Address Format

> AREA ADDRESS\[.BIT]\[.LEN\[H]\[L]]

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

#### .BIT

It can only be used in **non-bit type area**, which means to read the specified bit of the specified address, and the binary bit index range is [0, 15].

| Address | Data Type | Description |
| ------- | --------- | --------- |
| D20.0 | bit | D area, address is 20, bit 0   |
| D20.2 | bit | D area, address is 20, bit 2   |

#### .LEN\[H]\[L]

When the data type is string, **.LEN** indicates the length of the string;   **H** and **L** can be optional to indicate two byte orders, the default is **H** byte order.

### Address Examples

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
| D1002.16L | string  | D area, address is 1002, string length is 16, endianness is L |
| D1003.16 | string  | D area, address is 1003, string length is 16, endianness is H |
mac