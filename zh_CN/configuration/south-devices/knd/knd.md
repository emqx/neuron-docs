# KND CNC

凯恩帝 CNC 驱动通过 HTTP 协议访问凯恩帝 K2000、K1000 C/Ci/F/Fi、K1000TTCi 系列的数控系统，可以实时采集多种设备运行数据，包括程序名，主轴倍率，运行状态，PLC 点位等。

## 设备设置

| 字段 | 说明                 |
| ---- | -------------------- |
| host | 设备 IP 地址         |
| port | 设备端口号, 默认8000 |

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
* bit
* string

## CNC 数据

> address\[.m]

| tag 标识（地址）              | 说明               | 数据类型     | 参数 | 备注                                                                                                                                                                                                                                                                                                                                                                             |
| ----------------------------- | ------------------ | ------------ | ---- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| systemInfo.id                 | ID                 | int32        | -    | -                                                                                                                                                                                                                                                                                                                                                                                |
| systemInfo.type               | 系统类型           | string       | -    | -                                                                                                                                                                                                                                                                                                                                                                                |
| systemInfo.manufacturer       | 制造商             | string       | -    | -                                                                                                                                                                                                                                                                                                                                                                                |
| systemInfo.manufacture-time   | 生产时间           | string       | -    | -                                                                                                                                                                                                                                                                                                                                                                                |
| systemInfo.soft-version       | 系统软件版本号     | string       | -    | -                                                                                                                                                                                                                                                                                                                                                                                |
| systemInfo.fpga-version       | FPGA版本号         | string       | -    | -                                                                                                                                                                                                                                                                                                                                                                                |
| systemInfo.ladder-version     | 梯图版本号         | string       | -    | -                                                                                                                                                                                                                                                                                                                                                                                |
| systemInfo.user-axes          | 用户轴列表         | array string | -    | -                                                                                                                                                                                                                                                                                                                                                                                |
| systemStatus.run-status       | 当前运行状态       | int32        | -    | 0: CNC 处于停止状态 1: CNC 处于暂停（进给保持）状态 2: CNC 处于运行状态                                                                                                                                                                                                                                                                                                          |
| systemStatus.opr-mode         | 当前工作模式       | int32        | -    | 0: 录入方式 1: 自动方式 2: 无效方式 3: 编辑方式 4: 单步方式 5: 手动方式 8: 手轮方式 9: 机械回零方式 10: 程序回零方式                                                                                                                                                                                                                                                             |
| systemStatus.ready            | 是否准备就绪       | bool         | -    | -                                                                                                                                                                                                                                                                                                                                                                                |
| systemStatus.not-ready-reason | 准备未绪的原因掩码 | int32        | -    | 0x1: 急停信号有效 0x2: 伺服准备未绪 0x4: IO 准备未绪（远程 IO 设备等）                                                                                                                                                                                                                                                                                                           |
| systemStatus.alarms           | 报警列表           | array string | -    | -                                                                                                                                                                                                                                                                                                                                                                                |
| alarms                        | 报警描述信息       | string       | m    | prm-switch: 参数开关报警（系统参数开关或伺服参数开关）  reboot：开关机报警 plc：PLC 报警或提示（外部报警）ps：PS 报警（操作错）over-travel：超程报警 over-heat：过热报警 mem：存储器报警 servo：伺服驱动报警 servo-bus：伺服总线报警 over-workarea：超出工作区报警 io-bus：IO 总线报警  io-module：IO 模块报警 manufacture：机床厂报警 forbid-move：不允许移动的轴发生移动时报警 |
| absolute                      | 绝对坐标           | double       | m    | X Y Z                                                                                                                                                                                                                                                                                                                                                                            |
| machine                       | 机械坐标           | double       | m    | X Y Z                                                                                                                                                                                                                                                                                                                                                                            |
| relative                      | 相对坐标           | double       | m    | X Y Z                                                                                                                                                                                                                                                                                                                                                                            |
| cycleTime                     | 加工时间           | int32        | m    | total: 加工时间（单位：秒） cur: 循环时间（单位：秒）                                                                                                                                                                                                                                                                                                                            |
| workCounts                    | 加工计数           | int32        | m    | total: 总加工计数 batch: 单批加工计数                                                                                                                                                                                                                                                                                                                                            |
| workCountGoals                | 目标件数           | int32        | m    | total: 总目标件数 batch: 单批目标件数                                                                                                                                                                                                                                                                                                                                            |
| feedOverride                  | 当前进给倍率       | double       | -    | -                                                                                                                                                                                                                                                                                                                                                                                |
| jogOverride                   | 当前手动倍率       | double       | -    | -                                                                                                                                                                                                                                                                                                                                                                                |
| rapidOverride                 | 当前快速倍率       | double       | -    | -                                                                                                                                                                                                                                                                                                                                                                                |
| handleOverride                | 当前手轮/单步档位  | double       | -    | -                                                                                                                                                                                                                                                                                                                                                                                |
| spindleOverride               | 当前主轴倍率       | double       | m    | 1：主轴1 2：主轴2 3：主轴3                                                                                                                                                                                                                                                                                                                                                       |
| spSpeed                       | 当前主轴转速       | double       | m    | 1：主轴1 2：主轴2 3：主轴3                                                                                                                                                                                                                                                                                                                                                       |
| feedrate                      | 实际进给速率       | double       | -    | -                                                                                                                                                                                                                                                                                                                                                                                |
| g54                           | G54工件坐标系      | double       | m    | X Y Z                                                                                                                                                                                                                                                                                                                                                                            |
| g55                           | G55工件坐标系      | double       | m    | X Y Z                                                                                                                                                                                                                                                                                                                                                                            |
| g56                           | G56工件坐标系      | double       | m    | X Y Z                                                                                                                                                                                                                                                                                                                                                                            |
| g57                           | G57工件坐标系      | double       | m    | X Y Z                                                                                                                                                                                                                                                                                                                                                                            |
| g58                           | G58工件坐标系      | double       | m    | X Y Z                                                                                                                                                                                                                                                                                                                                                                            |
| g59                           | G59工件坐标系      | double       | m    | X Y Z                                                                                                                                                                                                                                                                                                                                                                            |
| workCoorsCur                  | 当前工件坐标系     | string       | -    | -                                                                                                                                                                                                                                                                                                                                                                                |
| vars                          | 宏变量             | double       | m    | 宏变量编号                                                                                                                                                                                                                                                                                                                                                                       |
| progCur                       | 当前程序           | int32        | -    | -                                                                                                                                                                                                                                                                                                                                                                                |
| progExecStatus                | 程序执行状态       | int32        | m    | O: 程序 O 号 N: 程序 N 号 P: 段落号                                                                                                                                                                                                                                                                                                                                              |

