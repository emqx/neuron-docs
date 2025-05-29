# MITSUBISHI CNC

Neuron can use the Neuron HUB driver and NEURON HUB Windows program to indirectly access Mitsubishi M70/M80 CNC systems, enabling real-time collection of various device operation data, including program names, feed speed, operation status, power consumption, PLC points, global variables, parameters, etc.

## NEURON HUB Windows Program Parameters

| Parameter | Description                                             |
| --------- | ------------------------------------------------------- |
| Node Name | Node name, must be unique to distinguish multiple nodes |
| Host      | IP address of the CNC device to connect to              |
| cnctype   | Device type (supported: M700L, M700M, M800L, M800M)     |
| cardno    | Control card number (default: 1)                        |

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
* ARRAY_DOUBLE  

## CNC Data

> address\[.m]\[.n]\[.k]\[.j]

| Tag Identifier (Address) | Description               | Data Type    | Parameters | Remarks                                                                                                          |
| ------------------------ | ------------------------- | ------------ | ---------- | ---------------------------------------------------------------------------------------------------------------- |
| systemStatus             | Current operation status  | int32        | m          | m: 0 Tool setting status 1 Auto status 2 Auto running status 3 Auto paused status                                |
| spindleInfo              | Spindle status            | int64        | m n        | m: Spindle number n: 0 Gain 1: Position deviation 2: Motor speed 3: Load 5: Alarm1 6: Alarm2 7: Alarm3 8: Alarm4 |
| servoInfo                | Servo axis status         | int64        | m n        | m: Axis number n: 0 Gain 1: Position deviation 2: Motor speed 3: Current 6: Load                                 |
| work                     | Workpiece coordinates     | double       | m          | m: Axis number                                                                                                   |
| machine                  | Machine coordinates       | double       | m          | m: Axis number                                                                                                   |
| relative                 | Relative coordinates      | double       | m          | m: Axis number                                                                                                   |
| distance                 | Remaining distance        | double       | m          | m: Axis number                                                                                                   |
| feedSpeed                | Feed speed                | double       | m          | 0 FA 1 FM 2 FS 3 Fc 4 FE                                                                                         |
| param                    | Parameters                | ARRAY_STRING | m n k j    | m: Axis number n: Group number k: Parameter number j: Parameter count                                            |
| toolOffset               | Tool compensation         | double       | m n k      | m: Type n: Tool compensation type k: Number                                                                      |
| alarm                    | Alarms                    | ARRAY_STRING | -          | -                                                                                                                |
| runTime                  | Auto run time             | int32        | -          | -                                                                                                                |
| startTime                | Auto start time           | int32        | -          | -                                                                                                                |
| aliveTime                | Power-on time             | int32        | -          | -                                                                                                                |
| estimateTime             | External integration time | int32        | m          | 1: Timer1 2: Timer2                                                                                              |
| commonVar                | Global variables          | double       | m          | Variable number                                                                                                  |
| localVar                 | Local variables           | double       | m n        | m: Variable number n: Level                                                                                      |
| invalidStatus            | Invalid status            | int32        | -          | -                                                                                                                |
| commandStatus            | Command status            | int32        | -          | -                                                                                                                |
| cuttingMode              | Cutting mode              | int32        | -          | -                                                                                                                |
| mainProgram              | Main program              | int32        | -          | -                                                                                                                |
| subProgram               | Subprogram                | int32        | -          | -                                                                                                                |
| mainSeqNum               | Main sequence number      | int32        | -          | -                                                                                                                |
| subSeqNum                | Sub sequence number       | int32        | -          | -                                                                                                                |
| programCurrentBlock      | Current program block     | string       | -          | -                                                                                                                |
| powerConsumption         | Power consumption         | ARRAY_DOUBLE | m          | m: Axis number [0]: Total system power [1]: Servo power [3]: Spindle power                                       |
| toolLife                 | Tool life                 | ARRAY_STRING | m n        | m: Group number n: Tool number                                                                                   |

::: tip  
commonVar is readable/writable; others are read-only.  
:::

*CNC Address Examples*

| Address           | Description                    |
| ----------------- | ------------------------------ |
| systemStatus.0    | Tool setting status            |
| machine.1         | Read axis 1 coordinate         |
| commonVar.100     | Read/write global variable 100 |
| feedSpeed.0       | Read current feed speed        |
| alarm             | Current alarm list             |
| param.1.30.8002.1 | Part count                     |

### PLC Data

