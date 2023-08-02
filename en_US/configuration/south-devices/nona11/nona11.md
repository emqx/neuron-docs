# NON A11

The non-A11 driver is applicable to non-A11 devices, with the plugin supporting both client and server modes for device interfacing. The plugin currently supports UINT16/INT16/UINT32/INT32/FLOAT/STRING data types and allows user-defined instructions for data reading.

## Add Device

Go to **Configuration -> South Devices**, then click **Add Device** to add the driver. Configure the following settings in the popup dialog box.

- Name: The name of this device node.
- Plugin: Select the **NON A11** plugin.

## Device Configuration

After clicking **Create**, you will be redirected to the **Device Configuration** page, where we will set up the parameters required for Neuron to establish a connection with the northbound application. You can also click the device configuration icon on the southbound device card to enter the **Device Configuration** interface.

| Parameter              | Description                                                  |
| ---------------------- | ------------------------------------------------------------ |
| **Connection Mode**    | The way the driver connects to the device, the default is client, which means that the neuron driver is used as the client |
| **IP Address**         | Only for **TCP** mode. <br />When Neuron is used as a client, fill in the IP of the remote device. <br />When Neuron is used as a server, fill in the IP of Neuron locally, 0.0.0.0 can be filled in by default. |
| **Port**               | Only for **TCP** mode. <br />When Neuron is used as a client, fill in the TCP port of the remote device. <br />When Neuron is used as a server, fill in the TCP port of Neuron. |
| **Site Number**        | Site number                                                  |
| **Connection Timeout** | Connection timeout, unit: ms                                 |
| **Send Interval**      | Send reading instruction interval, unit: ms                  |

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
* STRING

### Address Format

> SITE ! COMMAND ! OFFSET[.LEN]

### Example Addresses

| Address | Data Type          | Description                            |
| ------- | ------------------ | -------------------------------------- |
| 1!1!10.20 | string             | site 1, command 1, offset 10, string length 20 |
| 1!12!1    | uint16/int16       | site 1, command 12, offset 1                   |
| 1!20!32   | uint32/int32/float | site 1, command 20, offset 32                  |

## Data Monitoring

After completing the point configuration, you can click **Monitoring** -> **Data Monitoring** to view device information and control devices. For details, refer to [Data Monitoring](../../../usage/monitoring.md).