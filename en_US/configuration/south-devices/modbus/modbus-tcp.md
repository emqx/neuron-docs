# Modbus TCP

## Module Description

Modbus is a communication protocol commonly used to connect industrial automation equipment and control systems, and it can be implemented on various physical and transport layers, including serial and Ethernet. Modbus TCP and Modbus RTU are two commonly used implementation methods.

Modbus TCP uses Ethernet communication and is a protocol based on the TCP/IP protocol stack. In Neuron, the modbus-tcp and modbus-plus-tcp modules use the Modbus TCP protocol. When some devices that support Modbus RTU and other protocols need to be converted to Modbus TCP protocol for passthrough or similar functions, these two modules are also required.</br>
The difference between the two modules is that the modbus-tcp module is open source and does not require License authentication, while the modbus-plus-tcp module requires License authentication. The modbus-plus-tcp module supports configuring the Client/Server mode, as well as more data types, and also optimizes the read/write performance. Therefore, the functionality of the modbus-plus-tcp module is stronger than that of the modbus-tcp module. The modbus-tcp module is suitable for users who are familiar with the use of Neuron.

## Parameter Configuration

### Modbus TCP Parameter Setting

| Parameter     | Description                  |
| ------------- | ---------------------------- |
| **connection mode** | The way the driver connects to the device, the default is client, which means that the neuron driver is used as the client       |
| **host**            | When neuron is used as a client, host means the ip of the remote device. When used as a server, it means the ip used by neuron locally, and 0.0.0.0 can be filled in by default    |
| **port**           | When neuron is used as client, port means the tcp port of the remote device. When used as a server, it means the tcp port used by neuron locally.   |
| **timeout**         | Timeout for sending requests to the device                                   |

### Modbus RTU Parameter Setting

| Parameter     | Description                                         |
| ------------- | --------------------------------------------------- |
| **device**    | Use a serial device, e.g. **/dev/ttyUSB0**          |
| **stop**      | stopbits, default 1                                 |
| **parity**    | parity bit, default 2, which means even parity      |
| **baud**      | baudrate, default 9600                              |
| **data**      | bytesize, default 8                                 |
| **timeout**   | Timeout for sending requests to the device        |

### Support Data Type

* INT16
* INT32
* UINT16
* UINT32
* FLOAT
* BIT
* STRING

## Usage of Address Format

### Address Format

