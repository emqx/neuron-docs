# KND CNC

The KND CNC driver accesses KND K2000, K1000 C/Ci/F/Fi, and K1000TTCi series CNC systems via HTTP protocol, enabling real-time collection of various device operation data, including program name, spindle override, operating status, PLC points, etc.

## Device Settings

| Field | Description                      |
| ----- | -------------------------------- |
| host  | Device IP address                |
| port  | Device port number, default 8000 |

## Supported Data Types

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
* bit
* string

## CNC Data

> address\[.m]

| Tag Identifier (Address)      | Description                         | Data Type    | Parameter | Remarks                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| ----------------------------- | ----------------------------------- | ------------ | --------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| systemInfo.id                 | ID                                  | int32        | -         | -                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| systemInfo.type               | System Type                         | string       | -         | -                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| systemInfo.manufacturer       | Manufacturer                        | string       | -         | -                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| systemInfo.manufacture-time   | Manufacture Time                    | string       | -         | -                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| systemInfo.soft-version       | System Software Version             | string       | -         | -                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| systemInfo.fpga-version       | FPGA Version                        | string       | -         | -                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| systemInfo.ladder-version     | Ladder Version                      | string       | -         | -                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| systemInfo.user-axes          | User Axis List                      | array string | -         | -                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| systemStatus.run-status       | Current Run Status                  | int32        | -         | 0: CNC is stopped 1: CNC is paused (feed hold) 2: CNC is running                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| systemStatus.opr-mode         | Current Operation Mode              | int32        | -         | 0: Manual data input mode 1: Automatic mode 2: Invalid mode 3: Edit mode 4: Single step mode 5: Manual mode 8: Handle wheel mode 9: Machine zero return mode 10: Program zero return mode                                                                                                                                                                                                                                                                                                                 |
| systemStatus.ready            | Is Ready                            | bool         | -         | -                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| systemStatus.not-ready-reason | Not Ready Reason Mask               | int32        | -         | 0x1: Emergency stop signal active 0x2: Servo not ready 0x4: IO not ready (remote IO devices, etc.)                                                                                                                                                                                                                                                                                                                                                                                                        |
| systemStatus.alarms           | Alarm List                          | array string | -         | -                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| alarms                        | Alarm Description Information       | string       | m         | prm-switch: Parameter switch alarm (system parameter switch or servo parameter switch) reboot: Power on/off alarm plc: PLC alarm or prompt (external alarm) ps: PS alarm (operation error) over-travel: Over-travel alarm over-heat: Overheat alarm mem: Memory alarm servo: Servo drive alarm servo-bus: Servo bus alarm over-workarea: Out of work area alarm io-bus: IO bus alarm io-module: IO module alarm manufacture: Machine factory alarm forbid-move: Axis movement not allowed when axis moves |
| absolute                      | Absolute Coordinates                | double       | m         | X Y Z                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| machine                       | Machine Coordinates                 | double       | m         | X Y Z                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| relative                      | Relative Coordinates                | double       | m         | X Y Z                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| cycleTime                     | Processing Time                     | int32        | m         | total: Processing time (unit: seconds) cur: Cycle time (unit: seconds)                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| workCounts                    | Processing Counts                   | int32        | m         | total: Total processing count batch: Single batch processing count                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| workCountGoals                | Target Counts                       | int32        | m         | total: Total target count batch: Single batch target count                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| feedOverride                  | Current Feed Override               | double       | -         | -                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| jogOverride                   | Current Jog Override                | double       | -         | -                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| rapidOverride                 | Current Rapid Override              | double       | -         | -                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| handleOverride                | Current Handle/Single Step Override | double       | -         | -                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| spindleOverride               | Current Spindle Override            | double       | m         | 1: Spindle 1 2: Spindle 2 3: Spindle 3                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| spSpeed                       | Current Spindle Speed               | double       | m         | 1: Spindle 1 2: Spindle 2 3: Spindle 3                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| feedrate                      | Actual Feedrate                     | double       | -         | -                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| g54                           | G54 Work Coordinate System          | double       | m         | X Y Z                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| g55                           | G55 Work Coordinate System          | double       | m         | X Y Z                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| g56                           | G56 Work Coordinate System          | double       | m         | X Y Z                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| g57                           | G57 Work Coordinate System          | double       | m         | X Y Z                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| g58                           | G58 Work Coordinate System          | double       | m         | X Y Z                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| g59                           | G59 Work Coordinate System          | double       | m         | X Y Z                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| workCoorsCur                  | Current Work Coordinate System      | string       | -         | -                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| vars                          | Macro Variables                     | double       | m         | Macro variable number                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| progCur                       | Current Program                     | int32        | -         | -                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| progExecStatus                | Program Execution Status            | int32        | m         | O: Program O number N: Program N number P: Paragraph number                                                                                                                                                                                                                                                                                                                                                                                                                                               |

::: tip
Spindle numbers start from 1 and increase according to the actual number of spindles.

Macro variables (vars) are readable and writable, others are read-only.
:::

*CNC Address Examples*

| Address           | Description                          |
| ----------------- | ------------------------------------ |
| systemInfo.type   | Read processing main program number  |
| machine.X         | Read X-axis coordinate               |
| vars.100          | Read/write macro variable 100        |
| feedOverride      | Read current feed override           |
| alarms.plc        | PLC alarm or prompt (external alarm) |
| spindleOverride.1 | Spindle 1 override                   |
| spSpeed.1         | Spindle 1 speed                      |
| cycleTime.cur     | Cycle time                           |

### PLC Data

### Address Format

> AREA ADDRESS\[.BIT]\[.LEN]

| Identifier | Description                 | Type | Permission |
| ---------- | --------------------------- | ---- | ---------- |
| X          | DI Input                    | all  | Read       |
| Y          | DO Output                   | all  | Read       |
| F          | NC -> PLC                   | all  | Read       |
| G          | PLC -> NC                   | all  | Read       |
| R          | PLC Internal Control Relay  | all  | Read/Write |
| S          | PLC Internal Special Flag   | all  | Read       |
| K          | PLC Internal Power-On Relay | all  | Read       |
| D          | Data Table                  | all  | Read       |
| TL         | Label Sequence Number       | all  | Read       |

::: tip
Currently, only part of the R area can be set, i.e., R17000-R17099, and it requires explicit permission in the ladder diagram. The ladder diagram must set G138 to 181 to allow remote modification of the above R area.
:::

> AREA ADDRESS\[.cur/conf]

| Identifier | Description | Type         | Permission |
| ---------- | ----------- | ------------ | ---------- |
| T          | Timer       | int32/uint32 | Read       |
| C          | Counter     | int32/uint32 | Read       |

::: tip
When reading timers and counters, you need to specify whether it is the set value or the current value.
:::

*Common PLC Points*

| Address | Type   | Description                                        |
| ------- | ------ | -------------------------------------------------- |
| X0.0    | bit    | DI area, data at address 0                         |
| Y0.0    | bit    | DO area, data at address 0                         |
| D10     | int32  | Data table area, data at address 10                |
| R17000  | float  | Internal control relay area, data at address 17000 |
| D20.24  | string | Data table area, data at address 20                |
| T0.conf | int32  | Timer area, set value data at address 0            |
| T0.cur  | int32  | Timer area, current data at address 0              |