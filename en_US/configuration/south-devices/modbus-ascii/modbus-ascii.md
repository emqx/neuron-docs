# Modbus ASCII

Modbus ASCII and Modbus RTU (Remote Terminal Unit) both support serial communication. The main difference between these two variants lies in the different encoding methods for the data:

Modbus RTU: It uses binary encoding, which is highly efficient in transmission but more sensitive to interference and distance.
Modbus ASCII: It uses ASCII character encoding, which has relatively lower transmission efficiency but is easier to debug and diagnose since the transmitted information can be read directly.

Modbus ASCII is suitable for situations where high-speed data transmission is not required, and where the importance of debugging and diagnosing outweighs the efficiency of transmission.

## Add Device

Go to **Configuration -> South Devices**, then click **Add Device** to add the driver. Configure the following settings in the popup dialog box.

- Name: The name of this device node.
- Plugin: Select the **Modbus ASCII** plugin.

## Device Configuration

After clicking **Create**, you will be redirected to the **Device Configuration** page, where we will set up the parameters required for Neuron to establish a connection with the device. You can also click the device configuration icon on the southbound device card to enter the **Device Configuration** interface.

| Parameter                  | Description                                                    |
| -------------------- | ------------------------------------------------------- |
| **Connection Timeout** |  The time the system waits for a device to respond to a command. |
| **Maximum Retry Times** | The maximum number of retries after a failed attempt to send a read command.|
| **Retry Interval** | Resend reading instruction interval(ms) after a failed attempt to send a read command.|
| **Send Interval** | The waiting time between sending each read/write command. Some serial devices may discard certain commands if they receive consecutive commands in a short period of time. |
| **Endianness**    | Byte order of tags with 32 bits, ABCD corresponds to 1234. |
| **Start Address** | Address starts from 1 or 0. |
| **Serial Device** | The path to the serial device, e.g., /dev/ttyS0 in Linux systems. |
| **Stop Bits** | The serial connection parameter. |
| **Parity**    | The serial connection parameter. |
| **Baud Rate** | The serial connection parameter. |
| **Data Bits** | The serial connection parameter. |

## Configure Data Groups and Tags

After the plugin is added and configured, the next step is to establish communication between your device and Neuron by adding groups and tags to the Southbound driver.

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

### Address Format

