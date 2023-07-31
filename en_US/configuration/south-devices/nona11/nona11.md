# NON A11

## Module Description

The non a11 plugin is used for NON-A11 device.

## Add Device

Go to **Configuration -> South Devices**, then click **Add Device** to add the driver. Configure the following settings in the popup dialog box.

- Name: The name of this device node.
- Plugin: Select the **NON A11** plugin.

## Device Configuration

After clicking **Create**, you will be redirected to the **Device Configuration** page, where we will set up the parameters required for Neuron to establish a connection with the northbound application. You can also click the device configuration icon on the southbound device card to enter the **Device Configuration** interface.

| Parameter       | Description                                                  |
| --------------- | ------------------------------------------------------------ |
| connection mode | The way the driver connects to the device, the default is client, which means that the neuron driver is used as the client |
| host            | When neuron is used as a client, host means the ip of the remote device. When used as a server, it means the ip used by neuron locally, and 0.0.0.0 can be filled in by default |
| port            | When neuron is used as client, port means the tcp port of the remote device. When used as a server, it means the tcp port used by neuron locally. |

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

> SITE ! COMMAND ! OFFSET[.LEN]</span>

### Example Addresses

| Address | Data Type          | Description                            |
| ------- | ------------------ | -------------------------------------- |
| 1!1!10.20 | string             | site 1, command 1, offset 10, string length 20 |
| 1!12!1    | uint16/int16       | site 1, command 12, offset 1                   |
| 1!20!32   | uint32/int32/float | site 1, command 20, offset 32                  |