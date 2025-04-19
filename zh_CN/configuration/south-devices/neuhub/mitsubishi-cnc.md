# MITSUBISHI CNC

Neuron 可以使用 Neuron HUB 驱动和 NEURON HUB Windows 程序，间接访问三菱 M70,M80 CNC 系统。以实时采集多种设备运行数据，包括程序名，进给速度，运行状态，功耗, PLC 点位, 全局变量，参数等。

## NEURON HUB Windows 程序参数

| 参数      | 说明                                       |
| --------- | ------------------------------------------ |
| Node Name | 节点名称，必须唯一，用来区分多个节点       |
| Host      | 需要连接 CNC 设备 IP 地址                  |
| cnctype   | 设备类型，目前支持 M700L,M700M,M800L,M800M |
| cardno    | 控制卡号，默认填写 1                       |


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
* ARRAY_DOUBLE 


## CNC 数据

> address\[.m]\[.n]\[.k]\[.j]

| tag 标识（地址）    | 说明         | 数据类型     | 参数    | 备注                                                                                       |
| ------------------- | ------------ | ------------ | ------- | ------------------------------------------------------------------------------------------ |
| systemStatus        | 当前运行状态 | int32        | m       | m：0 对刀状态 1 自动状态 2 自动运行状态 3 自动暂停状态                                     |
| spindleInfo         | 主轴状态     | int64        | m n     | m：轴编号 n：0 增益 1：   位置偏差 2：电机转速 3：负载 5：报警1 6：报警2 7：报警3 8：报警4 |
| servoInfo           | 伺服轴状态   | int64        | m n     | m：轴编号 n：0 增益 1：   位置偏差 2：电机转速 3：电流 6：负载                             |
| work                | 工件坐标     | double       | m       | m：轴编号                                                                                  |
| machine             | 机械坐标     | double       | m       | m：轴编号                                                                                  |
| relative            | 相对坐标     | double       | m       | m：轴编号                                                                                  |
| distance            | 剩余距离     | double       | m       | m：轴编号                                                                                  |
| feedSpeed           | 进给速度     | double       | m       | 0 FA 1 FM 2 FS 3 Fc 4 FE                                                                   |
| param               | 参数         | ARRAY_STRING | m n k j | m: 轴编号 n：组号 k： 参数号 j：参数个数                                                   |
| toolOffset          | 刀补         | double       | m n k   | m：类型  n：刀补类型 k：编号                                                               |
| alarm               | 报警         | ARRAY_STRING | -       | -                                                                                          |
| runTime             | 自动运行时间 | int32        | -       | -                                                                                          |
| startTime           | 自动开始时间 | int32        | -       | -                                                                                          |
| aliveTime           | 上电时间     | int32        | -       | -                                                                                          |
| estimateTime        | 外部集成时间 | int32        | m       | 1：定时器1 2：定时器2                                                                      |
| commonVar           | 全局变量     | double       | m       | 变量编号                                                                                   |
| localVar            | 局部变量     | double       | m n     | m:变量编号 n: 等级                                                                         |
| invalidStatus       | 无效状态     | int32        | -       | -                                                                                          |
| commandStatus       | 操作命令状态 | int32        | -       | -                                                                                          |
| cuttingMode         | 切削模式     | int32        | -       | -                                                                                          |
| mainProgram         | 主程序       | int32        | -       | -                                                                                          |
| subProgram          | 子程序       | int32        | -       | -                                                                                          |
| mainSeqNum          | 主序列号     | int32        | -       | -                                                                                          |
| subSeqNum           | 子序列号     | int32        | -       | -                                                                                          |
| programCurrentBlock | 当前程序断   | string       | -       | -                                                                                          |
| powerConsumption    | 功耗         | ARRAY_DOUBLE | m       | m：轴编号       [0]：系统总功耗 [1]：伺服功耗 [3]：主轴功耗                                |
| toolLife            | 刀具寿命     | ARRAY_STRING | m n     | m：组编号 n：刀具编号                                                                      |

::: tip
commonVar 可读写，其他只读。
:::




*CNC 地址示例*

| 地址              | 说明                |
| ----------------- | ------------------- |
| systemStatus.0    | 对刀状态            |
| machine.1         | 读取轴1坐标         |
| commonVar.100     | 读写 100 号全局变量 |
| feedSpeed.0       | 读取当前进给速度    |
| alarm             | 当前报警列表        |
| param.1.30.8002.1 | 加工件数            |


### PLC 数据

