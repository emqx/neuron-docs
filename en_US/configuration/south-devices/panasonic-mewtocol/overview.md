# Panasonic mewtocol

The Mewtocol plug-in is used to access Panasonic's FP-XH, FP0H series PLCs via Ethernet.

## Parameters

|   Parameter     |  Description                      |
| -------- | -------------------------- |
| **PLC IP Address** |  Target PLC IPv4 address         |
| **PLC Port** | Target PLC IPv4 address, Default 2000 |
| **PLC Station** | Target PLC station, Default 1      |

## Data Types

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

## Address format

> AREA ADDRESS\[.BIT]\[.LEN\[H]\[L]]

### .BIT
Only available for **non-bit type area**, means read the specified binary bit of the specified address, the binary bit index interval is [0, 15].

### .LEN\[H]\[L]
When the data type is string type, **.LEN** indicates the length of the string; you can optionally fill in **H** and **L** to indicate two byte orders, and the default is the byte order of **H**.

### PLC Area

| Area | DATA TYPE | ATTRIBUTE  |  REMARK                          |
| ---- | --------- | ---------- | -------------------------------- |
| X    | uint16、uint32、uint64、bit | read/write | External input        |
| Y    | uint16、uint32、uint64、bit | read/write | External output        |
| R    | uint16、uint32、uint64、bit | read/write | Internal relay      |
| T    | uint16、uint32、uint64、bit | read/write | Timer       |
| C    | uint16、uint32、uint64、bit | read/write | Counter           |
| L    | uint16、uint32、uint64、bit | read/write | Link relay       |
| DT   | all | read/write (bit type readonly) | Data register DT   |
| LD   | all | read/write (bit type readonly) | Link data register LD    |
| FL   | all | read/write (bit type readonly) | File register FL     |
| S    | -- | -- | Timer/counter set value area SV     |
| K    | -- | -- | Timer/counter elapsed value area EV     |
| IX   | all   | read/write (bit type readonly) | Index register IX   |
| IY   | all   | read/write (bit type readonly) | Index register IY  |
| ID   | all   | read/write (bit type readonly) | Index register ID  |


## Examples

| Address   | Data type | Description |
| ----- | ------- | ----- |
| X0    | bit     | X Area, Address 0    |
| X1    | bit     | X Area, Address 1    |
| Y0    | bit     | Y Area, Address 0    |
| Y1    | bit     | Y Area, Address 1    |
| DT100 | int16   | D Area, Address 100  |
| DT1000 | uint16 | D Area, Address 1000 |
| DT200 | uint32  | D Area, Address 200  |
| DT10  | float   | D Area, Address 10   |
| DT20  | double  | D Area, Address 20   |
| DT20.0 | bit | D Area, Address 20, 0 bit |
| DT20.2 | bit | D Area, Address 20, 2 bit |
| DT1002.16L | string  | D Area, Address 1002, String length 16, Byte order L |
| DT1003.16 | string  | D Area, Address 1003, String length 16, Byte order H |
