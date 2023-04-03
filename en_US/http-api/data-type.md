# Data Type

## Concept

### Node

In Neuron, each node can establish a connection with a device or a northbound application.
* In the device node, you can add and manage device tags.
* In the northbound node, you can select the data group to subscribe to.

### Group

Under each node, multiple data groups can be created to classify tags. For example, if a device is connected to multiple temperature sensors and multiple humidity sensors, temperature and humidity data groups can be created to classify the collected tags. Neuron uploads the collected data to the northbound application based on groups.

### Tag

Under each group, multiple collection tags can be created. For example, a temperature sensor may collect multiple temperature values, with each temperature value treated as a collection tag.

### Plugin

In Neuron, each plugin corresponds to an implementation of a protocol. For example, one Modbus TCP protocol corresponds to one plugin, and one MQTT protocol corresponds to one plugin.

## Data Type

* INT8   = 1
* UINT8  = 2
* INT16  = 3
* UINT16 = 4
* INT32  = 5
* UINT32 = 6
* INT64  = 7
* UINT64 = 8
* FLOAT  = 9
* DOUBLE = 10
* BIT    = 11
* BOOL   = 12
* STRING = 13
* BYTES  = 14
* ERROR = 15
* WORD = 16
* DWORD = 17
* LWORD = 18

## Serial Port

### Baud

* 115200 = 0
* 57600  = 1
* 38400  = 2
* 19200  = 3
* 9600   = 4
* 4800   = 5
* 2400   = 6
* 1800   = 7
* 1200   = 8
* 600    = 9

### Parity

* NONE   = 0
* ODD    = 1
* EVEN   = 2
* MARK   = 3
* SPACE  = 4

### Stop

* Stop_1 = 0
* Stop_2 = 1

### Data

* Data_5 = 0
* Data_6 = 1
* Data_7 = 2
* Data_8 = 3

## Data Attribute

* READ = 0x01

* WRITE = 0x02

* SUBSCRIBE = 0x04

## Node

### Node Type

* DRIVER = 1
* APP = 2

### Node CTL

* START = 0
* STOP = 1

### Node State

* INIT = 1
* READY = 2
* RUNNING = 3
* STOPPED = 4

### Node Link State

* DISCONNECTED = 0
* CONNECTED = 1

## Plugin Kind

* STATIC = 0
* SYSTEM = 1
* CUSTOM = 2
