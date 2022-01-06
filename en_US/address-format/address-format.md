# Neuron Driver Address Format

## General

This document describes the tag address formats for Neuron to setup with various kind of industrial protocol drivers. Each Neuron driver has its own address format that will be parsed in configuration process for machine or device communication.

## Allen-Bradley PLC2 (half duplex)

### General Details

| Settings            | Parameters      |
| ------------------- | --------------- |
| Runtime module      | neuron_o_df1hp2 |
| Driver name         | df1hp2          |
| Protocol            | DF1 half-duplex |
| Physical interface  | RS485           |
| Default settings    | 9600/8/N/1      |

### Address String

> <span style="font-family:sans-serif; font-size:2em;">STN!DST!ADDR</span>

**STN** is the slave station device number

**DST** is the destination node (CPU)

**ADDR** is the register address as following:

| Type |     | Format | Range     | Description      |
| ---- | --- | ------ | --------- | ---------------- |
| Word |     | DDDDD  | 0 ~ 65535 | Work Area (word) |

Note: Because the 1771KG is directly connected to the CPU, the STN and DST should be set to the same number (address of 1771KG module).

Example: 16!16 (slave number 20 octal)

16!16!520 (word 1010 octal in slave number 20 octal)

Set 8 (10 octal) for 1771-KG and set 0 for 1785-KE and 1770-KF2 in KG mode

## Allen-Bradley PLC5 (half duplex)

### General Details

| Settings            | Parameters      |
| ------------------- | --------------- |
| Runtime module      | neuron_o_df1ph5 |
| Driver name         | df1ph5          |
| Protocol            | DF1 half-duplex |
| Physical interface  | RS485           |
| Default settings    | 9600/8/N/1      |

### Address String

> <span style="font-family:sans-serif; font-size:2em;">STN!DST!ADDR</span>

**STN** is the slave station device number (KE/KF2 module address)

**DST** is the destination node (CPU)

**ADDR** is the register address as following.

| Type |     | Format | Range     | Description      |
| ---- | --- | -----  | --------- | ---------------- |
| Word |     | DDDDD  | 0 ~ 65535 | Work Area (word) |

Note: the KE or KF2 module inserts its address as the source, and this address will be the used data file number in the PLC5.

Example: 28!16 (KE/KF2 module number 34 octal and destination node=CPU number 20 octal). 28!16!10 means word 10 in file N28 in slave number 20 (octal).

Set 8 (10 octal) for 1771-KG and set 0 for 1785-KE and 1770-KF2 in KG mode

## Schneider TSX7 SCM (Modbus RTU)

### General Details

| Settings            | Parameters      |
| ------------------- | --------------- |
| Runtime module      | neuron_o_tsxmbr |
| Driver name         | tsxmbr          |
| Protocol            | Modbus RTU      |
| Physical interface  | RS232           |
| Default settings    | 9600/8/N/1      |

### Address String

> <span style="font-family:sans-serif; font-size:2em;">STN!ADDR</span>

**STN** is the slave station number (CPU) (1 – 247)

**ADDR** is the register address as following.

| Type |     | Format | Range     | Description     |
| ---- | --- | -----  | --------- | --------------- |
| Word | W   | DDDDD  | 0 ~ 32767 | Register (word) |

Example: **10!W100** means word 100 in slave station 10.

## Schneider TSX7 SCM (Modbus TCP)

### General Details

| Settings            | Parameters      |
| ------------------- | --------------- |
| Runtime module      | neuron_o_tsxmbt |
| Driver name         | tsxmbt          |
| Protocol            | Modbus TCP      |
| Physical interface  | Ethernet        |
| Default settings    | 502             |

### Address String

> <span style="font-family:sans-serif; font-size:2em;">ADDR</span>

**ADDR** is the register address as following:

| Type |     | Format | Range     | Description      |
| ---- | --- | -----  | --------- | ---------------- |
| Word | W   | DDDDD  | 0 ~ 32767 | Register         |

Example:**W4000** means word address 4000.

## Schneider Telemecanique UNI-TE

### General Details

| Settings            | Parameters     |
| ------------------- | -------------- |
| Runtime module      | neuron_o_unite                                                                         |
| Driver name         | unite                                                                                  |
| Protocol            | TSX SCM 2161 (Uni-Telway), directly on the built-in UNI-TE port on a V4 (or later) CPU |
| Physical interface  | RS232                                                                                  |
| Default settings    | 9600/8/N/1                                                                             |

