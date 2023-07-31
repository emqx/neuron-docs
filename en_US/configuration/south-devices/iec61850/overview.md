# IEC60870-5-104

IEC61850 is an international communication standard protocol that achieves station-wide communication uniformity through a series of standardization of devices. IEC61850 is widely used in the power industry.

The MMS message specification is applied between the IEC61850 standard station control layer and the interval layer. MMS achieves interoperability between different manufacturing devices in a network environment through an object-oriented modeling approach to the actual devices.

The IEC61850 plug-in is used for read/write to the IEC61850 server and currently supports access to the MMS protocol.

## Add Device

Go to **Configuration -> South Devices**, then click **Add Device** to add the driver. Configure the following settings in the popup dialog box.

- Name: The name of this device node.
- Plugin: Select the **IEC60870-5-104** plugin.

## Device Configuration

After clicking **Create**, you will be redirected to the **Device Configuration** page, where we will set up the parameters required for Neuron to establish a connection with the northbound application. You can also click the device configuration icon on the southbound device card to enter the **Device Configuration** interface.

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

## Configure Data Groups and Tags

After the plug-in is added and configured, the next step is to establish communication between your device and Neuron by adding groups and tags to the Southbound driver.

Once device configuration is completed, navigate to the **South Devices** page. Click on the device card or device row to access the **Group List** page. Here, you can create a new group by clicking on **Create**, then specifying the group name and data collection interval.

Upon successfully creating a group, click on its name to proceed to the **Tag List** page. This page allows you to add device tags for data collection. You'll need to provide information such as the tag address, attributes, and data type.

For information on general configuration items, see [Connect to Southbound Devices](../south-devices.md). The subsequent section will concentrate on configurations specific to the driver.

### Data Types

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

### Address Format

> Logical Devices/Logical Nodes$FC$DO$DA</span>

### Example Addresses

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
