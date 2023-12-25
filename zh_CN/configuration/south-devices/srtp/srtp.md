# 概览

Neuron GE SRTP 插件通过 TCP 协议访问支持 SRTP 协议的 GE PLC 设备。

## 设备设置

| 字段    | 说明                                 |
| ------- | ------------------------------------ |
| host    | 设备 IP 地址                         |
| port    | 设备端口号, 默认 18245               |
| timeout | 请求发送接收超时时间, 默认 3000 毫秒 |

## 支持的数据类型

* uint8
* int8
* uint16
* int16
* uint32
* int32
* uint64
* int64
* float
* double
* bit
* string



## 地址格式

> AREA ADDRESS\[.BIT][.LEN]

### .BIT

选填，指某一地址的某一位，范围 0 - 15。

### .LEN

当数据类型为 string 类型时，是必填项，表示字符串长度。

### 区域


| 区域 | 数据类型                                              | 属性  | 备注           | PLC 区域                   |
| ---- | ----------------------------------------------------- | ----- | -------------- | -------------------------- |
| %I   | int8/uint8/bit                                        | 读    | 离散输入       | Discrete inputs            |
| %Q   | int8/uint8/bit                                        | 读/写 | 离散输出       | Discrete outputs           |
| %M   | int8/uint8/int32/uint32/int64/uint64/float/double/bit | 读/写 | 内部引用       | Internal references        |
| %T   | int8/uint8/int32/uint32/int64/uint64/float/double/bit | 读/写 | 临时引用       | Temporary references       |
| %SA  | int8/uint8/int32/uint32/int64/uint64/float/double/bit | 读/写 | 系统状态引用 A | System status references A |
| %SB  | int8/uint8/int32/uint32/int64/uint64/float/double/bit | 读/写 | 系统状态参考 B | System status references B |
| %SC  | int8/uint8/int32/uint32/int64/uint64/float/double/bit | 读/写 | 系统状态参考 C | System status references C |
| %S   | int8/uint8/int32/uint32/int64/uint64/float/double/bit | 读/写 | 系统状态引用   | System status references   |
| %G   | int32/uint32/int64/uint64/float/double/bit            | 读/写 | 离散全局       | Discrete globals           |
| %AI  | int32/uint32/int64/uint64/float/double/bit            | 读    | 模拟输入寄存器 | Analog input registers     |
| %AQ  | int32/uint32/int64/uint64/float/double/bit            | 读/写 | 模拟输出寄存器 | Analog output registers    |
| %R   | int32/uint32/int64/uint64/float/double/bit/string     | 读/写 | 系统寄存器引用 | System register reference  |



## 地址示例

| 地址     | 数据类型 | 说明                                  |
| -------- | -------- | ------------------------------------- |
| %I100    | bit      | %I100                                 |
| %I100    | uint8    | %I100~%I107                           |
| %Q200    | bit      | %Q200                                 |
| %Q200    | uint8    | %Q200~%Q207                           |
| %R100    | int16    | %R100                                 |
| %AI100   | float    | %AI100 float                          |
| %R10     | double   | %R10 double                           |
| %R100.2  | bit      | %R 区域，起始地址 100，第 2 位 bit    |
| %R200.12 | string   | %R 区域，起始地址 200，长度 12 字符串 |
