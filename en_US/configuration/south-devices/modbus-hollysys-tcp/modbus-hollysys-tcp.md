# HollySys Modbus TCP

The Neuron HollySys Modbus TCP plugin is for collecting HollySys PLC tags using the Modbus TCP protocol,

Modbus TCP is a version of the Modbus protocol based on Ethernet, which uses TCP/IP for communication. Unlike the traditional Modbus RTU protocol, Modbus TCP allows devices to be interconnected directly through Ethernet without any special hardware or communication interface. Therefore, Modbus TCP has higher communication speed and wider application range.


## Add Device

Go to **Configuration -> South Devices**, then click **Add Device** to add the driver. Configure the following settings in the popup dialog box.

- Name: The name of this device node.
- Plugin: Select the **HollySys Modbus TCP** plugin.


## Device Configuration

After clicking **Create**, you will be redirected to the **Device Configuration** page, where we will set up the parameters required for Neuron to establish a connection with the device. You can also click the device configuration icon on the southbound device card to enter the **Device Configuration** interface.

| Parameter                  | Description                                                    |
| -------------------- | ------------------------------------------------------- |
| **Maximum Retry Times** | The maximum number of retries after a failed attempt to send a read command. |
| **Retry Interval** | Resend reading instruction interval(ms) after a failed attempt to send a read command. |
| **Endianness**    | Byte order of tags with 32 bits, ABCD corresponds to 1234. |
| **Send Interval** | The waiting time between sending each read/write command. Some serial devices may discard certain commands if they receive consecutive commands in a short period of time. |
| **IP Address** | The IP address of the device when using TCP connection with Neuron as the client. |
| **Port** | The port number of the device when using TCP connection with Neuron as the client. |
| **Connection Timeout** |  The time the system waits for a device to respond to a command. |

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

#### **SLAVE**

Required, Slave is the slave address or site number.

#### **ADDRESS**

HollySys PLC maps data units onto the Modbus address space for access through the Modbus TCP protocol.
The Neuron HollySys Modbus TCP plugin frees users from details of the address mapping, and designates the PLC data unit name as the **ADDRESS**.


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
The byte order of a tag has a higher priority than the byte order configuration of a node. That is to say, once the byte order is configured for a tag, it follows the configuration of that tag and ignores the node configuration.
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
