# Neuron 驱动地址格式

## 总则

本文档描述了 Neuron 与各种工业协议驱动程序之间的标签地址格式。每个 Neuron 驱动程序都有自己的地址格式，在配置过程中会被解析，用于机器或设备的通信。

## Allen-Bradley PLC2（半双工）

### 一般资讯

| 設定            | 参数            |
| -------------- | --------------- |
| 运行时模块     | neuron_o_df1hp2 |
| 驱动名称       | df1hp2          |
| 协议           | DF1（半双工）   |
| 物理接口       | RS485           |
| 默认设置       | 9600/8/N/1      |

### 地址格式

> <span style="font-family:sans-serif; font-size:2em;">STN!DST!ADDR</span>

**STN** 为从站设备号

**DST** 为目的节点（CPU）

**ADDR** 是指如下的</u>寄存器</u>地址：

| 类  | 規格  | 範圍      | 描述         |
| --- | ----- | --------- | ------------ |
| 字  | DDDDD | 0 ~ 65535 | 寄存器（字） |

注：由于 1771KG 是直接与 CPU 连接的，所以 STN 和 DST 应设置为同一编号（1771KG 模块的地址）。

例如：16! 16 (从属号码 20 八进制)

**16！16！520**（字 1010 八进制中的从数 20 八进制）。

在 KG 模式下，1771-KG 设置为 8（10 八进制），1785-KE 和 1770-KF2 设置为 0。

## Allen-Bradley PLC5（半双工）

### 一般资讯

| 設定            | 参数            |
| -------------- | --------------- |
| 运行时模块     | neuron_o_df1ph5 |
| 驱动名称       | df1ph5          |
| 协议           | DF1（半双工）   |
| 物理接口       | RS485           |
| 默认设置       | 9600/8/N/1      |

### 地址格式

> <span style="font-family:sans-serif; font-size:2em;">STN!DST!ADDR</span>

**STN** 为从站设备号（KE/KF2 模块地址）

**DST** 为目的节点（CPU）

**ADDR** 是指如下的<u>寄存器</u>地址：

| 类  | 規格  | 範圍      | 描述         |
| --- | ----- | --------- | ------------ |
| 字  | DDDDD | 0 ~ 65535 | 寄存器（字） |

注：KE 或 KF2 模块插入它的地址作为源，这个地址将是 PLC5 中使用的数据文件号。

例如：28！16（ KE/KF2 模块号 34 八进制，目的节点 = CPU 号 20 八进制）。

**28！16！10** 表示文件 N28 中的字 10 在从机号 20（八进制）。

在 KG 模式下，1771-KG 设置为 8（10 八进制），1785-KE 和 1770-KF2 设置为 0。

## Schneider TSX7 SCM (Modbus RTU)

### 一般资讯

| 設定            | 参数            |
| -------------- | --------------- |
| 运行时模块     | neuron_o_tsxmbr |
| 驱动名称       | tsxmbr          |
| 协议           | Modbus RTU      |
| 物理接口       | RS232           |
| 默认设置       | 9600/8/N/1      |

### 地址格式

> <span style="font-family:sans-serif; font-size:2em;">STN!ADDR</span>

**STN** 为从站设备号（CPU）（1 – 247）

**ADDR** 是指如下的<u>寄存器</u>地址：

| 类  |     | 規格  | 範圍      | 描述         |
| --- | --- | ----- | --------- | ------------ |
| 字  | W   | DDDDD | 0 ~ 32767 | 寄存器（字） |

例如：**10！W100** 表示从站 10 中的字 100。

## Schneider TSX7 SCM (Modbus TCP)

### 一般资讯

| 設定            | 参数             |
| -------------- | --------------- |
| 运行时模块     | neuron_o_tsxmbt |
| 驱动名称       | tsxmbt          |
| 协议           | Modbus TCP      |
| 物理接口       | 以太网          |
| 默认设置       | 端口：502       |

### 地址格式

> <span style="font-family:sans-serif; font-size:2em;">ADDR</span>

**ADDR** 是指如下的寄存器地址：

| 类  |     | 規格  | 範圍      | 描述         |
| --- | --- | ----- | --------- | ------------ |
| 字  | W   | DDDDD | 0 ~ 32767 | 寄存器 |

例如：**W4000** 表示字地址 4000。

## Schneider Telemecanique UNI-TE

### 一般资讯