### Address String

> <span style="font-family:sans-serif; font-size:2em;">STN!ADDR</span>

**STN** is the slave station number (Ad0 in CPU) (1 – 31)

**ADDR** is the register address as following:

| Type |     | Format | Range     | Description     |
| ---- | --- | ------ | --------- | --------------- |
| Word | W   | DDDDD  | 0 ~ 32767 | Register (word) |

Example: **1!W100** means word 100 in slave number 1.

## ABB SattControl Comli

### General Details

| Settings            | Parameters     |
| ------------------- | -------------- |
| Runtime module      | neuron_o_comli |
| Driver name         | comli          |
| Protocol            | COMLI          |
| Physical interface  | RS232          |
| Default settings    | 9600/8/N/1     |

### Address String

> <span style="font-family:sans-serif; font-size:2em;">STN!ADDR</span>

**STN** is the slave station number (CPU) (1 – 247)

**ADDR** is the register address as following

| Type |     | Format | Range    | Description     |
| ---- | --- | ------ | -------- | --------------- |
| Word | R   | DDDD   | 0 ~ 3071 | Register (word) |

Example: **1!R100** means word 100 in slave number 1.

## Omron Single HostLink (Point to Point)

### General Details

| Settings           | Parameters     |
| ------------------ | -------------- |
| Runtime module     | neuron_o_omrhls           |
| Driver name        | omrhls                    |
| Protocol           | Host-Link sysmac c-series |
| Physical interface | RS232                     |
| Default settings   | 9600/8/N/1                |

### Address String

> <span style="font-family:sans-serif; font-size:2em;">ADDR</span>

**ADDR** is the register address as following:

| Type |     | Format | Range    | Description     |
| ---- | --- | ------ | -------- | --------------- |
| Word | AR  | DDDD | 0 ~ 4095 | Auxiliary Relay        |
| Word | IR  | DDDD | 0 ~ 4095 | I/O and Internal Relay |
| Word | HR  | DDDD | 0 ~ 4095 | Hold Relay             |
| Word | LR  | DDDD | 0 ~ 4095 | Link Relay             |
| Word | TC  | DDDD | 0 ~ 255  | Timer                  |
| Word | DM  | DDDD | 0 ~ 9999 | Data Register          |

Example: **DM100** means word 100 in DM data memory area.

## Omron Multiple HostLink (MasterSlave)

### General Details

| Settings           | Parameters     |
| ------------------ | -------------- |
| Runtime module     | neuron_o_omrhls           |
| Driver name        | omrhls                    |
| Protocol           | Host-Link sysmac c-series |
| Physical interface | RS232                     |
| Default settings   | 9600/8/N/1                |

### Address String

> <span style="font-family:sans-serif; font-size:2em;">STN!ADDR</span>

**STN** is station number/module number (0 – 31)

**ADDR** is the register address as following:

| Type |     | Format | Range    | Description     |
| ---- | --- | ------ | -------- | --------------- |
| Word | AR  | DDDD | 0 ~ 4095 | Auxiliary Relay        |
| Word | IR  | DDDD | 0 ~ 4095 | I/O and Internal Relay |
| Word | HR  | DDDD | 0 ~ 4095 | Hold Relay             |
| Word | LR  | DDDD | 0 ~ 4095 | Link Relay             |
| Word | TC  | DDDD | 0 ~ 255  | Timer                  |
| Word | DM  | DDDD | 0 ~ 9999 | Data Register          |

Example: **10!DM100** means word 100 in data memory in slave 10.

## Omron FINS on TCP

### General Details

| Settings           | Parameters         |
| ------------------ | ---------------    |
| Runtime module     | neuron_o_finstc    |
| Driver name        | finstc             |
| Protocol           | FINS on TCP        |
| Physical interface | Ethernet RJ45      |
| Default settings   | port：2000          |

### Address String

> <span style="font-family:sans-serif; font-size:2em;">ADDR[.BIT]</span>

**ADDR**  is the data memory word address starting with “DM”

**BIT**  bit(option)

