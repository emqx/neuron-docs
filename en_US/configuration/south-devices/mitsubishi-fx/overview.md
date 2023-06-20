# Mitsubishi FX

The Mitsubishi FX plug-in is used to access Mitsubishi's FX0, FX2, FX3 and other PLC series via the FX programming port.

## Parameter Configuration

|  Parameter    |  Description              |
| -------- | ------------------------------ |
| **timeout**  | Connection timeout, default is 3000 milliseconds |
| **interval** | Command transmission interval, default 20 ms     |
| **device**   | Serial device path                               |
| **stop**     | Stop bits, default is 1                          |
| **parity**   | Parity, default is even                          |
| **baud**     | Baud rate, default is 9600                       |
| **data**     | Data Bits, default is 7                          |

## Support Data Type

* INT16
* UINT16
* INT32
* UINT32
* FLOAT
* DOUBLE
* BIT
* STRING

### Usage of Address Format

### Address Format

> AREA ADDRESS\[.BIT]\[.LEN\[H]\[L]]</span>

#### AREA ADDRESS

| AREA | TYPE | ATTRIBUTE  |  REMARK                                  |
| ---- | -------- | ----- | -------------------------------------- |
| X    | bit      | read/write | Input relay (FX3U)                |
| Y    | bit      | read/write | Output relay (FX3U)               |
| M    | bit      | read/write | Internal relay (FX3U)             |
| S    | bit      | read/write | Status relay (FX3U)               |
| TS   | bit      | read/write | Timer Contact (FX3U)              |
| CS   | bit      | read/write | Counter Contact (FX3U)            |
| TN   | all      | read/write | Timer Current value (FX3U)        |
| CN   | all      | read/write | Counter Current value (FX3U)      |
| D    | all      | read/write | Data register (FX3)               |

#### .BIT

Only available for **non-bit type area**, means read the specified binary bit of the specified address, the binary bit index interval is [0, 15].

| Address  | Data Type |  Description                      |
| ----- | -------- | -------------------------- |
| D20.0 | bit      | D Area，address 20，bit 0 |
| D20.2 | bit      | D Area，address 20，bit 2 |

#### .LEN\[H]\[L]

When the data type is string type, **.LEN** indicates the length of the string; you can optionally fill in **H** and **L** to indicate two byte orders, and the default is the byte order of **H**.

### Address Examples

| Address      | Data Type |  Description                                          |
| --------- | -------- | -------------------------------------------- |
| X0    | bit      | X Area，address is 0    |
| X1    | bit      | X Area，address is 1    |
| Y0    | bit      | Y Area，address is 0    |
| Y1    | bit      | Y Area，address is 1    |
| D100  | int16    | D Area，address is 100  |
| D120  | uint16   | D Area，address is 120  |
| D200  | uint32   | D Area，address is 200  |
| D10   | float    | D Area，address is 10   |
| D20   | double   | D Area，address is 20   |
| D152.16L | string   | D Area，address is 152，string length is 16，endianness is L |
| D183.16  | string   | D Area，address is 183，string length is 16，endianness H |
