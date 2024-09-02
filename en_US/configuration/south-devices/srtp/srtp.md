# GE SRTP

Neuron GE SRTP plugin accesses GE PLC devices that support SRTP over TCP.

## Parameter Configuration

| Parameter | Description                                                 |
| --------- | ----------------------------------------------------------- |
| host      | PLC IP address                                              |
| port      | PLC port, default 18245                                     |
| timeout   | Timeout for sending requests to the device, default 3000 ms |

## Support Data Type

* uint8
* int8
* uint16
* int16
* uint32
* int32
* uint64
* int64
* float
* double
* bit
* string



## ADDRESS 

> AREA ADDRESS\[.BIT][.LEN]

### .BIT

Optional, referring to a bit of an address, range 0 - 15.

### .LEN

When the data type is a string type, it is required and indicates the length of the string.


### ADDRESS AREA


| AREA | DATA TYPE                                             | ATTRIBUTE | PLC AREA                   |
| ---- | ----------------------------------------------------- | --------- | -------------------------- |
| %I   | int8/uint8/bit                                        | R         | Discrete inputs            |
| %Q   | int8/uint8/bit                                        | R/W       | Discrete outputs           |
| %M   | int8/uint8/int32/uint32/int64/uint64/float/double/bit | R/W       | Internal references        |
| %T   | int8/uint8/int32/uint32/int64/uint64/float/double/bit | R/W       | Temporary references       |
| %SA  | int8/uint8/int32/uint32/int64/uint64/float/double/bit | R/W       | System status references A |
| %SB  | int8/uint8/int32/uint32/int64/uint64/float/double/bit | R/W       | System status references B |
| %SC  | int8/uint8/int32/uint32/int64/uint64/float/double/bit | R/W       | System status references C |
| %S   | int8/uint8/int32/uint32/int64/uint64/float/double/bit | R/W       | System status references   |
| %G   | int32/uint32/int64/uint64/float/double/bit            | R/W       | Discrete globals           |
| %AI  | int32/uint32/int64/uint64/float/double/bit            | R         | Analog input registers     |
| %AQ  | int32/uint32/int64/uint64/float/double/bit            | R/W       | Analog output registers    |
| %R   | int32/uint32/int64/uint64/float/double/bit/string     | R/W       | System register reference  |



## Address Examples

| ADDRESS  | DATA TYPE | Des                                                               |
| -------- | --------- | ----------------------------------------------------------------- |
| %I100    | bit       | %I100                                                             |
| %I100    | uint8     | %I100~%I107                                                       |
| %Q200    | bit       | %Q200                                                             |
| %Q200    | uint8     | %Q200~%Q207                                                       |
| %R100    | int16     | %R100                                                             |
| %AI100   | float     | %AI100 float                                                      |
| %R10     | double    | %R10 double                                                       |
| %R100.2  | bit       | %R area, the starting data word is 100, bit 2                     |
| %R200.12 | string    | %R area, the starting data word is 200, a string of 12 characters |
