# Mitsubishi 4E

The Mitsubishi 3E plug-in is used to access Mitsubishi's PLCs, including iQ-F Series (SLMP), and iQ-R Series, via Ethernet.

The Mitsubishi 4E is fully compatible with the Mitsubishi SLMP protocol.

## Add Device

Go to **Configuration -> South Devices**, then click **Add Device** to add the driver. Configure the following settings in the popup dialog box.

- Name: The name of this device node.
- Plugin: Select the **Mitsubishi 4E** plugin.

## Device Configuration

After clicking **Create**, you will be redirected to the **Device Configuration** page, where we will set up the parameters required for Neuron to establish a connection with the northbound application. You can also click the device configuration icon on the southbound device card to enter the **Device Configuration** interface.

|  Parameter      |  Description                      |
| -------- | -------------------------- |
| **Transport Mode** |  Use TCP mode or UDP mode      |
| **PLC IP Address** |  Target PLC IPv4 address         |
| **PLC Port** | Target PLC IPv4 address, Default 2000 |
| **Respons Timeout** | PLC's maximum response timeout, default is 15000 ms. |

## Configure Data Groups and Tags

After the plug-in is added and configured, the next step is to establish communication between your device and Neuron by adding groups and tags to the Southbound driver.

Once device configuration is completed, navigate to the **South Devices** page. Click on the device card or device row to access the **Group List** page. Here, you can create a new group by clicking on **Create**, then specifying the group name and data collection interval.

Upon successfully creating a group, click on its name to proceed to the **Tag List** page. This page allows you to add device tags for data collection. You'll need to provide information such as the tag address, attributes, and data type.

For information on general configuration items, see [Connect to Southbound Devices](../south-devices.md). The subsequent section will concentrate on configurations specific to the driver.

### Data types

* INT16
* UINT16
* INT32
* UINT32
* FLOAT
* DOUBLE
* BIT
* STRING

### Address Format

> AREA ADDRESS\[.BIT]\[.LEN\[H]\[L]]

#### .BIT

Only available for **non-bit type area**, which means reading the specified binary bit of the specified address, the binary bit index interval is [0, 15].

#### .LEN\[H]\[L]

When the data type is string type, **`.LEN`** indicates the length of the string; you can optionally fill in **H** and **L** to indicate two-byte orders, and the default is the byte order of **H**.

#### PLC Area 

| AREA | DATA TYPE | ATTRIBUTE  | REMARK                           |
| ---- | --------- | ---------- | -------------------------------- |
| X    | bit       | read/write | Input relay (iQ-F)             |
| DX   | bit       | read/write | (iQ-F)                         |
| Y    | bit       | read/write | Output relay (iQ-F)            |
| DY   | bit       | read/write | (iQ-F)                         |
| B    | bit       | read/write | Link relay (iQ-F)              |
| SB   | bit       | read/write | Link special relay               |
| M    | bit       | read/write | Internal relay (iQ-F)          |
| SM   | bit       | read/write | Special relay (iQ-F)           |
| L    | bit       | read/write | Latch relay (iQ-F)             |
| F    | bit       | read/write | Annunciator (iQ-F)             |
| V    | bit       | read/write | Edge relay (iQ-F)              |
| S    | bit       | read/write | (iQ-F)                         |
| TS   | bit       | read/write | Timer Contact (iQ-F)           |
| TC   | bit       | read/write | Timer Coil (iQ-F)              |
| SS   | bit       | read/write | (iQ-F)                         |
| STS  | bit       | read/write | Retentive timer Contact (iQ-F) |
| SC   | bit       | read/write | (iQ-F)                         |
| CS   | bit       | read/write | Counter Contact (iQ-F)         |
| CC   | bit       | read/write | Counter Coil (iQ-F)            |
| TN   | all       | read/write | Timer Current value (iQ-F)     |
| STN  | all       | read/write | Retentive timer (iQ-F)         |
| SN   | all       | read/write | (iQ-F)                         |
| CN   | all       | read/write | Counter Current value  (iQ-F)  |
| D    | all       | read/write | Data register (iQ-F)           |
| DSH  | --        |            |                                  |
| DSL  | --        |            |                                  |
| SD   | all       | read/write | Specical register (iQ-F)       |
| W    | all       | read/write | Link register (iQ-F)           |
| WSH  | --        |            |                                  |
| WSL  | --        |            |                                  |
| SW   | all       | read/write | Link special register (iQ-F)   |
| R    | all       | read/write | File register (iQ-F)           |
| ZR   | all       | read/write | File register (iQ-F)           |
| RSH  | --        |            |                                  |
| ZRSH | --        |            |                                  |
| RSL  | --        |            |                                  |
| ZRSL | --        |            |                                  |
| Z    | all       | read/write | Index register (iQ-F)          |

### Example Addresses

|  Address  | Data type | Description |
| ----- | ------- | ----- |
| X0    | bit     | X area, Address 0   |
| X1    | bit     | X area, Address 1   |
| Y0    | bit     | Y area, Address 0   |
| Y1    | bit     | Y area, Address 1   |
| D100  | int16   | D area, Address 100 |
| D1000 | uint16  | D area, Address 1000 |
| D200  | uint32  | D area, Address 200 |
| D10   | float   | D area, Address 10  |
| D20   | double  | D area, Address 20  |
| D20.0 | bit | D area, Address 20, 0 bit |
| D20.2 | bit | D area, Address 20, 2 bit |
| D1002.16L | string  | D area, Address 1002, String length 16, Endian L |
| D1003.16 | string  | D area, Address 1003, String length 16, Endian H |

## Use Case

FX5U PLC's settings can refer to the relevant settings of Mitsubishi 3E:

- [FX5U](../mitsubishi-3e/fx5u.md)

## Data Monitoring

After completing the point configuration, you can click **Monitoring** -> **Data Monitoring** to view device information and control devices. For details, refer to [Data Monitoring](../../../admin/monitoring.md).
