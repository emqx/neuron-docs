# Overview

Neuron can indirectly access the OPC DA server running on Windows OS through the external helper program neuopc.exe. NeuOPC converts the DA protocol to UA protocol and then acquires data through Neuron's existing OPC UA plug-in, all accessible points of the DA are mapped to the UA "namespace2" and the point The point IDs are consistent with those of the DA.

The NeuOPC component packages can be downloaded from the [Project page](https://github.com/neugates/neuopc) of NeuOPC (NeuOPC is an open source project under the GPL agreement). For installation and system configuration for remote connection, refer to [NeuOPC Installation](./install.md) and [NeuOPC Remote Access](./remote.md).

## Parameters 

### NeuOPC Parameters

| Parameter   | Description                                                  |
| ----------- | ------------------------------------------------------------ |
| DA Host     | Need to connect to the target host ID, which can be the target IP or Hostname, and this machine can not be set |
| DA Server   | The name of the DA server, such as "Matrikon.OPC.Simulation.1", after filling in the DA Host, you can click the drop-down button to try to get the Server list |
| UA Port     | The listening port setting of the UA server, the default `48401` |
| UA User     | Authorized access user name of UA server, default `admin`    |
| UA Password | Access password of UA server, default `123456`               |


### Neuron opcua Parameters

| Parameter    | Description                                                  |
| ------------ | ------------------------------------------------------------ |
| Endpoint Url | The access address of NeuOPC, the default is `opc.tcp://127.0.0.1:48401/` |
| Username     | Authorized username for NeuOPC                               |
| Password     | Access password for NeuOPC                                   |

## Data Types

* INT8（SBYTE type）
* INT16
* INT32
* INT64
* UINT8（BYTE type）
* UINT16
* UINT32（also used to represent DATETIME types）
* UINT64
* FLOAT
* DOUBLE
* BOOL
* STRING

## Address Format

> IX!NODEID

**IX** Namespace index, IX can only be 2 when accessing NeuOPC.

**NODEID** Node ID, consistent with the string in the UA server.

## Examples

| Address                | Data Type | Description                                                  |
| ---------------------- | --------- | ------------------------------------------------------------ |
| 1!Bucket Brigade.UInt2 | UINT16    | Get a datatag of type UINT16; NS is 2, NODEID is Bucket Brigade.UInt2 |