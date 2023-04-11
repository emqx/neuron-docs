# Siemens FetchWrite

## Module Description

The s5fetch-write plug-in is used for accessing Siemens PLCs with network expansion module CP443, such as s7-300/400.

## Parameter Configurations

| Parameter | Description                  |
| --------- | ---------------------------- |
| **host**  | remote plc ip                |
| **port**  | remote plc port, default 102 |

## Support Data Type

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

## Usage of Address Format

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

#### .BIT

Optional, refers to a certain digit of a certain address.

#### .LEN

When the data type is string type, it is a required item, indicating the length of the string.

### Address Example

| Address      | Data Type | Description                                    |
| ------------ | --------- | ---------------------------------------------- |
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
| DB1.DBW12.20 | string    | DB area, address 1，start 12，string length 20 |