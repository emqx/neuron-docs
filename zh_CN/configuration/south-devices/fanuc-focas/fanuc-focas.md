# Fanuc Focas Ethernet

Neuron FOCAS 驱动支持使用 FOCAS2 协议对 FANUC 各类型设备（包含多通道设备）进行数据获取和写入，支持坐标，运行状态，报警，操作信息，宏变量，参数，诊断数据，程序数据，刀偏，刀具，刀具寿命，PMC等。

**支持架构**: amd64, arm/v7

## 设备设置

| 字段    | 说明                          |
| ------- | ----------------------------- |
| host    | 设备 IP 地址                  |
| port    | 设备端口号, 默认 8193         |
| timeout | 连接超时时间， 默认 3000 毫秒 |

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

## CNC 数据

### 地址格式

> address\[.m]\[.n]\[.l]\[@p]

address 最多可以支持3个参数，@ 指定 address 所在通道。


| tag 标识（地址）      | 说明                 | 数据类型            | 参数                                        | 备注                                                                                                                                      |
| --------------------- | -------------------- | ------------------- | ------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------- |
| actf                  | 实际进给速度         | int64/uint64        | -                                           |                                                                                                                                           |
| absolute.m            | 轴绝对坐标           | int64/uint64        | 轴序号                                      | 计算了刀偏，和 CNC 界面显示可能不一致                                                                                                     |
| absolute2.m           | 轴绝对坐标2          | int64/uint64        | 轴序号                                      | 数据与 CNC 界面一致                                                                                                                       |
| machine.m             | 轴机械坐标           | int64/uint64        | 轴序号                                      |                                                                                                                                           |
| relative.m            | 轴相对坐标           | int64/uint64        | 轴序号                                      | 计算了刀偏，和 CNC 界面显示可能不一致                                                                                                     |
| relative2.m           | 轴相对坐标2          | int64/uint64        | 轴序号                                      | 数据与 CNC 界面一致                                                                                                                       |
| distance.m            | 轴剩余距离坐标       | int64/uint64        | 轴序号                                      |                                                                                                                                           |
| acts                  | 实际主轴转速         | int64/uint64        | -                                           |                                                                                                                                           |
| acts2.m               | 实际主轴转速         | int64/uint64        | 主轴序号                                    |                                                                                                                                           |
| skip                  | 轴跳过坐标           | int64/uint64        | 轴序号                                      |                                                                                                                                           |
| srvdelay              | 轴伺服延迟量         | int64/uint64        | 轴序号                                      |                                                                                                                                           |
| accdecdly             | 轴加速/减速延迟量    | int64/uint64        | 轴序号                                      |                                                                                                                                           |
| spcss_srpm            | 转换主轴速度         | int64/uint64        | -                                           |                                                                                                                                           |
| spcss_sspm            | 指定表面速度         | int64/uint64        | -                                           |                                                                                                                                           |
| spcss_smax            | 夹具最大主轴速度     | int64/uint64        | -                                           |                                                                                                                                           |
| movrlap_input.m       | 输入重叠运动值       | int64/uint64        | 轴序号                                      |
| movrlap_output.m      | 输出重叠运动值       | int64/uint64        | 轴序号                                      |
| spload.m              | 主轴负载             | int32/uint32        | 主轴序号                                    |                                                                                                                                           |
| spmaxrpm.m            | 主轴最大转速比率     | int32/uint32        | 主轴序号                                    |                                                                                                                                           |
| spgear.m              | 主轴齿轮比           | int32/uint32        | 主轴序号                                    |                                                                                                                                           |
| runState              | 运行状态             | int32/uint32        | -                                           | 1：故障 2：运行 3：空闲                                                                                                                   |
| controlMode           | 控制模式             | int32/uint32        | -                                           | 0：MID 1：AUTO 3：EDIT 5：JOB 8：INC feed 9：REFerence 10：ReMoTe                                                                         |
| programMain           | 加工程序名           | string              | -                                           |                                                                                                                                           |
| mainProgramNo         | 主程序号             | int16/uint16        | -                                           |                                                                                                                                           |
| subProgramNo          | 子程序号             | int16/uint16        | -                                           |                                                                                                                                           |
| alarm                 | 报警ID               | int32/uint32        | -                                           | 0：WS 1：PW 2：IO 3：PS                                                                                                                   |
| alarmMsg.m            | 报警内容             | string              | m 为序号                                    | 取值范围为1~16                                                                                                                            |
| param.m.n             | 参数                 | int32/uint32        | m 为参数 ID，n 为轴数                       | 如果参数不是轴相关则设置为0                                                                                                               |
| alarmMsg2.m.n         | 报警内容             | int16/uint16/string | m 为序号, n 为 值参数                       | m 取值范围为1~16， n=0 报警类型 n=1 报警编号 n=2 报警内容                                                                                 |
| macroType             | 宏变量类型           | int16/uint16        | -                                           |                                                                                                                                           |
| macroInfo.m           | 宏变量信息           | int16/uint16        | n 为值参数                                  | n=0 局部变量数 n=1 公共变量指标                                                                                                           |
| macro.m.n             | 宏变量类型           | int32/uint32        | m 为变量 ID n 为值参数                      | n=0 宏变量值 n=1 小数位数                                                                                                                 |
| paraNum.m             | 参数数量             | int16/uint16        | n 为值参数                                  | n=0 参数最小数目 n=1 参数最大数目 n=3 参数总数                                                                                            |
| pitchInfoNum.m        | 俯仰误差补偿数据数量 | int16/uint16        | -                                           | -                                                                                                                                         |
| pitch.m               | 俯仰误差补偿数据     | int8/uint8          | m 为序号                                    | -                                                                                                                                         |
| tool.m.n              | 刀具数据             | int64/uint64        | m 为刀具编号，n 为值变量                    | m 从 1 开始，n=0 刀具号 n=1 使用次数 n=2 刀具寿命 n=3 预警寿命                                                                            |
| toolf2.m.n            | 刀具数据             | int64/uint64        | m 为刀具编号，n 为值变量                    | m 从 1 开始，n=0 刀具号 n=1 使用次数 n=2 刀具寿命 n=3 预警寿命                                                                            |
| toolOffset.m.n        | 刀偏数据             | int32/uint32        | m 为刀具编号，n 为刀偏类型                  | m 从 1 开始，n 和具体的系统型号有关，以 0i-D 为例，n=0 半径磨损， n=1 半径形状，n=2 长度磨损, n=3 长度形状                                |
| toolOffsetRange.m.n.l | 刀偏数据设定范围     | int32/uint32        | m 为刀具编号，n 为刀偏类型，l 为 值类型     | m 从 1 开始，n 和具体的系统型号有关，以 0i-D 为例，n=0 半径磨损， n=1 半径形状，n=2 长度磨损, n=3 长度形状, l=0 最小值 l=1 最大值 l=2状态 |
| toolOffsetInfo.m      | 刀偏信息             | int16/uint16        | m 为刀偏类型                                | m=0 内存类型， m=1 可用刀偏数量，n=2 刀偏类型                                                                                             |
| wkcdsfms.m            | 工件坐标偏移测量值   | int32/uint32        | 轴序号                                      | M 系列不支持                                                                                                                              |
| wkcdshft.m            | 工件坐标偏移值       | int32/uint32        | 轴序号                                      | M 系列不支持                                                                                                                              |
| wksftRange.m          | 工件坐标偏移值范围   | int32/uint32        | n 为值变量                                  | m=0 最小值， m=1 最大值， m=2 类型，       M 系列不支持                                                                                   |
| zofs                  | 工件零点偏移值       | int32/uint32        | -                                           | -                                                                                                                                         |
| zofsInfoNum           | 工件零点偏移值数量   | int32/uint32        | -                                           | -                                                                                                                                         |
| zofsRange.m.n.l       | 件零点偏移设定范围   | int32/uint32        | m 为工件坐标偏移编号，n 为轴号，l 为 值类型 | l=0 最小值 l=1 最大值 l=2状态                                                                                                             |
| blkCount              | 块计数器             | int32/uint32        | -                                           | -                                                                                                                                         |
| execProg              | 当前真正执行的程序段 | string              | -                                           | -                                                                                                                                         |
| mdiPntr               | MDI执行信息          | int32/uint32        | -                                           | 设备处于 MDI 模式时才可读                                                                                                                 |
| programMainFile       | 主程序文件信息       | string              | -                                           | -                                                                                                                                         |
| pdfCurDir             | 当前程序目录         | string              | -                                           | -                                                                                                                                         |
| pdfDrive.m            | 程序设备信息         | string              | m 为 设备序号                               | m 从1开始                                                                                                                                 |
| progInfo.m            | 程序管理信息         | int32/uint32        | m 为值参数                                  | m=0 已注册程序数 m=1 可使用程序数 m=2 已用内存字符数 m=2 未用内存的字符数                                                                 |
| seqNum                | 程序序列号           | int32/uint32        | -                                           | -                                                                                                                                         |
| exaxisName.m.n        | 控制轴和主轴名       | string              | m 为轴类型，n 为序号                        | m=0 控制轴, m=1 主轴， n 从1开始                                                                                                          |
| axisName.m            | 控制轴名             | int8/uint8          | m 为序号                                    | m 从1开始                                                                                                                                 |
| hndintrpt.m.n         | 手轮中断值           | int32/uint32        | m 为类型，n 为序号                          | m =0 输入 m=1 输出，n 从1开始                                                                                                             |
| spdlName.m            | 主轴名               | int8/uint8          | m  为序号                                   | m 从1开始                                                                                                                                 |
| spmeter.m.n           | 主轴负载百分比       | int32/uint32        | m 为类型，n 为序号                          | m=0 主轴负载 m=1 主轴电机负载, n 为序号                                                                                                   |
| svmeter.m             | 伺服负载百分比       | int32/uint32        | m 为序号                                    | m 为序号                                                                                                                                  |
| almhisno              | 历史报警数           | int16/uint16        | -                                           | -                                                                                                                                         |
| almhistry.m.n         | 历史报警内容         | int16/uint16/string | m 为序号, n 为 值参数                       | m 从1开始， n=0 报警类型 n=1 报警编号 n=2 报警内容                                                                                        |
| omhisno               | 历史额外操作信息数   | int16/uint16        | -                                           | -                                                                                                                                         |
| omhistry.m.n          | 历史额外操作信息内容 | int16/uint16/string | m 为序号, n 为 值参数                       | m 从1开始， n=0 显示标志 n=1 操作信息编号 n=2 操作信息内容                                                                                |
| ophisno               | 历史操作信息数       | int16/uint16        | -                                           | -                                                                                                                                         |
| ophistry.m.n          | 历史操作信息内容     | int16/uint16        | m 为序号, n 为 值参数                       | m 从1开始                                                                                                                                 |
| timer.m.n             | 日期时间             | int16/uint16        | m 为类型, n 为 值参数                       | m=0 日期， n=0 年， n=1 月， n=2 日；m=1 时间， n=0 时， n=1 分， n=2 秒                                                                  |
| diagdata.m.n          | 诊断数据             | int32/uint32        | m 为诊断号, n 为 值参数                     | n = 0 诊断值，n=1 小数点                                                                                                                  |
| opmsg.m.n             | 当前操作信息         | int16/uint16/string | m 为序号, n 为 值参数                       | m 从1开始，n = 0 类型，n=1 编号，n=2 内容                                                                                                 |
| tlGrpinfo.m.n         | 刀具寿命管理信息     | int32/uint32        | m 为刀具组号, n 为 值参数                   | m 从1开始，n = 0 刀具数量，n=1 剩余刀具数量，n=2 刀具寿命，n=3 刀具已使用寿命, n=6， 刀具预警寿命                                         |

