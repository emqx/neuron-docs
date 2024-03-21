# KUKA

Neuron KUKA Ethernet KRL TCP plugin accesses KUKA robot devices with the KUKA Ethernet KRL module installed through TCP protocol. Currently, the Neuron KUKA plugin supports the robot device server mode and client mode.

## Parameter Configuration

| Parameter       | Description                                       |
| --------------- | ------------------------------------------------- |
| host            | Target Device IP address or binding IP address    |
| port            | Target Device port or binding port, default 54601 |
| connection_mode | Connection Mode, default 1                        |
## Support Data Type

* uint8
* int8
* uint16
* int16
* uint32
* int32
* uint64
* int64
* float
* double
* bool
* string

## KUKA Ethernet KRL script setting

On-site robot devices need to have the KUKA Ethernet KRL module installed in advance. Neuron provides robotic equipment-side TCP Server script and TCP Client script examples. You can directly [contact us](https://www.emqx.com/en/contact?product=neuron) to obtain the scripts and configuration documents.

## ADDRESS

The plugin address is in the form of XML XPATH.

## Address Examples

| Address                 | Type  | Des                |
| ----------------------- | ----- | ------------------ |
| /RobotState/Current/@A1 | float | current of A1 axis |
| /RobotState/Current/@A2 | float | current of A2 axis |
| /RobotState/Torque/@A1  | float | torque of A1 axis  |
| /RobotState/Torque/@A2  | float | torque of A2 axis  |
| /RobotState/Err/@number | int32 | error number       |

