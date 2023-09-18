# Overview

Neuron KUKA Ethernet KRL TCP plugin accesses KUKA robot devices with the KUKA Ethernet KRL module installed through TCP protocol. Currently, the Neuron KUKA plugin supports the robot device server mode, and the plugin actively connects as a client.

## Parameter Configuration

| Parameter | Description                      |
| --------- | -------------------------------- |
| host      | Target Device IP address         |
| port      | Target Device port, default 5000 |
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

On-site robot devices need to have the KUKA Ethernet KRL module installed in advance. Neuron provides sample TCP Server scripts demo and configuration documents. You can directly [contact us](https://www.emqx.com/en/contact?product=neuron) to obtain the scripts and configuration documents.

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

