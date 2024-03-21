# HEIDENHAIN CNC

The Heidenhain CNC drive accesses Heidenhain TNC640, iTNC530 and other series of machine tools and machining centers through the LSV2 protocol, and can collect real-time operating data from multiple devices, including program names, spindle override , runing status, spindle tools, PLC points, and more.


## Parameter Configuration

| Parameter | Description                        |
| --------- | ---------------------------------- |
| host      | device ip address                  |
| port      | device port, default 19000         |
| timeout   | connection timeout, default 5000ms |


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
* bool
* string

## CNC Data

| tag address       | description             | data type | parameter      | note                                                                                                |
| ----------------- | ----------------------- | --------- | -------------- | --------------------------------------------------------------------------------------------------- |
| runState          | run state               | int16     | -              | 0:STARTED 1:STOPPED 2:FINISHED 3:CANCELLED 4:INTERRUPTED 5:ERROR 6:ERROR_CLEARED 7:IDLE 8:UNDEFINED |
| programMain       | main program            | string    | -              | -                                                                                                   |
| programCurrent    | current program         | string    | -              | -                                                                                                   |
| programLineNo     | current program line no | int32     | -              | -                                                                                                   |
| controlMode       | control mode            | int16     | -              | 0:MANUAL 1:MDI 2:PASS_REFERENCES 3:SINGLE_STEP 4:AUTOMATIC 5:UNDEFINED                              |
| spindleToolNumber | spindle tool number     | int32     | -              | -                                                                                                   |
| spindleToolLength | spindle tool length     | double    | -              | -                                                                                                   |
| spindleToolRadius | spindle tool radius     | double    | -              | -                                                                                                   |
| feedOverride      | feed override           | int32     | -              | -                                                                                                   |
| spindleOverride   | spindle override        | int32     | -              | -                                                                                                   |
| rapidOverride     | rapid override          | int32     | -              | -                                                                                                   |
| machinePosition   | machine position        | double    | .X .Y .Z .A .C | -                                                                                                   |
| parameter         | cnc setting parameter   | string    | .(name)        | -                                                                                                   |


*CNC address example*

| address                                 | description                        |
| --------------------------------------- | ---------------------------------- |
| ProgramMain                             | read the main program              |
| machinePosition.X                       | read x asix of machine position    |
| parameter.CfgDisplayLanguage.ncLanguage | TNC640 read/write language setting |


### PLC Data

| tag address | description | data type                                                      | r/w  |
| ----------- | ----------- | -------------------------------------------------------------- | ---- |
| M           | MARKER      | bool                                                           | read |
| I           | INPUT       | bool                                                           | read |
| O           | OUTPUT      | bool                                                           | read |
| T           | TIMER       | bool                                                           | read |
| C           | COUNTER     | bool                                                           | read |
| B           | BYTE        | uint8/int8/int16/uint16/int32/uint32/int64/uint64/float/double | read |
| W           | WORD        | int16/uint16/int32/uint32/int64/uint64/float/double            | read |
| D           | DWORD       | int32/uint32/int64/uint64/float/double                         | read |
| N           | INPUT WORD  | int16/uint16/int32/uint32/int64/uint64/float/double            | read |
| U           | OUTPUT WORD | int16/uint16/int32/uint32/int64/uint64/float/double            | read |
| S           | STRING      | string                                                         | read |

*PLC Common Address*

| address | data type | descrption                                    |
| ------- | --------- | --------------------------------------------- |
| M0      | bool      | PLC Marker area，address 0                    |
| I10     | bool      | PLC Input area，address 10                    |
| O20     | bool      | PLC Output area，address 20                   |
| C30     | bool      | PLC Counter area，address 30                  |
| T40     | bool      | PLC Timer area，address 40                    |
| B0      | int8      | PLC Byte area，address 0                      |
| B20     | int16     | PLC Byte area，address 20                     |
| B40     | double    | PLC Byte area，address 40                     |
| W2      | int16     | PLC Word area，address 2                      |
| D4      | int32     | PLC Word area，address 2                      |
| N2      | int16     | PLC Input Word area，address 2                |
| U2      | int16     | PLC OutPut Word area，address 2               |
| S0.128  | string    | PLC String area，address 0，string length 128 |
