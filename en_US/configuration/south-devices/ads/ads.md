# Beckhoff ADS

[TwinCAT] is a control technology developed by Beckhoff Automation. It is a
software-based control system used in automation and control applications.
TwinCAT is capable of running on a variety of platforms and supports various
programming languages.

The Neuron ADS plugin enables users to connect to Beckhoff TwinCAT PLC over
TCP/IP.

## ADS protocol

[ADS] (Automation Device Specification) is the communication protocol of
TwinCAT. It enables the data exchange and control of TwinCAT systems via
media-independent serial or network connections. ADS was designed to provide a
standardized interface for communication between the controller and the user
interface in a TwinCAT system.

### AMS Net ID

The [AMS Net ID] is the address of the local computer in the TwinCAT network.
It consists of 6 bytes and is represented in a dot notation (e.g., "1.2.3.4.5.6").
The AMS Net IDs must be unique in the TwinCAT network to avoid communication
conflicts. By default, TwinCAT generates an AMS Net ID by appending ".1.1" to
the IP address of the system. For example, in a system with IP address
"172.17.213.60", the default generated AMS Net ID would be "172.17.213.60.1.1".

### AMS port

An ADS device in the TwinCAT network is identified by an AMS Net ID and a
[AMS port number]. Each TwinCAT system typically uses specific port numbers
designated as reserved for certain purposes. For example, port 801 is reserved
for system communication and port 851 is reserved for event notification.

### Index group/offset

ADS [index group and index offset] are specifications used in the TwinCAT ADS
system services for data exchange between devices or programs. All read and
write operations take place on the PLC via the index group and index offset.
The index group is of 16 bits and the index offset is of 32 bits.
The index group is used to specify the category or type of data that is being
accessed, while the index offset specifies the specific data element within that
category or type.

## Parameters

| Parameter       | Description                                                  |
| --------------- | ------------------------------------------------------------ |
| host            | IP address of the remote device.                             |
| port            | TCP port of the remote device (default 48898).               |
| src-ams-net-id  | AMS Net ID of the machine running neuron.                    |
| src-ads-port    | AMS port number of the machine running neuron.               |
| dst-ams-net-id  | AMS Net ID of the target PLC.                                |
| dst-ads-port    | AMS port number of the target PLC.                           |

Note that a ADS route corresponding to the parameter setting should be created
in the target TwinCAT software, so that neuron could correctly communicate with
the TwinCAT PLC.

## Data types

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

## Address format

In the context of the ADS plugin, a tag address consists of two components,
`INDEX_GROUP` and `INDEX_OFFSET`, which represents the index group and the
index offset respectively.

> INDEX_GROUP,INDEX_OFFSET

Both `INDEX_GROUP` and `INDEX_OFFSET` could be in decimal or hexadecimal format.

### Address Examples

| Address         | Data Type          | Description                                               |
| --------------- | ------------------ | --------------------------------------------------------- |
| 0x4040,0x7d01c  | bool               | index_group 0x4040, index_offset 0x7d01c                  |
| 16448,51029     | uint8              | index_group 0x4040, index_offset 0x7d01d                  |
| 0x4040,512896.5 | string             | index_group 0x4040, index_offset 0x7d380, string length 5 |


[TwinCAT]: https://www.beckhoff.com/en-us/products/automation/twincat/
[ADS]: https://infosys.beckhoff.com/english.php?content=../content/1033/tcadscommon/12440276875.html
[AMS Net ID]: https://infosys.beckhoff.com/english.php?content=../content/1033/tc3_userinterface/3813966475.html
[AMS port number]: https://infosys.beckhoff.com/english.php?content=../content/1033/tcplclib_tc2_system/31064331.html
[index group and index offset]: https://infosys.beckhoff.com/english.php?content=../content/1033/tcadscommon/12495372427.html
