# Modbus RTU

Modbus RTU is a version of the Modbus protocol that is based on serial communication. Unlike the Modbus TCP protocol, Modbus RTU is typically used to connect sensors, actuators, and other control devices on a factory production line. It is a fast, reliable, and flexible serial communication protocol that provides reliable data transmission and control functions.

The Modbus RTU protocol uses binary encoding and can transmit data over RS-232, RS-485, or other serial communication media. Neuron Modbus RTU plugin adds an implementation based on Ethernet TCP and enables remote device data acquisition and control through a DTU device.

## Add Device

Go to **Configuration -> South Devices**, then click **Add Device** to add the driver. Configure the following settings in the popup dialog box.

- Name: The name of this device node.
- Plugin: Select the **Modbus RTU** plugin.

## Device Configuration

After clicking **Create**, you will be redirected to the **Device Configuration** page, where we will set up the parameters required for Neuron to establish a connection with the device. You can also click the device configuration icon on the southbound device card to enter the **Device Configuration** interface.

| Parameter                  | Description                                                    |
| -------------------- | ------------------------------------------------------- |
| **Physical Link** | Selects the communication medium, either serial or Ethernet. |
| **Connection Timeout** |  The time the system waits for a device to respond to a command. |
| **Maximum Retry Times** | The maximum number of retries after a failed attempt to send a read command. |
| **Retry Interval** | Resend reading instruction interval(ms) after a failed attempt to send a read command. |
| **Send Interval** | The waiting time between sending each read/write command. Some serial devices may discard certain commands if they receive consecutive commands in a short period of time. |
| **Serial Device** | Only needed in **Serial** mode, the path to the serial device when using a serial connection, e.g., /dev/ttyS0 in Linux systems. |
| **Stop Bits** | Only for the **Serial** mode, the serial connection parameter. |
| **Parity** | Only for the **Serial** mode, the serial connection parameter. |
| **Baud Rate** | Only for the **Serial** mode, the serial connection parameter. |
| **Data Bits** | Only for the **Serial** mode, the serial connection parameter. |
| **Connection Mode** | Only for the **Ethernet** mode, you can choose Neuron as the TCP client or server. |
| **IP Address** | Only for the **Ethernet** mode,  the IP address of the device when using TCP connection with Neuron as the client, or the IP address of Neuron when using TCP connection with Neuron as the server. The default value is 0.0.0.0. |
| **Port** | Only for the **Ethernet** mode, the port number of the device when using TCP connection with Neuron as the client, or the port number of Neuron when using TCP connection with Neuron as the server. |
| **Maximum Retry Times** | The maximum number of retries after a failed attempt to send a read command.|
| **Retry Interval** | Resend reading instruction interval(ms) after a failed attempt to send a read command.|

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

### Address Format

> SLAVE!ADDRESS\[.BIT][#ENDIAN]\[.LEN\[H]\[L]\[D]\[E]]

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

::: tip
Some device specification documents may use function codes and register addresses to describe commands. Since register address number starts at 0, the register address range for each area is 0 to 65535. Neuron uses a PLC configuration address specification, so the addresses configured in Neuron start from 1.

The conversion rule for the configuration address specification is as follows: determine the highest digit of the address based on the function code, and add 1 to the register address to obtain the address used in Neuron.

For example, if the function code is 0x03 and the register address is 0, the address used in Neuron is 400001. If the function code is 0x02 and the register address is 5, the address used in Neuron is 100006.

:::



#### **.BIT**

Optional, specify a specific bit in a register.

| Address         | Data Type | Description                                                |
| ----------- | ------- | --------------------------------------------------- |
| 1!300004.0  | bit     | Refers to station 1, input area, address 300004, bit 0 |
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

### Example Addresses

| Address        | Data Type | Description |
| ----------- | ------- | --------- |
| 1!300004    | int16 | Refers to station 1, input area, address 300004, byte order #L |
| 1!300004#B  | int16    | Refers to station 1, input area, address 300004, byte order #B |
| 1!300004#L  | uint16   | Refers to station 1, input area, address 300004, byte order #L |
| 1!400004    | int16    | Refers to station 1, hold register area, address 400004, byte order #L |
| 1!400004#L  | int16    | Refers to station 1, hold register area, address 400004, byte order #L |
| 1!400004#B  | uint16   | Refers to station 1, hold register area, address 400004, byte order #B |
| 1!300004    | int32    | Refers to station 1, input area, address 300004, byte order #LL |
| 1!300004#BB | uint32   | Refers to station 1, input area, address 300004, byte order #BB |
| 1!300004#LB | uint32   | Refers to station 1, input area, address 300004, byte order #LB |
| 1!300004#BL | float    | Refers to station 1, input area, address 300004, byte order #BL |
| 1!300004#LL | int32    | Refers to station 1, input area, address 300004, byte order #LL |
| 1!400004    | int32    | Refers to station 1, hold register area, address 400004, byte order #LL|
| 1!400004#LB | uint32   | Refers to station 1, hold register area, address 400004, byte order #LB|
| 1!400004#BB | uint32   | Refers to station 1, hold register area, address 400004, byte order #BB|
| 1!400004#LL | int32    | Refers to station 1, hold register area, address 400004, byte order #LL|
| 1!400004#BL | float    | Refers to station 1, hold register area, address 400004, byte order #BL|
| 1!300001.10  | String  | Refers to station 1, input area, address 300001, character length 10, byte order L, which occupies addresses 300001 to 300005|
| 1!300001.10H | String  | Refers to station 1, input area, address 300001, character length 10, byte order H, which occupies addresses 300001 to 300005|
| 1!300001.10L | String  | Refers to station 1, input area, address 300001, character length 10, byte order L, which occupies addresses 300001 to 300005|
| 1!400001.10  | String  | Refers to station 1, hold register area, address 400001, character length 10, byte order L, which occupies addresses 400001 to 400005|
| 1!400001.10H | String  | Refers to station 1, hold register area, address 400001, character length 10, byte order H, which occupies addresses 400001 to 400005|
| 1!400001.10L | String  | Refers to station 1, hold register area, address 400001, character length 10, byte order L, which occupies addresses 400001 to 400005|
| 1!400001.10D | String  | Refers to station 1, hold register area, address 300001, character length 10, byte order D, which occupies addresses 400001 to 400005|
| 1!400001.10E | String  | Refers to station 1, hold register area, address 300001, character length 10, byte order E, which occupies addresses 400001 to 400005|

## Use Case

This chapter also provides practical examples to facilitate a quick start.

- [Modbus Slave Simulator](./example/modbus-slave/modbus-slave.md)
- [USR DTU](./example/dtu/dtu-connection.md)

## Data Monitoring

After completing the point configuration, you can click **Monitoring** -> **Data Monitoring** to view device information and control devices. For details, refer to [Data Monitoring](../../../usage/monitoring.md).