| 設定            | 参数             |
| -------------- | --------------- |
| 运行时模块     | neuron_o_unite                                                                     |
| 驱动名称       | unite                                                                              |
| 协议           | TSX SCM 2161（Uni-Telway），直接在 V4（或更高版本） CPU 上的内置 UNI-TE 端口上使用 |
| 物理接口       | RS232                                                                              |
| 默认设置       | 9600/8/N/1                                                                         |

### 地址格式

> <span style="font-family:sans-serif; font-size:2em;">STN!ADDR</span>

**STN** 为从站设备号（Ad0 in CPU）（1 – 31）

**ADDR** 是指如下的<u>寄存器</u>地址：

| 类  |     | 規格  | 範圍      | 描述         |
| --- | --- | ----- | --------- | ------------ |
| 字  | W   | DDDDD | 0 ~ 32767 | 寄存器（字） |

例如：**1！W100** 表示从站 1 中的字 100。

## ABB SattControl Comli

### 一般资讯

| 設定            | 参数            |
| -------------- | -------------- |
| 运行时模块     | neuron_o_comli |
| 驱动名称       | comli          |
| 协议           | COMLI          |
| 物理接口       | RS232          |
| 默认设置       | 9600/8/N/1     |

### 地址格式

> <span style="font-family:sans-serif; font-size:2em;">STN!ADDR</span>

**STN** 为从站设备号（CPU）（1 – 247）

**ADDR** 是指如下的<u>寄存器</u>地址：

| 类  |     | 規格  | 範圍      | 描述         |
| --- | --- | ----- | --------- | ------------ |
| 字  | W   | DDDDD | 0 ~ 3071 | 寄存器（字） |

例如：**1！R100** 表示从站 1 中的字 100。

## Omron Single HostLink (点对点)

### 一般资讯

| 設定            | 参数            |
| -------------- | --------------- |
| 运行时模块     | neuron_o_omrhls           |
| 驱动名称       | omrhls                    |
| 协议           | Host-Link sysmac c-series |
| 物理接口       | RS232                     |
| 默认设置       | 9600/8/N/1                |

### 地址格式

> <span style="font-family:sans-serif; font-size:2em;">ADDR</span>

**ADDR** 是指如下的<u>寄存器</u>地址：

| 类  |     | 規格  | 範圍      | 描述         |
| --- | --- | ----- | --------- | ------------ |
| 字  | AR  | DDDDD | 0 ~ 4095  | 辅助继电器       |
| 字  | IR  | DDDDD | 0 ~ 4095  | I/O 和内部继电器 |
| 字  | HR  | DDDDD | 0 ~ 4095  | 保持中继         |
| 字  | LR  | DDDDD | 0 ~ 4095  | 链接中继         |
| 字  | TC  | DDDDD | 0 ~ 255   | 定时器           |
| 字  | DM  | DDDDD | 0 ~ 9999  | 数据寄存器       |

例如：**DM100** 表示 DM 数据存储区的字 100。

## Omron Multiple HostLink (主从模式)

### 一般资讯

| 設定            | 参数             |
| -------------- | --------------- |
| 运行时模块     | neuron_o_omrhls           |
| 驱动名称       | omrhls                    |
| 协议           | Host-Link sysmac c-series |
| 物理接口       | RS232                     |
| 默认设置       | 9600/8/N/1                |

### 地址格式

> <span style="font-family:sans-serif; font-size:2em;">STN!ADDR</span>

**STN** 为站号/模块号（0-31）

**ADDR** 是指如下的<u>寄存器</u>地址：

| 类  |     | 規格  | 範圍     | 描述         |
| --- | --- | ----- | -------- | ------------ |
| 字  | AR  | DDDDD | 0 ~ 4095 | 辅助继电器       |
| 字  | IR  | DDDDD | 0 ~ 4095 | I/O 和内部继电器 |
| 字  | HR  | DDDDD | 0 ~ 4095 | 保持中继         |
| 字  | LR  | DDDDD | 0 ~ 4095 | 链接中继         |
| 字  | TC  | DDDDD | 0 ~ 255  | 定时器           |
| 字  | DM  | DDDDD | 0 ~ 9999 | 数据寄存器       |

例如：**10！DM100** 表示从机 10 的数据存储器中的字 100。

## Omron FINS on TCP

### 一般资讯

| 設定            | 参数             |
| -------------- | ---------------  |
| 运行时模块     | neuron_o_finstc    |
| 驱动名称       | finstc             |
| 协议           | FINS on TCP       |
| 物理接口       | Ethernet RJ45      |
| 默认设置       | 端口：2000          |

### 地址格式

> <span style="font-family:sans-serif; font-size:2em;">ADDR[.BIT]</span>

**ADDR** 是指以 "DM "开头的数据存储器字地址；

