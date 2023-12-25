# HOSTLINK CMODE

The Hostlink protocol is a protocol defined by Omron for communication between other devices and Omron PLC.
The Hostlink communication protocol has two modes: C-mode and FINS.
Cmode adopts ASCII code, and the upper computer actively sends instructions to the CPU; FINS adopts binary code and can be used in various network devices, and can be actively issued by CPU, IO module, and upper computer.

The Neuron HostLink Cmode plugin is used to communicate with the Omron PLC through a serial network.

## Add Device

Go to **Configuration -> South Devices**, then click **Add Device** to add the driver. Configure the following settings in the popup dialog box.

- Name: The name of this device node.
- Plugin: Select the **HOSTLINK CMODE** plugin.

## Device Configuration

After clicking **Create**, you will be redirected to the **Device Configuration** page, where we will set up the parameters required for Neuron to establish a connection with the northbound application. You can also click the device configuration icon on the southbound device card to enter the **Device Configuration** interface.

| Parameter                 | Description                                                    |
| -------------------- | ------------------------------------------------------- |
| **Recv Timeout** | The time of the system waits for a device to respond to a command.  |
| **Send Interval** | 	The waiting time between sending each read/write command. Some serial devices may discard certain commands if they receive consecutive commands in a short period of time. |
| **Serial Port** | The path to the serial device when using a serial connection, e.g., /dev/ttyS0 in Linux systems. |
| **Stop Bits** | Serial connection parameter. |
| **Parity** | Serial connection parameter. |
| **Baud Rate** | Serial connection parameter. |
| **Data Size** | Serial connection parameter. |

## Configure Data Groups and Tags

After the plug-in is added and configured, the next step is to establish communication between your device and Neuron by adding groups and tags to the Southbound driver.

Once device configuration is completed, navigate to the **South Devices** page. Click on the device card or device row to access the **Group List** page. Here, you can create a new group by clicking on **Create**, then specifying the group name and data collection interval.

Upon successfully creating a group, click on its name to proceed to the **Tag List** page. This page allows you to add device tags for data collection. You'll need to provide information such as the tag address, attributes, and data type.

For information on general configuration items, see [Connect to Southbound Devices](../south-devices.md). The subsequent section will concentrate on configurations specific to the driver.

### Data Types

* BOOL
* INT16
* UINT16
* INT32
* UINT32
* INT64
* UINT64
* FLOAT
* DOUBLE
* STRING

### Address format

> AREA ADDRESS.ID\[.BIT]\[.LEN\[H]\[L]]

#### AREA ADDRESS

| AREA | DATA TYPE                                                 | ATTRIBUTE  | REMARK           |
| ---- | --------------------------------------------------------- | ---------- | ---------------- |
| CIO  | uint16/int16/uint32/int32/uint64/int64/FLOAT/DOUBLE/STRING  | read/write    | IR/SR CIO area |
| LR   | uint16/int16/uint32/int32/uint64/int64/FLOAT/DOUBLE/STRING  | read/write    | LR area        |
| HR   | uint16/int16/uint32/int32/uint64/int64/FLOAT/DOUBLE/STRING  | read/write    | HR area        |
| D    | uint16/int16/uint32/int32/uint64/int64/FLOAT/DOUBLE/STRING  | read/write    | DM area        |
| A    | uint16/int16/uint32/int32/uint64/int64/FLOAT/DOUBLE/STRING  | read          | AR area        |
| TD   | uint16/int16/uint32/int32/uint64/int64/FLOAT/DOUBLE/STRING  | read/write    | TC value       |
| TS   | BOOL                                                        | read/write    | TC status      |

#### .ID

Required, unit ID. For example, unit id is 10, area is CIO, address is 0, then fill in CIO0000.10

#### .LEN\[H]\[L]\[D]\[E]

When the data type is STRING, .LEN is a required field, indicating the number of bytes the string occupies. Each register contains four storage methods: H, L, D, and E, as shown in the table below.
| Symbol | Description                                 |
| --- | ------------------------------------- |
| H   | One register stores two bytes, with the high byte first |
| L   | One register stores two bytes, with the low byte first |
| D   | One register stores one byte, and it is stored in the low byte      |
| E   | One register stores one byte, and it is stored in the high byte|

### Example Addresses

| Address         | Data Type | Description |
| ----------- | ------- | --------- |
| CIO0001.10        | int16   | CIO Area, address is 1, unit id is 10      |
| CIO0002.10        | uint16  | CIO Area, address is 2, unit id is 10      |
| LR0020.10         | double  | LR Area, address is 20, unit id is 10      |
| LR0030.10         | uint32  | LR Area, address is 30, unit id is 10      |
| HR0010.10         | int32   | HR Area, address is 10, unit id is 10      |
| HR0020.10         | float   | HR Area, address is 20, unit id is 10      |
| D0010.10          | int32   | DM Area, address is 10, unit id is 10      |
| D0020.10          | float   | DM Area, address is 20, unit id is 10      |
| A0002.10          | int32   | AR Area, address is 2, unit id is 10       |
| A0004.10          | uint32  | AR Area, address is 4, unit id is 10       |
| TD0002.10         | uint16  | TC value, address is 2, unit id is 10      |
| TD0004.10         | uint32  | TC value, address is 4, unit id is 10      |
| TS0002.10         | BOOL    | TC status, address is 2, unit id is 10     |
| TS0004.10         | BOOL    | TC status, address is 4, unit id is 10     |
| CIO0000.20.20      | string   | CIO Area, address is 0, unit id is 10, the string length is 20 bytes, and the endianness is L      |
| CIO0001.20H        | string   | CIO Area, address is 1, unit id is 10, the string length is 20 bytes, and the endianness is H      |

## Data Monitoring

After completing the point configuration, you can click **Monitoring** -> **Data Monitoring** to view device information and control devices. For details, refer to [Data Monitoring](../../../admin/monitoring.md).