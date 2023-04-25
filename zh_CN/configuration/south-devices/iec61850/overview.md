# 概览

IEC61850 是一种国际通信标准协议，通过对设备的一系列规范化，达到了全站的通讯统一。 IEC61850 广泛应用于电力行业。

MMS 报文规范运用在 IEC61850 标准站控层和间隔层之间，MMS 通过对实际设备进行面向对象建模方法，实现了网络环境下不同制造设备之间的互操作。

IEC61850 插件用于对 IEC61850 服务器的读/写，目前支持 MMS 协议的访问。

## 参数

|  参数    | 说明                       |
| -------- | -------------------------- |
| **设备 IP 地址** | 目标设备 IP              |
| **设备端口** | 目标设备端口号，默认为 102 |
| **本地 AP 标题** | 当前客户端的 ACSE AP-Title 字符串 (缺省 = '1,1,1,999') |
| **本地 AE 限定符** | 当前客户端的 ACSE AP-Title 字符串 (缺省 = '12') |
| **本地 P 选择器** | 当前客户端的 PSAP-Address (缺省 = 1) |
| **本地 S 选择器** | 当前客户端的 SSAP-Address (缺省 = 1) |
| **本地 T 选择器** | 当前客户端的 TSAP-Address (缺省 = 1) |
| **远程 AP 标题** | 远程设备的 ACSE AP-Title 字符串 (缺省 = '1,1,1,999.1') |
| **远程 AE 限定符** | 远程设备的 ACSE AE-Qualifier (缺省 = 12) |
| **远程 P 选择器** | 远程设备的 PSAP-Address (缺省 = 1) |
| **远程 S 选择器** | 远程设备的 SSAP-Address (缺省 = 1) |
| **远程 T 选择器** | 远程设备的 TSAP-Address (缺省 = 1) |
| **开启连接认证** | 是否开启连接认证 |
| **连接认证方式** | 连接认证方式，密码/无 |
| **认证密码** | 认证密码 |

## 数据类型

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
* BOOL
* STRING

## 地址格式

> Logical Devices/Logical Nodes$FC$DO$DA</span>

IEC61850 数据分层模型通常有以下几种：

| 模型层名称                           | 描述         |
| ------------------------------------ | ------------ |
| IED（Intelligent Electronic Device） | 智能电子设备 |
| LD（Logical Devices）                | 逻辑设备     |
| LN（Logical Nodes）                  | 逻辑节点     |
| DO（Data Objects）                   | 数据对象     |
| DA （Data Attributes）               | 数据属性     |

**FC** 是功能的约束值（即功能码），如下表所示：

|   功能约束   | 描述         |
| -----  | ------------ |
| ST | 状态信息          |
| MX | 测量值 - 模拟值   |
| SP | 设定点            |
| SV | 替换              |
| CF | 配置              |
| DC | 说明              |
| SG | 设置组            |
| SE | 设置组别可编辑    |
| SR | 服务响应/服务跟踪 |
| OR | 操作收到          |
| BL | 屏蔽              |
| EX | 扩展定义          |
| CO | 控制              |
| US | 单播 SV           |
| MS | 多播 SV           |
| RP | 无缓冲报告        |
| BR | 缓冲报告          |
| LG | 日志控制块        |

## 地址示例

| 地址                                  | 数据类型 | 说明                                                 |
| ------------------------------------- | -------- | ---------------------------------------------------- |
| GenericIO/GGIO1$CF$Mod$ctlModel       | INT8     | LD-GenericIO,LN-GGIO1,FC-CF,DO-Mod,DA-ctlModel       |
| GenericIO/GGIO1$CO$SPCSO1$Oper$ctlNum | UINT8    | LD-GenericIO,LN-GGIO1,FC-CO,DO-SPCSO1,DA-Oper$ctlNum |
| GenericIO/GGIO1$CF$SPCSO1$ctlModel    | INT16    | LD-GenericIO,LN-GGIO1,FC-CF,DO-SPCSO1,DA-ctlModel    |
| GenericIO/GGIO1$CO$SPCSO2$Oper$ctlNum | UINT16   | LD-GenericIO,LN-GGIO1,FC-CO,DO-SPCSO2,DA-Oper$ctlNum |
| GenericIO/GGIO1$CF$SPCSO2$ctlModel    | INT32    | LD-GenericIO,LN-GGIO1,FC-CF,DO-SPCSO2,DA-ctlModel    |
| GenericIO/GGIO1$ST$SPCSO4$Oper$ctlNum | UINT32   | LD-GenericIO,LN-GGIO1,FC-ST,DO-SPCSO4,DA-Oper$ctlNum |
| GenericIO/GGIO1$CF$SPCSO3$ctlModel    | INT64    | LD-GenericIO,LN-GGIO1,FC-CF,DO-SPCSO3,DA-ctlModel    |
| GenericIO/GGIO1$ST$SPCSO1$ctlNum      | UINT64   | LD-GenericIO,LN-GGIO1,FC-ST,DO-SPCSO1,DA-ctlNum      |
| GenericIO/GGIO1$MX$AnIn1$mag$f        | FLOAT    | LD-GenericIO,LN-GGIO1,FC-MX,DO-AnIn1,DA-mag$f        |
| GenericIO/GGIO1$MX$AnIn3$mag$f        | DOUBLE   | LD-GenericIO,LN-GGIO1,FC-MX,DO-AnIn3,DA-mag$f        |
| GenericIO/GGIO1$CO$SPCSO1$Oper$Test   | BOOL     | LD-GenericIO,LN-GGIO1,FC-CO,DO-SPCSO1,DA-Oper$Test   |
| GenericIO/LLN0$DC$NamPlt$vendor       | STRING   | LD-GenericIO,LN-GGIO1,FC-DC,DO-NamPlt,DA-vendor      |
