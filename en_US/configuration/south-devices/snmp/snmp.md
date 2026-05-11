# SNMP

SNMP (Simple Network Management Protocol) is a standard protocol used for managing network devices. Through SNMP, network administrators can monitor and manage the status and performance of network devices such as routers, switches, and servers. Currently, the SNMP plugin supports SNMP v2c and plans to support SNMP v3 in future versions to provide enhanced security.

## Adding the Plugin

In **Configuration -> South Devices**, click **Add Device** to create a device node. Enter the plugin name and select **SNMP** as the plugin type to enable the plugin.

## Device Configuration

| <div style="width:100pt">Field</div> | Description |
| ------ | ----------------- |
| **IP Address** | The IP address of the target device.|
| **Local Port** | The local port number used when connecting to the device. The default is 0, which means the system will automatically assign a local port.|
| **Target Port** | The SNMP port number of the target device. The default is 161 |

## Setting Up Groups and Tags

After adding and configuring the plugin, to establish communication between the device and Neuron, you first need to add groups and tags for the southbound driver.

After completing the device configuration, on the **South Devices** page, click the device card/device column to enter the **Group List** page. Click **Create** to create a group, setting the group name and collection interval. After creating the group, click the group name to enter the **Tag List** page, where you can add the device tags to be collected, including tag address, tag attributes, data types, etc.

Common configuration items can be referred to in [Connecting South Devices](../south-devices.md). This page will introduce the supported data types and address formats.

### Data Types

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
* BIT
* BOOL
* STRING
* BYTES

### Address Format

> community|object_identifier

#### **community**

Required. The SNMP community string used to identify the source and permissions of SNMP messages.

#### **object_identifier**

Required. Represents the unique identifier (OID) of the SNMP object to be accessed. The OID consists of a series of numbers representing specific objects in the SNMP Management Information Base (MIB). For example,

### Address Examples

* public|1.3.6.1.2.1.1.1
* private|1.3.6.1.2.1.1.1