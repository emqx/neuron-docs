# Allen-Bradley DF1

DF1 is a proprietary communication protocol developed by Rockwell Automation, primarily used for data exchange between its Allen Bradley series PLCs (Programmable Logic Controllers) and other devices.
The Neuron Allen Bradley DF1 plugin supports point-to-point communication and data transmission through serial communication lines.

## Add Device

Go to **Configuration -> South Devices**, then click **Add Device** to add the driver. Configure the following settings in the popup dialog box.

- Name: The name of this device node.
- Plugin: Select the **Allen-Bradley DF1** plugin.

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

* INT16
* UINT16
* INT32
* UINT32
* FLOAT
* BIT
* STRING

### Address format

> FILE NUM:ELEM[.BIT][#ENDIAN]\[.LEN\[H]\[L]]

For example, N7:0

#### **FILE**

Required, File is the type or the file.
| FILE | FILE TYPE |
| ---- | --------- |
| U    |  STATUS     |
| B    |  BIT        |
| T    |  TIMER      |
| C    |  COUNTER    |
| R    |  COUNTROL   |
| N    |  INTEGER    |
| F    |  FLOAT      |
| S    |  STRING     |
| A    |  ASCII      |

#### NUM

Required, NUM is the number or the file.

#### ELEM

Required, ELEM is the number or the elem.


#### **.BIT**

Optional, specify a specific bit in a register, as:
| Address         | Data Type | Description                                                |
| ----------- | ------- | --------------------------------------------------- |
| N7:0.0  | bit     | Refers to INT FILE 7 , address 0, bit 0.     |
| N7:0.15 | bit     | Refers to INT FILE 7 , address 0, bit 15.    |

#### **#ENDIAN**

Optional, byte order, applicable to data types int16/uint16/int32/uint32/float/, see the table below for details.
| Symbol | Byte Order | Supported Data Types        | Note |
| --- | ------- | ------------------ | ----- |
| #B  | 2,1 or 8,7,6,5,4,3,2,1     | int16/uint16       |       |
| #L  | 1,2 or 1,2,3,4,5,6,7,8    | int16/uint16       | Default byte order if not specified |
| #LL | 1,2,3,4 | int32/uint32/float | Default byte order if not specified |
| #LB | 2,1,4,3 | int32/uint32/float | |
| #BB | 3,4,1,2 | int32/uint32/float | |
| #BL | 4,3,2,1 | int32/uint32/float | |

#### .LEN\[H]\[L]

When the data type is STRING, .LEN is a required field, indicating the number of bytes the string occupies. Each register contains two storage methods: H and L, as shown in the table below.
| Symbol | Description                                 |
| --- | ------------------------------------- |
| H   | One register stores two bytes, with the high byte first |
| L   | One register stores two bytes, with the low byte first |

::: tip
The address data for the T C R region is six bytes.
The first two bytes can use bit or int16, uint16 types;
The middle two bytes of data need to be of type int16 or uint16, with the address suffix added .PRE;
The last two bytes of data should be of type int16 or uint16, with the address suffix added .ACC。
For example, T2:1.ACC
:::

## Data Monitoring

After completing the point configuration, you can click **Monitoring** -> **Data Monitoring** to view device information and control devices. For details, refer to [Data Monitoring](../../../admin/monitoring.md).