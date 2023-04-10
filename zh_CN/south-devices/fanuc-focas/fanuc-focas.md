# 概览

**支持架构**: amd64, arm/v7

## 设备设置

| 字段    | 说明         |
| ------- | ------------ |
| host    | 设备 IP 地址   |
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

| tag 标识（地址） | 说明                                         | 数据类型     | 参数               |
| --------------- | -------------------------------------------- | ------------ | ------------------ |
| actf            | actual feed rate                             | int64/uint64 | -                  |
| absolute        | absolute position data of axis               | int64/uint64 | axis number(.n)    |
| machine         | machine position data of axis                | int64/uint64 | axis number(.n)    |
| relative        | relative position data of axis               | int64/uint64 | axis number(.n)    |
| distance        | distance to go of axis                       | int64/uint64 | axis number(.n)    |
| acts            | actual rotational speed of the spindle       | int64/uint64 | -                  |
| skip            | skipped position of axis                     | int64/uint64 | axis number(.n)    |
| srvdelay        | servo delay amount of axis                   | int64/uint64 | axis number(.n)    |
| accdecdly       | acceleration/deceration delay amount of axis | int64/uint64 | axis number(.n)    |
| spcss_srpm      | converted spindle speed                      | int64/uint64 | -                  |
| spcss_sspm      | specified surface speed                      | int64/uint64 | -                  |
| spcss_smax      | clamp of maxmum spindle speed                | int64/uint64 | -                  |
| movrlap_input   | input overlapped motion value                | int64/uint64 | axis number(.n)    |
| movrlap_output  | output overlapped motion value               | int64/uint64 | axis number(.n)    |
| spload          | load information of the serial spindle       | int32/uint32 | spindle number(.n) |
| spmaxrpm        | maximum r.p.m ratio of serial spindle        | int32/uint32 | spindle number(.n) |
| spgear          | gear ratio of the serial spindle             | int32/uint32 | spindle number(.n) |

*CNC 地址示例*

| 地址       | 说明                                  |
| ---------- | ------------------------------------- |
| actf       | 读取 actual feed rate                 |
| absolute.1 | 读取第1个 axis 的 absolute position      |
| machine.3  | 读取第3个 axis 的 machine position       |
| spload.1   | 读取第1个 spindle 的 load information    |
| spmaxrpm.3 | 读取第3个 spindle 的 maximum r.p.m ratio |

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

| 地址 | 类型                                                         | 说明                                                    |
| ---- | ------------------------------------------------------------ | ------------------------------------------------------- |
| A0   | uint8/int8/uint16/int16/uint32/int32/int64/uint64/float/double | PMC **message demand** 区域，地址0的数据                |
| A0.1 | bit                                                          | PMC **message demand** 区域，地址0的的字节，第1个 bit 位  |
| A0.0 | bit                                                          | PMC **message demand** 区域，地址0的字节，第0个 bit 位    |
| A0.2 | string                                                       | PMC **message demand** 区域，地址0开始，长度为2的字符串 |
| D0.2 | string                                                       | PMC **data table** 区域，地址0开始，长度为2的字符串     |
| D0.7 | bit                                                          | PMC **data table** 区域，地址0的字节，第7个 bit 位        |