| Type |  Address prefix   | Format    | Range       | Description       |
| ---- | --------- | -----   | --------------| ------------------   |
| Word/Bit | CIO       | DDDD[.dd]    | 0 ~ 6143      | CIO Area           |
| Word/Bit | WR        | DDD[.dd]     | 0 ~ 511       | Work Area            |
| Word/Bit | HR        | DDD[.dd]     | 0 ~ 511       | Holding Bit Area           |
| Word/Bit | AR        | DDD[.dd]     | 0 ~ 959       | Auxiliary Bit Area 0~447 read only    |
| Word/Bit | PV (Timer/Counter)       | DDDD[.dd]    | 0 ~ 4095      | Timer / Counter    |
| Bit      | F (Completion Flag) | DDDD         | 0 ~ 4095      | Completion Flag     |
| Word/Bit | DM        | DDDDD[.dd]   | 0 ~ 32767     | Data Memory           |
| Word/Bit | EM0~EM18  | DDDDD[.dd]   | 0 ~ W32767    | Extended Memory, use W separate area and address    |

Example: DM100 means word 100 in data memory.

## Siemens S5 3964R/RK512

### General Details

| Settings           | Parameters     |
| ------------------ | -------------- |
| Runtime module     | neuron_o_s539rk |
| Driver name        | s539rk          |
| Protocol           | 3964R/RK512     |
| Physical interface | RS232           |
| Default settings   | 9600/8/N/1      |

### Address String

> <span style="font-family:sans-serif; font-size:2em;">ADDR</span>

**ADDR** is the address as following

DB is the data block (0 – 999)

DBW(_ **word offset** _) is the data word in that data block

| Type |     | Format | Range    | Description     |
| ---- | ----------- | ---------- | ------------------ | ------------- |
| Word | I           | DDDD       | 0 ~ 4095           | Input         |
| Word | Q           | DDDD       | 0 ~ 4095           | Output        |
| Word | M           | DDDD       | 0 ~ 4095           | Marker Memory |
| Word | DB0~999.DBW | DDDDD</br>DDDDD | 0 ~ 65535</br>0 ~ 65535 | Data Memory   |
| Word | T           | DDD        | 0 ~ 255            | Timer         |
| Word | C           | DDD        | 0 ~ 255            | Counter       |

Example: DB100 (data block 100)

**DB100.DBW20** (DBddd.DBWddddd) means data word 20 in data block 100

## Siemens S7 3964R/RK512 
### General Details

| Settings            | Parameters     |
| ------------------- | -------------- |
| Runtime module      | neuron_o_s739rk |
| Driver name         | S739rk          |
| Protocol            | 3964R/RK512     |
| Physical interface  | RS232           |
| Default settings    | 9600/8/N/1      |

### Address String

> <span style="font-family:sans-serif; font-size:2em;">ADDR</span>

**ADDR** is the address as following

**DB** is the data block (0 – 999)

**DBW**(_**byte offset**_) is the data word in that data block

| Type |     | Format | Range    | Description     |
| ---- | ----------- | ---------- | ------------------ | -------------------------------------- |
| Byte | IW          | DDDD       | 0 ~ 4095           | Input                                  |
| Byte | QW          | DDDD       | 0 ~ 4095           | Output                                 |
| Byte | MW          | DDDD       | 0 ~ 4095           | Marker Memory                          |
| Byte | DB0~999.DBW | DDDDD</br>DDDDD | 0 ~ 65535</br>0 ~ 65535 | Data Memory (must be in even byte no.) |
| Byte | T           | DDD        | 0 ~ 255            | Timer                                  |
| Byte | C           | DDD        | 0 ~ 255            | Counter                                |

Note: The real DBW should be used (eg. DBW0, DBW2 etc) and the driver will read the byte start from 0 and the byte start from 2. It reads a word from byte 0, byte 2 respectively.

Example: DB100 (data block 100)

**DB100.DBW20** (DBddd.DBWddddd) means data word 20 in data block 100

## Siemens FETCH/WRITE 
### General Details

| Settings           | Parameters     |
| ------------------ | -------------- |
| Runtime module      | neuron_o_siefw               |
| Driver name         | siefw                        |
| Protocol            | Siemens Fetch/Write Protocol |
| Physical interface  | Ethernet                     |
| Default port no.    | 2200                   |

### Address String

> <span style="font-family:sans-serif; font-size:2em;">ADDR</span>

**ADDR** is the address as following

