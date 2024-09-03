# Inovance Modbus TCP

Inovance Modbus TCP is a version of the Modbus protocol based on Ethernet, utilizing TCP/IP for communication.

The Neuron Inovance Modbus TCP plugin is tailored for Inovance PLC tags.

## Add Device

Go to **Configuration -> South Devices**, then click **Add Device** to add the driver. Configure the following settings in the popup dialog box.

| Plugin | Description |
| --- | --- | 
| **Inovance Modbus TCP** |Modbus TCP protocol implementation, adapted for Inovance PLC points. |

## Device Configuration

After clicking **Create**, you will be redirected to the **Device Configuration** page, where we will set up the parameters required for Neuron to establish a connection with the device. You can also click the device configuration icon on the southbound device card to enter the **Device Configuration** interface.

| Parameter                  | Description                                                    |
| -------------------- | ------------------------------------------------------- |
| **Endianness** | Byte order of tags with 32 bits, ABCD corresponds to 1234. |
| **Send Interval** | The waiting time between sending each read/write command. Some serial devices may discard certain commands if they receive consecutive commands in a short period of time. |
| **PLC IP Address** | The IP address of the device. |
| **PLC Port** | The port number of the device.|
| **Connection Timeout** |  The time the system waits for a device to respond to a command. |
| **Check Header** | Choose whether to verify the message header. After selecting True, when encountering packet header errors, the neuron and device will reconnect. |

## Configure Data Groups and Tags

After the plugin is added and configured, the next step is to establish communication between your device and Neuron by adding groups and tags to the Southbound driver.

Once device configuration is completed, navigate to the **South Devices** page. Click on the device card or device row to access the **Group List** page. Here, you can create a new group by clicking on **Create**, then specifying the group name and data collection interval.

Upon successfully creating a group, click on its name to proceed to the **Tag List** page. This page allows you to add device tags for data collection. You'll need to provide information such as the tag address, attributes, and data type.

For information on general configuration items, see [Connect to Southbound Devices](../south-devices.md). The subsequent section will concentrate on configurations specific to the driver.

### Data types

* BIT
* INT8
* UINT8
* INT16
* UINT16
* INT32
* UINT32
* INT64
* UINT64
* FLOAT
* DOUBLE
* STRING
* BYTES

### Address format