**BIT（可选）** 表示比特位。

| 类         | 地址前缀             | 規格         | 範圍           | 描述                       |
| ----      | ------------------- | ---------   | -------------- | ------------------------- |
| 字/比特    | CIO                 | DDDD[.dd]    | 0 ~ 6143      | CIO区域                    |
| 字/比特    | WR                  | DDD[.dd]     | 0 ~ 511       | 工作区              |
| 字/比特    | HR                  | DDD[.dd]     | 0 ~ 511       | 保持位区域          |
| 字/比特    | AR                  | DDD[.dd]     | 0 ~ 959       | 辅助位区0~447只读    |
| 字/比特    | PV (Timer/Counter)        | DDDD[.dd]    | 0 ~ 4095      | 定时器/计数器        |
| 比特       | F (Completion Flag) | DDDD         | 0 ~ 4095      | Completion Flag     |
| 字/比特    | DM                  | DDDDD[.dd]   | 0 ~ 32767     | 数据存储器          |
| 字/比特    | EM0~EM18            | DDDDD[.dd]   | 0 ~ W32767    | 扩展存储器，使用W独立的区域和地址  |

例如：**DM100** 表示数据存储器中的字100。

## Siemens S5 3964R/RK512

### 一般资讯

| 設定            | 参数            |
| -------------- | --------------- |
| 运行时模块     | neuron_o_s539rk |
| 驱动名称       | s539rk          |
| 协议           | 3964R/RK512     |
| 物理接口       | RS232           |
| 默认设置       | 9600/8/N/1      |

### 地址格式

> <span style="font-family:sans-serif; font-size:2em;">ADDR</span>

**ADDR** 为以下地址

DB 是数据块（0 - 999）

DBW（**字偏移量**）是该数据块中的数据字

| 类  |     | 規格  | 範圍      | 描述         |
| --- | --- | ----- | --------- | ------------ |
| 字  | I           | DDDD        | 0 ~ 4095            | 输入       |
| 字  | Q           | DDDD        | 0 ~ 4095            | 输出       |
| 字  | M           | DDDD        | 0 ~ 4095            | 标记存储器 |
| 字  | DB0~999.DBW | DDDDD</br>DDDDD | 0 ~ 65535</br>0 ~ 65535 | 数据存储器 |
| 字  | T           | DDD         | 0 ~ 255             | 定时器     |
| 字  | C           | DDD         | 0 ~ 255             | 计数器     |

例如：DB100（数据块 100）

**DB100.DBW20** (DBddd.DBWddddd) 指数据块 100 中的数据字 20

## Siemens S7 3964R/RK512

### 一般资讯

| 設定            | 参数             |
| -------------- | --------------- |
| 运行时模块     | neuron_o_s739rk |
| 驱动名称       | S739rk          |
| 协议           | 3964R/RK512     |
| 物理接口       | RS232           |
| 默认设置       | 9600/8/N/1      |

### 地址格式

> <span style="font-family:sans-serif; font-size:2em;">ADDR</span>

**ADDR** 为以下地址

**DB** 是数据块（0 - 999）

**DBW**（**字偏移量**）是该数据块中的数据字

| 类  |     | 規格  | 範圍      | 描述         |
| --- | --- | ----- | --------- | ------------ |
| 字节 | I           | DDDD        | 0 ~ 4095            | 输入                               |
| 字节 | Q           | DDDD        | 0 ~ 4095            | 输出                               |
| 字节 | M           | DDDD        | 0 ~ 4095            | 标记存储器                         |
| 字节 | DB0~999.DBW | DDDDD</br>DDDDD | 0 ~ 65535</br>0 ~ 65535 | 数据存储器（必须是偶数字节号）字节 |
| 字节 | T           | DDD         | 0 ~ 255             | 定时器                             |
| 字节 | C           | DDD         | 0 ~ 255             | 计数器                             |

注意：应使用真实的 DBW（如 DBW0、DBW2 等），驱动程序将从 0 开始读取字节，从 2 开始读取字节，它分别从字节 0、字节 2 读取一个字。

例如：DB100（数据块 100）

**DB100.DBW20** (DBddd.DBWddddd) 指数据块 100 中的数据字 20

## Siemens FETCH/WRITE

### 一般资讯

| 設定            | 参数            |
| -------------- | --------------- |
| 运行时模块     | neuron_o_siefw               |
| 驱动名称       | siefw                        |
| 协议           | Siemens Fetch/Write Protocol |
| 物理接口       | 以太网                       |
| 默认设置       | 端口：2200                   |

