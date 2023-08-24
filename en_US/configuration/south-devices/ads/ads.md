# Beckhoff ADS

[TwinCAT] is a control technology developed by Beckhoff Automation. It is a software-based control system used in automation and control applications. TwinCAT is capable of running on a variety of platforms and supports various programming languages.

The Neuron ADS plugin enables users to connect to Beckhoff TwinCAT PLC over TCP/IP.

## Add Device

Go to **Configuration -> South Devices**, then click **Add Device** to add the driver. Configure the following settings in the popup dialog box.

- Name: The name of this device node.
- Plugin: Select the **Beckhoff** plugin.

## Device Configuration

After clicking **Create**, you will be redirected to the **Device Configuration** page, where we will set up the parameters required for Neuron to establish a connection with the northbound application. You can also click the device configuration icon on the southbound device card to enter the **Device Configuration** interface.

| Parameter          | Description                                                  |
| ------------------ | ------------------------------------------------------------ |
| PLC IP Address     | IP address of the remote device.                             |
| PLC Port           | TCP port of the remote device (default 48898).               |
| Source AdsAmsNetId | AMS Net ID of the machine running neuron.                    |
| Source AdsPortNr   | AMS port number of the machine running neuron (default 851). |
| Target AdsAmsNetId | AMS Net ID of the target PLC.                                |
| Target AdsPortNr   | AMS port number of the target PLC (default 851).             |

Note that an ADS route corresponding to the parameter setting should be created in the target TwinCAT software, so that Neuron could correctly communicate with the TwinCAT PLC.

Below are the relevant ADS key concepts:

| Concepts           | Description                                                  |
| ------------------ | ------------------------------------------------------------ |
| ADS protocol       | [ADS] (Automation Device Specification) is the communication protocol of TwinCAT. It enables the data exchange and control of TwinCAT systems via media-independent serial or network connections. ADS was designed to provide a standardized interface for communication between the controller and the user interface in a TwinCAT system. |
| AMS Net ID         | The [AMS Net ID] is the address of the local computer in the TwinCAT network. It consists of 6 bytes and is represented in a dot notation (e.g., "1.2.3.4.5.6"). The AMS Net IDs must be unique in the TwinCAT network to avoid communication conflicts. By default, TwinCAT generates an AMS Net ID by appending ".1.1" to the IP address of the system. For example, in a system with IP address "172.17.213.60", the default generated AMS Net ID would be "172.17.213.60.1.1". But this is not always the case, the most reliable way is to check the AMS Net ID in TwinCAT. |
| AMS port           | An ADS device in the TwinCAT network is identified by an AMS Net ID and a [AMS port number]. Each TwinCAT system typically uses specific port numbers designated as reserved for certain purposes. For example, port 801 is reserved for system communication, and port 851 is reserved for event notification. |
| Index group/offset | ADS [index group and index offset] are specifications used in the TwinCAT ADS system services for data exchange between devices or programs. All read/write operations take place on the PLC via the index group and index offset. The index group is of 16 bits and the index offset is of 32 bits. The index group is used to specify the category or type of data that is being accessed, while the index offset specifies the specific data element within that category or type. |

## Configure Data Groups and Tags

After the plug-in is added and configured, the next step is to establish communication between your device and Neuron by adding groups and tags to the Southbound driver.

Once device configuration is completed, navigate to the **South Devices** page. Click on the device card or device row to access the **Group List** page. Here, you can create a new group by clicking on **Create**, then specifying the group name and data collection interval.

Upon successfully creating a group, click on its name to proceed to the **Tag List** page. This page allows you to add device tags for data collection. You'll need to provide information such as the tag address, attributes, and data type.

For information on general configuration items, see [Connect to Southbound Devices](../south-devices.md). The subsequent section will concentrate on configurations specific to the driver.

### Data Types

* BOOL
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

### Address Format

In the context of the ADS plugin, a tag address consists of two components,
`INDEX_GROUP` and `INDEX_OFFSET`, which represents the index group and the
index offset respectively.

> INDEX_GROUP,INDEX_OFFSET

Both `INDEX_GROUP` and `INDEX_OFFSET` could be in decimal or hexadecimal format.

### Example Addresses

| Address         | Data Type          | Description                                               |
| --------------- | ------------------ | --------------------------------------------------------- |
| 0x4040,0x7d01c  | bool               | index_group 0x4040, index_offset 0x7d01c                  |
| 16448,51029     | uint8              | index_group 0x4040, index_offset 0x7d01d                  |
| 0x4040,512896.5 | string             | index_group 0x4040, index_offset 0x7d380, string length 5 |


[TwinCAT]: https://www.beckhoff.com/en-us/products/automation/twincat/
[ADS]: https://infosys.beckhoff.com/english.php?content=../content/1033/tcadscommon/12440276875.html
[AMS Net ID]: https://infosys.beckhoff.com/english.php?content=../content/1033/tc3_userinterface/3813966475.html
[AMS port number]: https://infosys.beckhoff.com/english.php?content=../content/1033/tcplclib_tc2_system/31064331.html
[index group and index offset]: https://infosys.beckhoff.com/english.php?content=../content/1033/tcadscommon/12495372427.html

## Use Case

YOu can use Neuron to collect data from Beckhoff software PLCs using the Neuron ADS plugin, for details, see [Data Acquisition with Beckhoff ADS Plugin](./plc-ads/ads.md).

## Data Monitoring

After completing the point configuration, you can click **Monitoring** -> **Data Monitoring** to view device information and control devices. For details, refer to [Data Monitoring](../../../usage/monitoring.md).
