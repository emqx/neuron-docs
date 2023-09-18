# Panasonic Mewtocol

Mewtocol is a Panasonic-developed protocol enabling data exchange between its PLC devices and various others, such as computers and HMI devices

The Mewtocol plugin is used to access Panasonic's FP-XH, FP0H series PLCs via Ethernet.

## Add Device

Go to **Configuration -> South Devices**, then click **Add Device** to add the driver. Configure the following settings in the popup dialog box.

- Name: The name of this device node.
- Plugin: Select the **Panasonic Mewtocol** plugin.

## Device Configuration

After clicking **Create**, you will be redirected to the **Device Configuration** page, where we will set up the parameters required for Neuron to establish a connection with the northbound application. You can also click the device configuration icon on the southbound device card to enter the **Device Configuration** interface.

|   Parameter     |  Description                      |
| -------- | -------------------------- |
| **PLC IP Address** |  Target PLC IPv4 address         |
| **PLC Port** | Target PLC IPv4 address, Default 2000 |
| **PLC Station** | Target PLC station, Default 1      |
| **Timeout (ms)** | Target PLC read timeout |

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
* INT64
* UINT64
* FLOAT
* DOUBLE
* BIT
* STRING

### Address format

> AREA ADDRESS\[.BIT]\[.LEN\[H]\[L]]

#### .BIT
Only available for **non-bit type area**, which means reading the specified binary bit of the specified address, the binary bit index interval is [0, 15].

#### .LEN\[H]\[L]
When the data type is string type, **`.LEN`** indicates the length of the string; you can optionally fill in **H** and **L** to indicate two-byte orders, and the default is the byte order of **H**.

#### PLC Area

| Area | DATA TYPE | ATTRIBUTE  |  REMARK                          |
| ---- | --------- | ---------- | -------------------------------- |
| X    | uint16, uint32, uint64, bit | read/write | External input        |
| Y    | uint16, uint32, uint64, bit | read/write | External output        |
| R    | uint16, uint32, uint64, bit | read/write | Internal relay      |
| T    | uint16, uint32, uint64, bit | read/write | Timer       |
| C    | uint16, uint32, uint64, bit | read/write | Counter           |
| L    | uint16, uint32, uint64, bit | read/write | Link relay       |
| DT   | all | read/write (bit type read-only) | Data register DT   |
| LD   | all | read/write (bit type read-only) | Link data register LD    |
| FL   | all | read/write (bit type read-only) | File register FL     |
| S    | -- | -- | Timer/counter set value area SV     |
| K    | -- | -- | Timer/counter elapsed value area EV     |
| IX   | all   | read/write (bit type read-only) | Index register IX   |
| IY   | all   | read/write (bit type read-only) | Index register IY  |
| ID   | all   | read/write (bit type read-only) | Index register ID  |


### Example Addresses

| Address   | Data type | Description |
| ----- | ------- | ----- |
| X0    | bit     | X Area, Address 0    |
| X1    | bit     | X Area, Address 1    |
| Y0    | bit     | Y Area, Address 0    |
| Y1    | bit     | Y Area, Address 1    |
| DT100 | int16   | D Area, Address 100  |
| DT1000 | uint16 | D Area, Address 1000 |
| DT200 | uint32  | D Area, Address 200  |
| DT10  | float   | D Area, Address 10   |
| DT20  | double  | D Area, Address 20   |
| DT20.0 | bit | D Area, Address 20, 0 bit |
| DT20.2 | bit | D Area, Address 20, 2 bit |
| DT1002.16L | string  | D Area, Address 1002, String length 16, Byte order L |
| DT1003.16 | string  | D Area, Address 1003, String length 16, Byte order H |

## Use Case

You can use Neuron Panasonic Mewtocol plugin to connect FP-XH C30T, for details, see [Connect to FP-XH C30T](./fp-xh-c30t.md). 

## Data Monitoring

After completing the point configuration, you can click **Monitoring** -> **Data Monitoring** to view device information and control devices. For details, refer to [Data Monitoring](../../../usage/monitoring.md).