| Identifier | Description                     | Type            | Permission |
| ---------- | ------------------------------- | --------------- | ---------- |
| B          | Counters (fixed counters)       | bit/16bit/32bit | Read/Write |
| C          | Counter coils                   | bit/16bit/32bit | Read/Write |
| D          | Data registers                  | 16bit/32bit     | Read/Write |
| E          | Special relays                  | bit/16bit/32bit | Read/Write |
| F          | Alarm message temporary memory  | bit/16bit/32bit | Read/Write |
| G          | Temporary memory                | bit/16bit/32bit | Read/Write |
| I          | Devices                         | bit/16bit/32bit | Read/Write |
| J          | J devices                       | bit/16bit/32bit | Read/Write |
| L          | Latch relays (backup memory)    | bit/16bit/32bit | Read/Write |
| M          | Temporary memory                | bit/16bit/32bit | Read/Write |
| Q          | Q devices                       | bit/16bit/32bit | Read/Write |
| R          | File registers                  | 16bit/32bit     | Read/Write |
| SM         | Special relays (for linking)    | bit/16bit/32bit | Read/Write |
| SD         | Special registers               | 16bit/32bit     | Read/Write |
| ST         | Accumulative timers             | 16bit/32bit     | Read/Write |
| SW         | Special registers (for linking) | 16bit/32bit     | Read/Write |
| T          | 10ms timer units                | bit/16bit/32bit | Read/Write |
| U          | Input signals to PLC            | bit/16bit/32bit | Read/Write |
| V          | V devices                       | bit/16bit/32bit | Read/Write |
| W          | Input signals to PLC            | bit/16bit/32bit | Read/Write |
| X          | Input signals                   | bit/16bit/32bit | Read/Write |
| Y          | Output signals                  | bit/16bit/32bit | Read/Write |
| ZR         | File registers                  | 16bit/32bit     | Read/Write |

::: tip  
Addresses should be entered in hexadecimal format.  
:::

*Common PLC Addresses*

| Address | Type   | Description                                                                                                                                                                                          |
| ------- | ------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| R69     | uint16 | PLC R area, address 69 data (EMG emergency stop flag: 65519 ON, 65535 OFF)                                                                                                                           |
| R2500   | uint16 | PLC R area, address 2500 data (feed override)                                                                                                                                                        |
| R7008   | uint16 | PLC R area, address 7008 data (spindle override)                                                                                                                                                     |
| R6506   | uint32 | PLC R area, address 6506 data (actual spindle speed)                                                                                                                                                 |
| R7000   | uint32 | PLC R area, address 7000~7001 data (command spindle speed)                                                                                                                                           |
| R6525   | uint16 | PLC R area, address 6525 data (spindle load)                                                                                                                                                         |
| R6529   | uint16 | PLC R area, address 6529 data (spindle alarm number)                                                                                                                                                 |
| R606    | uint32 | PLC R area, address 606~607 data (current part count)                                                                                                                                                |
| R608    | uint32 | PLC R area, address 608~609 data (maximum part count)                                                                                                                                                |
| R11824  | uint32 | PLC R area, address 11824~11825 data (currently used tool group number)                                                                                                                              |
| R11826  | uint32 | PLC R area, address 11826~11827 data (currently used tool number)                                                                                                                                    |
| R11830  | uint32 | PLC R area, address 11830~11831 data (currently used tool cumulative usage time)                                                                                                                     |
| R11832  | uint32 | PLC R area, address 11832~11833 data (currently used tool life setting time)                                                                                                                         |
| XC00    | uint16 | PLC X area, address C00~C0F data (control mode: 1 JOG mode 2 Handwheel mode 4 Increment mode 8 Manual feed mode 16 Reference return mode 32 Auto initial setting mode 256 Memory mode 2048 MDI mode) |
| XC12    | bit    | PLC X area, address C12 data (auto running)                                                                                                                                                          |
| XC13    | bit    | PLC X area, address C13 data (auto running start)                                                                                                                                                    |
| XC14    | bit    | PLC X area, address C14 data (auto running pause)                                                                                                                                                    |
| XC15    | bit    | PLC X area, address C15 data (reset)                                                                                                                                                                 |
| XC20    | bit    | PLC X area, address C20 data (rapid feed)                                                                                                                                                            |
| XC21    | bit    | PLC X area, address C21 data (cutting feed)                                                                                                                                                          |
| XC22    | bit    | PLC X area, address C22 data (tapping)                                                                                                                                                               |
| XC23    | bit    | PLC X area, address C23 data (thread cutting)                                                                                                                                                        |
| XC24    | bit    | PLC X area, address C24 data (synchronous feed)                                                                                                                                                      |
| XC25    | bit    | PLC X area, address C25 data (constant speed)                                                                                                                                                        |
| XC26    | bit    | PLC X area, address C26 data (jump)                                                                                                                                                                  |
| XC27    | bit    | PLC X area, address C27 data (reference return)                                                                                                                                                      |

::: tip  
For more PLC data, refer to Mitsubishi's official "PLC Development Manual - M800/M80/E80 Series" for additional system operation data.  
:::