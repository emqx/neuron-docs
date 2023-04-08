# Mitsubishi MELSEC A1E

## Module Description

The a1e plug-in is used to access Mitsubishi's A series, FX3U, FX3G, iQ-F series PLCs via Ethernet, iQ-F requires a specific firmware version.

## Parameter Configuration

| Parameter | Description                   |
| --------- | ----------------------------- |
| **host**  | remote plc ip                 |
| **port**  | remote plc port, default 2000 |

## Support Data Type

* INT16
* UINT16
* INT32
* UINT32
* FLOAT
* DOUBLE
* BIT
* STRING

## Usage of Address Format

### Address Format

> AREA ADDRESS\[.BIT]\[.LEN\[H]\[L]]</span>

#### AREA ADDRESS

| AREA | TYPE | ATTRIBUTE  | REMARK                                |
| ---- | ---- | ---------- | ------------------------------------- |
| X    | bit  | read/write | Input relay (FX3/iQ-F)                |
| Y    | bit  | read/write | Output relay (FX3/iQ-F)               |
| M    | bit  | read/write | Internal relay (FX3/iQ-F)             |
| L    | bit  | read/write | Latch relay (FX3/iQ-F)                |
| F    | bit  | read/write | Annunciator (FX3/iQ-F)                |
| B    | bit  | read/write | Link relay (FX3/iQ-F)                 |
| SB   | bit  | read/write | Link special relay (FX3/iQ-F)         |
| S    | bit  | read/write | (FX3/iQ-F)                            |
| D    | all  | read/write | Data register (FX3/iQ-F)              |
| W    | all  | read/write | Link register (FX3/iQ-F)              |
| TS   | bit  | read/write | Timer Contact (FX3/iQ-F)              |
| TC   | bit  | read/write | Timer Coil (FX3/iQ-F)                 |
| TN   | all  | read/write | Timer Current value (FX3/iQ-F)        |
| STS  | bit  | read/write | Retentive timer Contact (FX3/iQ-F)    |
| STC  | bit  | read/write | Retentive timer Coil (FX3/iQ-F)       |
| STN  | all  | read/write | Retentive timer (FX3/iQ-F)            |
| CS   | bit  | read/write | Counter Contact (FX3/iQ-F)            |
| CC   | bit  | read/write | Counter Coil (FX3/iQ-F)               |
| CN   | all  | read/write | Counter Current value (FX3/iQ-F)      |
| LCS  | bit  | read/write | Long Counter Contact (FX3/iQ-F)       |
| LCC  | bit  | read/write | Long Counter Coil (FX3/iQ-F)          |
| LCN  | all  | read/write | Long Counter Current value (FX3/iQ-F) |
| SB   | bit  | read/write | Link special relay (FX3/iQ-F)         |
| SW   | all  | read/write | Link special register (FX3/iQ-F)      |
| SM   | bit  | read/write | Special relay (FX3/iQ-F)              |
| SD   | all  | read/write | Specical register (FX3/iQ-F)          |
| Z    | all  | read/write | Index register (FX3/iQ-F)             |
| LZ   | all  | read/write | Long Index register (FX3/iQ-F)        |
| DX   | bit  | read/write | Link input (FX3/iQ-F)                 |
| DY   | bit  | read/write | Link output(FX3/iQ-F)                 |
| R    | all  | read/write | File register (FX3/iQ-F)              |

#### .BIT

It can only be used in **non-bit type area**, which means to read the specified bit of the specified address, and the binary bit index range is [0, 15].

| Address | Data Type | Description                  |
| ------- | --------- | ---------------------------- |
| D20.0   | bit       | D area, address is 20, bit 0 |
| D20.2   | bit       | D area, address is 20, bit 2 |

#### .LEN\[H]\[L]

When the data type is string, **.LEN** indicates the length of the string;   **H** and **L** can be optional to indicate two byte orders, the default is **H** byte order.

### Address Examples

| Address   | Data Type | Description                                                  |
| --------- | --------- | ------------------------------------------------------------ |
| X0      | bit       | X area, address is 0    |
| X1      | bit       | X area, address is 1    |
| Y0      | bit       | Y area, address is 0    |
| Y1      | bit       | Y area, address is 1    |
| D100    | int16     | D area, address is 100  |
| D1000   | uint16    | D area, address is 1000 |
| D200    | uint32    | D area, address is 200  |
| D10     | float     | D area, address is 10   |
| D20     | double    | D area, address is 20   |
| D1002.16L | string    | D area, address is 1002, string length is 16, endianness is L |
| D1003.16  | string    | D area, address is 1003, string length is 16, endianness is H |