### 地址格式

> <span style="font-family:sans-serif; font-size:2em;">ADDR</span>

**ADDR** 为以下地址

| 类  |     | 規格  | 範圍      | 描述         |
| --- | --- | ----- | --------- | ------------ |
| 字节 | IW           | DDDD        | 0 ~ 4095            | 输入                               |
| 字节 | QW           | DDDD        | 0 ~ 4095            | 输出                               |
| 字节 | MW           | DDDD        | 0 ~ 4095            | 标记存储器                         |
| 字节 | DB0~999.DBW | DDDDD</br>DDDDD | 0 ~ 65535</br>0 ~ 65535 | 数据存储器（必须是偶数字节号）字节 |
| 字节 | T            | DDD         | 0 ~ 255             | 定时器                             |
| 字节 | C            | DDD         | 0 ~ 255             | 计数器                             |

**DB** 是数据块（0 - 999）

**DBW**（**字偏移量**）是该数据块中的数据字（起始）

注意：协议中有一个限制。DB 只能在 1-255 之间，读写表的起始地址不能超过 DBW2047，然而表的末端可以。但在测试过程中，可以从地址 DBW32766 开始。

注意：在 Simatic PLC 中，您只需定义一个 TCP/IP 连接，用于 FETCH 被动（只读）或 WRITE 被动（只写），在某个端口上监听。目前没有 FETCH/WRITE 被动设置，所以需要两个不同端口的连接，一个用于读，一个用于写。

例如：**DB100.DBW20** (DBddd.DBWddddd) 指数据块 200 中的数据字 20

## Siemens 工业以太网 S7 ISOTCP

### 一般资讯

| 設定            | 参数             |
| -------------- | --------------- |
| 运行时模块     | neuron_o_s7pro        |
| 驱动名称       | s7pro                 |
| 协议           | S7 ISO TCP（S7 协议） |
| 物理接口       | 以太网                |
| 默认设置       | 端口：102             |

### 地址格式

> <span style="font-family:sans-serif; font-size:2em;">ADDR</span>

**ADDR** 为以下地址

注意：DB 是数据块（0 - 999）

DBW（**字偏移量**）是该数据块中的数据字（起始）

| 类  |     | 規格  | 範圍      | 描述         |
| --- | --- | ----- | --------- | ------------ |
| 字节 | IW           | DDDD        | 0 ~ 4095            | 输入                               |
| 字节 | QW           | DDDD        | 0 ~ 4095            | 输出                               |
| 字节 | MW           | DDDD        | 0 ~ 4095            | 标记存储器                         |
| 字节 | DB0~999.DBW | DDDDD</br>DDDDD | 0 ~ 65535</br>0 ~ 65535 | 数据存储器（必须是偶数字节号）字节 |
| 字节 | T            | DDD         | 0 ~ 255             | 定时器                             |
| 字节 | C            | DDD         | 0 ~ 255             | 计数器                             |

例如：**DB100.DBW20** (DBddd.DBWddddd) 指数据块 200 中的数据字 20。

S7P_SCRTSAP 是 S7 协议的源 TSAP（默认值0x0101）

S7P_DSTTSAP 是 S7 协议的目标 TSAP（默认值0x0101）

TSAP由两个字节构成：
第一个字节，01：PG or PC  ; 02: OS   ; 03: Others,such as OPC server,simatic s7 plc
第二个字节，高四位表示rack number ，低四位表示cpu slot

### 提示

Neuron连接S7-1200/1500设备时，只进行基本的数据传输。

不支持其他的PG操作（控制等）。

如果要访问S71500中的数据块，需要对PLC进行一些额外的设置：

1. 只有全局数据块可以被访问。
2. 在块的属性设置中“优化的块访问”必须被关闭。
3. 在PLC的属性设置中，访问级别必须是 "完全访问权限"，连接机制必须勾选“允许来自远程对象的PUT/GET通信访问”。

## Mitsubishi FX0S/FX0N/FX1S/FX1N/FX2

### 一般资讯

| 設定            | 参数             |
| -------------- | --------------- |
| 运行时模块 | neuron_o_fxnpro |
| 驱动名称   | fxnpro          |
| 协议       | RS 命令         |
| 物理接口   | RS232           |
| 默认设置   | 9600/7/E/1      |

### 地址格式

> <span style="font-family:sans-serif; font-size:2em;">ADDR</span>

**ADDR** 是<u>寄存器</u>地址