> ADDRESS\[.BIT][#ENDIAN]\[.LEN\[H]\[L]\[D]\[E]]\[.BYTES]

::: tip
Since communication is done via TCP/IP, the device is searched through the IP address and port number, making it unnecessary to specify the station number in the message. Neuron defaults the station number to 1.
:::

#### **ADDRESS**

Required, refers to the register address. HuiChuan PLC supports coil and register access for MODBUS protocol. Different from the standard Modbus protocol, each area's address range is as follows:

The address areas are divided into two types according to the PLC model.

Small PLCs: EASY series, H5U, etc.

| Area                       | Address Range          | Quantity        | Attribute        | Register Size     | Function Code | Data Type|
| ------------------------- | ---------------- | ---------- | ---------- | ------------- | ------------ | ------- |
| M0-M7999(Coils)            | 0x0000-0x1F3F  (0-7999)        | 8000       |Read/Write        | 1Bit          | 0x01,0x05,0x0f | BIT    |
| B0-B32767(Coils)           | 0x3000-0xAFFF  (12288-45055)   | 32768      |Read/Write        | 1Bit          | 0x01,0x05,0x0f | BIT    |
| S0-S4095(Coils)            | 0xE000-0xEFFF  (57344-61439)   | 4096       |Read/Write        | 1Bit          | 0x01,0x05,0x0f | BIT    |
| X0-X1777(octal) (Coils)   | 0xF800-0xFBFF  (63488-64511)   | 1024       |Read/Write       | 1Bit          | 0x01,0x05,0x0f | BIT    |
| Y0-X1777(octal) (Coils)   | 0xFC00-0xFFFF  (64512-65535)   | 1024       |Read/Write        | 1Bit          | 0x01,0x05,0x0f | BIT    |
| D0-D7999(Holding Registers)      | 0x0000-0x1F3F  (0-7999)        | 8000       |Read/Write        | 16Bit,2Byte   | 0x03,0x06,0x10 | Various   |
| R0-R32767(Holding Registers)     | 0x3000-0xAFFF  (12288-45055)   | 32768      |Read/Write        | 16Bit,2Byte   | 0x03,0x06,0x10 | Various   |

::: tip
The X and Y areas' addresses are represented in octal.
:::

Medium PLCs: AM series, AC series, etc.

| Area                       | Address Range          | Quantity        | Attribute        | Register Size     | Function Code | Data Type|
| -------------------------- | ------------------------------ | ----------  | ----------- | ------------- | -------------  | ------- |
| QX0.0-QX8191.7（Coils）            | 0x0000-0xFFFF  (0-65536)       | 65536       |Read/Write        | 1Bit          | 0x01,0x05,0x0f | BIT     |
| IX0.0-IX8191.7（Input）            | 0x0000-0xFFFF (0-65536)        | 65536       |Read               | 1Bit          | 0x01,0x05,0x0f | BIT    |
| MW0-MW65535（Holding Registers）   | 0x0000-0xFFFF  (0-65536)       | 65536       |Read/Write         | 16Bit,2Byte   | 0x03,0x06,0x10 | Various    |
| SM0-SM7999                         | 0x0000-0x1F3F  (0-7999)        | 8000       |Read/Write        | 16Bit,2Byte   | 0x01,0x05,0x0f  | BIT    |
| SD0-SD7999                         | 0x0000-0x1F3F  (0-7999)        | 8000       |Read/Write        | 16Bit,2Byte   | 0x03,0x06,0x10  | Various    |

::: tip
The M,I,Q area supports multiple addressing methods, including (M|I|Q)X, (M|I|Q)B, (M|I|Q)W, (M|I|Q)D, which correspond to addressing by bit, Byte, Word, and Dword, respectively.

When using MX and MB addressing methods, the tags only support read attributes.

:::

#### **.BIT**

Optional, specify a specific bit in a register

| Address         | Data Type | Description                                                |
| ----------- | ------- | --------------------------------------------------- |
| D4.0  | bit     | D area, address 4, bit 0 |
| D10.4  | bit     | D area, address 10, bit 4    |
| D1.15 | bit     | D area, address 1, bit 15   |

#### **#ENDIAN**

Optional, byte order, applicable to data types int16/uint16/int32/uint32/float, see the table below for details.
| Symbol | Byte Order | Supported Data Types | Note |
| --- | ------- | ------------------ | ----- |
| #B  | 2,1     | int16/uint16       |       |
| #L  | 1,2     | int16/uint16       | Default byte order if not specified |
| #LL | 3,4,1,2 | int32/uint32/float | Default byte order if not specified |
| #LB | 4,3,2,1 | int32/uint32/float | |
| #BL | 1,2,3,4 | int32/uint32/float | |
| #BB | 2,1,4,3 | int32/uint32/float | |

::: tip
The byte order of a tag has a higher priority than the byte order configuration of a node. That is to say, once the byte order is configured for a tag, it follows the configuration of that tag and ignores the node configuration.
:::

#### .LEN\[H]\[L]

When the data type is STRING, `.LEN` is a required field, indicating the number of bytes the string occupies. Each register contains two storage methods: H, L, as shown in the table below.
| Symbol | Description                                 |
| --- | ------------------------------------- |
| H   | One register stores two bytes, with the high byte first |
| L   | One register stores two bytes, with the low byte first |

::: tip
Please note, the default byte order for Inovance plugin strings is L.
:::

#### **.BYTES**

Optional, read and write the length of bytes type data, applicable to bytes data type.

::: tip
A register of the Modbus driver contains 2 bytes. When reading and writing Modbus register data in the bytes data type, please ensure that the bytes parameter is set to an even number.
:::

### Example Addresses

| Address        | Data Type | Description |
| ----------- | ------- | --------- |
| D4    | int16    | D area, address 4, byte order #L |
| D4#L  | int16    | D area, address 4, byte order #L |
| D4#B  | uint16   | D area, address 4, byte order #B |
| D4    | int32    | D area, address 4, byte order #LL|
| D4#LB | uint32   | D area, address 4, byte order #LB|
| D4#BB | uint32   | D area, address 4, byte order #BB|
| D4#LL | int32    | D area, address 4, byte order #LL|
| D4#BL | float    | D area, address 4, byte order #BL|
| D1.10  | String  | D area, address 1, character length 10, byte order L, which occupies addresses D1 to D5|
| D1.10H | String  | D area, address 1, character length 10, byte order H, which occupies addresses D1 to D5|
| D1.10L | String  | D area, address 1, character length 10, byte order L, which occupies addresses D1 to D5|
| M8     | bit     | M area, address 8 |
| X10    | bit     | M area, address 8 |
| MX1.1  | bit      | M area, address is the tenth bit of the first register  |
| MB1    | int8     | X area, address is the low byte of the first register  |
| MW1    | int16    | X area, address is the second register   |
| MD1    | int32    | X area, address is the third register   |

## Use Case

Using Inovance' PLC programming software AutoShop, you can quickly connect to the PLC and Neuron for debugging. For specific operations, see [Connect to Easy521](./example/autoshop/autoshop-modbus).

## Data Monitoring

After completing the point configuration, you can click **Monitoring** -> **Data Monitoring** to view device information and control devices. For details, refer to [Data Monitoring](../../../admin/monitoring.md).