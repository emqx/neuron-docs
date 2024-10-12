## DNP 3.0

DNP 3.0 (Distributed Network Protocol 3.0) is a communication protocol primarily used in the industrial automation field, especially in power systems for supervisory control and data acquisition (SCADA) systems. It enables reliable data exchange between remote terminal units (RTUs) and master station systems.

## Device Settings

| Field              | Description                               |
| ------------------ | ----------------------------------------- |
| host               | Device IP address                         |
| port               | Device port number, default 20000         |
| masterid           | Master station ID, default 1              |
| slaveid            | Slave station ID, default 2               |
| class0123_interval | Class0123 pull interval, default 20000 ms |
| class123_interval  | Class123 pull interval, default 1000 ms   |
| time_sync          | Time synchronization, default No          |

## Supported Data Types

* uint8
* uint16
* int16
* uint32
* int32
* float
* bit
  
## Address Format

> obj.var.index(.attribute)
> 
> CROB.index:counter:on-time:off-time

### obj and var

In the DNP 3.0 protocol, obj and var are used to define an object type, and index specifies a specific object within a group of objects. The attribute currently only supports value. If not specified, the default is value.

Currently supported objects are as follows:

| obj | var | Object                                     | r/w | Type          |
| --- | --- | ------------------------------------------ | --- | ------------- |
| 1   | 1   | binary input                               | r   | bit           |
| 1   | 2   | binary input with status                   | r   | bit           |
| 2   | 1   | binary input change without time           | r   | bit           |
| 2   | 2   | binary input change with absolute time     | r   | bit           |
| 2   | 3   | binary input change without relative time  | r   | bit           |
| 10  | 1   | binary output                              | r   | bit           |
| 10  | 2   | binary output with status                  | r   | bit           |
| 10  | 3   | binary output change with time             | r   | bit           |
| 20  | 1   | 32-bit binary counter with flag            | r   | uint32/int32  |
| 20  | 2   | 16-bit binary counter with flag            | r   | uint16/uint16 |
| 20  | 5   | 32-bit binary counter without flag         | r   | uint32/int32  |
| 20  | 6   | 16-bit binary counter without flag         | r   | uint16/int16  |
| 21  | 1   | 32-bit frozen binary counter               | r   | uint32/int32  |
| 21  | 2   | 16-bit frozen binary counter               | r   | uint16/int16  |
| 30  | 1   | 32-bit analog input                        | r   | uint32/int32  |
| 30  | 2   | 16-bit analog input                        | r   | uint16/int16  |
| 30  | 3   | 32-bit analog input without flag           | r   | uint32/int32  |
| 30  | 5   | 32-bit float analog input                  | r   | float         |
| 32  | 1   | 32-bit analog input change without time    | r   | uint32/int32  |
| 32  | 2   | 16-bit analog input change without time    | r   | uint16/int16  |
| 32  | 3   | 32-bit analog input change with time       | r   | uint32/int32  |
| 32  | 4   | 16-bit analog input change with time       | r   | uint16/int16  |
| 32  | 7   | 32-bit float analog input change with time | r   | float         |
| 40  | 1   | 32-bit analog output                       | r   | uint32/int32  |
| 40  | 2   | 16-bit analog output                       | r   | uint16/int16  |
| 40  | 3   | 32-bit float analog output                 | r   | flaot         |
| 41  | 1   | 32-bit analog output block                 | w   | uint32/int32  |
| 41  | 2   | 16-bit analog output block                 | w   | uint16/int16  |
| 41  | 3   | 32-bit float analog output block           | w   | float         |
| 42  | 7   | 32-bit float analog output event with time | r   | float         |

CROB (Control Relay Output Block) is a special object associated with actuating on/off type output devices, write-only, type `uint8`, because it requires setting counter, on-time, and off-time in addition to Control Code. 

Control Code values are as follows:

| Control Code | Action                    |
| ------------ | ------------------------- |
| 1            | output pluse on           |
| 2            | output pluse off          |
| 3            | output latch on           |
| 4            | output latch off          |
| 65           | output pluse on + close   |
| 66           | output pluse off + close  |
| 67           | output latch on  + close  |
| 68           | output latch off  + close |
| 129          | output pluse on + trip    |
| 130          | output pluse off + trip   |
| 131          | output latch on  + trip   |
| 132          | output latch off  + trip  |
| +16          | + queue                   |
| +32          | + clear                   |

## Address Examples

| Address      | Data Type | Description                                           |
| ------------ | --------- | ----------------------------------------------------- |
| 1.2.0        | bit       | Value of binary input index 0                         |
| 1.2.1        | bit       | Value of binary input index 1                         |
| 2.2.1        | bit       | Value of binary input index 1 with absolute timestamp |
| CROB.0:0:0:0 | bit       | Control binary output index 0 output                  |
| 40.1.0       | bit       | Value of 32-bit binary output index 0                 |
