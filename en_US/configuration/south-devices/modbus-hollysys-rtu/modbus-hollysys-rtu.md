# HollySys Modbus RTU

The Neuron HollySys Modbus RTU plugin is for collecting HollySys PLC tags using the Modbus RTU protocol,


## Add Device

Go to **Configuration -> South Devices**, then click **Add Device** to add the driver. Configure the following settings in the popup dialog box.

- Name: The name of this device node.
- Plugin: Select the **HollySys Modbus RTU** plugin.

## Device Configuration


After clicking **Create**, you will be redirected to the **Device Configuration** page, where we will set up the parameters required for Neuron to establish a connection with the device. You can also click the device configuration icon on the southbound device card to enter the **Device Configuration** interface.

| Parameter                  | Description                                                                            |
| -------------------------- | -------------------------------------------------------------------------------------- |
| **Physical Link**          | Selects the communication medium, either serial or Ethernet.                           |
| **Connection Timeout**     | The time the system waits for a device to respond to a command.                        |
| **Maximum Retry Times**    | The maximum number of retries after a failed attempt to send a read command.           |
| **Retry Interval**         | Resend reading instruction interval(ms) after a failed attempt to send a read command. |
| **Send Interval**          | The waiting time between sending each read/write command. Some serial devices may discard certain commands if they receive consecutive commands in a short period of time. |
| **Serial Device**          | Only needed in **Serial** mode, the path to the serial device when using a serial connection, e.g., /dev/ttyS0 in Linux systems. |
| **Stop Bits**              | Only for the **Serial** mode, the serial connection parameter.                         |
| **Parity**                 | Only for the **Serial** mode, the serial connection parameter.                         |
| **Baud Rate**              | Only for the **Serial** mode, the serial connection parameter.                         |
| **Data Bits**              | Only for the **Serial** mode, the serial connection parameter.                         |
| **Connection Mode**        | Only for the **Ethernet** mode, you can choose Neuron as the TCP client or server.     |
| **IP Address**             | Only for the **Ethernet** mode,  the IP address of the device when using TCP connection with Neuron as the client, or the IP address of Neuron when using TCP connection with Neuron as the server. The default value is 0.0.0.0. |
| **Port**                   | Only for the **Ethernet** mode, the port number of the device when using TCP connection with Neuron as the client, or the port number of Neuron when using TCP connection with Neuron as the server. |
| **Maximum Retry Times**    | The maximum number of retries after a failed attempt to send a read command.           |
| **Retry Interval**         | Resend reading instruction interval(ms) after a failed attempt to send a read command. |

The HollySys Modbus RTU plugin configuration is similar to that of the [Modbus RTU driver module](../modbus-rtu/modbus-rtu.md).

## Configure Data Groups and Tags

After the plugin is added and configured, the next step is to establish communication between your device and Neuron by adding groups and tags to the Southbound driver.

Once device configuration is completed, navigate to the **South Devices** page. Click on the device card or device row to access the **Group List** page. Here, you can create a new group by clicking on **Create**, then specifying the group name and data collection interval.

Upon successfully creating a group, click on its name to proceed to the **Tag List** page. This page allows you to add device tags for data collection. You'll need to provide information such as the tag address, attributes, and data type.

For information on general configuration items, see [Connect to Southbound Devices](../south-devices.md). The subsequent section will concentrate on configurations specific to the driver.

### Data types

* BIT
* BOOL
* INT16
* UINT16
* WORD

### Address format

> SLAVE!ADDRESS[#ENDIAN]

The address format is nearly the same to that of the [Modbus RTU driver module](../modbus-rtu/modbus-rtu.md), the only difference is in the **ADDRESS** part.

#### **SLAVE**

Required, Slave is the slave address or site number.

#### **ADDRESS**

HollySys PLC maps data units onto the Modbus address space for access through the Modbus RTU protocol.
The Neuron HollySys Modbus RTU plugin frees users from details of the address mapping, and designates the PLC data unit name as the **ADDRESS**.


| Area                            | Data unit example                           | Attribute  | Register Size | Data Type      |
| ------------------------------- | ------------------------------------------- | ---------- | ------------- | -------------- |
| IX (Input)                      | IX0.0 ... IX0.7, IX1.0 ... IX1.7 ...        | Read       | 1Bit          |  BOOL/BIT      |
| IW (Input Registers)            | IW0, IW1, ...                               | Read       | 16Bit,2Byte   |  INT16/UINT16  |
| QX (Coils)                      | QX0.0 ... QX0.7, QX1.0 ... QX1.7 ...        | Read/Write | 1Bit          |  BOOL/BIT      |
| QW (Hold Registers)             | QW0, QW1, ...                               | Read/Write | 16Bit,2Byte   |  INT16/UINT16  |
| MX (Coils)                      | MX0.0 ... MX0.7, MX1.0 ... MX1.7 ...        | Read/Write | 1Bit          |  BOOL/BIT      |
| MW (Hold Registers)             | MW0, MW1, ...                               | Read/Write | 16Bit,2Byte   |  INT16/UINT16  |


#### **#ENDIAN**

Optional, byte order, applicable to data types int16/uint16, see the table below for details.
| Symbol | Byte Order | Supported Data Types | Note                                |
| ------ | ---------- | -------------------- | ----------------------------------- |
| #B     | 2,1        | int16/uint16         |                                     |
| #L     | 1,2        | int16/uint16         | Default byte order if not specified |

::: tip
The byte order can be illustrated using the notation ABCD, which corresponds directly to the sequence 1234. As an example, the ABCD designation represents the standard or default Endianness 1234. (#LL).
:::


### Example Addresses

| Address        | Data Type | Description                                        |
| -------------- | --------- | -------------------------------------------------- |
| 1!IX1.0        | bit       | Data unit IX1.0 on slave 1, read only.             |
| 1!QW0          | int16     | Data unit QW0 on slave 1, support read/write.      |
| 2!MW1          | int16     | Data unit MW1 on slave 1, support read/write.      |


## Data Monitoring

After completing the point configuration, you can click **Monitoring** -> **Data Monitoring** to view device information and control devices. For details, refer to [Data Monitoring](../../../admin/monitoring.md).
