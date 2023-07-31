# ABB Comli

This comli plugin is used to access ABB's COMLI compatible control system through serial port.

## Add Device

Go to **Configuration -> South Devices**, then click **Add Device** to add the driver. Configure the following settings in the popup dialog box.

- Name: The name of this device node.
- Plugin: Select the **ABB COMLI*** plugin.

## Device Configuration

After clicking **Create**, you will be redirected to the **Device Configuration** page, where we will set up the parameters required for Neuron to establish a connection with the northbound application. You can also click the device configuration icon on the southbound device card to enter the **Device Configuration** interface.

| Parameter                 | Description                                                    |
| -------------------- | ------------------------------------------------------- |
| **Recv Timeout** | The time of the system waits for a device to respond to a command.  |
| **Send Interval** | 	The waiting time between sending each read/write command. Some serial devices may discard certain commands if they receive consecutive commands in a short period of time. |
| **Send Retry** | The number of retransmissions of the master request command when the slave returns with no response command. |
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
* INT64
* UINT64
* FLOAT
* DOUBLE
* BIT
* STRING

### Address format

> SLAVE!AREA.ADDRESS\[.BIT][#ENDIAN]\[.LEN\[H]\[L]\[D]\[E]]</span>

#### **SLAVE**

Required, Slave is the slave address or site number.

#### AREA ADDRESS

| Area |Data Type | Register Size|Attribute  | Address Range| Area Description|Note                           |
| ---- | ---------|----- | ---------- | ---- | ---- | -------------------------------- |
| 0    | bit     | 1bit | Read/Write | 0 ~ 16383 | I/O-bits             ||
| 1   | ALL      | 16bit, 2byte| Read/Write| 0 ~ 3071 | Register                         | the type of bit  read only|


#### **.BIT**

Optional, specify a specific bit in a register, as:
| Address         | Data Type | Description                                                |
| ----------- | ------- | --------------------------------------------------- |
| 1!1.100.0  | bit     | Refers to station 1，Register area，address 100，bit 0.    |
| 1!1.100.4  | bit     | Refers to station 1，Register area，address 100，bit 4.     |
| 2!1.200.15 | bit     | Refers to station 2，Register area，address 200，bit 15. |

#### **#ENDIAN**

Optional, byte order, applicable to data types int16/uint16/int32/uint32/float/int64/uint64/double, see the table below for details.
| Symbol | Byte Order | Supported Data Types        | Note |
| --- | ------- | ------------------ | ----- |
| #B  | 2,1 or 8,7,6,5,4,3,2,1     | int16/uint16/int64/uint64/double       |       |
| #L  | 1,2 or 1,2,3,4,5,6,7,8    | int16/uint16/int64/uint64/double       | Default byte order if not specified |
| #LL | 1,2,3,4 | int32/uint32/float | Default byte order if not specified |
| #LB | 2,1,4,3 | int32/uint32/float | |
| #BB | 3,4,1,2 | int32/uint32/float | |
| #BL | 4,3,2,1 | int32/uint32/float | |

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
| 1!0.10      | bit      | Refers to station 1，I/O-bits area, address 10 |
| 1!0.1000      | bit      | Refers to station 1，I/O-bits area, address 1000 |
| 1!0.1100      | bit      | Refers to station 1，I/O-bits area, address 1100 |
| 1!1.10.12   | bit      | Refers to station 1，Register area, address 10，bit 12 |
| 1!1.10      | int16    | Refers to station 1，Register area, address 10，byte order #L |
| 1!1.10#L    | int16    | Refers to station 1，Register area, address 10，byte order #L |
| 1!1.10#B    | int16    | Refers to station 1，Register area, address 10，byte order #B |
| 1!1.10      | uint16    | Refers to station 1，Register area, address 10，byte order #L |
| 1!1.10#L    | uint16    | Refers to station 1，Register area, address 10，byte order #L |
| 1!1.10#B    | uint16    | Refers to station 1，Register area, address 10，byte order #B |
| 1!1.10    | int32    | Refers to station 1，Register area, address 10，byte order #LL |
| 1!1.10#BB | int32   | Refers to station 1，Register area, address 10，byte order #BB |
| 1!1.10#LB | int32   | Refers to station 1，Register area, address 10，byte order #LB |
| 1!1.10#BL | int32   | Refers to station 1，Register area, address 10，byte order #BL |
| 1!1.10    | uint32    | Refers to station 1，Register area, address 10，byte order #LL |
| 1!1.10#BB | uint32   | Refers to station 1，Register area, address 10，byte order #BB |
| 1!1.10#LB | uint32   | Refers to station 1，Register area, address 10，byte order #LB |
| 1!1.10#BL | uint32   | Refers to station 1，Register area, address 10，byte order #BL |
| 1!1.10 | float    | Refers to station 1，Register area, address 10，byte order #LL |
| 1!1.10#BB | float    | Refers to station 1，Register area, address 10，byte order #BB |
| 1!1.10#LB | float    | Refers to station 1，Register area, address 10，byte order #LB |
| 1!1.10#BL | float    | Refers to station 1，Register area, address 10，byte order #BL |
| 1!1.10    | uint64    | Refers to station 1，Register area, address 10，byte order #L |
| 1!1.10#B | uint64   | Refers to station 1，Register area, address 10，byte order #B |
| 1!1.10#L | uint64   | Refers to station 1，Register area, address 10，byte order #L |
| 1!1.10 | int64    | Refers to station 1，Register area, address 10，byte order #L |
| 1!1.10#B    | int64    | Refers to station 1，Register area, address 10，byte order #B |
| 1!1.10#L | int64   | Refers to station 1，Register area, address 10，byte order #L |
| 1!1.10 | double    | Refers to station 1，Register area, address 10，byte order #L |
| 1!1.10#B    | double    | Refers to station 1，Register area, address 10，byte order #B |
| 1!1.10#L | double   | Refers to station 1，Register area, address 10，byte order #L |
| 1!1.10.10  | String  | Refers to station1，Register area, address 10，character length 10，byte order L，which occupies addresses 10 to 15 |
| 1!1.10.10H | String  | Refers to station1，Register area, address 10，character length 10，byte order H，which occupies addresses 10 to 15 |
| 1!1.10.10L | String  | Refers to station1，Register area, address 10，character length 10，byte order L，which occupies addresses 10 to 15 |
| 1!1.10.10D | String  | Refers to station1，Register area, address 10，character length 10，byte order D，which occupies addresses 10 to 20 |
| 1!1.10.10E | String  | Refers to station1，Register area, address 10，character length 10，byte order E，which occupies addresses 10 to 20 |