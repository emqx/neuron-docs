# DNP 3.0 

DNP 3.0 （Distributed Network Protocol 3.0）是一种通信协议，主要用于工业自动化领域，特别是在电力系统中，用于监控和数据采集（SCADA）系统。它允许远程终端单元（RTU）和主站系统之间进行可靠的数据交换。


## 设备设置

| 字段               | 说明                              |
| ------------------ | --------------------------------- |
| host               | 设备 IP 地址                      |
| port               | 设备端口号, 默认20000             |
| masterid           | 主站 ID, 默认1                    |
| slaveid            | 从站 ID, 默认2                    |
| class0123_interval | Class0123 拉取间隔, 默认20000毫秒 |
| class123_interval  | Class123 拉取间隔, 默认1000毫秒   |
| time_sync          | 时间同步, 默认 No                 |

## 支持的数据类型

* uint8
* uint16
* int16
* uint32
* int32
* float
* bit

## 地址格式

> obj.var.index(.attribute)
> 
> CROB.index:counter:on-time:off-time

### obj 和 var

在 DNP 3.0 协议中，使用 obj 和 var 来定义一个对象类型，index 指定一组对象实体的具体的对象，下表索引从0开始。attribute 目前只支持 value，如果不填写，默认为value。

目前支持下列对象：

| obj | var | 对象                                       | r/w | 类型          |
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

CROB（Control Relay Output Block）是一个特殊的对象，用于驱动开关型输出设备 （binary output），只写，类型为 `uint8`, 因为其除了 Control Code 之外，还需要设置 counter，on-time 和 off-time。 
Control Code 取值如下：
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


## 地址示例

| 地址         | 数据类型 | 说明                                 |
| ------------ | -------- | ------------------------------------ |
| 1.2.0        | bit      | binary input 下标0的值               |
| 1.2.1        | bit      | binary input 下标1的值               |
| 2.2.1        | bit      | binary input 下标1的值，带绝对时间戳 |
| CROB.0:0:0:0 | bit      | 控制 biary output 下标0输出          |
| 40.1.0       | bit      | 32-bit binary output 下标0的值       |