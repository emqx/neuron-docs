# Overview

**Support arch**: amd64, armv7

## Parameter Configuration

| Parameter | Description                        |
| --------- | ---------------------------------- |
| host      | device ip address                  |
| port      | device port, default 8193          |
| timeout   | connection timeout, default 3000ms |

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

## CNC Data

| tag address    | description                                  | data type    | parameter          |
| -------------- | -------------------------------------------- | ------------ | ------------------ |
| actf           | actual feed rate                             | int64/uint64 | -                  |
| absolute       | absolute position data of axis               | int64/uint64 | axis number(.n)    |
| machine        | machine position data of axis                | int64/uint64 | axis number(.n)    |
| relative       | relative position data of axis               | int64/uint64 | axis number(.n)    |
| distance       | distance to go of axis                       | int64/uint64 | axis number(.n)    |
| acts           | actual rotational speed of the spindle       | int64/uint64 | -                  |
| skip           | skipped position of axis                     | int64/uint64 | axis number(.n)    |
| srvdelay       | servo delay amount of axis                   | int64/uint64 | axis number(.n)    |
| accdecdly      | acceleration/deceration delay amount of axis | int64/uint64 | axis number(.n)    |
| spcss_srpm     | converted spindle speed                      | int64/uint64 | -                  |
| spcss_sspm     | specified surface speed                      | int64/uint64 | -                  |
| spcss_smax     | clamp of maxmum spindle speed                | int64/uint64 | -                  |
| movrlap_input  | input overlapped motion value                | int64/uint64 | axis number(.n)    |
| movrlap_output | output overlapped motion value               | int64/uint64 | axis number(.n)    |
| spload         | load information of the serial spindle       | int32/uint32 | spindle number(.n) |
| spmaxrpm       | maximum r.p.m ratio of serial spindle        | int32/uint32 | spindle number(.n) |
| spgear         | gear ratio of the serial spindle             | int32/uint32 | spindle number(.n) |

*CNC address example*

| address    | description                               |
| ---------- | ----------------------------------------- |
| actf       | read actual feed rate                     |
| absolute.1 | read absolute position of no.1 axis       |
| machine.3  | read machine position of no.3 axis        |
| spload.1   | read load information of no.1 spindle     |
| spmaxrpm.3 | read maximum r.p.m ratio  of no.3 spindle |

## PMC Data

| tag address | description                     | data type | access     |
| ----------- | ------------------------------- | --------- | ---------- |
| A           | message demand                  | all       | read/write |
| C           | counter                         | all       | read/write |
| D           | data table                      | all       | read/write |
| E           | extended relay                  | all       | read/write |
| F           | signal to CNC -> PMC            | all       | read       |
| G           | signal to PMC -> CNC            | all       | read/write |
| K           | keep relay                      | all       | read/write |
| M           | input signal from other device  | all       | read/write |
| N           | output signal from other device | all       | read/write |
| R           | internal relay                  | all       | read/write |
| T           | changeable timer                | all       | read/write |
| X           | signal to machine -> PMC        | all       | read       |
| Y           | signal to PMC -> machine        | all       | read/write |

*PMC address example*

| address | data type                                                    | descrption                                                   |
| ------- | ------------------------------------------------------------ | ------------------------------------------------------------ |
| A0      | uint8/int8/uint16/int16/uint32/int32/int64/uint64/float/double | PMC **message demand**，address 0                            |
| A0.1    | bit                                                          | PMC **message demand** ，no.1 bit of address 0               |
| A0.0    | bit                                                          | PMC **message demand** ，no.0 bit of address 0               |
| A0.2    | string                                                       | PMC **message demand** ，address 0 starts with a string of length 2 |
| D0.2    | string                                                       | PMC **data table** ，address 0 starts with a string of length 2 |
| D0.7    | bit                                                          | PMC **data table** ，no.7 bit of address 0                   |