**DB** is the data block (0 – 999)

**DBW**(_**byte offset**_) is the data word (start) in that data block.

| Type |     | Format | Range    | Description     |
| ---- | ----------- | ---------- | ------------------ | ------------------------------------- |
| Byte | IW          | DDDD       | 0 ~ 4095           | Input                                 |
| Byte | QW          | DDDD       | 0 ~ 4095           | Output                                |
| Byte | MW          | DDDD       | 0 ~ 4095           | Marker Memory                         |
| Byte | DB0~999.DBW | DDDDD</br>DDDDD | 0 ~ 65535</br>0 ~ 65535 | Data Memory (must be in even byte no) |
| Byte | T           | DDD        | 0 ~ 255            | Timer                                 |
| Byte | C           | DDD        | 0 ~ 255            | Counter                               |

Note: There is a limitation in the protocol. The DB can only be between 1-255 and the start address of a read or write table cannot go beyond DBW2047, however the end of a table can. But during the test, it was possible to start at address DBW32766.

Note: In the Simatic PLC you just define a TCP/IP connection for either FETCH passive (read only) or WRITE passive (write only), listening on a certain port. Currently there is no FETCH/WRITE passive setting, so two connections with different ports are required, one for read and one for write.

Example: **DB200.DBW20** (DBddd.DBWddddd) means data word 20 in data block 200.

## Siemens Industrial Ethernet S7 ISOTCP 
### General Details

| Settings            | Parameters     |
| ------------------- | -------------- |
| Runtime module      | neuron_o_s7pro           |
| Driver name         | s7pro                    |
| Protocol            | S7 ISO TCP (S7 protocol) |
| Physical interface  | Ethernet                 |
| Default port no.    | 102                |

### Address String

> <span style="font-family:sans-serif; font-size:2em;">ADDR</span>

**ADDR** is the address as following

Note: DB is the data block (0 – 999)

DBW(_**byte offset**_) is the data word (start) in that data block.

| Type |     | Format | Range    | Description     |
| ---- | --- | ------ | -------- | --------------- |
| Byte | IW         | DDDD       | 0 ~ 4095           | Input                                  |
| Byte | QW         | DDDD       | 0 ~ 4095           | Output                                 |
| Byte | MW         | DDDD       | 0 ~ 4095           | Marker Memory                          |
| Byte | DB0~999DBW | DDDDD</br>DDDDD | 0 ~ 65535</br>0 ~ 65535 | Data Memory (must be in even byte no.) |
| Byte | T          | DDD        | 0 ~ 255            | Timer                                  |
| Byte | C          | DDD        | 0 ~ 255            | Counter                                |

Example: **DB200.DBW20** (DBddd.DBWddddd) means data word 20 in data block 200.

S7P_SCRTSAP is the source TSAP for S7 protocol(default 0x0101)

S7P_DSTTSAP is the destination TSAP for S7 protocol(default 0x0101)

TSAP(2Byte):
frist byte: 0x01: PG or PC, 0x02: OS, 0x03: Others, such as OPC server, s7 plc
second byte:
|7-4 bit| 3-0bit|
|--|--|
|rack number|cpu slot|

### Notes

An external equipment can access to S71200/1500 CPU using the S7 “base” protocol, only working as an HMI, i.e. only basic data transfer are allowed.

All other PG operations (control/directory/etc..) must follow the extended protocol.

Particularly to access a DB in S71500 some additional setting plc-side are needed.

1. Only global DBs can be accessed.
2. The optimized block access must be turned off.
3. The access level must be “full” and the “connection mechanism” must allow GET/PUT.

## Mitsubishi FX0S/FX0N/FX1S/FX1N/FX2

### General Details

| Settings           | Parameters     |
| ------------------ | -------------- |
| Runtime module     | neuron_o_fxnpro |
| Driver name        | fxnpro          |
| Protocol           | RS command      |
| Physical interface | RS232           |
| Default settings   | 9600/7/E/1      |

### Address String

> <span style="font-family:sans-serif; font-size:2em;">ADDR</span>

**ADDR** is the register address

