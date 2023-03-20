# Introduction and Usage of NON A11

## Module Description

The non a11 plugin is used for NON-A11 device.

## Parameter Configuration

| Parameter       | Description                                                  |
| --------------- | ------------------------------------------------------------ |
| connection mode | The way the driver connects to the device, the default is client, which means that the neuron driver is used as the client |
| host            | When neuron is used as a client, host means the ip of the remote device. When used as a server, it means the ip used by neuron locally, and 0.0.0.0 can be filled in by default |
| port            | When neuron is used as client, port means the tcp port of the remote device. When used as a server, it means the tcp port used by neuron locally. |
| site            | NON-A11 device site number.                                  |

## Support Data Type

* INT16
* UINT16
* INT32
* UINT32
* FLOAT
* STRING

## Usage of Address Format

### Address Format

> COMMAND ! OFFSET[.LEN]</span>

### Address Examples

| Address | Data Type          | Description                            |
| ------- | ------------------ | -------------------------------------- |
| 1!10.20 | string             | command 1, offset 10, string length 20 |
| 12!1    | uint16/int16       | command 12, offset 1                   |
| 20!32   | uint32/int32/float | command 20, offset 32                  |