# OPC UA

OPC UA is a machine-to-machine communication protocol for industrial automation developed and maintained by the OPC Foundation. OPC UA provides a standardized way for different devices and systems to communicate with each other.

The Neuron OPC UA plug-in can be used as a client to access KEPServerEX, Industrial Gateway OPC Server, Prosys Simulation Server, Ignition and other OPC UA servers. You can also directly access the built-in OPC UA Server of hardware equipment, such as: the built-in Server of Siemens S7-1200 PLC, the built-in Server of Omron NJ series PLC, etc.

## Parameters

|  Parameter              |  Description                       |
| ----------------- | --------------------------- |
| **Endpoint URL**  | Target OPC UA Server URL, the default value is `opc.tcp://127.0.0.1:4840/` |
| **Username**      | User name used to connect to the target OPC UA Server     |
| **Password**      | Password for connecting to the target OPC UA Server       |
| **Cert**          | Client certificate in DER format          |
| **Key**           | The client key in DER format   |

## Data types

* INT8（OPC UA SBYTE type）
* INT16
* INT32
* INT64
* UINT8（OPC UA BYTE type）
* UINT16
* UINT32（It is also used to indicate the OPC UA DATETIME type）
* UINT64
* FLOAT
* DOUBLE
* BOOL
* STRING


## Address format

> NS!NODEID</span>

**NS** Namespace index.

**NODEID** Node ID. The value can be a number or a string.

## Examples

|  Address               | Data type | Description                                                 |
| ---------------------- | -------- | ------------------------------------------------------------ |
| 0!2258                 | UINT32   | Get the timestamp of the OPC UA server using the digital NODEID. The NS value is 0, and the NODEID is 2258 |
| 2!Device1.Module1.Tag1 | INT8     | Use the string NODEID to get the data point of type SBYTE. If NS is 2, NODEID is Device1.Module1.Tag1 |

You can use UaExpert software to help you view the namespace index and node ID information for the required points.

:::tip
For an explanation of namespace indexes and node ids, refer to the OPC UA standard.

The Neuron set data type must match the OPC UA data type.
:::
