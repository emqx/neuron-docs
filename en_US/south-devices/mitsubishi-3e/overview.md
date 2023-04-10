# Overview

The Mitsubishi 3E plug-in is used to access Mitsubishi's QnA-compatible PLCs, including the Q Series (MC), iQ-F Series (SLMP), and iQ-L Series, via Ethernet.

The Mitsubishi 3E is fully compatible with the Mitsubishi SLMP protocol.

## Parameters

|  Parameter      |  Description                      |
| -------- | -------------------------- |
| **PLC IP Address** |  Target PLC IPv4 address         |
| **PLC Port** | Target PLC IPv4 address, Default 2000 |

## Data types

* INT16
* UINT16
* INT32
* UINT32
* FLOAT
* DOUBLE
* BIT
* STRING

## Address format

> AREA ADDRESS\[.BIT]\[.LEN\[H]\[L]]</span>

### .BIT

Only available for **non-bit type area**, means read the specified binary bit of the specified address, the binary bit index interval is [0, 15].

### .LEN\[H]\[L]

When the data type is string type, **.LEN** indicates the length of the string; you can optionally fill in **H** and **L** to indicate two byte orders, and the default is the byte order of **H**.

### PLC Area 

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

## Examples

|  Address  | Data type | Description |
| ----- | ------- | ----- |
| X0    | bit     | X area，Address 0    |
| X1    | bit     | X area，Address 1    |
| Y0    | bit     | Y area，Address 0    |
| Y1    | bit     | Y area，Address 1    |
| D100  | int16   | D area，Address 100  |
| D1000 | uint16  | D area，Address 1000 |
| D200  | uint32  | D area，Address 200  |
| D10   | float   | D area，Address 10   |
| D20   | double  | D area，Address 20   |
| D20.0 | bit | D area，Address 20，0 bit|
| D20.2 | bit | D area，Address 20，2 bit|
| D1002.16L | string  | D area，Address 1002，String length 16，Endian L |
| D1003.16 | string  | D area，Address 1003，String length 16，Endian H |
