# Introduction and Usage of Beckhoff ADS

## Module Description

The ads plugin is used for Beckhoff ADS/AMS devices.

## Parameter Configuration

| Parameter       | Description                                                  |
| --------------- | ------------------------------------------------------------ |
| host            | the IP of the remote device.                                 |
| port            | the TCP port of the remote device (default 48898).           |
| src-ams-net-id  | The AMSNetId of the machine running neuron.                  |
| src-ads-port    | The AMSPort of the machine running neuron.                   |
| dst-ams-net-id  | The AMSNetId of the target PLC.                              |
| dst-ads-port    | The AMSPort of the target PLC.                               |

Note that a ADS route corresponding to the parameter setting should created in the
target TC runtime (PLC), so that neuron could correctly communicate with the PLC.

## Support Data Type

* BOOL
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
* STRING

## Usage of Address Format

### Address Format

> INDEX_GROUP,INDEX_OFFSET</span>

Both `INDEX_GROUP` and `INDEX_OFFSET` could be in decimal or hexadecimal format independently.

### Address Examples

| Address         | Data Type          | Description                                               |
| --------------- | ------------------ | --------------------------------------------------------- |
| 0x4040,0x7d01c  | bool               | index_group 0x4040, index_offset 0x7d01c                  |
| 16448,51029     | uint8              | index_group 0x4040, index_offset 0x7d01d                  |
| 0x4040,512896.5 | string             | index_group 0x4040, index_offset 0x7d380, string length 5 |