| Type |     | Format | Range    | Description     |
| ---- | --- | ------ | -------- | --------------- |
| Bit   | X   | OOO  | 0 ~ 377     | Input Relay           |
| Bit   | Y   | OOO  | 0 ~ 377     | Output Relay          |
| Bit   | M   | DDDD | 0 ~ 7999    | Auxiliary Relay       |
| Bit   | T   | DDD  | 0 ~ 255     | Timer Relay           |
| Bit   | C   | DDD  | 0 ~ 255     | Counter Relay         |
| Bit   | SM  | DDDD | 8000 ~ 9999 | Special Aux. Relays   |
| Bit   | S   | DDDD | 0 ~ 4095    | States                |
| Word  | TN  | DDD  | 0 ~ 255     | Timer Memory          |
| Word  | CN  | DDD  | 0 ~ 199     | Counter Memory        |
| Word  | D   | DDDD | 0 ~ 7999    | Data Register         |
| DWord | CN2 | DDD  | 200 ~ 255   | Counter Memory        |
| Word  | SD  | DDDD | 8000 ~ 9999 | Special Data Register |

Example: **D100** means word 100 in D data memory area.

## Mitsubishi FX2N/FX3U/FX3G Series

### General Details

| Settings           | Parameters     |
| ------------------ | --------------- |
| Runtime module     | neuron_o_fx3u3g |
| Driver name        | fx3u3g          |
| Protocol           | RS command      |
| Physical interface | RS232           |
| Default settings   | 9600/7/E/1      |

### Address String

> <span style="font-family:sans-serif; font-size:2em;">ADDR</span>

**ADDR** is the register address as following:

| Type |     | Format | Range    | Description     |
| ---- | --- | ------ | -------- | --------------- |
| Bit   | X   | OOO  | 0 ~ 764     | Input Relay           |
| Bit   | Y   | OOO  | 0 ~ 764     | Output Relay          |
| Bit   | M   | DDDD | 0 ~ 7999    | Auxiliary Relay       |
| Bit   | T   | DDD  | 0 ~ 511     | Timer Relay           |
| Bit   | C   | DDD  | 0 ~ 255     | Counter Relay         |
| Bit   | SM  | DDDD | 8000 ~ 9999 | Special Aux. Relays   |
| Bit   | S   | DDDD | 0 ~ 4095    | States                |
| Word  | TN  | DDD  | 0 ~ 511     | Timer Memory          |
| Word  | CN  | DDD  | 0 ~ 199     | Counter Memory        |
| Word  | D   | DDDD | 0 ~ 7999    | Data Register         |
| DWord | CN2 | DDD  | 200 ~ 255   | Counter Memory        |
| Word  | SD  | DDDD | 8000 ~ 9999 | Special Data Register |
| Word  | R   | DDDD | 0 ~ 32767   | Extended Register     |

Example: **D100** means word 100 in D data memory area.

## Mitsubishi Melsec E71 for Q Series

### General Details

| Settings           | Parameters     |
| ------------------ | -------------- |
| Runtime module      | neuron_o_mele71 |
| Driver name         | mele71          |
| Protocol            | MELSEC E71      |
| Physical interface  | Ethernet        |
| Default port no.    | 2000            |

### Caution

Multiple connection requests cannot be handled by a single port in Q series PLCs. When connecting to a PLC using the E71 protocol, be sure to assign a separate port for each neuron instance in the parameter settings of the PLC and specify the protocol as TCP and MC.

### Address String

> <span style="font-family:sans-serif; font-size:2em;">ADDR</span>

**ADDR** is the register address as following:

