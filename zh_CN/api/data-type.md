# 数据类型

## 概念解析

### Node 节点

在 Neuron 中每个节点都可以与一台设备或一个北向应用建立连接。
* 在设备节点中，可以添加和管理设备点位。
* 在北向节点中，可以选择需要订阅的数据组。

### Group 组

每个节点底下都可以创建多个数据组，对点位进行分类。例如，一台设备连接多个温度传感器和多个湿度传感器，可以创建温度和湿度两个数据组对采集的点位进行分类。Neuron 按组为单位，将采集数据上传到北向应用。
### Tag 点位

在每个组底下可以创建多个采集点位，例如，一台温度传感器采集多个温度值，一个温度值作为一个点位。

### Plugin 插件

在 Neuron 中，每个插件对应一种协议的实现。例如，一种 modbus tcp 协议对应一个插件，mqtt 协议对应一个插件。

## 数据类型

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
* ARRAY_CHAR = 22
* ARRAY_INT8    = 23  
* ARRAY_UINT8   = 24  
* ARRAY_INT16   = 25  
* ARRAY_UINT16  = 26  
* ARRAY_INT32   = 27  
* ARRAY_UINT32  = 28  
* ARRAY_INT64   = 29  
* ARRAY_UINT64  = 30  
* ARRAY_FLOAT   = 31  
* ARRAY_DOUBLE  = 32  
* ARRAY_BOOL    = 33  
* ARRAY_STRING  = 34  
* JSON        = 40 

## 串口

### 波特率

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

### 校验位

* NONE   = 0
* ODD    = 1
* EVEN   = 2
* MARK   = 3
* SPACE  = 4

### 停止位

* Stop_1 = 0
* Stop_2 = 1

### 数据位

* Data_5 = 0
* Data_6 = 1
* Data_7 = 2
* Data_8 = 3

## 点位属性

* READ = 0x01

* WRITE = 0x02

* SUBSCRIBE = 0x04

## Node 节点

### Node 类型

* DRIVER = 1
* APP = 2

### Node 控制

* START = 0
* STOP = 1

### Node 状态

* INIT = 1
* READY = 2
* RUNNING = 3
* STOPPED = 4

### Node 连接状态

* DISCONNECTED = 0
* CONNECTED = 1

## 插件类型

* STATIC = 0
* SYSTEM = 1
* CUSTOM = 2