::: tip
轴数从1开始，根据实际轴数递增。
使用刀具寿命管理功能，需要开启设备相应的参数。
参数地址不设置 @p，默认为通道1。
:::

*CNC 地址示例*

| 地址            | 说明                                       |
| --------------- | ------------------------------------------ |
| actf            | 读取 actual feed rate                      |
| absolute.1      | 读取第1个 axis 的 absolute position        |
| absolute.1@2    | 读取通道2的第1个 axis 的 absolute position |
| machine.3       | 读取第3个 axis 的 machine position         |
| spload.1        | 读取第1个 spindle 的 load information      |
| spmaxrpm.3      | 读取第3个 spindle 的 maximum r.p.m ratio   |
| param.6712.0    | 总加工件数                                 |
| param.6711.0    | 加工件数                                   |
| param.6750.0    | 上电时间                                   |
| param.6753.0    | 切削时间                                   |
| macro.3142.0    | 宏变量#3142的值                            |
| tool.1.0        | 编号1刀具的刀具号                          |
| tool.1.1        | 编号1刀具的已使用次数                      |
| tool.1.2        | 编号1刀具的总寿命                          |
| tool.1.3        | 编号1刀具的预警寿命                        |
| diagdata.1333.3 | 诊断1333号的数据                           |
| tlGrpinfo.1.1   | 刀具寿命组1的剩余刀具寿命                  |
| toolOffset.1.2  | 刀具编号1的长度磨损                        |



