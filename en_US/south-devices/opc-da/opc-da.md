# OPC DA

## Module Description

Neuron can indirectly access OPCDA servers running on Windows operating systems through the external auxiliary program neuopc.exe. neuopc converts the DA protocol to the UA protocol, and then obtains data through Neuron's existing opcua driver. All accessible points of DA are mapped to the "namespace 2" of UA, and the ID of the point is kept with DA. unanimous.

## Parameter Configuration

The component package of neuopc can be downloaded from the [project page](https://github.com/neugates/neuopc) of neuopc (neuopc is an open source project under the GPL agreement). Refer to [neuopc operating environment settings](./neuopc/neuopc.md) for system configuration of installation and remote connection.

![neuopc-setting](./neuopc/assets/neuopc-setting.png)

### neuopc setting

| Parameter   | Description                                                  |
| ----------- | ------------------------------------------------------------ |
| DA Host     | Need to connect to the target host ID, which can be the target IP or Hostname, and this machine can not be set |
| DA Server   | The name of the DA server, such as "Matrikon.OPC.Simulation.1", after filling in the DA Host, you can click the drop-down button to try to get the Server list |
| UA Port     | The listening port setting of the UA server, the default `48401` |
| UA User     | Authorized access user name of UA server, default `admin`    |
| UA Password | Access password of UA server, default `123456`               |

step:

1. Fill in DA Host, you can fill in IP or Hostname, if you don’t fill in, it defaults to this machine;
2. Try to click the drop-down button of DA Server, you can try to get the DA Server list of the target Host, if the drop-down is empty, it means that no DA Server on the target host can be detected;
3. Click the Connect button. After the server is successfully connected, all available measuring point information of the current DA Server will be displayed, and the connection information of the current server will appear in the status bar, as shown in Figure 8;
4. Set UA Port;
5. Set UA User;
6. Set UA Password;
7. Click the Run button. After the UA server starts, all the measuring points in the list will be mapped to the NeuOPC directory of the UA Server. The UA namespace of all measuring points is 2. At this time, the related setting items of UA will become unavailable. ;
8. Double-click the Name column of the neuopc measuring point list to copy the corresponding measuring point name to the clipboard, and then paste it in the neuron tag form.

### Neuron opcua connection configuration

| Parameter    | Description                                                  |
| ------------ | ------------------------------------------------------------ |
| endpoint url | The access address of neuopc, the default is `opc.tcp://127.0.0.1:48401/` |
| username     | Authorized username for neuopc                               |
| password     | Access password for neuopc                                   |

step:

1. Add an opcua device in neuron southbound device management;
2. Modify the endpoint url in the device configuration to the UA Server address of neuopc;
3. Fill in the Username in the device configuration, which is consistent with the setting in neuopc;
4. Fill in the Password in the device configuration, which is the same as that set in neuopc;
5. Submit the setup form directly without filling in the Cert and Key.

## Support Data Type

* INT8（OPCUA SBYTE type）
* INT16
* INT32
* INT64
* UINT8（OPCUA BYTE type）
* UINT16
* UINT32（also used to represent DATETIME types）
* UINT64
* FLOAT
* DOUBLE
* BOOL
* STRING

## Usage of Address Format

### Address Format

> IX!NODEID</span>

**IX** Namespace index, IX can only be 2 when accessing neuopc.

**NODEID** Node ID, consistent with the string in the UA server.

### Address Examples

| Address                | Data Type | Description                                                  |
| ---------------------- | --------- | ------------------------------------------------------------ |
| 1!Bucket Brigade.UInt2 | UINT16    | Get a datatag of type UINT16; NS is 2, NODEID is Bucket Brigade.UInt2 |