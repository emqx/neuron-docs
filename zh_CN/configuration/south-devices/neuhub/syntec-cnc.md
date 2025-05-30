# SYNTEC CNC

Neuron 可以使用 Neuron HUB 驱动和 NeuronHUB Windows 程序，间接访问新代 CNC 系统。以实时采集多种设备运行数据，包括程序名，主轴倍率，运行状态，PLC 点位, 参数，全局变量等。

## NEURON HUB Windows 程序参数

| 参数      | 说明                                 |
| --------- | ------------------------------------ |
| Node Name | 节点名称，必须唯一，用来区分多个节点 |
| Host      | 需要连接 CNC 设备 IP 地址            |


## 支持的数据类型

* uint8
* int8
* uint32
* int32
* uint64
* int64
* float
* double
* bit
* string    
* ARRAY_STRING 


## CNC 数据

> address\[.m]\[.n]

| tag 标识（地址）       | 说明           | 数据类型     | 参数 | 备注                                                                                                                                                                      |
| ---------------------- | -------------- | ------------ | ---- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| systemInfo.axes        | 可控制轴数     | int32        | -    | -                                                                                                                                                                         |
| systemInfo.cnc_type    | 系统类型       | string       | -    | -                                                                                                                                                                         |
| systemInfo.max_axes    | 最大轴数       | int32        | -    | -                                                                                                                                                                         |
| systemInfo.series      | M/T 类型       | string       | -    | -                                                                                                                                                                         |
| systemInfo.nc_ver      | 系统软件版本   | string       | -    | -                                                                                                                                                                         |
| systemInfo.axis_name   | 各轴坐标名称   | array string | -    | -                                                                                                                                                                         |
| systemStatus.status    | 当前运行状态   | string       | -    | -                                                                                                                                                                         |
| systemStatus.main_prog | 主程序名       | string       | -    | 0: 录入方式 1: 自动方式 2: 无效方式 3: 编辑方式 4: 单步方式 5: 手动方式 8: 手轮方式 9: 机械回零方式 10: 程序回零方式                                                      |
| systemStatus.cur_prog  | 目前执行程序名 | string       | -    | -                                                                                                                                                                         |
| systemStatus.mode      | 模式           | string       | -    | 0x1: 急停信号有效 0x2: 伺服准备未绪 0x4: IO 准备未绪（远程 IO 设备等）                                                                                                    |
| systemStatus.alarm     | 报警           | string       | -    | -                                                                                                                                                                         |
| systemStatus.emg       | 紧停           | string       | -    | -                                                                                                                                                                         |
| alarms                 | 当前报警       | array string | -    | -                                                                                                                                                                         |
| halarms                | 历史报警       | array string | -    | -                                                                                                                                                                         |
| oplog                  | 操作记录       | array string | -    | -                                                                                                                                                                         |
| absolute               | 绝对坐标       | double       | m    | X Y Z                                                                                                                                                                     |
| machine                | 机械坐标       | double       | m    | X Y Z                                                                                                                                                                     |
| relative               | 相对坐标       | double       | m    | X Y Z                                                                                                                                                                     |
| distance               | 剩余距离       | double       | m    | X Y Z                                                                                                                                                                     |
| time                   | 时间           | int32        | m    | power: 上电时间（单位：秒） cutting: 切削时间（单位：秒）cycle: 循环时间（单位：秒） work: 加工时间（单位：秒）                                                           |
| partCount              | 加工计数       | int32        | m    | total: 总加工计数 cur: 当前加工计数 req: 要求加工件数                                                                                                                     |
| ovfeed                 | 当前进给倍率   | double       | -    | -                                                                                                                                                                         |
| ovspindle              | 当前主轴倍率   | double       | -    | -                                                                                                                                                                         |
| actfeed                | 实际进给速度   | double       | -    | -                                                                                                                                                                         |
| actspindle             | 实际主轴转速   | int32        | -    | -                                                                                                                                                                         |
| gcode                  | G 代码         | array string | -    | -                                                                                                                                                                         |
| otherCode              | Other 代码     | int32        | m    | hcode   dcode   mcode    tcode   fcode    scode                                                                                                                           |
| macro                  | 全局变量       | double       | m    | 全局变量编号                                                                                                                                                              |
| param                  | 参数           | int32        | m    | 参数编号                                                                                                                                                                  |
| toolOffset             | 刀补           | double       | m，n | m：刀补编号。 n：RADIUS_GEOM，RADIUS_WEAR，LENGTH_GEOM，LENGTH_WEAR，WEAR_X，WEAR_Z，WEAR_A，LENGTH_X，LENGTH_Y，LENGTH_A， TOOL_NOSE_RADIUS，TOOL_NOSE_R_WEAR，TOOL_NOSE |

::: tip
macro，param 可读写，其他只读。
:::




*CNC 地址示例*

| 地址                    | 说明                |
| ----------------------- | ------------------- |
| systemInfo.nc_ver       | 读取系统软件版本    |
| machine.X               | 读取 X 轴坐标       |
| macro.100               | 读写 100 号全局变量 |
| feedOverride            | 读取当前进给倍率    |
| alarms                  | 当前报警            |
| partCount.total         | 总加工计数          |
| toolOffset1.RADIUS_GEOM | 刀补1，半径补偿     |


### PLC 数据

### 地址格式

> AREA ADDRESS\[.BIT]\[.LEN]

| 标识 | 说明        | 类型                                              | 权限  |
| ---- | ----------- | ------------------------------------------------- | ----- |
| I    | Input Bits  | bit/int8/uint8                                    | 读    |
| O    | Output Bits | bit/int8/uint8                                    | 读    |
| C    | C Bits      | bit/int8/uint8                                    | 读    |
| S    | S Bits      | bit/int8/uint8                                    | 读    |
| A    | A Bits      | bit/int8/uint8                                    | 读    |
| R    | 寄存器      | bit/int32/uint32/int64/uint64/float/double/string | 读/写 |


::: tip
目前只支持设置部分 R 区，不支持 bit 写入。
:::

> AREA ADDRESS\[.setting/value/state]

| 标识 | 说明   | 类型         | 权限 |
| ---- | ------ | ------------ | ---- |
| T    | 定时器 | int32/uint32 | 读   |
| N    | 计数器 | int32/uint32 | 读   |

::: tip
读取定时器和计数器时，需要指定是设置值，当前值还是状态。
:::

*PLC 常用点位*

| 地址       | 类型  | 说明                           |
| ---------- | ----- | ------------------------------ |
| I0.0       | bit   | Input Bits  区域，地址0的数据  |
| A10        | int8  | A Bits 区域，地址10的数据      |
| R100       | float | 寄存器 区域，地址100的数据     |
| T0.setting | int32 | 定时器 区域，地址0的设定值数据 |
| T0.value   | int32 | 定时器 区域，地址0的当前数据   |