| Type |     | Format | Range    | Description     |
| ---- | --- | ------ | -------- | --------------- |
| Bit  | X   | HHHH    | 0 ~ 1fff    | Input Relay             |
| Bit  | Y   | HHHH    | 0 ~ 1fff    | Output Relay            |
| Bit  | M   | DDDDD   | 0 ~ 61439   | Internal Relay          |
| Bit  | L   | DDDDD   | 0 ~ 32767   | Latch Relay             |
| Bit  | F   | DDDDD   | 0 ~ 32767   | Annunciator             |
| Bit  | V   | DDDDD   | 0 ~ 32767   | Edge Relay              |
| Bit  | B   | HHHH    | 0 ~ efff    | Link Relay              |
| Bit  | TC  | DDDD    | 0 ~ 2047    | Timer Coil              |
| Bit  | SS  | DDDDD   | 0 ~ 25471   | Retentive Timer Contact |
| Bit  | SC  | DDDDD   | 0 ~ 25471   | Retentive Timer Coil    |
| Bit  | CS  | DDDDD   | 0 ~ 25471   | Counter Contact         |
| Bit  | CC  | DDDDD   | 0 ~ 25471   | Counter Coil            |
| Bit  | SB  | HHH     | 0 ~ 7ff     | Special Link Relay      |
| Bit  | DX  | HHHH    | 0 ~ 1fff    | Direct Input            |
| Bit  | DY  | HHHH    | 0 ~ 1fff    | Direct Output           |
| Bit  | TS  | DDDD    | 0 ~ 2047    | Timer Contact           |
| Word | W   | HHHH    | 0 ~ 2fff    | Link Register           |
| Word | TN  | DDDD    | 0 ~ 2047    | Timer Current Value     |
| Word | SN  | DDDD    | 0 ~ 2047    | Retentive Timer Current |
| Word | CN  | DDDD    | 0 ~ 1023    | Counter Value           |
| Word | SW  | HHH     | 0 ~ 7ff     | Special Link Register   |
| Word | Z   | DD      | 0 ~ 19      | Index Register          |
| Word | ZR  | HHHHH   | 0 ~ fe7a5   | File Register           |
| Word | D   | DDDDDDD | 0 ~ 4212735 | Data Register           |
| Word | SD  | DDDD    | 0 ~ 2047    |                         |

Example: **D100** means word 100 in D data memory area.

## Modbus RTU

### General Details

| Settings           | Parameters     |
| ------------------ | -------------- |
| Runtime module       | neuron_o_mbsrtu |
| Driver name          | mbsrtu          |
| Protocol             | Modbus RTU      |
| Physical interface   | RS485           |
| Default settings     | 9600/8/N/1      |

### Address String

