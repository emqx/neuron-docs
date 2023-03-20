# Siemens FetchWrite 介绍与使用

## 模块描述

s5fetch-write 插件用于带有网络扩展模块CP443的西门子PLC的访问，如，s7-300/400。

## 参数配置

| 字段     | 说明                        |
| -------- | --------------------------- |
| **host** | 远程 PLC 的 IP              |
| **port** | 远程 PLC 的端口，默认为 102 |

## 支持的数据类型

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
* BIT
* STRING

## 地址格式用法

### 地址格式

> AREA ADDRESS\[.BIT][.LEN]</span>

#### AREA ADDRESS

| 区域 | 数据类型                                                     | 属性  | 备注                    |
| ---- | ------------------------------------------------------------ | ----- | ----------------------- |
| DB   | int16/uint16/bit/int32/uint32/int64/uint64/float/double/string | 读    | 主存数据块，以words读写 |
| M    | int8/uint8/int16/uint16/bit/int32/uint32/int64/uint64/float/double/string | 读/写 | 标志内存M，以bytes读写  |
| I    | int8/uint8/int16/uint16/bit/int32/uint32/int64/uint64/float/double/string | 读/写 | 输入，以bytes读写       |
| Q    | int8/uint8/int16/uint16/bit/int32/uint32/int64/uint64/float/double/string | 读/写 | 输出，以bytes读写       |
| PEPA | int8/uint8/int16/uint16/bit/int32/uint32/int64/uint64/float/double/string | 读/写 | IO modules，以bytes读写 |
| Z    | int16/uint16/bit/int32/uint32/int64/uint64/float/double/string | 读/写 | 计数器，以words读写     |
| T    | int16/uint16/bit/int32/uint32/int64/uint64/float/double/string | 读/写 | 计时器，以words读写     |

#### .BIT

选填，指某一地址的某一位。

#### .LEN

当数据类型为 string 类型时，是必填项，表示字符串长度。

### 地址示例

| 地址         | 数据类型 | 说明                                         |
| ------------ | -------- | -------------------------------------------- |
| I0         | int16    | I 区域，地址为 0             |
| I1         | uint16   | I 区域，地址为 1             |
| Q2         | int16    | Q 区域，地址为 2             |
| Q3         | uint16   | Q 区域，地址为 3             |
| PEPA4      | int16    | PEPA 区域，地址为 4          |
| PEPA5      | int16    | PEPA 区域，地址为 5          |
| T6         | int16    | T 区域，地址为 6             |
| T7         | int16    | T 区域，地址为 7             |
| Z8         | uint16   | Z 区域，地址为 8             |
| Z9         | uint16   | Z 区域，地址为 9             |
| DB10.DBW10 | int16    | 10 数据块中，起始数据字为 10 |
| DB12.DBW10 | uint16   | 12 数据块中，起始数据字为 10 |
| DB10.DBW10 | float    | 10 数据块中，起始数据字为 10 |
| DB11.DBW10 | double   | 11 数据块中，起始数据字为 10 |
| I0.0        | bit      | I 区域，地址为0，第 0 位             |
| I0.1        | bit      | I 区域，地址为0，第 1 位             |
| Q1.0        | bit      | Q 区域，地址为1，第 0 位             |
| Q1.2        | bit      | Q 区域，地址为1，第 2 位             |
| PEPA2.1     | bit      | PEPA 区域，地址为2，第 1 位          |
| PEPA2.2     | bit      | PEPA 区域，地址为2，第 2 位          |
| T3.3        | bit      | T 区域，地址为3，第 3 位             |
| T3.4        | bit      | T 区域，地址为3，第 4 位             |
| Z4.5        | bit      | Z 区域，地址为4，第 5 位             |
| Z4.6        | bit      | Z 区域，地址为4，第 6 位             |
| DB1.DBW10.1 | bit      | 1 数据块中，起始数据字为 10，第 0 位 |
| DB2.DBW1.15 | bit      | 2 数据块中，起始数据字为 1，第 15 位 |
| DB1.DBW12.20 | string   | 1 数据块中，起始数据字为 12，字符串长度为 20 |