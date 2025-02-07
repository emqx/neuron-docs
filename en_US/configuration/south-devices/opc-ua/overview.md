# OPC UA

OPC UA is a machine-to-machine communication protocol for industrial automation developed and maintained by the OPC Foundation. OPC UA provides a standardized way for different devices and systems to communicate with each other.

The Neuron OPC UA plugin can be used as a client to access KEPServerEX, Industrial Gateway OPC Server, Prosys Simulation Server, Ignition, and other OPC UA servers. You can also directly access the built-in OPC UA Server of hardware equipment, such as the built-in Server of Siemens S7-1200 PLC, the built-in Server of Omron NJ series PLC, etc.

## Add Device

Go to **Configuration -> South Devices**, then click **Add Device** to add the driver. Configure the following settings in the popup dialog box.

- Name: The name of this device node.
- Plugin: Select the **OPC UA** plugin.

## Device Configuration

After clicking **Create**, you will be redirected to the **Device Configuration** page, where we will set up the parameters required for Neuron to establish a connection with the device. You can also click the device configuration icon on the southbound device card to enter the **Device Configuration** interface.

| Parameter        | Description                                                                |
| ---------------- | -------------------------------------------------------------------------- |
| **Endpoint URL** | Target OPC UA Server URL, the default value is `opc.tcp://127.0.0.1:4840/` |
| **Username**     | User name used to connect to the target OPC UA Server                      |
| **Password**     | Password for connecting to the target OPC UA Server                        |
| **Cert**         | Client certificate in DER format                                           |
| **Key**          | The client key in DER format                                               |

## Configure Data Groups and Tags

After the plug-in is added and configured, the next step is to establish communication between your device and Neuron by adding groups and tags to the Southbound driver.

Once device configuration is completed, navigate to the **South Devices** page. Click on the device card or device row to access the **Group List** page. Here, you can create a new group by clicking on **Create**, then specifying the group name and data collection interval.

Upon successfully creating a group, click on its name to proceed to the **Tag List** page. This page allows you to add device tags for data collection. You'll need to provide information such as the tag address, attributes, and data type.

For information on general configuration items, see [Connect to Southbound Devices](../south-devices.md). The subsequent section will concentrate on configurations specific to the driver.

::: tip

You can use UaExpert to view the **Namespace Index** ( `NamespaceIndex`) and is the **Node ID** ( `Identifier`), for details, see [UaExpert](./uaexpert.md). 

- For an explanation of namespace indexes and node ids, refer to the OPC UA standard.
- The Neuron set data type must match the OPC UA data type.

:::

### Data Types

* INT8（OPC UA SBYTE type）
* INT16
* INT32
* INT64
* UINT8（OPC UA BYTE type）
* UINT16
* UINT32（also used to indicate the OPC UA DATETIME type）
* UINT64
* FLOAT
* DOUBLE
* BOOL
* BIT
* STRING
* ARRAY_CHAR
* ARRAY_INT8
* ARRAY_UINT8
* ARRAY_INT16
* ARRAY_UINT16
* ARRAY_INT32
* ARRAY_UINT32
* ARRAY_INT64
* ARRAY_UINT64
* ARRAY_FLOAT
* ARRAY_DOUBLE
* ARRAY_BOOL
* JSON

### Data Type Conversion

| OPC UA Data Type         | Neuron Data Type                  |
| ------------------------ | --------------------------------- |
| SByte                    | INT8                              |
| Int16                    | INT16                             |
| Int32                    | INT32                             |
| Int64                    | INT64                             |
| Byte                     | UINT8                             |
| UInt16                   | UINT16                            |
| UInt32                   | UINT32                            |
| UInt64                   | UINT64                            |
| Float                    | FLOAT                             |
| Double                   | DOUBLE                            |
| Boolean                  | BOOL (The value is true or false) |
| Boolean                  | BIT (The value is 0 or 1)         |
| String                   | STRING                            |
| Datetime                 | UINT32                            |
| LocalizedText(Read Only) | STRING                            |
| SByte Array              | ARRAY_INT8                        |
| Int16 Array              | ARRAY_INT16                       |
| Int32 Array              | ARRAY_INT32                       |
| Int64 Array              | ARRAY_INT64                       |
| Byte  Array              | ARRAY_UINT8, ARRAY_CHAR           |
| UInt16 Array             | ARRAY_UINT16                      |
| UInt32 Array             | ARRAY_UINT32                      |
| UInt64 Array             | ARRAY_UINT64                      |
| Float  Array             | ARRAY_FLOAT                       |
| Double Array             | ARRAY_DOUBLE                      |
| Boolean Array            | ARRAY_BOOL                        |
| OPCUA Exentision Object  | JSON                              |

ARRAY_CHAR displays and writes in the form of a string.
JSON displays and writes in the form of a JSON string.

### Address Format

> NS[x,y,z]!NODEID

**NS** Namespace index.

**[x,y,z]** Array index, when the data type is array, you can use the index to get to the value of a specific location, the dimension counts from 0, the dimension is not more than 2. x means one-dimensional index, y means two-dimensional index, z means three-dimensional index.

**NODEID** The node ID, which can be set as a number, a string, or a GUID.

### Example Addresses

| Address                                | Data type | Description                                                                                                                                                                         |
| -------------------------------------- | --------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 0!2258                                 | UINT32    | Get the timestamp of the OPC UA server using the digital NODEID. The NS value is 0, and the NODEID is 2258                                                                          |
| 2!Device1.Module1.Tag1                 | INT8      | Use the string NODEID to get the data point of type SBYTE. If NS is 2, NODEID is Device1.Module1.Tag1                                                                               |
| 0!c496578a-0dfe-4b8f-870a-745238c6ae00 | BOOL      | Get a data point of type BOOL using a NODEID of type GUID; NS is 0 and NODEID is c496578a-0dfe-4b8f-870a-745238c6ae00                                                               |
| 1[2]!array1d[string]                   | STRING    | Accesses the 3rd element of the STRING array; NS is 1, NODEID is array1d[string], one-dimensional index is 2                                                                        |
| 1[2,3]!array2d[int]                    | INT32     | Access the elements of row 3 and column 4 of the INT32 array; NS is 1, NODEID is array2d[int], one-dimensional index is 2, and two-dimensional index is 3.                          |
| 1[2,3,4]!array3d[float]                | FLOAT     | Accesses row 3, column 4, and element 5 of the FLOAT array; NS is 1, NODEID is array3d[float], one-dimensional index is 2, two-dimensional index is 3, three-dimensional index is 4 |
| 0!3D.Point                             | JSON      | Get an extended object representing a 3D position, which contains three member elements: x, y, and z.                                                                               |

## Use Case

This chapter also provides practical examples to facilitate a quick start.

- [Siemens S7-1200](./s71200.md)
- [KEPServerEX](kepserverex.md)
- [Industrial Gateway OPC Server](igs.md)
- [Ignition](ignition.md)
- [Prosys Simulation Server](prosys.md)

## Data Monitoring

After completing the point configuration, you can click **Monitoring** -> **Data Monitoring** to view device information and control devices. For details, refer to [Data Monitoring](../../../admin/monitoring.md).
