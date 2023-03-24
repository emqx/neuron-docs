# Data Type

Neuron provide a series of API services for IIoT platform, to query the basic information, to control gateway behaviors or to setup the polling configuration. IIoT platform can initiate the communication by sending request message to Neuron. By return, Neuron would send back the required information or execute the deserved action. If there is error, a error code would be returned to tell the reason of failure.

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