| 类  |     | 規格  | 範圍      | 描述         |
| --- | --- | ----- | --------- | ------------ |
| 比特  | X   | OOO  | 0 ~ 377     | 输入继电器          |
| 比特  | Y   | OOO  | 0 ~ 377     | 输出继电器          |
| 比特  | M   | DDDD | 0 ~ 7999    | 辅助继电器          |
| 比特  | T   | DDD  | 0 ~ 255     | 计时器继电器        |
| 比特  | C   | DDD  | 0 ~ 255     | 计数器继电器        |
| 比特  | SM  | DDDD | 8000 ~ 9999 | 特殊辅助设备 继电器 |
| 比特  | S   | DDDD | 0 ~ 4095    | 国家                |
| 字    | TN  | DDD  | 0 ~ 255     | 定时器存储器        |
| 字    | CN  | DDD  | 0 ~ 199     | 计数器存储器        |
| 字    | D   | DDDD | 0 ~ 7999    | 数据寄存器          |
| 双字  | CN2 | DDD  | 200 ~ 255   | 计数器存储器        |
| 字    | SD  | DDDD | 8000 ~ 9999 | 特殊数据寄存器      |

例如：**D100** 表示在 D 数据存储区的字 100。

## Mitsubishi FX2N/FX3U/FX3G 系列

### 一般资讯

| 設定            | 参数             |
| -------------- | --------------- |
| 运行时模块 | neuron_o_fx3u3g |
| 驱动名称   | fx3u3g          |
| 协议       | RS 命令         |
| 物理接口   | RS232           |
| 默认设置   | 9600/7/E/1      |

### 地址格式

> <span style="font-family:sans-serif; font-size:2em;">ADDR</span>

**ADDR** 是如下<u>寄存器</u>地址：

| 类  |     | 規格  | 範圍      | 描述         |
| --- | --- | ----- | --------- | ------------ |
| 比特  | X   | OOO  | 0 ~ 377     | 输入继电器          |
| 比特  | Y   | OOO  | 0 ~ 377     | 输出继电器          |
| 比特  | M   | DDDD | 0 ~ 7999    | 辅助继电器          |
| 比特  | T   | DDD  | 0 ~ 255     | 计时器继电器        |
| 比特  | C   | DDD  | 0 ~ 255     | 计数器继电器        |
| 比特  | SM  | DDDD | 8000 ~ 9999 | 特殊辅助设备 继电器 |
| 比特  | S   | DDDD | 0 ~ 4095    | 国家                |
| 字    | TN  | DDD  | 0 ~ 255     | 定时器存储器        |
| 字    | CN  | DDD  | 0 ~ 199     | 计数器存储器        |
| 字    | D   | DDDD | 0 ~ 7999    | 数据寄存器          |
| 双字  | CN2 | DDD  | 200 ~ 255   | 计数器存储器        |
| 字    | SD  | DDDD | 8000 ~ 9999 | 特殊数据寄存器      |
| 字    | R   | DDDD | 0 ~ 32767   | 扩展寄存器          |

例如：**D100** 表示在 D 数据存储区的字 100。

## Mitsubishi Melsec E71 for Q 系列

### 一般资讯

| 設定            | 参数            |
| -------------- | --------------- |
| 运行时模块     | neuron_o_mele71 |
| 驱动名称       | mele71          |
| 协议           | MELSEC E71      |
| 物理接口       | 以太网          |
| 默认设置       | 端口：2000      |

### 注意事项

Q系列PLC中单个端口不能处理多个连接请求，在使用E71协议连接PLC时，请务必在PLC的参数设置中为每一个neuron实例分配独立端口，并指定协议为TCP和MC。

### 地址格式

> <span style="font-family:sans-serif; font-size:2em;">ADDR</span>

**ADDR** 是如下<u>寄存器</u>地址：

