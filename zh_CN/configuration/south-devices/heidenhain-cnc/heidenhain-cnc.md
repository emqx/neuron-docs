# HEIDENHAIN CNC

海德汉 CNC 驱动通过 LSV2 协议访问海德汉 TNC640, iTNC530 等系列机床和加工中心，可以实时采集多种设备运行数据，包括程序名，主轴倍率，运行状态，主轴刀具，PLC点位等。

## 设备设置

| 字段    | 说明                       |
| ------- | -------------------------- |
| host    | 设备 IP 地址               |
| port    | 设备端口号, 默认19000      |
| timeout | 连接超时时间, 默认5000毫秒 |

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
* bool
* string

## CNC 数据

| tag 标识（地址）  | 说明             | 数据类型 | 参数           | 备注                                                                           |
| ----------------- | ---------------- | -------- | -------------- | ------------------------------------------------------------------------------ |
| runState          | 运行状态         | int16    | -              | 0:已开始 1:已停止 2:已完成 3:已取消 4:已中断 5:错误 6:错误清除 7:空闲 8:未定义 |
| programMain       | 主程序           | string   | -              | -                                                                              |
| programCurrent    | 当前程序         | string   | -              | -                                                                              |
| programLineNo     | 当前程序行号     | int32    | -              | -                                                                              |
| controlMode       | 控制模式         | int16    | -              | 0:手动 1:手动命令输入 2:参考点 3:单步 4:自动 5:未定义                          |
| spindleToolNumber | 主轴当前刀具号   | int32    | -              | -                                                                              |
| spindleToolLength | 主轴当前刀具长度 | double   | -              | -                                                                              |
| spindleToolRadius | 主轴当前刀具半径 | double   | -              | -                                                                              |
| feedOverride      | 进给倍率         | int32    | -              | -                                                                              |
| spindleOverride   | 主轴倍率         | int32    | -              | -                                                                              |
| rapidOverride     | 快速进给倍率     | int32    | -              | -                                                                              |
| machinePosition   | 机械坐标         | double   | .X .Y .Z .A .C | -                                                                              |
| parameter         | 参数             | string   | .(name)        | -                                                                              |


*CNC 地址示例*

| 地址                                    | 说明                |
| --------------------------------------- | ------------------- |
| ProgramMain                             | 读取加工主程序号    |
| machinePosition.X                       | 读取X轴坐标         |
| parameter.CfgDisplayLanguage.ncLanguage | TNC640 读写语言设置 |


### PLC 数据

| 标识 | 说明        | 类型                                                           | 权限 |
| ---- | ----------- | -------------------------------------------------------------- | ---- |
| M    | Marker 信号 | bool                                                           | 读   |
| I    | 输入信号    | bool                                                           | 读   |
| O    | 输出信号    | bool                                                           | 读   |
| T    | Timer信号   | bool                                                           | 读   |
| C    | Counter信号 | bool                                                           | 读   |
| B    | Byte        | uint8/int8/int16/uint16/int32/uint32/int64/uint64/float/double | 读   |
| W    | Word        | int16/uint16/int32/uint32/int64/uint64/float/double            | 读   |
| D    | DWord       | int32/uint32/int64/uint64/float/double                         | 读   |
| N    | Input Word  | int16/uint16/int32/uint32/int64/uint64/float/double            | 读   |
| U    | OutPut Word | int16/uint16/int32/uint32/int64/uint64/float/double            | 读   |
| S    | String      | string                                                         | 读   |

*PLC 常用点位*

| 地址   | 类型   | 说明                                  |
| ------ | ------ | ------------------------------------- |
| M0     | bool   | PLC Marker 区域，地址0的数据          |
| I10    | bool   | PLC Input 区域，地址10的数据          |
| O20    | bool   | PLC Output 区域，地址20的数据         |
| C30    | bool   | PLC Counter 区域，地址30的数据        |
| T40    | bool   | PLC Timer 区域，地址40的数据          |
| B0     | int8   | PLC Byte 区域，地址0的数据            |
| B20    | int16  | PLC Byte 区域，地址20的数据           |
| B40    | double | PLC Byte 区域，地址40的数据           |
| W2     | int16  | PLC Word 区域，地址2的数据            |
| D4     | int32  | PLC Word 区域，地址2的数据            |
| N2     | int16  | PLC Input Word 区域，地址2的数据      |
| U2     | int16  | PLC OutPut Word 区域，地址2的数据     |
| S0.128 | string | PLC String 区域，地址0，长度128的数据 |
