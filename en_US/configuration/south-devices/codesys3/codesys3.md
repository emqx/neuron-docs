# CODESYS V3 TCP
The Neuron CODESYS V3 TCP plugin enables access to PLCs and motion control systems based on the CODESYS V3 platform through the TCP protocol.
## Device Settings
| Field    | Description                                     |
| -------- | ----------------------------------------------- |
| host     | Device IP address                               |
| port     | Device port, default is 11740                   |
| timeout  | Request send/receive timeout, default is 3000ms |
| username | Device username                                 |
| password | Device password                                 |
## Supported Data Types
- uint8
- int8
- uint16
- int16
- uint32
- int32
- float
- bool
- string
Type Mapping Table

| CODESYS V3 | Neuron |
| ---------- | ------ |
| Bool       | bool   |
| Byte       | uint8  |
| SInt       | int8   |
| USInt      | uint8  |
| Word       | uint16 |
| Int        | int16  |
| UInt       | uint16 |
| DWord      | uint32 |
| DInt       | int32  |
| Real       | float  |
| UDInt      | uint32 |
| String     | string |

## ADDRESS
> TAG NAME

The symbol configuration exported by the CODESYS V3 platform is the address of the Nueron location.

## Address Examples
| Address                            | Data Type | Description                                                 |
| ---------------------------------- | --------- | ----------------------------------------------------------- |
| Application.PLC_PRG.ok             | bool      | Boolean flag                                                |
| Application.PLC_PRG.d1arr[1]       | int16     | Value of index 1 in a 1D array                              |
| Application.PLC_PRG.d2arr[1,1]     | int32     | Value of index 1,1 in a 2D array                            |
| Application.PLC_PRG.d3arr[1,1,1]   | int16     | Value of index 1,1,1 in a 3D array                          |
| Application.PLC_PRG.point.Y        | float     | Y variable value of the Point structure                     |
| Application.PLC_PRG.points[1].Name | string    | Name variable value of the Point structure array at index 1 |