| 标识 | 说明                     | 类型            | 权限 |
| ---- | ------------------------ | --------------- | ---- |
| B    | 计数器（固定计数器）     | bit/16bit/32bit | 读写 |
| C    | 计数器线圈               | bit/16bit/32bit | 读写 |
| D    | 数据寄存器               | 16bit/32bit     | 读写 |
| E    | 特殊继电器               | bit/16bit/32bit | 读写 |
| F    | 报警消息临时内存         | bit/16bit/32bit | 读写 |
| G    | 临时存储器               | bit/16bit/32bit | 读写 |
| I    | 设备                     | bit/16bit/32bit | 读写 |
| J    | J设备                    | bit/16bit/32bit | 读写 |
| L    | 锁存继电器（备份存储器） | bit/16bit/32bit | 读写 |
| M    | 临时存储器               | bit/16bit/32bit | 读写 |
| Q    | Q设备                    | bit/16bit/32bit | 读写 |
| R    | 文件寄存器               | 16bit/32bit     | 读写 |
| SM   | 特殊继电器（用于链接）   | bit/16bit/32bit | 读写 |
| SD   | 特殊寄存器               | 16bit/32bit     | 读写 |
| ST   | 累积定时器               | 16bit/32bit     | 读写 |
| SW   | 特殊寄存器（用于链接）   | 16bit/32bit     | 读写 |
| T    | 10ms定时器单元           | bit/16bit/32bit | 读写 |
| U    | 输入信号线至可编程控制器 | bit/16bit/32bit | 读写 |
| V    | V 设备                   | bit/16bit/32bit | 读写 |
| W    | 输入信号至可编程控制器   | bit/16bit/32bit | 读写 |
| X    | 输入信号                 | bit/16bit/32bit | 读写 |
| Y    | 输出信号                 | bit/16bit/32bit | 读写 |
| ZR   | 文件寄存器               | 16bit/32bit     | 读写 |

::: tip
地址输入形式为 16 进制。
:::


*PLC 常用点位*

| 地址   | 类型   | 说明                                                                                                                                                                                      |
| ------ | ------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| R69    | uint16 | PLC R 区域，地址69的数据，其值为EMG急停标志（65519 ON 65535 OFF）                                                                                                                         |
| R2500  | uint16 | PLC R 区域，地址2500的数据，其值为进给倍率                                                                                                                                                |
| R7008  | uint16 | PLC R 区域，地址7008的数据，其值为主轴倍率                                                                                                                                                |
| R6506  | uint32 | PLC R 区域，地址6506的数据，其值为主轴实际旋转转速                                                                                                                                        |
| R7000  | uint32 | PLC R 区域，地址7000~7001的数据，其值为指令设定主轴转速                                                                                                                                   |
| R6525  | uint16 | PLC R 区域，地址6525的数据，其值为主轴负载                                                                                                                                                |
| R6529  | uint16 | PLC R 区域，地址6529的数据，其值为主轴报警编号                                                                                                                                            |
| R606   | uint32 | PLC R 区域，地址606 ~ 607 的数据，其值为工件加工数当前值                                                                                                                                  |
| R608   | uint32 | PLC R 区域，地址608 ~ 609 的数据，其值为工件加工数最大值                                                                                                                                  |
| R11824 | uint32 | PLC R 区域，地址11824 ~ 11825 的数据，其值为使用中刀具组号                                                                                                                                |
| R11826 | uint32 | PLC R 区域，地址11826 ~ 11827 的数据，其值为使用中刀具刀号号                                                                                                                              |
| R11830 | uint32 | PLC R 区域，地址11830 ~ 11831 的数据，其值为使用中刀具使用累计时间数据                                                                                                                    |
| R11832 | uint32 | PLC R 区域，地址11832 ~ 11833 的数据，其值为 使用中刀具寿命设定时间数据                                                                                                                   |
| XC00   | uint16 | PLC X 区域，地址 C00 ~ C0F 的数据，其值为控制模式（1 JOG 模式中 2 手轮模式中 4 增量模式中 8 手动任意进给模式中 16 参考点返回模式中 32 自动初始设定模式中 256 内存模式中 2048 MDI 模式中） |
| XC12   | bit    | PLC X 区域，地址 C12 的数据，其值为自动运行中                                                                                                                                             |
| XC13   | bit    | PLC X 区域，地址 C13 的数据，其值为自动运行启动中                                                                                                                                         |
| XC14   | bit    | PLC X 区域，地址 C14 的数据，其值为自动运行暂停中                                                                                                                                         |
| XC15   | bit    | PLC X 区域，地址 C15 的数据，其值为复位中                                                                                                                                                 |
| XC20   | bit    | PLC X 区域，地址 C20 的数据，其值为快速进给中                                                                                                                                             |
| XC21   | bit    | PLC X 区域，地址 C21 的数据，其值为切削进给中                                                                                                                                             |
| XC22   | bit    | PLC X 区域，地址 C22 的数据，其值为攻丝中                                                                                                                                                 |
| XC23   | bit    | PLC X 区域，地址 C23 的数据，其值为螺纹切削中                                                                                                                                             |
| XC24   | bit    | PLC X 区域，地址 C24 的数据，其值为同步进给中                                                                                                                                             |
| XC25   | bit    | PLC X 区域，地址 C25 的数据，其值为恒速中                                                                                                                                                 |
| XC26   | bit    | PLC X 区域，地址 C26 的数据，其值为跳跃中                                                                                                                                                 |
| XC27   | bit    | PLC X 区域，地址 C27 的数据，其值为参考点返回中                                                                                                                                           |

::: tip
PLC 数据表可以查看三菱官网提供的《PLC开发说明书-M800/M80/E80系列》，获取更多系统运行数据。
:::



