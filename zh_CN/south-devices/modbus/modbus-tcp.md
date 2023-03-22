# Modbus 介绍与使用

## 模块描述

Modbus 是一种通信协议，常用于连接工业自动化设备和控制系统，它可以在多种不同的物理层和传输层上实现，包括串行、以太网等。其中，Modbus TCP 和 Modbus RTU 是两种常用的实现方式。

Modbus TCP 使用以太网通信，是一种基于 TCP/IP 协议栈的协议。Neuron 中 modbus-tcp 和 modbus-plus-tcp 两个模块使用 Modbus TCP 协议。在一些透传及类似功能的设备将 Modbus RTU 等协议转换为 Modbus TCP 协议时，也需要使用这两个模块。</br>
两个模块的区别在于 modbus-tcp 模块开源，不需要 License 认证，modbus-plus-tcp 模块需要 License 认证，并且 modbus-plus-tcp 模快支持配置 Client/Server 模式，也支持更多的数据类型，在读写上也做了优化。因此，modbus-plus-tcp 模块的功能要强于 modbus-tcp 模块。modbus-tcp 模块适用于用户了解 Neuron 的使用。

## 参数配置

### Modbus TCP 设备配置

| 字段                  | 说明                                                    |
| -------------------- | ------------------------------------------------------- |
| **connection mode** | 驱动程序连接到设备的方式，默认为 client，即把 Neuron 作为客户端使用 |
| **host**            | 当 Neuron 作为客户端使用时，host 指远程设备的 IP。当 Neuron 作为服务端使用时，host 指 Neuron 在本地使用的 IP，默认可填写 0.0.0.0  |
| **port**            | 当 Neuron 作为客户端使用时，post 指远程设备的 TCP 端口。当 Neuron 作为服务端使用时，host 指 Neuron 在本地使用的 TCP 端口，默认为 502  |
| **timeout**         | 向设备发送请求超时时间                                   |

### Modbus RTU 设备配置

| 字段        | 说明                               |
| ----------- | -------------------------------- |
| **device**  | 使用串口设备，例如“/dev/ttyUSB0”    |
| **stop**    | 停止位，默认值是 1                  |
| **parity**  | 校验位，默认值是 2，代表偶校验        |
| **baud**    | 波特率，默认值是 9600               |
| **data**    | 数据位，默认值是 8                  |
| **timeout** | 向设备发送请求超时时间               |

## 支持的数据类型

* INT16
* INT32
* UINT16
* UINT32
* FLOAT
* BIT
* STRING

## 地址格式用法

### 地址格式

