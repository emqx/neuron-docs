# SYNTEC CNC

Neuron can use the Neuron HUB driver and NeuronHUB Windows program to indirectly access the SYNTEC CNC system, enabling real-time collection of various device operation data, including program names, spindle override, operation status, PLC points, parameters, global variables, etc.

## NEURON HUB Windows Program Parameters

| Parameter | Description                                             |
| --------- | ------------------------------------------------------- |
| Node Name | Node name, must be unique to distinguish multiple nodes |
| Host      | IP address of the CNC device to connect to              |

## Supported Data Types

* uint8  
* int8  
* uint32  
* int32  
* uint64  
* int64  
* float  
* double  
* bit  
* string    
* ARRAY_STRING  

## CNC Data

> address\[.m]\[.n]

| Tag Identifier (Address) | Description                      | Data Type    | Parameters | Remarks                                                                                                                                                                                 |
| ------------------------ | -------------------------------- | ------------ | ---------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| systemInfo.axes          | Controllable axes count          | int32        | -          | -                                                                                                                                                                                       |
| systemInfo.cnc_type      | System type                      | string       | -          | -                                                                                                                                                                                       |
| systemInfo.max_axes      | Maximum axes count               | int32        | -          | -                                                                                                                                                                                       |
| systemInfo.series        | M/T type                         | string       | -          | -                                                                                                                                                                                       |
| systemInfo.nc_ver        | System software version          | string       | -          | -                                                                                                                                                                                       |
| systemInfo.axis_name     | Axis coordinate names            | array string | -          | -                                                                                                                                                                                       |
| systemStatus.status      | Current operation status         | string       | -          | -                                                                                                                                                                                       |
| systemStatus.main_prog   | Main program name                | string       | -          | 0: Input mode 1: Auto mode 2: Invalid mode 3: Edit mode 4: Step mode 5: Manual mode 8: Handwheel mode 9: Mechanical homing mode 10: Program homing mode                                 |
| systemStatus.cur_prog    | Currently executing program name | string       | -          | -                                                                                                                                                                                       |
| systemStatus.mode        | Mode                             | string       | -          | 0x1: Emergency stop signal active 0x2: Servo not ready 0x4: IO not ready (remote IO devices, etc.)                                                                                      |
| systemStatus.alarm       | Alarm                            | string       | -          | -                                                                                                                                                                                       |
| systemStatus.emg         | Emergency stop                   | string       | -          | -                                                                                                                                                                                       |
| alarms                   | Current alarms                   | array string | -          | -                                                                                                                                                                                       |
| halarms                  | Historical alarms                | array string | -          | -                                                                                                                                                                                       |
| oplog                    | Operation logs                   | array string | -          | -                                                                                                                                                                                       |
| absolute                 | Absolute coordinates             | double       | m          | X Y Z                                                                                                                                                                                   |
| machine                  | Machine coordinates              | double       | m          | X Y Z                                                                                                                                                                                   |
| relative                 | Relative coordinates             | double       | m          | X Y Z                                                                                                                                                                                   |
| distance                 | Remaining distance               | double       | m          | X Y Z                                                                                                                                                                                   |
| time                     | Time                             | int32        | m          | power: Power-on time (seconds) cutting: Cutting time (seconds) cycle: Cycle time (seconds) work: Processing time (seconds)                                                              |
| partCount                | Part count                       | int32        | m          | total: Total part count cur: Current part count req: Required part count                                                                                                                |
| ovfeed                   | Current feed override            | double       | -          | -                                                                                                                                                                                       |
| ovspindle                | Current spindle override         | double       | -          | -                                                                                                                                                                                       |
| actfeed                  | Actual feed speed                | double       | -          | -                                                                                                                                                                                       |
| actspindle               | Actual spindle speed             | int32        | -          | -                                                                                                                                                                                       |
| gcode                    | G-code                           | array string | -          | -                                                                                                                                                                                       |
| otherCode                | Other codes                      | int32        | m          | hcode dcode mcode tcode fcode scode                                                                                                                                                     |
| macro                    | Global variables                 | double       | m          | Global variable number                                                                                                                                                                  |
| param                    | Parameters                       | int32        | m          | Parameter number                                                                                                                                                                        |
| toolOffset               | Tool compensation                | double       | m, n       | m: Tool compensation number. n: RADIUS_GEOM, RADIUS_WEAR, LENGTH_GEOM, LENGTH_WEAR, WEAR_X, WEAR_Z, WEAR_A, LENGTH_X, LENGTH_Y, LENGTH_A, TOOL_NOSE_RADIUS, TOOL_NOSE_R_WEAR, TOOL_NOSE |

::: tip  
macro and param are readable/writable; others are read-only.  
:::

*CNC Address Examples*

| Address                 | Description                              |
| ----------------------- | ---------------------------------------- |
| systemInfo.nc_ver       | Read system software version             |
| machine.X               | Read X-axis coordinate                   |
| macro.100               | Read/write global variable 100           |
| feedOverride            | Read current feed override               |
| alarms                  | Current alarms                           |
| partCount.total         | Total part count                         |
| toolOffset1.RADIUS_GEOM | Tool compensation 1, radius compensation |

### PLC Data

### Address Format

> AREA ADDRESS\[.BIT]\[.LEN]

| Identifier | Description | Type                                              | Permission |
| ---------- | ----------- | ------------------------------------------------- | ---------- |
| I          | Input Bits  | bit/int8/uint8                                    | Read       |
| O          | Output Bits | bit/int8/uint8                                    | Read       |
| C          | C Bits      | bit/int8/uint8                                    | Read       |
| S          | S Bits      | bit/int8/uint8                                    | Read       |
| A          | A Bits      | bit/int8/uint8                                    | Read       |
| R          | Registers   | bit/int32/uint32/int64/uint64/float/double/string | Read/Write |

::: tip  
Currently, only partial R area writing is supported; bit writing is not supported.  
:::

> AREA ADDRESS\[.setting/value/state]

| Identifier | Description | Type         | Permission |
| ---------- | ----------- | ------------ | ---------- |
| T          | Timer       | int32/uint32 | Read       |
| N          | Counter     | int32/uint32 | Read       |

::: tip  
When reading timers and counters, specify whether to read the setting value, current value, or state.  
:::

*Common PLC Addresses*

| Address    | Type  | Description                         |
| ---------- | ----- | ----------------------------------- |
| I0.0       | bit   | Input Bits area, address 0 data     |
| A10        | int8  | A Bits area, address 10 data        |
| R100       | float | Register area, address 100 data     |
| T0.setting | int32 | Timer area, address 0 setting value |
| T0.value   | int32 | Timer area, address 0 current value |