::: tip
主轴数从1开始，根据实际主轴数递增。

vars 宏变量可读写，其他只读。
:::




*CNC 地址示例*

| 地址              | 说明                       |
| ----------------- | -------------------------- |
| systemInfo.type   | 读取加工主程序号           |
| machine.X         | 读取 X 轴坐标              |
| vars.100          | 读写100号宏变量置          |
| feedOverride      | 读取当前进给倍率           |
| alarms.plc        | PLC 报警或提示（外部报警） |
| spindleOverride.1 | 主轴1倍率                  |
| spSpeed.1         | 主轴1转速                  |
| cycleTime.cur     | 循环时间                   |


### PLC 数据

### 地址格式

> AREA ADDRESS\[.BIT]\[.LEN]

| 标识 | 说明                   | 类型 | 权限  |
| ---- | ---------------------- | ---- | ----- |
| X    | DI 输入                | all  | 读    |
| Y    | DO 输出                | all  | 读    |
| F    | NC -> PLC              | all  | 读    |
| G    | PLC -> NC              | all  | 读    |
| R    | PLC 内部控制继电器     | all  | 读/写 |
| S    | PLC 内部特殊标志       | all  | 读    |
| K    | PLC 内部掉电保护继电器 | all  | 读    |
| D    | 数据表                 | all  | 读    |
| TL   | 标号序号               | all  | 读    |


::: tip
目前只支持设置部分 R 区，即 R17000-R17099，并且需要梯图显式允许，梯图必
须将 G138 赋为 181，才能远程修改上述 R 区。
:::

> AREA ADDRESS\[.cur/conf]

| 标识 | 说明   | 类型         | 权限 |
| ---- | ------ | ------------ | ---- |
| T    | 定时器 | int32/uint32 | 读   |
| C    | 计数器 | int32/uint32 | 读   |

::: tip
读取定时器和计数器时，需要指定是设置值还是当前值。
:::

*PLC 常用点位*

| 地址    | 类型   | 说明                                 |
| ------- | ------ | ------------------------------------ |
| X0.0    | bit    | DI  区域，地址0的数据                |
| Y0.0    | bit    | DO 区域，地址0的数据                 |
| D10     | int32  | 数据表 区域，地址10的数据            |
| R17000  | float  | 内部控制继电器 区域，地址17000的数据 |
| D20.24  | string | 数据表 区域，地址20的数据            |
| T0.conf | int32  | 定时器 区域，地址0的设定值数据       |
| T0.cur  | int32  | 定时器 区域，地址0的当前数据         |