## PMC 数据

### 地址格式

> AREA ADDRESS\[.BIT]\[.LEN]\[@p]

| 标识 | 说明                            | 类型 | 权限 |
| ---- | ------------------------------- | ---- | ---- |
| A    | message demand                  | all  | 读写 |
| C    | counter                         | all  | 读写 |
| D    | data table                      | all  | 读写 |
| E    | extended relay                  | all  | 读写 |
| F    | signal to CNC -> PMC            | all  | 只读 |
| G    | signal to PMC -> CNC            | all  | 读写 |
| K    | keep relay                      | all  | 读写 |
| M    | input signal from other device  | all  | 读写 |
| N    | output signal from other device | all  | 读写 |
| R    | internal relay                  | all  | 读写 |
| T    | changeable timer                | all  | 读写 |
| X    | signal to machine -> PMC        | all  | 只读 |
| Y    | signal to PMC -> machine        | all  | 读写 |

*PMC 点位示例*

| 地址 | 类型                                                           | 说明                                                                             |
| ---- | -------------------------------------------------------------- | -------------------------------------------------------------------------------- |
| A0   | uint8/int8/uint16/int16/uint32/int32/int64/uint64/float/double | PMC **message demand** 区域，地址0的数据                                         |
| A0.1 | bit                                                            | PMC **message demand** 区域，地址0的的字节，第1个 bit 位                         |
| A0.0 | bit                                                            | PMC **message demand** 区域，地址0的字节，第0个 bit 位                           |
| A0.2 | string                                                         | PMC **message demand** 区域，地址0开始，长度为2的字符串                          |
| D0.2 | string                                                         | PMC **data table** 区域，地址0开始，长度为2的字符串                              |
| D0.7 | bit                                                            | PMC **data table** 区域，地址0的字节，第7个 bit 位                               |
| G12  | uint8                                                          | PMC **signal to PMC -> CNC** 区域，地址12的数据，255-(G12)，其值代表当前进给倍率 |
| G30  | uint16                                                         | PMC **signal to PMC -> CNC** 区域，地址30的数，其值为主轴倍率                    |