> <span style="font-family:sans-serif; font-size:2em;">STN!ADDR[.BIT][#ENDIAN]</span>

**STN** is slave number or device ID (0-247)

**ADDR** is the register address as following:

**BIT** Bit no.(0-15)

**ENDIAN** Endianness of the value

| Type |     | Format | Range    | Description     |
| ---- | --- | ------ | -------- | --------------- |
| Bit  | 01/05/15 | DDDDDD | 000001 ~ 065536 | Discrete Output Coils           |
| Bit  | 02       | DDDDDD | 100001 ~ 165536 | Discrete Input Contacts         |
| Word | 04       | DDDDDD | 300001 ~ 365536 | Analog Input Registers          |
| Word | 03/06/16 | DDDDDD | 400001 ~ 465536 | Analog Output Holding Registers |

## Modbus TCP

### General Details

| Settings           | Parameters     |
| ------------------ | -------------- |
| Runtime module     | neuron_o_mbstcp |
| Driver name        | mbstcp          |
| Protocol           | Modbus TCP      |
| Physical interface | Ethernet        |
| Default port no.   | 502             |

### Address String

> <span style="font-family:sans-serif; font-size:2em;">STN!ADDR[.BIT][#ENDIAN]</span>

**STN** is slave number or device ID (0-247)

**ADDR** is the register address as following:

**BIT** Bit no.(0-15)

**ENDIAN** Endianness of the value

| Type |     | Format | Range    | Description     |
| ---- | --- | ------ | -------- | --------------- |
| Bit  | 01/05/15 | DDDDDD | 000001 ~ 065536 | Discrete Output Coils           |
| Bit  | 02       | DDDDDD | 100001 ~ 165536 | Discrete Input Contacts         |
| Word | 04       | DDDDDD | 300001 ~ 365536 | Analog Input Registers          |
| Word | 03/06/16 | DDDDDD | 400001 ~ 465536 | Analog Output Holding Registers |

Example:**2!404001** means word address 4000 with in slave number 2.

## Modbus RTU over TCP

### General Details

| Settings           | Parameters     |
| ------------------ | -------------- |
| Runtime module     | neuron_o_mbsrot     |
| Driver name        | mbsrot              |
| Protocol           | Modbus RTU over TCP |
| Physical interface | Ethernet            |
| Default port no.   | 502                 |

### Address String

> <span style="font-family:sans-serif; font-size:2em;">STN!ADDR[.BIT][#ENDIAN]</span>

**STN** is slave number or device ID (0-247)

**ADDR** is the register address as following:

**BIT** Bit no.(0-15) 

**ENDIAN** Endianness of the value

| Type |     | Format | Range    | Description     |
| ---- | --- | ------ | -------- | --------------- |
| Bit  | 01/05/15 | DDDDDD | 000001 ~ 065536 | Discrete Output Coils           |
| Bit  | 02       | DDDDDD | 100001 ~ 165536 | Discrete Input Contacts         |
| Word | 04       | DDDDDD | 300001 ~ 365536 | Analog Input Registers          |
| Word | 03/06/16 | DDDDDD | 400001 ~ 465536 | Analog Output Holding Registers |

Example:**2!404001** means word address 4000 with in slave number 2.

## IEC 61850

### General Details

| Settings           | Parameters     |
| ------------------ | -------------- |
| Runtime module     | neuron_o_i61850 |
| Driver name        | i61850          |
| Protocol           | IEC 61850       |
| Physical interface | Ethernet        |
| Default settings   | 102             |

### Address String

> <span style="font-family:sans-serif; font-size:2em;">FC!ADDR</span>

**FC** is functional constraints value as following:

| Fn  |     Format     |     Description     |
| --- | -------------- | ----------------------------------- |
| 0   | IEC61850_FC_ST | Status information                  |
| 1   | IEC61850_FC_MX | Measurands - analog values          |
| 2   | IEC61850_FC_SP | Setpoint                            |
| 3   | IEC61850_FC_SV | Substitution                        |
| 4   | IEC61850_FC_CF | Configuration                       |
| 5   | IEC61850_FC_DC | Description                         |
| 6   | IEC61850_FC_SG | Setting group                       |
| 7   | IEC61850_FC_SE | Setting group editable              |
| 8   | IEC61850_FC_SR | Service response / Service tracking |
| 9   | IEC61850_FC_OR | Operate received                    |
| 10  | IEC61850_FC_BL | Blocking                            |
| 11  | IEC61850_FC_EX | Extended definition                 |
| 12  | IEC61850_FC_CO | Control                             |
| 13  | IEC61850_FC_US | Unicast SV                          |
| 14  | IEC61850_FC_MS | Multicast SV                        |
| 15  | IEC61850_FC_RP | Unbuffered report                   |
| 16  | IEC61850_FC_BR | Buffered report                     |
| 17  | IEC61850_FC_LG | Log control blocks                  |

**ADDR** is the object reference address string

The IEC61850 data hierarchical model are usually as following:

Physical Device (IED)

Logical Device (LD)

Logical Node (LN)

Object Data (DO)

Object Attribute (DA)

Example:**1!testmodelSENSORS/TTMP1.TmpSv.instMag.f**

means the functional constraint of this tag is 1 (IEC61850_FC_MX –analog measurands). The object reference address string are (IED) – testmodel, (LD) – SENSORS, (LN) – TTMP1, (DO) – TmpSv, (DA) – instMag.f for floating value.

## OPC UA

### General Details

| Settings           | Parameters     |
| ------------------ | -------------- |
| Runtime module     | neuron_o_opcua |
| Driver name        | opcua          |
| Protocol           | OPC UA         |
| Physical interface | Ethernet       |
| Default port no.   | 4840           |

### Certificate Setting

OPCUA can login to OPC-UA server by user self-signed certificate, certificate and key must meet the following conditions.

* CERTIFICATE and KEYFILE must be set at the same time
* Certificate must be generated by X.509v3 standard
* The SAN field of the Certficate must contain ` URI:urn:xxx.xxx.xxx`, with the "xxx" part being a custom part
* Certificate file and key file must be encoded with DER format

The certificate file can be imported into the target server in advance and set as trust, or it can be set by neuron and submitted automatically and then set as trust by the server.

Certificate generation steps(Windows/Linux/Mac):

```bash
$openssl req -config localhost.cnf -new -nodes -x509 -sha256 -newkey rsa:2048 -keyout localhost.key -days 365 -subj "/C=DE/O=neuron/CN=NeuronClient@localhost" -out localhost.crt
$openssl x509 -in localhost.crt -outform der -out client_cert.der
$openssl rsa -inform PEM -in localhost.key -outform DER -out client_key.der
$rm localhost.crt
$rm localhost.key
```

The *.cnf file specified by `-config` can be modified using the [template file for openssl]([openssl/openssl.cnf at master - openssl/openssl (github.com)](https://github.com/openssl/openssl /blob/master/apps/openssl.cnf)) to be modified to include the following configuration section:

```ini
[ v3_req ]

# Extensions to add to a certificate request

basicConstraints = CA:FALSE
keyUsage = nonRepudiation, digitalSignature, keyEncipherment
subjectAltName = @alt_names

[ alt_names ]
URI.1 = urn:xxx.xxx.xxx
DNS.1 = localhost
#DNS.2 = localhost
IP.1 = 127.0.0.1
#IP.2 = 0.0.0.0
```

`-days` can set the value as desired.

### Certificate conversion
You can convert PEM certificate and private key to DER format by following steps and commands
1. Save all the contents including "-----BEGIN CERTIFICATE-----" and "-----END CERTIFICATE-----" as 1.crt;
2. Save all the contents including "-----BEGIN PRIVATE KEY-----" and "-----END PRIVATE KEY-----" as 1.key;
3. Execute the following command:
```bash
$ openssl x509 -in 1.crt -outform der -out cert.der   
$ openssl rsa -inform PEM -in 1.key -outform DER -out key.der
```

### Address String

> <span style="font-family:sans-serif; font-size:2em;">IX!NODEID</span>

**IX** is the namespace index. (1-32767)

**NODEID** is the node ID. (any string exclude &#39;!&#39;)

Example: 2!Device1.Module1.Tag1 represents namespace index is 2 and node ID is Device1.Module1.Tag1

Neuron version 1.4 already supports fixed-length string read and write, you need to add the string length identifier - #length to the node ID, if you want to set Device1.Module1.Tag1 to a string type with length 20, the full access address is 2!Device1 .Module1.Tag1#20

Please refer to OPC UA standard for the explanation of namespace index and node id.

## IEC 60870-5-104

### General Details

| Settings       | Parameters      |
| -------------- | --------------- |
| Runtime module | neuron_o_iec104 |
| Driver name| IEC 60870-5-104  |
| Protocol       | IEC 60870-5-104 |
| Physical interface| Ethernet|
| Default port no.| 2404     |

### Parameters

| Settings    | Parameters            | Description      |
| ------ | -------| -------- |
| k   |        | default 12|
| w   |        | default 8|
| t0  |Timeout of connection establishment| default 30|
| t1  |Timeout for sending APDU           | default 15     |
| t2  |Timeout for acknowledges in case of no data message t2 M t1| default 10|
| t3  |Timeout for sending frames| default 20     |

### Address String

> <span style="font-family:sans-serif; font-size:2em;">CA!IOA</span>

**CA** Station Address

**IOA** Starting Information Object Address

|data name|data type|
|--------|-------|
|M_ME_NA_1|WORD,UWORAD,DWORD,UDWORD |
|M_ME_TD_1|WORD,UWORAD,DWORD,UDWORD |
|M_ME_ND_1|WORD,UWORAD,DWORD,UDWORD |
|M_ME_NB_1|WORD,UWORAD,DWORD,UDWORD |
|M_ME_TE_1|WORD,UWORAD,DWORD,UDWORD |
|M_ME_NC_1|FLOAT,DOUBLE|
|M_ME_TF_1|FLOAT,DOUBLE|
|M_SP_NA_1|BOOL|
|M_SP_TB_1|BOOL|

Example: 1!2 represents Station Address is 1 and IOA is 2

## DL/T645-2007

### General Details

| Settings            | Parameters             |
| -------------- | --------------- |
| Runtime module | neuron_o_dlt645 |
| Driver name    | dlt645          |
| Protocol       | DL/T645-2007      |
| Physical interface   | RS485           |
| Default settings   | 9600/8/N/1      |
The calibration method of general electricity meter is even calibration.

### Address String

> <span style="font-family:sans-serif; font-size:2em;">STN1!STN2!ADDR</span>

**STN1** is the first three bytes of the communication address of the meter.

**STN2** is the last three bytes of the communication address of the meter

**ADDR** is the corresponding data identification:

|  data identification    | Description                  |
| ----------- | -------------------- |
| 33343435    | Read A-phase voltage             |
| 33343535    | Read A-phase current             |
| 33333333    | Read the total active energy of the current combination   |

Example：210220!003011!33343435 represents the voltage value of the device with communication address 210220003011
