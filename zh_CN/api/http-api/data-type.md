# 数据类型

Neuron 将为 IIoT 平台提供一系列 API 服务，用于查询基本信息、控制网关行为或设置轮询配置。 IIoT 平台必须通过向 Neuron 发送请求消息来启动通信。 通过返回，Neuron 将返回所需的信息或执行相应的操作。 如果有错误，将返回一个错误代码来说明失败的原因。

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

## 串口

### 波特率

* 115200 = 0
* 57600  = 1
* 38400  = 2
* 19200  = 3
* 9600   = 4

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