> SLAVE!ADDRESS\[.BIT][#ENDIAN]\[.LEN\[H]\[L]\[D]\[E]]</span>

#### **SLAVE**

Required, Slave is the slave address or site number.

#### **ADDRESS**

Required,  Address is the register address.The Modbus protocol has four areas, each area has a maximum of 65536 registers, and the address range of each area is shown in the table below. It should be noted that the storage area as large as 65536 is generally not required in practical applications. Generally, PLC manufacturers generally use an address range within 10000. Please pay attention to fill in the correct point address according to the area and function code of the device.

| AREA           | ADDRESS RANGE   | ATTRIBUTE  | REGISTER SIZE | FUNCTION     | DATA TYPE  |
| -------------- | --------------- | ---------- | ------------- | ------------ | ---------- |
| coil           | 000001 ~ 065536 | read/write | 1bit          | 0x1,0x5,0x0f | bit        |
| input          | 100001 ~ 165536 | read       | 1bit          | 0x2          | bit        |
| input register | 300001 ~ 365536 | read       | 16bit         | 0x4          | bit,int16,uint16,int32,uint32,float,string |
| hold register  | 400001 ~ 465536 | read/write | 16bit         | 0x3,0x6,0x10 | bit,int16,uint16,int32,uint32,float,string |

::: tip
Some device documents use function codes and register addresses to describe instructions. Because register address numbers start from 0, the register address range for each region is 0 to 65535. First, determine the highest digit of the address according to the function code, and add 1 to the register address as the address of Neuron.
:::

example, function is 0x03, and register address is 0, then address used by neuron is 400001. function is 0x02, and register address is 5, then address used by neuron is 100006.

#### **.BIT**

Optional, a bit of a register address.

#### **#ENDIAN**

Optional, endianness, applicable to int16/uint16/int32/uint32/float data types, see the table below for details.
| Symbol     | endianness | Data Type | Remark                       |
| ---------- | --------- | ----------------------- | ----- |
| #B         | 2,1       | int16/uint16            |       |
| #L         | 1,2       | int16/uint16            | Leave blank, default byte order |
| #LL        | 1,2,3,4   | int32/uint32/float      | Leave blank, default byte order |
| #LB        | 2,1,4,3   | int32/uint32/float      | |
| #BB        | 3,4,1,2   | int32/uint32/float      | |
| #BL        | 4,3,2,1   | int32/uint32/float      | |

#### .LEN\[H]\[L]\[D]\[E]

When the data type is string type, **.LEN** is a required, indicating the length of bytes that the string needs to occupy. Each register contains **H**, **L**, **D** and **E** four storage methods, as shown in the table below.
| Symbol | Description                                  |
| --- | ------------------------------------- |
| H   | A register stores two bytes, the high byte is in front of the low byte |
| L   | A register stores two bytes, the low byte is in front of the high byte |
| D   | A register stores one byte, and is stored in the low byte      |
| E   | A register stores one byte, and is stored in the high byte      |

### Address Examples

| Address     | Data Type | Description                                                 |
| ----------- | --------- | --------------------------------------------------- |
| 1!300004.0  | bit     | Refers to station number 1, input register area, address 300004, bit 0    |
| 1!400010.4  | bit     | Refers to station number 1, hold register area, address 400010, bit 4    |
| 2!400001.15 | bit     | Refers to station number 2, hold register area, address 400001, bit 15   |
| 1!300004    | int16    | Refers to station number 1, input register area, address 300004, endianness is #L |
| 1!300004#B  | int16    | Refers to station number 1, input register area, address 300004, endianness is #B |
| 1!300004#L  | uint16   | Refers to station number 1, input register area, address 300004, endianness is #L |
| 1!400004    | int16    | Refers to station number 1, hold register area, address 400004, endianness is #L |
| 1!400004#L  | int16    | Refers to station number 1, hold register area, address 400004, endianness is #L  |
| 1!400004#B  | uint16   | Refers to station number 1, hold register area, address 400004, endianness is #B |
| 1!300004    | int32    | Refers to station number 1, input register area, address 300004, endianness is #LL |
| 1!300004#BB | uint32   | Refers to station number 1, input register area, address 300004, endianness is #BB |
| 1!300004#LB | uint32   | Refers to station number 1, input register area, address 300004, endianness is #LB |
| 1!300004#BL | float    | Refers to station number 1, input register area, address 300004, endianness is #BL |
| 1!300004#LL | int32    | Refers to station number 1, input register area, address 300004, endianness is #LL |
| 1!400004    | int32    | Refers to station number 1, hold register area, address 400004, endianness is #LL |
| 1!400004#LB | uint32   | Refers to station number 1, hold register area, address 400004, endianness is #LB |
| 1!400004#BB | uint32   | Refers to station number 1, hold register area, address 400004, endianness is #BB |
| 1!400004#LL | int32    | Refers to station number 1, hold register area, address 400004, endianness is #LL |
| 1!400004#BL | float    | Refers to station number 1, hold register area, address 400004, endianness is #BL |
| 1!300001.10  | String  | Refers to station number is 1, input register area, the address is 300001, the string length is 10, and endianness is L, the occupied address is 300001-300005 |
| 1!300001.10H | String  | Refers to station number is 1, input register area, the address is 300001, the string length is 10, and endianness is H, the occupied address is 300001-300005 |
| 1!300001.10L | String  |  Refers to station number is 1, input register area, the address is 300001, the string length is 10, and endianness is L, the occupied address is 300001-300005 |
| 1!400001.10  | String  | Refers to station number is 1, hold register area, the address is 400001, the string length is 10, and endianness is L, the occupied address is 400001-400005 |
| 1!400001.10H | String  | Refers to station number is 1, hold register area, the address is 400001, the string length is 10, and endianness is H, the occupied address is400001 ～ 400005 |
| 1!400001.10L | String  | Refers to station number is 1, hold register area, the address is 400001, the string length is 10, and endianness is L, the occupied address is 400001-400005  |
| 1!400001.10D | String  | Refers to station number is 1, hold register area, the address is 400001, the string length is 10, and endianness is D, the occupied address is 400001-400010 |
| 1!400001.10E | String  | Refers to station number is 1, hold register area, the address is 400001, the string length is 10, and endianness is E, the occupied address is 400001-400010 |