> SLAVE!ADDRESS\[.BIT][#ENDIAN]\[.LEN\[H]\[L]\[D]\[E]]\[.BYTES]

#### **SLAVE**

Required, Slave is the slave address or site number.

#### **ADDRESS**

Required, Address is the register address. The Modbus protocol has four areas, each area has a maximum of 65536 registers, and the address range of each area is shown in the table below. It should be noted that a storage area as large as 65536 is generally not required in practical applications. Generally, PLC manufacturers generally use an address range within 10000. Please pay attention to fill in the correct point address according to the area and function code of the device.

| Area                       | Address Range          | Attribute        | Register Size     | Function Code | Data Type|
| ------------------------- | ---------------- | ---------- | ------------- | ------------ | ------- |
| Coil                | 000001 ~ 065536 | Read/Write       | 1Bit          | 0x01, 0x05, 0x0f | BIT     |
| Input          | 100001 ~ 165536 | Read/Write         | 1Bit         | 0x02          | BIT     |
| Input Register| 300001 ~ 365536 | Read/Write         | 16Bit,2Byte         | 0x04          | BIT, INT16, UINT16,<br />INT32, UINT32,<br />INT64, UINT64,<br />FLOAT, DOUBLE, STRING |
| Hold Register  | 400001 ~ 465536 | Read/Write       | 16Bit,2Byte         | 0x03, 0x06, 0x10 | BIT, INT16, UINT16,<br />INT32, UINT32, INT64,<br />UINT64, FLOAT, DOUBLE,<br />STRING |

#### **.BIT**

Optional, specify a specific bit in a register.

| Address         | Data Type | Description                                                |
| ----------- | ------- | --------------------------------------------------- |
| 1!300004.0  | bit     | Refers to station 1, input register area, address 300004, bit 0 |
| 1!400010.4  | bit     | Refers to station 1, hold register area, address 400010, bit 4    |
| 2!400001.15 | bit     | Refers to station 2, hold register area, address 400001, bit 15   |

#### **#ENDIAN**

Optional, byte order, applicable to data types int16/uint16/int32/uint32/float, see the table below for details.
| Symbol | Byte Order | Supported Data Types | Note |
| --- | ------- | ------------------ | ----- |
| #B  | 2,1     | int16/uint16       |       |
| #L  | 1,2     | int16/uint16       | Default byte order if not specified |
| #LL | 1,2,3,4 | int32/uint32/float | Default byte order if not specified |
| #LB | 2,1,4,3 | int32/uint32/float | |
| #BL | 3,4,1,2 | int32/uint32/float | |
| #BB | 4,3,2,1 | int32/uint32/float | |

::: tip
The byte order of a tag has a higher priority than the byte order configuration of a node. That is to say, once the byte order is configured for a tag, it follows the configuration of that tag and ignores the node configuration.
The byte order can be illustrated using the notation ABCD, which corresponds directly to the sequence 1234. As an example, the ABCD designation represents the standard or default Endianness 1234. (#LL).
:::

#### .LEN\[H]\[L]\[D]\[E]

When the data type is STRING, `.LEN` is a required field, indicating the number of bytes the string occupies. Each register contains four storage methods: H, L, D, and E, as shown in the table below.
| Symbol | Description                                 |
| --- | ------------------------------------- |
| H   | One register stores two bytes, with the high byte first |
| L   | One register stores two bytes, with the low byte first |
| D   | One register stores one byte, and it is stored in the low byte      |
| E   | One register stores one byte, and it is stored in the high byte|

#### **.BYTES**

Optional, read and write the length of bytes type data, applicable to bytes data type.

::: tip
A register of the Modbus driver contains 2 bytes. When reading and writing Modbus register data in the bytes data type, please ensure that the bytes parameter is set to an even number.
:::

### Example Addresses

| Address        | Data Type | Description |
| ----------- | ------- | --------- |
| 1!300004    | int16    | Refers to station 1, input register area, address 300004, byte order #L |
| 1!300004#B  | int16    | Refers to station 1, input register area, address 300004, byte order #B |
| 1!300004#L  | uint16   | Refers to station 1, input register area, address 300004, byte order #L |
| 1!400004    | int16    | Refers to station 1, hold register area, address 400004, byte order #L |
| 1!400004#L  | int16    | Refers to station 1, hold register area, address 400004, byte order #L |
| 1!400004#B  | uint16   | Refers to station 1, hold register area, address 400004, byte order #B |
| 1!300004    | int32    | Refers to station 1, input register area, address 300004, byte order #LL |
| 1!300004#BB | uint32   | Refers to station 1, input register area, address 300004, byte order #BB |
| 1!300004#LB | uint32   | Refers to station 1, input register area, address 300004, byte order #LB |
| 1!300004#BL | float    | Refers to station 1, input register area, address 300004, byte order #BL |
| 1!300004#LL | int32    | Refers to station 1, input register area, address 300004, byte order #LL |
| 1!400004    | int32    | Refers to station 1, hold register area, address 400004, byte order #LL|
| 1!400004#LB | uint32   | Refers to station 1, hold register area, address 400004, byte order #LB|
| 1!400004#BB | uint32   | Refers to station 1, hold register area, address 400004, byte order #BB|
| 1!400004#LL | int32    | Refers to station 1, hold register area, address 400004, byte order #LL|
| 1!400004#BL | float    | Refers to station 1, hold register area, address 400004, byte order #BL|
| 1!300001.10  | String  | Refers to station 1, input register area, address 300001, character length 10, byte order L, which occupies addresses 300001 to 300005|
| 1!300001.10H | String  | Refers to station 1, input register area, address 300001, character length 10, byte order H, which occupies addresses 300001 to 300005|
| 1!300001.10L | String  | Refers to station 1, input register area, address 300001, character length 10, byte order L, which occupies addresses 300001 to 300005|
| 1!400001.10  | String  | Refers to station 1, hold register area, address 400001, character length 10, byte order L, which occupies addresses 400001 to 400005|
| 1!400001.10H | String  | Refers to station 1, hold register area, address 400001, character length 10, byte order H, which occupies addresses 400001 to 400005|
| 1!400001.10L | String  | Refers to station 1, hold register area, address 400001, character length 10, byte order L, which occupies addresses 400001 to 400005|
| 1!400001.10D | String  | Refers to station 1, hold register area, address 300001, character length 10, byte order D, which occupies addresses 400001 to 400005|
| 1!400001.10E | String  | Refers to station 1, hold register area, address 300001, character length 10, byte order E, which occupies addresses 400001 to 400005|

## Data Monitoring

After completing the point configuration, you can click **Monitoring** -> **Data Monitoring** to view device information and control devices. For details, refer to [Data Monitoring](../../../admin/monitoring.md).