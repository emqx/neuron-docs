# 概览

**支持架构**: amd64, arm/v7

## 设备设置

| 字段    | 说明         |
| ------- | ------------ |
| host    | 设备 IP 地址 |
| port    | 设备端口号   |
| timeout | 连接超时时间 |

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

| tag 标识（地址） | 说明              | 数据类型     | 参数                                                              |
| ---------------- | ----------------- | ------------ | ----------------------------------------------------------------- |
| actf             | 实际进给速度      | int64/uint64 | -                                                                 |
| absolute         | 轴绝对坐标        | int64/uint64 | axis number(.n)                                                   |
| machine          | 轴机械坐标        | int64/uint64 | axis number(.n)                                                   |
| relative         | 轴相对坐标        | int64/uint64 | axis number(.n)                                                   |
| distance         | 轴剩余距离坐标    | int64/uint64 | axis number(.n)                                                   |
| acts             | 实际主轴转速      | int64/uint64 | -                                                                 |
| skip             | 轴跳过坐标        | int64/uint64 | axis number(.n)                                                   |
| srvdelay         | 轴伺服延迟量      | int64/uint64 | axis number(.n)                                                   |
| accdecdly        | 轴加速/减速延迟量 | int64/uint64 | axis number(.n)                                                   |
| spcss_srpm       | 转换主轴速度      | int64/uint64 | -                                                                 |
| spcss_sspm       | 指定表面速度      | int64/uint64 | -                                                                 |
| spcss_smax       | 夹具最大主轴速度  | int64/uint64 | -                                                                 |
| spload           | 主轴负载          | int32/uint32 | spindle number(.n)                                                |
| spmaxrpm         | 主轴最大转速比率  | int32/uint32 | spindle number(.n)                                                |
| spgear           | 主轴齿轮比        | int32/uint32 | spindle number(.n)                                                |
| runState         | 运行状态          | int32/uint32 | 1：故障 2：运行 3：空闲                                           |
| controlMode      | 控制模式          | int32/uint32 | 0：MID 1：AUTO 3：EDIT 5：JOB 8：INC feed 9：REFerence 10：ReMoTe |
| programMain      | 加工程序名        | string       | -                                                                 |
| mainProgramNo    | 主程序号          | int16/uint16 | -                                                                 |
| subProgramNo     | 子程序号          | int16/uint16 | -                                                                 |
| alarm            | 报警ID            | int32/uint32 | 0：WS 1：PW 2：IO 3：PS                                           |
| alarmMsg         | 报警内容          | string       | alarmMsg.(1~16)                                                   |
| param            | 参数              | int32/uint32 | param.(number).(.n)                                               |



轴数从1开始，根据数据轴数递增。



*CNC 地址示例*

| 地址         | 说明                                     |
| ------------ | ---------------------------------------- |
| actf         | 读取 actual feed rate                    |
| absolute.1   | 读取第1个 axis 的 absolute position      |
| machine.3    | 读取第3个 axis 的 machine position       |
| spload.1     | 读取第1个 spindle 的 load information    |
| spmaxrpm.3   | 读取第3个 spindle 的 maximum r.p.m ratio |
| param.6712.0 | 总加工件数                               |
| param.6711.0 | 加工件数                                 |
| param.6750.0 | 上电时间                                 |
| param.6753.0 | 切削时间                                 |


### PMC 数据

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