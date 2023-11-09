# Mitsubishi 1E

Mitsubishi 1E is a part of Mitsubishi Electric's PLC series that leverages the MELSEC Communication protocol for efficient and reliable data exchange in diverse industrial automation applications.

Neuron's a1e plug-in is used to access Mitsubishi's A series, FX3U, FX3G, iQ-F series PLCs via Ethernet, iQ-F requires a specific firmware version.

## Add Device

Go to **Configuration -> South Devices**, then click **Add Device** to add the driver. Configure the following settings in the popup dialog box.

- Name: The name of this device node.
- Plugin: Select the **Mitsubishi 1E** plugin.

## Device Configuration

After clicking **Create**, you will be redirected to the **Device Configuration** page, where we will set up the parameters required for Neuron to establish a connection with the northbound application. You can also click the device configuration icon on the southbound device card to enter the **Device Configuration** interface.

|  Parameter      |  Description                      |
| -------- | -------------------------- |
| **Transport Mode** |  Use TCP mode or UDP mode      |
| **PLC IP Address** |  Target PLC IPv4 address         |
| **PLC Port** | Target PLC IPv4 address, Default 2000 |
| **UDP Source Port** | Target device port number, available when UDP mode is enabled, default is 52001 |


## Configure Data Groups and Tags

After the plug-in is added and configured, the next step is to establish communication between your device and Neuron by adding groups and tags to the Southbound driver.

Once device configuration is completed, navigate to the **South Devices** page. Click on the device card or device row to access the **Group List** page. Here, you can create a new group by clicking on **Create**, then specifying the group name and data collection interval.

Upon successfully creating a group, click on its name to proceed to the **Tag List** page. This page allows you to add device tags for data collection. You'll need to provide information such as the tag address, attributes, and data type.

For information on general configuration items, see [Connect to Southbound Devices](../south-devices.md). The subsequent section will concentrate on configurations specific to the driver.

### Data Types

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

#### AREA ADDRESS

| AREA | TYPE | ATTRIBUTE  | REMARK                                |
| ---- | ---- | ---------- | ------------------------------------- |
| X    | bit  | read/write | Input relay (FX3/iQ-F)                |
| Y    | bit  | read/write | Output relay (FX3/iQ-F)               |
| M    | bit  | read/write | Internal relay (FX3/iQ-F)             |
| L    | bit  | read/write | Latch relay (FX3/iQ-F)                |
| F    | bit  | read/write | Annunciator (FX3/iQ-F)                |
| B    | bit  | read/write | Link relay (FX3/iQ-F)                 |
| SB   | bit  | read/write | Link special relay (FX3/iQ-F)         |
| S    | bit  | read/write | (FX3/iQ-F)                            |
| D    | all  | read/write | Data register (FX3/iQ-F)              |
| W    | all  | read/write | Link register (FX3/iQ-F)              |
| TS   | bit  | read/write | Timer Contact (FX3/iQ-F)              |
| TC   | bit  | read/write | Timer Coil (FX3/iQ-F)                 |
| TN   | all  | read/write | Timer Current value (FX3/iQ-F)        |
| STS  | bit  | read/write | Retentive timer Contact (FX3/iQ-F)    |
| STC  | bit  | read/write | Retentive timer Coil (FX3/iQ-F)       |
| STN  | all  | read/write | Retentive timer (FX3/iQ-F)            |
| CS   | bit  | read/write | Counter Contact (FX3/iQ-F)            |
| CC   | bit  | read/write | Counter Coil (FX3/iQ-F)               |
| CN   | all  | read/write | Counter Current value (FX3/iQ-F)      |
| LCS  | bit  | read/write | Long Counter Contact (FX3/iQ-F)       |
| LCC  | bit  | read/write | Long Counter Coil (FX3/iQ-F)          |
| LCN  | all  | read/write | Long Counter Current value (FX3/iQ-F) |
| SB   | bit  | read/write | Link special relay (FX3/iQ-F)         |
| SW   | all  | read/write | Link special register (FX3/iQ-F)      |
| SM   | bit  | read/write | Special relay (FX3/iQ-F)              |
| SD   | all  | read/write | Specical register (FX3/iQ-F)          |
| Z    | all  | read/write | Index register (FX3/iQ-F)             |
| LZ   | all  | read/write | Long Index register (FX3/iQ-F)        |
| DX   | bit  | read/write | Link input (FX3/iQ-F)                 |
| DY   | bit  | read/write | Link output(FX3/iQ-F)                 |
| R    | all  | read/write | File register (FX3/iQ-F)              |

#### .BIT

It can only be used in **non-bit type area**, which means to read the specified bit of the specified address, and the binary bit index range is [0, 15].

| Address | Data Type | Description                  |
| ------- | --------- | ---------------------------- |
| D20.0   | bit       | D area, address is 20, bit 0 |
| D20.2   | bit       | D area, address is 20, bit 2 |

#### .LEN\[H]\[L]

When the data type is string, **.LEN** indicates the length of the string;   **H** and **L** can be optional to indicate two byte orders, the default is **H** byte order.

### Example Addresses

| Address   | Data Type | Description                                                  |
| --------- | --------- | ------------------------------------------------------------ |
| X0      | bit       | X area, address is 0    |
| X1      | bit       | X area, address is 1    |
| Y0      | bit       | Y area, address is 0    |
| Y1      | bit       | Y area, address is 1    |
| D100    | int16     | D area, address is 100  |
| D1000   | uint16    | D area, address is 1000 |
| D200    | uint32    | D area, address is 200  |
| D10     | float     | D area, address is 10   |
| D20     | double    | D area, address is 20   |
| D1002.16L | string    | D area, address is 1002, string length is 16, endianness is L |
| D1003.16  | string    | D area, address is 1003, string length is 16, endianness is H |

## Data Monitoring

After completing the point configuration, you can click **Monitoring** -> **Data Monitoring** to view device information and control devices. For details, refer to [Data Monitoring](../../../admin/monitoring.md).