| 类  |     | 規格  | 範圍      | 描述         |
| --- | --- | ----- | --------- | ------------ |
| 比特 | X   | HHHH    | 0 ~ 1fff    | 输入继电器                   |
| 比特 | Y   | HHHH    | 0 ~ 1fff    | 输出继电器                   |
| 比特 | M   | DDDDD   | 0 ~ 61439   | 内部继电器                   |
| 比特 | L   | DDDDD   | 0 ~ 32767   | 锁定继电器                   |
| 比特 | F   | DDDDD   | 0 ~ 32767   | <u>报幕员</u>                |
| 比特 | V   | DDDDD   | 0 ~ 32767   | 边缘继电器                   |
| 比特 | B   | HHHH    | 0 ~ efff    | 链接中继                     |
| 比特 | TC  | DDDD    | 0 ~ 2047    | 定时器线圈                   |
| 比特 | SS  | DDDDD   | 0 ~ 25471   | 保留计时器触点               |
| 比特 | SC  | DDDDD   | 0 ~ 25471   | 固定式定时器线圈             |
| 比特 | CS  | DDDDD   | 0 ~ 25471   | <u>Counter Contact</u>       |
| 比特 | CC  | DDDDD   | 0 ~ 25471   | 计数器线圈                   |
| 比特 | SB  | HHH     | 0 ~ 7ff     | 特殊链路继电器               |
| 比特 | DX  | HHHH    | 0 ~ 1fff    | 直接输入                     |
| 比特 | DY  | HHHH    | 0 ~ 1fff    | 直接输出                     |
| 比特 | TS  | DDDD    | 0 ~ 2047    | 定时器触点                   |
| 字   | W   | HHHH    | 0 ~ 2fff    | <u>Link Register</u>         |
| 字   | TN  | DDDD    | 0 ~ 2047    | 定时器当前值                 |
| 字   | SN  | DDDD    | 0 ~ 2047    | 保留计时器电流               |
| 字   | CN  | DDDD    | 0 ~ 1023    | 计数值                       |
| 字   | SW  | HHH     | 0 ~ 7ff     | <u>Special Link Register</u> |
| 字   | Z   | DD      | 0 ~ 19      | 索引寄存器                   |
| 字   | ZR  | HHHHH   | 0 ~ fe7a5   | <u>File Register</u>         |
| 字   | D   | DDDDDDD | 0 ~ 4212735 | 数据寄存器                   |
| 字   | SD  | DDDD    | 0 ~ 2047    | <div></div>                  |

例如：**D100** 表示在 D 数据存储区的字 100。

## Modbus RTU

### 一般资讯

| 設定            | 参数             |
| -------------- | --------------- |
| 运行时模块 | neuron_o_mbsrtu |
| 驱动名称   | mbsrtu          |
| 协议       | Modbus RTU      |
| 物理接口   | RS485           |
| 默认设置   | 9600/8/N/1      |

### 参数配置

| 参数            | 说明 | 范围 |
| -------------- | --------------- | ----------- |
| BYTEORDER | 全局数据字节序 | DCBA： 0、CDAB：1、ABCD：2、BADC：3|

### 地址格式