> SLAVE!ADDRESS\[.BIT][#ENDIAN]\[.LEN\[H]\[L]\[D]\[E]]</span>

#### **SLAVE**

必填，指从机地址或者是站点号。

#### **ADDRESS**

必填，指寄存器地址。Modbus 协议有四个区域，每个区域最大有 65536 个寄存器，每个区域的地址范围如下表所示。需要注意的是实际应用中一般不需要 65536 这么大的存储区，一般 PLC 厂家普遍采用 10000 以内的地址范围，请注意根据设备的区域及功能码，正确填写点位地址。

| 区域                       | 地址范围          | 属性        | 寄存器大小     | 功能码        | 数据类型 |
| ------------------------- | ---------------- | ---------- | ------------- | ------------ | ------- |
| coil（线圈）                | 000001 ~ 065536 | 读/写       | 1bit          | 0x01,0x05,0x0f | bit     |
| input（离散量输入）          | 100001 ~ 165536 | 读          | 1bit          | 0x02          | bit     |
| input register（输入寄存器） | 300001 ~ 365536 | 读          | 16bit         | 0x04          | bit,int16,uint16,int32,uint32,float,string |
| hold register（保持寄存器）  | 400001 ~ 465536 | 读/写       | 16bit         | 0x03,0x06,0x10 | bit,int16,uint16,int32,uint32,float,string |

::: tip
一些设备文件会使用功能码和寄存器地址来描述指令，因为寄存器地址编号是从 0 开始的，所以每个区域的寄存器地址范围为 0 ～ 65535。首先，根据功能码确定地址的最高位数，并在寄存器地址上加1，作为 Neuron 的使用地址。
:::

例如，功能码是 0x03，寄存器地址是 0，Neuron 使用的地址是 400001。功能码是 0x02，寄存器地址是 5，Neuron 使用的地址是 100006。

#### **.BIT**

选填，一个寄存器地址的某一位，例如：
| 地址         | 数据类型 | 说明                                                |
| ----------- | ------- | --------------------------------------------------- |
| 1!300004.0  | bit     | 指站号为1，离散量输入区域，地址为 300004，第 0 位    |
| 1!400010.4  | bit     | 指站号为1，保持寄存器区域，地址为 400010，第 4 位    |
| 2!400001.15 | bit     | 指站号为2，保持寄存器区域，地址为 400001，第 15 位   |

#### **#ENDIAN**

选填，字节顺序，适用于 int16/uint16/int32/uint32/float 数据类型，详细说明见下表。
| 符号 | 字节顺序 | 支持的数据类型        | 备注 |
| --- | ------- | ------------------ | ----- |
| #B  | 2,1     | int16/uint16       |       |
| #L  | 1,2     | int16/uint16       | 不填，默认字节顺序 |
| #LL | 1,2,3,4 | int32/uint32/float | 不填，默认字节顺序 |
| #LB | 2,1,4,3 | int32/uint32/float | |
| #BB | 3,4,1,2 | int32/uint32/float | |
| #BL | 4,3,2,1 | int32/uint32/float | |

#### .LEN\[H]\[L]\[D]\[E]

当数据类型为 string 类型时，**.LEN** 是必填项，表示字符串需要占用的字节长度，每个寄存器中包含**H**，**L**，**D** 和**E** 四种存储方式，如下列表格所示。
| 符号 | 说明                                  |
| --- | ------------------------------------- |
| H   | 一个寄存器存储两个字节，高字节在前低字节在后 |
| L   | 一个寄存器存储两个字节，低字节在前高字节在后 |
| D   | 一个寄存器存储一个字节，且存储在低字节      |
| E   | 一个寄存器存储一个字节，且存储在高字节      |

### 地址示例

| 地址         | 数据类型 | 说明 |
| ----------- | ------- | --------- |
| 1!300004    | int16    | 指站号为 1，离散量输入区域，地址为 300004，字节顺序为 #L |
| 1!300004#B  | int16    | 指站号为 1，离散量输入区域，地址为 300004，字节顺序为 #B |
| 1!300004#L  | uint16   | 指站号为 1，离散量输入区域，地址为 300004，字节顺序为 #L |
| 1!400004    | int16    | 指站号为 1，保持寄存器区域，地址为 400004，字节顺序为 #L |
| 1!400004#L  | int16    | 指站号为 1，保持寄存器区域，地址为 400004，字节顺序为 #L |
| 1!400004#B  | uint16   | 指站号为 1，保持寄存器区域，地址为 400004，字节顺序为 #B |
| 1!300004    | int32    | 指站号为 1，离散量输入区域，地址为 300004，字节顺序为 #LL |
| 1!300004#BB | uint32   | 指站号为 1，离散量输入区域，地址为 300004，字节顺序为 #BB |
| 1!300004#LB | uint32   | 指站号为 1，离散量输入区域，地址为 300004，字节顺序为 #LB |
| 1!300004#BL | float    | 指站号为 1，离散量输入区域，地址为 300004，字节顺序为 #BL |
| 1!300004#LL | int32    | 指站号为 1，离散量输入区域，地址为 300004，字节顺序为 #LL |
| 1!400004    | int32    | 指站号为 1，保持寄存器区域，地址为 400004，字节顺序为 #LL |
| 1!400004#LB | uint32   | 指站号为 1，保持寄存器区域，地址为 400004，字节顺序为 #LB |
| 1!400004#BB | uint32   | 指站号为 1，保持寄存器区域，地址为 400004，字节顺序为 #BB |
| 1!400004#LL | int32    | 指站号为 1，保持寄存器区域，地址为 400004，字节顺序为 #LL |
| 1!400004#BL | float    | 指站号为 1，保持寄存器区域，地址为 400004，字节顺序为 #BL |
| 1!300001.10  | String  | 指站号为1，离散量输入区域，地址为 300001，字符长度为 10，字节顺序为 L，即占用的地址为 300001 ～ 300005 |
| 1!300001.10H | String  | 指站号为1，离散量输入区域，地址为 300001，字符长度为 10，字节顺序为 H，即占用的地址为 300001 ～ 300005 |
| 1!300001.10L | String  | 指站号为1，离散量输入区域，地址为 300001，字符长度为 10，字节顺序为 L，即占用的地址为 300001 ～ 300005 |
| 1!400001.10  | String  | 指站号为1，保持寄存器区域，地址为 400001，字符长度为 10，字节顺序为 L，即占用的地址为 400001 ～ 400005 |
| 1!400001.10H | String  | 指站号为1，保持寄存器区域，地址为 400001，字符长度为 10，字节顺序为 H，即占用的地址为 400001 ～ 400005 |
| 1!400001.10L | String  | 指站号为1，保持寄存器区域，地址为 400001，字符长度为 10，字节顺序为 L，即占用的地址为 400001 ～ 400005 |
| 1!400001.10D | String  | 指站号为1，保持寄存器区域，地址为 400001，字符长度为 10，字节顺序为 D，即占用的地址为 400001 ～ 400010 |
| 1!400001.10E | String  | 指站号为1，保持寄存器区域，地址为 400001，字符长度为 10，字节顺序为 E，即占用的地址为 400001 ～ 400010 |