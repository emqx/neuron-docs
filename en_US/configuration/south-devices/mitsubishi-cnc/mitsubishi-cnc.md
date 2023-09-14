# Overview

The Mitsubishi CNC driver can access Mitsubishi M70 and M80 series machine tools and machining centers through TCP/IP protocol, and collect various CNC operation data in real time, including program name, spindle speed, spindle speed override, spindle load, emergency stop, etc.

## Parameter Configuration

| Parameter | Description              |
| --------- | ------------------------ |
| host      | device ip address        |
| port      | device port, default 683 |

## Support Data Type

* uint16
* int16
* uint32
* int32
* bit
* string

## CNC Data

| tag address | description                    | data type | parameter |
| ----------- | ------------------------------ | --------- | --------- |
| ProgramMain | main program no                | string    | -         |
| FeedSpeedFA | F command feed speed           | double    | -         |
| FeedSpeedFM | Manual effective feed speed    | double    | -         |
| FeedSpeedFS | Synchronization feed speed     | double    | -         |
| FeedSpeedFC | Automatic effective feed speed | double    | -         |
| FeedSpeedFE | Screw lead                     | double    | -         |

*CNC address example*

| address     | description          |
| ----------- | -------------------- |
| ProgramMain | read main program no |


### PLC Data

| tag address | description                              | data type       | access |
| ----------- | ---------------------------------------- | --------------- | ------ |
| X           | input signal to programmable controller  | bit/16bit/32bit | rw     |
| Y           | output signal to programmable controller | bit/16bit/32bit | rw     |
| R           | file register                            | 16bit/32bit     | rw     |

*PLC Common Address*

| address | data type | descrption                                                                                         |
| ------- | --------- | -------------------------------------------------------------------------------------------------- |
| R69     | uint16    | PLC R area, address 69,emergency stop（65519 ON 65535 OFF）                                        |
| R2500   | uint16    | PLC R area, address 2500, feed rate                                                                |
| R7008   | uint16    | PLC R area, address 7008, spindle rate                                                             |
| R6506   | uint32    | PLC R area, address 6506, actual spindle speed                                                     |
| R7000   | uint32    | PLC R area, address 7000~7001, S commond spindle speed                                             |
| R6525   | uint16    | PLC R area, address 6525, spindle load                                                             |
| R6529   | uint16    | PLC R area, address 6529, spindle alarm no                                                         |
| R606    | uint32    | PLC R area, address 606 ~ 607 , current value of workpiece processing number                       |
| R608    | uint32    | PLC R area, address 608 ~ 609 , maximum value of workpiece processing number                       |
| R11824  | uint32    | PLC R area, address 11824 ~ 11825 , tool group number in use                                       |
| R11826  | uint32    | PLC R area, address 11826 ~ 11827 , tool number in use                                             |
| R11830  | uint32    | PLC R area, address 11830 ~ 11831 , cumulative data on tool usage time in use                      |
| R11832  | uint32    | PLC R area, address 11832 ~ 11833 , data on tool life setting time in use                          |
| XC00    | uint16    | PLC X area, address C00 ~ C0F , control mode (1 JOG 2 HO 4 SO 8  16 PTPO 32 ASTO 256 MEMO 2048 DO) |
| XC12    | bit       | PLC X area, address C12 , auto running                                                             |
| XC13    | bit       | PLC X area, address C13 , auto running start                                                       |
| XC14    | bit       | PLC X area, address C14 , auto running pause                                                       |
| XC15    | bit       | PLC X area, address C15 , reset                                                                    |
| XC20    | bit       | PLC X area, address C20 , fast feed                                                                |
| XC21    | bit       | PLC X area, address C21 , machining feed                                                           |
| XC22    | bit       | PLC X area, address C22 , tapping                                                                  |
| XC23    | bit       | PLC X area, address C23 , thread cutting                                                           |
| XC24    | bit       | PLC X area, address C24 , synchronous feed                                                         |
| XC25    | bit       | PLC X area, address C25 , constant speed                                                           |
| XC26    | bit       | PLC X area, address C26 , jumping                                                                  |
| XC27    | bit       | PLC X area, address C27 , reference point return in progress                                       |

::: tip
The PLC data sheet can be found on Mitsubishi's official website provided in the "PLC Development Manual - M800/M80/E80 Series", which contains more information on system operation data.
:::