> <span style="font-family:sans-serif; font-size:2em;">STN!ADDR[.BIT][#ENDIAN]</span>

**STN** 为从机号或设备 ID（0-247）

**ADDR** 是指如下的</u>寄存器</u>地址：

| 类  |  功能码   | 規格  | 範圍      | 描述         |
| --- | --- | ----- | --------- | ------------ |
| 比特 | 01/05/15 | DDDDDD | 000001 ~ 065536 | 离散输出线圈       |
| 比特 | 02       | DDDDDD | 100001 ~ 165536 | 离散输入触点       |
| 字   | 04       | DDDDDD | 300001 ~ 365536 | 模拟输入寄存器     |
| 字   | 03/06/16 | DDDDDD | 400001 ~ 465536 | 模拟输出保持寄存器 |

**BIT** 取第n位bit，范围0-15

**ENDIAN** 数值字节序，优先级高于全局字节序配置

## Modbus TCP

### 一般资讯

| 設定            | 参数            |
| -------------- | --------------- |
| 运行时模块 | neuron_o_mbstcp |
| 驱动名称   | mbstcp          |
| 协议       | Modbus TCP      |
| 物理接口   | 以太网          |
| 默认设置   | 端口：502       |

### 参数配置

| 参数            | 说明 | 范围 |
| -------------- | --------------- | ----------- |
| BYTEORDER | 数据字节序 | DCBA： 0、CDAB：1、ABCD：2、BADC：3|

### 地址格式

> <span style="font-family:sans-serif; font-size:2em;">STN!ADDR[.BIT][#ENDIAN]</span>

**STN** 为从机号或设备 ID（0-247）

**ADDR** 是指如下的<u>寄存器</u>地址：

| 类  |   功能码  | 規格  | 範圍      | 描述         |
| --- | --- | ----- | --------- | ------------ |
| 比特 | 01/05/15 | DDDDDD | 000001 ~ 065536 | 离散输出线圈       |
| 比特 | 02       | DDDDDD | 100001 ~ 165536 | 离散输入触点       |
| 字   | 04       | DDDDDD | 300001 ~ 365536 | 模拟输入寄存器     |
| 字   | 03/06/16 | DDDDDD | 400001 ~ 465536 | 模拟输出保持寄存器 |

**BIT** 取第n位bit，范围0-15

**ENDIAN** 数值字节序，优先级高于全局字节序配置

例如：**2！404001** 表示字地址 4000，在子号 2 中。

## Modbus RTU over TCP

### 一般资讯

| 設定            | 参数             |
| -------------- | --------------- |
| 运行时模块 | neuron_o_mbstcp |
| 驱动名称   | mbstcp          |
| 协议       | Modbus TCP      |
| 物理接口   | 以太网          |
| 默认设置   | 端口：502       |

### 参数配置

| 参数            | 说明 | 范围 |
| -------------- | --------------- | ----------- |
| BYTEORDER | 数据字节序 | DCBA： 0、CDAB：1、ABCD：2、BADC：3|

### 地址格式

> <span style="font-family:sans-serif; font-size:2em;">STN!ADDR[.BIT][#ENDIAN]</span>

**STN** 为从机号或设备 ID（0-247）

**ADDR** 是指如下的<u>寄存器</u>地址：

| 类  |   功能码  | 規格  | 範圍      | 描述         |
| --- | --- | ----- | --------- | ------------ |
| 比特 | 01/05/15 | DDDDDD | 000001 ~ 065536 | 离散输出线圈       |
| 比特 | 02       | DDDDDD | 100001 ~ 165536 | 离散输入触点       |
| 字   | 04       | DDDDDD | 300001 ~ 365536 | 模拟输入寄存器     |
| 字   | 03/06/16 | DDDDDD | 400001 ~ 465536 | 模拟输出保持寄存器 |

**BIT** 取第n位bit，范围0-15

**ENDIAN** 数值字节序，优先级高于全局字节序配置

例如：**2！404001** 表示字地址 4000，在设备 2 中。
     **2! 400001.1** 表示设备2，地址0000，第1位bit。
     **2! 400001.2** 表示设备2，地址0000，数据字节序为ABCD。

## IEC 61850

### 一般资讯

| 設定            | 参数            |
| -------------- | --------------- |
| 运行时模块 | neuron_o_i61850 |
| 驱动名称   | i61850          |
| 协议       | IEC 61850       |
| 物理接口   | 以太网          |
| 默认设置   | 端口：102       |

### 地址格式

> <span style="font-family:sans-serif; font-size:2em;">FC!ADDR</span>

**FC** 是功能约束值，如下所示：

| 类  |   規格       | 描述         |
| --- | -----  | ------------ |
| 0   | IEC61850_FC_ST | 状态信息          |
| 1   | IEC61850_FC_MX | 测量值 - 模拟值   |
| 2   | IEC61850_FC_SP | 设定点            |
| 3   | IEC61850_FC_SV | 替换              |
| 4   | IEC61850_FC_CF | 配置              |
| 5   | IEC61850_FC_DC | 说明              |
| 6   | IEC61850_FC_SG | 设置组            |
| 7   | IEC61850_FC_SE | 设置组别可编辑    |
| 8   | IEC61850_FC_SR | 服务响应/服务跟踪 |
| 9   | IEC61850_FC_OR | 操作收到          |
| 10  | IEC61850_FC_BL | 屏蔽              |
| 11  | IEC61850_FC_EX | 扩展定义          |
| 12  | IEC61850_FC_CO | 控制              |
| 13  | IEC61850_FC_US | 单播 SV           |
| 14  | IEC61850_FC_MS | 多播 SV           |
| 15  | IEC61850_FC_RP | 无缓冲报告        |
| 16  | IEC61850_FC_BR | 缓冲报告          |
| 17  | IEC61850_FC_LG | 日志控制块        |

**ADDR** 是对象参考地址字符串

EC61850 数据分层模型通常有以下几种：

物理设备（IED）

逻辑设备（LD）

逻辑节点（LN）

对象数据（DO）

对象属性（DA）

例如：**1!testmodelSENSORS/TTMP1.TmpSv.instMag.f** 表示该标签的功能约束为 1（IEC61850_FC_MX--模拟测量器）。对象参考地址串为 (IED)--测试模型，(LD)--传感器，(LN)--TTMP1，(DO)--TmpSv，(DA)--instMag.f 为浮动值。

## OPC UA

### 一般资讯

| 設定            | 参数             |
| -------------- | --------------- |
| 运行时模块 | neuron_o_opcua |
| 驱动名称   | opcua          |
| 协议       | OPC UA         |
| 物理接口   | 以太网         |
| 默认设置   | 端口：4840     |

### 证书设置

OPCUA可通过用户自签名证书登录到OPC-UA服务器，certificate和key必须满足以下条件：

* CERTIFICATE和KEYFILE必须同时设置
* Certificate必须以X.509v3标准生成
* Certficate的SAN字段必须包含` URI:urn:xxx.xxx.xxx`,“xxx”部分为自定义部分
* Certificate文件和key文件必须使用DER格式编码

证书文件可以提前导入到目标服务器中并设置为信任，也可以由neuron设置后自动提交再由服务端设置为信任。

证书生成步骤（Windows/Linux/Mac）：

```bash
$openssl req -config localhost.cnf -new -nodes -x509 -sha256 -newkey rsa:2048 -keyout localhost.key -days 365 -subj "/C=DE/O=neuron/CN=NeuronClient@localhost" -out localhost.crt
$openssl x509 -in localhost.crt -outform der -out client_cert.der
$openssl rsa -inform PEM -in localhost.key -outform DER -out client_key.der
$rm localhost.crt
$rm localhost.key
```

`-config`指定的*.cnf文件可以使用 [openssl 的模版文件](https://github.com/openssl/openssl/blob/master/apps/openssl.cnf)进行修改，需包含如下配置节：

```ini
[ v3_req ]

# Extensions to add to a certificate request

basicConstraints = CA:FALSE
keyUsage = nonRepudiation, digitalSignature, keyEncipherment
subjectAltName = @alt_names

[ alt_names ]
URI.1 = urn:xxx.xxx.xxx
DNS.1 = localhost
#DNS.2 = localhost
IP.1 = 127.0.0.1
#IP.2 = 0.0.0.0
```

`-days`可以根据需要设置数值。

### 地址格式C

> <span style="font-family:sans-serif; font-size:2em;">IX!NODEID</span>

**IX** 为命名空间索引（1-32767）

**NODEID** 是节点 ID（任意字符串，不包括 '!'）

例如：2!Device1.Module1.Tag1 代表命名空间索引为 2，节点 ID 为 Device1.Module1.Tag1

命名空间索引和节点 ID 的解释请参考 OPC UA 标准。

## IEC 60870-5-104

### 一般资讯

| 設定            | 参数             |
| -------------- | --------------- |
| 运行时模块 | neuron_o_iec104 |
| 驱动名称   | IEC 60870-5-104  |
| 协议       | IEC 60870-5-104 |
| 物理接口   | 以太网         |
| 默认设置   | 端口：2404     |

### 参数设定

| 设定            | 参数             | 备注 |
| -------------- | --------------- | -------- |
| k | | default 12|
| w | | default 8|
| t0 |建立连接超时时间| default 30|
| t1 |发送APDU超时时间| default 15|
| t2 |应答超时时间| default 10|
| t3 |发送frames超时时间| default 20|

### 地址格式

> <span style="font-family:sans-serif; font-size:2em;">CA!IOA</span>

**CA** 站地址

**IOA** 数据对象地址

数据类型说明：

|类型名称|数据类型|
|--------|-------|
|M_ME_NA_1|WORD,UWORAD,DWORD,UDWORD |
|M_ME_TD_1|WORD,UWORAD,DWORD,UDWORD |
|M_ME_ND_1|WORD,UWORAD,DWORD,UDWORD |
|M_ME_NB_1|WORD,UWORAD,DWORD,UDWORD |
|M_ME_TE_1|WORD,UWORAD,DWORD,UDWORD |
|M_ME_NC_1|FLOAT,DOUBLE|
|M_ME_TF_1|FLOAT,DOUBLE|
|M_SP_NA_1|BOOL|
|M_SP_TB_1|BOOL|

例如：1!2 代表地址为1的站，数据地址为2

## DL/T645-2007

### 一般资讯

| 設定            | 参数             |
| -------------- | --------------- |
| 运行时模块 | neuron_o_dlt645 |
| 驱动名称   | dlt645          |
| 协议       | DL/T645-2007      |
| 物理接口   | RS485           |
| 默认设置   | 9600/8/E/1      |

注意：一般电表的校验方式为偶校验（Even）

### 地址格式

> <span style="font-family:sans-serif; font-size:2em;">STN1!STN2!ADDR</span>

**STN1** 为电表通讯地址前三个字节

**STN2** 为电表通讯地址后三个字节

**ADDR** 是对应的数据标识：

|  数据标识    | 描述                  |
| ----------- | -------------------- |
| 33343435    | 读A相电压             |
| 33343535    | 读A相电流             |
| 33333333    | 读当前组合有功总电能    |

例如：210220!003011!33343435 代表的是通讯地址为210220003011设备的电压值
