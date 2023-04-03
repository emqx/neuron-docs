# Overview

IEC61850 is an international communication standard protocol that achieves station-wide communication uniformity through a series of standardization of devices. IEC61850 is widely used in the power industry.

The MMS message specification is applied between the IEC61850 standard station control layer and the interval layer. MMS achieves interoperability between different manufacturing devices in a network environment through an object-oriented modeling approach to the actual devices.

The IEC61850 plug-in is used for read/write to the IEC61850 server and currently supports access to the MMS protocol.

## Parameters

|   Parameters   | Description                      |
| -------- | -------------------------- |
| **Device IP Address** |  Target device IP             |
| **Device Port** | Target device port, Default 102 |
| **Local AP Title** | ACSE AP-Title of this device as string (default = '1,1,1,999') |
| **Local AE Qualifier** | ACSE AE-Qualifier of this device (default = 12) |
| **Local P Selector** | Local PSAP-Address (PSAP = Presentation Service Access Point, default = 1) |
| **Local S Selector** | Local SSAP-Address (SSAP = Session Service Access Point, default = 1) |
| **Local T Selector** | Local TSAP-Address (TSAP = Transport Service Access Point, default = 1) |
| **Remote AP Title** | ACSE AP-Title of remote device as string (default = '1,1,1,999.1') |
| **Remote AE Qualifier** | ACSE AE-Qualifier of remote device (default = 12) |
| **Remote P Selector** | Remote PSAP-Address (PSAP = Presentation Service Access Point, default = 1) |
| **Remote S Selector** | Remote SSAP-Address (SSAP = Session Service Access Point, default = 1) |
| **Remote T Selector** | Remote TSAP-Address (TSAP = Transport Service Access Point, default = 1) |
| **Authentication Enabled** | Whether to enable Authentication |
| **Authentication Method** | Authentication Method, Password/None |
| **Authentication Password** | Authentication Password |

## Data Types

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
* BOOL
* STRING

## Address forma

> Logical Devices/Logical Nodes$FC$DO$DA</span>

## Examples

|  Address                                 | Data type | Description                                                 |
| ------------------------------------- | -------- | ---------------------------------------------------- |
| GenericIO/GGIO1$CF$Mod$ctlModel       | INT8     | LD-GenericIO,LN-GGIO1,FC-CF,DO-Mod,DA-ctlModel       |
| GenericIO/GGIO1$CO$SPCSO1$Oper$ctlNum | UINT8    | LD-GenericIO,LN-GGIO1,FC-CO,DO-SPCSO1,DA-Oper$ctlNum |
| GenericIO/GGIO1$CF$SPCSO1$ctlModel    | INT16    | LD-GenericIO,LN-GGIO1,FC-CF,DO-SPCSO1,DA-ctlModel    |
| GenericIO/GGIO1$CO$SPCSO2$Oper$ctlNum | UINT16   | LD-GenericIO,LN-GGIO1,FC-CO,DO-SPCSO2,DA-Oper$ctlNum |
| GenericIO/GGIO1$CF$SPCSO2$ctlModel    | INT32    | LD-GenericIO,LN-GGIO1,FC-CF,DO-SPCSO2,DA-ctlModel    |
| GenericIO/GGIO1$ST$SPCSO4$Oper$ctlNum | UINT32   | LD-GenericIO,LN-GGIO1,FC-ST,DO-SPCSO4,DA-Oper$ctlNum |
| GenericIO/GGIO1$CF$SPCSO3$ctlModel    | INT64    | LD-GenericIO,LN-GGIO1,FC-CF,DO-SPCSO3,DA-ctlModel    |
| GenericIO/GGIO1$ST$SPCSO1$ctlNum      | UINT64   | LD-GenericIO,LN-GGIO1,FC-ST,DO-SPCSO1,DA-ctlNum      |
| GenericIO/GGIO1$MX$AnIn1$mag$f        | FLOAT    | LD-GenericIO,LN-GGIO1,FC-MX,DO-AnIn1,DA-mag$f        |
| GenericIO/GGIO1$MX$AnIn3$mag$f        | DOUBLE   | LD-GenericIO,LN-GGIO1,FC-MX,DO-AnIn3,DA-mag$f        |
| GenericIO/GGIO1$CO$SPCSO1$Oper$Test   | BOOL     | LD-GenericIO,LN-GGIO1,FC-CO,DO-SPCSO1,DA-Oper$Test   |
| GenericIO/LLN0$DC$NamPlt$vendor       | STRING   | LD-GenericIO,LN-GGIO1,FC-DC,DO-NamPlt,DA-vendor      |
