# XINJE Modbus RTU

Neuron XINJE Modbus RTU 插件使用 Modbus RTU 协议，用于采集信捷 PLC 标签的数据，支持信捷 XC/XD/XL 系列 PLC 型号。

## 添加插件

在 **配置 -> 南向设备**，点击**添加设备**来创建设备节点，输入插件名称，插件类型选择 **XINJE Modbus RTU** 启用插件。

## 设备配置

点击插件卡片或插件列，进入**设备配置**页。配置 Neuron 与设备建立连接所需的参数，下表为插件相关配置项。

| <div style="width:100pt">参数</div>               | 说明                                                    |
| -------------------- | ---------------------------------------------------------------------------------------------- |
| **PLC 型号**         | 选择信捷 PLC 型号。                                                                                |
| **物理链路**         | 选择使用 Serial （串口）或者是 Ethernet（以太网）通信介质。                                    |
| **连接超时时间**     | 等待设备返回指令响应的时间。                                                                   |
| **最大重试次数**     | 发送读取指令失败后最大重试次数。                                                               |
| **指令重新发送间隔** | 发送读取指令失败后重新发送读指令时间间隔，单位为毫秒。                                         |
| **指令发送间隔**     | 发送每条读写指令之间的等待时间。某些串口设备在较短时间内接收到连续指令时，可能会丢弃某些指令。 |
| **串口设备**         | 串口模式下，串口设备的路径，如 Linux 系统中 /dev/ttyS0。                                       |
| **停止位**           | 串口模式下，串口连接参数。                                                                     |
| **校验位**           | 串口模式下，串口连接参数。                                                                     |
| **波特率**           | 串口模式下，串口连接参数。                                                                     |
| **数据位**           | 串口模式下，串口连接参数。                                                                     |
| **连接模式**         | Ethernet 模式下，可以选择 Neuron 作为 TCP 的客户端或是服务端。                                 |
| **IP 地址**          | Ethernet 模式下，设备的 IP 地址（Neuron 作为客户端）；或是 Neuron 本机的 IP 地址（Neuron 作为服务端），默认可填 0.0.0.0。 |
| **端口**             | Ethernet 模式下，设备的端口号（Neuron 作为客户端）；或是 Neuron 本机的端口（Neuron 作为服务端）。|
| **最大重试次数**     | 发送读取指令失败后最大重试次数。                                                               |
| **指令重新发送间隔** | 发送读取指令失败后重新发送读指令时间间隔，单位为毫秒。                                         |

XINJE Modbus RTU 插件的配置与 [Modbus RTU驱动模块](../modbus-rtu/modbus-rtu.md)相似。

## 设置组和点位

完成插件的添加和配置后，要建立设备与 Neuron 之间的通信，首先为南向驱动程序添加组和点位。

完成设备配置后，在**南向设备**页，点击设备卡片/设备列进入**组列表**页。点击**创建**来创建组，设定组名称以及采集间隔。完成组的创建后，点击组名称进入**点位列表**页，添加需要采集的设备点位，包括点位地址，点位属性，数据类型等。

公共配置项部分可参考[连接南向设备](../south-devices.md)，本页将介绍支持的数据类型和地址格式部分。

### 数据类型

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

### 地址格式

> SLAVE!ADDRESS\[.BIT][#ENDIAN]\[.LEN\[H]\[L]\[D]\[E]]\[.BYTES]

#### **SLAVE**

必填，指从机地址或者是站点号。

#### **ADDRESS**

信捷 PLC 将内存数据单元（输入/输出继电器、定时器、计数器等）映射到 Modbus 地址空间，以通过 Modbus RTU 协议进行访问。
根据 PLC 型号，此类地址映射可能会有所不同。
Neuron XINJE Modbus RTU 插件将 PLC 数据单元名称指定为 **ADDRESS**，用户不需要关心地址映射的细节。

用户可以根据 PLC 型号从[信捷官方文档](https://m.xinje.com/xj_service/xj_xzzx.html)中查看地址映射的细节。
为了方便起见，以下表格将其列在这里。

::: warning 注意
X 和 Y 区域的数据单元使用八进制进行编号。

例如，对于XC1/XC2/XC3/XC5/XCM/XCC PLC 型号：

* X0~X7：对应于Modbus地址空间中的 16384~16384+7。
* X10~X17：对应于Modbus地址空间中的 16384+8~16384+15。
* X70~X77：对应于Modbus地址空间中的 16384+56~16384+63。
:::

* XC1/XC2/XC3/XC5/XCM/XCC PLC 型号:

| 数据区                          | Modbus 地址范围                | 数量       | 属性       | 寄存器大小    | 数据类型  |
| ------------------------------- | ------------------------------ | ---------- | ---------- | ------------- | --------- |
| M0-M7999 (Coils)                | 0x0000-0x1F3F  (0-7999)        | 8000       | Read/Write | 1Bit          |  BIT      |
| X0-X1037 (Coils)                | 0x4000-0x421F  (16384-16927)   | 543        | Read/Write | 1Bit          |  BIT      |
| Y0-Y1037 (Coils)                | 0x4800-0x4A1F  (18432-18975)   | 543        | Read/Write | 1Bit          |  BIT      |
| S0-S1023 (Coils)                | 0x5000-0x53FF  (20480-21503)   | 1024       | Read/Write | 1Bit          |  BIT      |
| M8000-M8511 (Coils)             | 0x6000-0x61FF  (24576-25087)   | 512        | Read/Write | 1Bit          |  BIT      |
| T0-T618 (Coils)                 | 0x6400-0x666A  (25600-26218)   | 619        | Read/Write | 1Bit          |  BIT      |
| C0-C634 (Coils)                 | 0x6C00-0x6E7A  (27648-28282)   | 635        | Read/Write | 1Bit          |  BIT      |
| D0-D7999 (Hold Registers)       | 0x0000-0x1F3F  (0-7999)        | 8000       | Read/Write | 16Bit,2Byte   |  Various  |
| TD0-TD618 (Hold Registers)      | 0x3000-0x326A  (12288-12906)   | 619        | Read/Write | 16Bit,2Byte   |  Various  |
| CD0-CD634 (Hold Registers)      | 0x3800-0x3A7A  (14336-14970)   | 635        | Read/Write | 16Bit,2Byte   |  Various  |
| D8000-D8511 (Hold Registers)    | 0x4000-0x41FF  (16384-16895)   | 512        | Read/Write | 16Bit,2Byte   |  Various  |
| FD0-FD5000 (Hold Registers)     | 0x4800-0x5B88  (18432-23432)   | 5000       | Read/Write | 16Bit,2Byte   |  Various  |
| FD8000-FD8511 (Hold Registers)  | 0x6800-0x69FF  (26624-27135)   | 512        | Read/Write | 16Bit,2Byte   |  Various  |
| ED0-ED36863 (Hold Registers)    | 0x7000-0xFFFF  (28672-65535)   | 36864      | Read/Write | 16Bit,2Byte   |  Various  |


* XD1/XD2/XD3/XL1/XL3 PLC 型号:

| 数据区                              | Modbus 地址范围                | 数量       | 属性       | 寄存器大小    | 数据类型  |
| ----------------------------------- | ------------------------------ | ---------- | ---------- | ------------- | --------- |
| M0-M7999 (Coils)                    | 0x0000-0x1F3F  (0-7999)        | 8000       | Read/Write | 1Bit          |  BIT      |
| X0-X77 (Coils)                      | 0x5000-0x503F  (20480-20543)   | 64         | Read/Write | 1Bit          |  BIT      |
| X10000-X11177 (Coils)               | 0x5100-0x537F  (20736-21375)   | 640        | Read/Write | 1Bit          |  BIT      |
| X20000-X20177 (Coils)               | 0x58D0-0x594F  (22736-22863)   | 128        | Read/Write | 1Bit          |  BIT      |
| X30000-X30077 (Coils)               | 0x5BF0-0x5C2F  (23536-23599)   | 64         | Read/Write | 1Bit          |  BIT      |
| Y0-Y77 (Coils)                      | 0x6000-0x603F  (24576-24639)   | 64         | Read/Write | 1Bit          |  BIT      |
| Y10000-Y11177 (Coils)               | 0x6100-0x637F  (24832-25471)   | 640        | Read/Write | 1Bit          |  BIT      |
| Y20000-Y20177 (Coils)               | 0x68D0-0x694F  (26832-26959)   | 128        | Read/Write | 1Bit          |  BIT      |
| Y30000-Y30077 (Coils)               | 0x6BF0-0x6C2F  (27632-27695)   | 64         | Read/Write | 1Bit          |  BIT      |
| S0-S1023 (Coils)                    | 0x7000-0x73FF  (28672-29695)   | 1024       | Read/Write | 1Bit          |  BIT      |
| SM0-SM2047 (Coils)                  | 0x9000-0x97FF  (36864-38911)   | 2048       | Read/Write | 1Bit          |  BIT      |
| T0-T575 (Coils)                     | 0xA000-0xA23F  (40960-41535)   | 576        | Read/Write | 1Bit          |  BIT      |
| C0-C575 (Coils)                     | 0xB000-0xB23F  (45056-45631)   | 576        | Read/Write | 1Bit          |  BIT      |
| ET0-ET31 (Coils)                    | 0xC000-0xC01F  (49152-49183)   | 32         | Read/Write | 1Bit          |  BIT      |
| SEM0-SEM31 (Coils)                  | 0xC080-0xC09F  (49280-49311)   | 32         | Read/Write | 1Bit          |  BIT      |
| HM0-HM959 (Coils)                   | 0xC100-0xC4BF  (49408-50367)   | 960        | Read/Write | 1Bit          |  BIT      |
| HS0-HS127 (Coils)                   | 0xD900-0xD97F  (55552-55679)   | 128        | Read/Write | 1Bit          |  BIT      |
| HT0-HT95 (Coils)                    | 0xE100-0xE15F  (57600-57695)   | 96         | Read/Write | 1Bit          |  BIT      |
| HC0-HC95 (Coils)                    | 0xE500-0xE55F  (58624-58719)   | 96         | Read/Write | 1Bit          |  BIT      |
| HSC0-HSC31 (Coils)                  | 0xE900-0xE91F  (59648-59679)   | 32         | Read/Write | 1Bit          |  BIT      |
| D0-D7999 (Hold Registers)           | 0x0000-0x1F3F  (0-7999)        | 8000       | Read/Write | 16Bit,2Byte   |  Various  |
| ID0-ID99 (Hold Registers)           | 0x5000-0x5063  (20480-20579)   | 100        | Read/Write | 16Bit,2Byte   |  Various  |
| ID10000-ID10999 (Hold Registers)    | 0x5100-0x54E7  (20736-21735)   | 1000       | Read/Write | 16Bit,2Byte   |  Various  |
| ID20000-ID20199 (Hold Registers)    | 0x58D0-0x5997  (22736-22935)   | 200        | Read/Write | 16Bit,2Byte   |  Various  |
| ID30000-ID30099 (Hold Registers)    | 0x5BF0-0x5C53  (23536-23635)   | 100        | Read/Write | 16Bit,2Byte   |  Various  |
| QD0-ID99 (Hold Registers)           | 0x6000-0x6063  (24576-24675)   | 100        | Read/Write | 16Bit,2Byte   |  Various  |
| QD10000-QD10999 (Hold Registers)    | 0x6100-0x64E7  (24832-25831)   | 1000       | Read/Write | 16Bit,2Byte   |  Various  |
| QD20000-QD20199 (Hold Registers)    | 0x68D0-0x6997  (26832-26931)   | 200        | Read/Write | 16Bit,2Byte   |  Various  |
| QD30000-QD30099 (Hold Registers)    | 0x6BF0-0x6C53  (27632-27731)   | 100        | Read/Write | 16Bit,2Byte   |  Various  |
| SD0-SD2047 (Hold Registers)         | 0x7000-0x77FF  (28672-30719)   | 2048       | Read/Write | 16Bit,2Byte   |  Various  |
| TD0-TD575 (Hold Registers)          | 0x8000-0x823F  (32768-33343)   | 576        | Read/Write | 16Bit,2Byte   |  Various  |
| CD0-CD575 (Hold Registers)          | 0x9000-0x923F  (36864-37439)   | 576        | Read/Write | 16Bit,2Byte   |  Various  |
| ETD0-ETD31 (Hold Registers)         | 0xA000-0xA01F  (40960-40991)   | 32         | Read/Write | 16Bit,2Byte   |  Various  |
| HD0-HD999 (Hold Registers)          | 0xA080-0xA467  (41088-42087)   | 1000       | Read/Write | 16Bit,2Byte   |  Various  |
| HSD0-HSD499 (Hold Registers)        | 0xB880-0xBA73  (47232-47731)   | 500        | Read/Write | 16Bit,2Byte   |  Various  |
| HTD0-HTD95 (Hold Registers)         | 0xBC80-0xBCDF  (48256-48351)   | 96         | Read/Write | 16Bit,2Byte   |  Various  |
| HCD0-HCD95 (Hold Registers)         | 0xC080-0xC0DF  (49280-49375)   | 96         | Read/Write | 16Bit,2Byte   |  Various  |
| HSCD0-HSCD31 (Hold Registers)       | 0xC480-0xC49F  (50304-50335)   | 32         | Read/Write | 16Bit,2Byte   |  Various  |
| FD0-FD5119 (Hold Registers)         | 0xC4C0-0xD8BF  (50368-55487)   | 5120       | Read/Write | 16Bit,2Byte   |  Various  |
| SFD0-SFD1999 (Hold Registers)       | 0xE4C0-0xEC8F  (58560-60559)   | 2000       | Read/Write | 16Bit,2Byte   |  Various  |
| FS0-FS47 (Hold Registers)           | 0xF4C0-0xF4EF  (62656-62703)   | 48         | Read/Write | 16Bit,2Byte   |  Various  |


* XD5/XDM/XDC/XD5E/XDME/XL5/XL5E/XL5H/XLME PLC 型号:

| 数据区                              | Modbus 地址范围                | 数量       | 属性       | 寄存器大小    | 数据类型  |
| ----------------------------------- | ------------------------------ | ---------- | ---------- | ------------- | --------- |
| M0-M20479 (Coils)                   | 0x0000-0x4FFF  (0-20479)       | 20480      | Read/Write | 1Bit          |  BIT      |
| X0-X77 (Coils)                      | 0x5000-0x503F  (20480-20543)   | 64         | Read/Write | 1Bit          |  BIT      |
| X10000-X11777 (Coils)               | 0x5100-0x54FF  (20736-21759)   | 1024       | Read/Write | 1Bit          |  BIT      |
| X20000-X20177 (Coils)               | 0x58D0-0x594F  (22736-22863)   | 128        | Read/Write | 1Bit          |  BIT      |
| X30000-X30077 (Coils)               | 0x5BF0-0x5C2F  (23536-23599)   | 64         | Read/Write | 1Bit          |  BIT      |
| Y0-Y77 (Coils)                      | 0x6000-0x603F  (24576-24639)   | 64         | Read/Write | 1Bit          |  BIT      |
| Y10000-Y11777 (Coils)               | 0x6100-0x64FF  (24832-25855)   | 1024       | Read/Write | 1Bit          |  BIT      |
| Y20000-Y20177 (Coils)               | 0x68D0-0x694F  (26832-26959)   | 128        | Read/Write | 1Bit          |  BIT      |
| Y30000-Y30077 (Coils)               | 0x6BF0-0x6C2F  (27632-27695)   | 64         | Read/Write | 1Bit          |  BIT      |
| S0-S7999 (Coils)                    | 0x7000-0x8F3F  (28672-36671)   | 8000       | Read/Write | 1Bit          |  BIT      |
| SM0-SM4095 (Coils)                  | 0x9000-0x9FFF  (36864-40959)   | 4096       | Read/Write | 1Bit          |  BIT      |
| T0-T4095 (Coils)                    | 0xA000-0xAFFF  (40960-45055)   | 4096       | Read/Write | 1Bit          |  BIT      |
| C0-C4095 (Coils)                    | 0xB000-0xBFFF  (45056-49151)   | 4096       | Read/Write | 1Bit          |  BIT      |
| ET0-ET39 (Coils)                    | 0xC000-0xC027  (49152-49183)   | 40         | Read/Write | 1Bit          |  BIT      |
| SEM0-SEM127 (Coils)                 | 0xC080-0xC0FF  (49280-49407)   | 128        | Read/Write | 1Bit          |  BIT      |
| HM0-HM6143 (Coils)                  | 0xC100-0xD8FF  (49408-55551)   | 6144       | Read/Write | 1Bit          |  BIT      |
| HS0-HS999 (Coils)                   | 0xD900-0xDCEF  (55552-56551)   | 1000       | Read/Write | 1Bit          |  BIT      |
| HT0-HT1023 (Coils)                  | 0xE100-0xE4FF  (57600-58623)   | 1024       | Read/Write | 1Bit          |  BIT      |
| HC0-HC1023 (Coils)                  | 0xE500-0xE8FF  (58624-59647)   | 1024       | Read/Write | 1Bit          |  BIT      |
| HSC0-HSC39 (Coils)                  | 0xE900-0xE927  (59648-59687)   | 40         | Read/Write | 1Bit          |  BIT      |
| D0-D20479 (Hold Registers)          | 0x0000-0x4FFF  (0-20479)       | 20480      | Read/Write | 16Bit,2Byte   |  Various  |
| ID0-ID99 (Hold Registers)           | 0x5000-0x5063  (20480-20579)   | 100        | Read/Write | 16Bit,2Byte   |  Various  |
| ID10000-ID11599 (Hold Registers)    | 0x5100-0x573F  (20736-22335)   | 1600       | Read/Write | 16Bit,2Byte   |  Various  |
| ID20000-ID20199 (Hold Registers)    | 0x58D0-0x5997  (22736-22935)   | 200        | Read/Write | 16Bit,2Byte   |  Various  |
| ID30000-ID30099 (Hold Registers)    | 0x5BF0-0x5C53  (23536-23635)   | 100        | Read/Write | 16Bit,2Byte   |  Various  |
| QD0-ID99 (Hold Registers)           | 0x6000-0x6063  (24576-24675)   | 100        | Read/Write | 16Bit,2Byte   |  Various  |
| QD10000-QD11599 (Hold Registers)    | 0x6100-0x673F  (24832-26431)   | 1600       | Read/Write | 16Bit,2Byte   |  Various  |
| QD20000-QD20199 (Hold Registers)    | 0x68D0-0x6997  (26832-26931)   | 200        | Read/Write | 16Bit,2Byte   |  Various  |
| QD30000-QD30099 (Hold Registers)    | 0x6BF0-0x6C53  (27632-27731)   | 100        | Read/Write | 16Bit,2Byte   |  Various  |
| SD0-SD4095 (Hold Registers)         | 0x7000-0x7FFF  (28672-32767)   | 4096       | Read/Write | 16Bit,2Byte   |  Various  |
| TD0-TD4095 (Hold Registers)         | 0x8000-0x8FFF  (32768-36863)   | 4096       | Read/Write | 16Bit,2Byte   |  Various  |
| CD0-CD4095 (Hold Registers)         | 0x9000-0x9FFF  (36864-40959)   | 4096       | Read/Write | 16Bit,2Byte   |  Various  |
| ETD0-ETD39 (Hold Registers)         | 0xA000-0xA027  (40960-40999)   | 40         | Read/Write | 16Bit,2Byte   |  Various  |
| HD0-HD6143 (Hold Registers)         | 0xA080-0xB87F  (41088-47231)   | 6144       | Read/Write | 16Bit,2Byte   |  Various  |
| HSD0-HSD1023 (Hold Registers)       | 0xB880-0xBC7F  (47232-48255)   | 1024       | Read/Write | 16Bit,2Byte   |  Various  |
| HTD0-HTD1023 (Hold Registers)       | 0xBC80-0xC07F  (48256-49279)   | 1024       | Read/Write | 16Bit,2Byte   |  Various  |
| HCD0-HCD1023 (Hold Registers)       | 0xC080-0xC47F  (49280-50303)   | 1024       | Read/Write | 16Bit,2Byte   |  Various  |
| HSCD0-HSCD39 (Hold Registers)       | 0xC480-0xC4A7  (50304-50343)   | 40         | Read/Write | 16Bit,2Byte   |  Various  |
| FD0-FD8199 (Hold Registers)         | 0xC4C0-0xE4BF  (50368-58559)   | 8192       | Read/Write | 16Bit,2Byte   |  Various  |
| SFD0-SFD4095 (Hold Registers)       | 0xE4C0-0xF4BF  (58560-62655)   | 4096       | Read/Write | 16Bit,2Byte   |  Various  |
| FS0-FS47 (Hold Registers)           | 0xF4C0-0xF4EF  (62656-62703)   | 48         | Read/Write | 16Bit,2Byte   |  Various  |


* XDH/XLH PLC 型号:

| 数据区                              | Modbus 地址范围                | 数量       | 属性       | 寄存器大小    | 数据类型  |
| ----------------------------------- | ------------------------------ | ---------- | ---------- | ------------- | --------- |
| M0-M20479 (Coils)                   | 0x0000-0x4FFF  (0-20479)       | 20480      | Read/Write | 1Bit          |  BIT      |
| X0-X77 (Coils)                      | 0x5000-0x503F  (20480-20543)   | 64         | Read/Write | 1Bit          |  BIT      |
| X10000-X11777 (Coils)               | 0x5100-0x54FF  (20736-21759)   | 1024       | Read/Write | 1Bit          |  BIT      |
| X20000-X20177 (Coils)               | 0x58D0-0x594F  (22736-22863)   | 128        | Read/Write | 1Bit          |  BIT      |
| X30000-X30077 (Coils)               | 0x5BF0-0x5C2F  (23536-23599)   | 64         | Read/Write | 1Bit          |  BIT      |
| Y0-Y77 (Coils)                      | 0x6000-0x603F  (24576-24639)   | 64         | Read/Write | 1Bit          |  BIT      |
| Y10000-Y11777 (Coils)               | 0x6100-0x64FF  (24832-25855)   | 1024       | Read/Write | 1Bit          |  BIT      |
| Y20000-Y20177 (Coils)               | 0x68D0-0x694F  (26832-26959)   | 128        | Read/Write | 1Bit          |  BIT      |
| Y30000-Y30077 (Coils)               | 0x6BF0-0x6C2F  (27632-27695)   | 64         | Read/Write | 1Bit          |  BIT      |
| S0-S7999 (Coils)                    | 0x7000-0x8F3F  (28672-36671)   | 8000       | Read/Write | 1Bit          |  BIT      |
| SM0-SM4095 (Coils)                  | 0x9000-0x9FFF  (36864-40959)   | 4096       | Read/Write | 1Bit          |  BIT      |
| T0-T4095 (Coils)                    | 0xA000-0xAFFF  (40960-45055)   | 4096       | Read/Write | 1Bit          |  BIT      |
| C0-C4095 (Coils)                    | 0xB000-0xBFFF  (45056-49151)   | 4096       | Read/Write | 1Bit          |  BIT      |
| ET0-ET39 (Coils)                    | 0xC000-0xC027  (49152-49183)   | 40         | Read/Write | 1Bit          |  BIT      |
| SEM0-SEM127 (Coils)                 | 0xC080-0xC0FF  (49280-49407)   | 128        | Read/Write | 1Bit          |  BIT      |
| HM0-HM6143 (Coils)                  | 0xC100-0xD8FF  (49408-55551)   | 6144       | Read/Write | 1Bit          |  BIT      |
| HS0-HS999 (Coils)                   | 0xD900-0xDCEF  (55552-56551)   | 1000       | Read/Write | 1Bit          |  BIT      |
| HT0-HT1023 (Coils)                  | 0xE100-0xE4FF  (57600-58623)   | 1024       | Read/Write | 1Bit          |  BIT      |
| HC0-HC1023 (Coils)                  | 0xE500-0xE8FF  (58624-59647)   | 1024       | Read/Write | 1Bit          |  BIT      |
| HSC0-HSC39 (Coils)                  | 0xE900-0xE927  (59648-59687)   | 40         | Read/Write | 1Bit          |  BIT      |
| D0-D20479 (Hold Registers)          | 0x0000-0x4FFF  (0-20479)       | 20480      | Read/Write | 16Bit,2Byte   |  Various  |
| ID0-ID99 (Hold Registers)           | 0x5000-0x5063  (20480-20579)   | 100        | Read/Write | 16Bit,2Byte   |  Various  |
| ID10000-ID11599 (Hold Registers)    | 0x5100-0x573F  (20736-22335)   | 1600       | Read/Write | 16Bit,2Byte   |  Various  |
| ID20000-ID20199 (Hold Registers)    | 0x58D0-0x5997  (22736-22935)   | 200        | Read/Write | 16Bit,2Byte   |  Various  |
| ID30000-ID30099 (Hold Registers)    | 0x5BF0-0x5C53  (23536-23635)   | 100        | Read/Write | 16Bit,2Byte   |  Various  |
| QD0-ID99 (Hold Registers)           | 0x6000-0x6063  (24576-24675)   | 100        | Read/Write | 16Bit,2Byte   |  Various  |
| QD10000-QD11599 (Hold Registers)    | 0x6100-0x673F  (24832-26431)   | 1600       | Read/Write | 16Bit,2Byte   |  Various  |
| QD20000-QD20199 (Hold Registers)    | 0x68D0-0x6997  (26832-26931)   | 200        | Read/Write | 16Bit,2Byte   |  Various  |
| QD30000-QD30099 (Hold Registers)    | 0x6BF0-0x6C53  (27632-27731)   | 100        | Read/Write | 16Bit,2Byte   |  Various  |
| SD0-SD4095 (Hold Registers)         | 0x7000-0x7FFF  (28672-32767)   | 4096       | Read/Write | 16Bit,2Byte   |  Various  |
| TD0-TD4095 (Hold Registers)         | 0x8000-0x8FFF  (32768-36863)   | 4096       | Read/Write | 16Bit,2Byte   |  Various  |
| CD0-CD4095 (Hold Registers)         | 0x9000-0x9FFF  (36864-40959)   | 4096       | Read/Write | 16Bit,2Byte   |  Various  |
| ETD0-ETD39 (Hold Registers)         | 0xA000-0xA027  (40960-40999)   | 40         | Read/Write | 16Bit,2Byte   |  Various  |
| HD0-HD6143 (Hold Registers)         | 0xA080-0xB87F  (41088-47231)   | 6144       | Read/Write | 16Bit,2Byte   |  Various  |
| HSD0-HSD1023 (Hold Registers)       | 0xB880-0xBC7F  (47232-48255)   | 1024       | Read/Write | 16Bit,2Byte   |  Various  |
| HTD0-HTD1023 (Hold Registers)       | 0xBC80-0xC07F  (48256-49279)   | 1024       | Read/Write | 16Bit,2Byte   |  Various  |
| HCD0-HCD1023 (Hold Registers)       | 0xC080-0xC47F  (49280-50303)   | 1024       | Read/Write | 16Bit,2Byte   |  Various  |
| HSCD0-HSCD39 (Hold Registers)       | 0xC480-0xC4A7  (50304-50343)   | 40         | Read/Write | 16Bit,2Byte   |  Various  |
| FD0-FD8199 (Hold Registers)         | 0xC4C0-0xE4BF  (50368-58559)   | 8192       | Read/Write | 16Bit,2Byte   |  Various  |
| SFD0-SFD4095 (Hold Registers)       | 0xE4C0-0xF4BF  (58560-62655)   | 4096       | Read/Write | 16Bit,2Byte   |  Various  |
| FS0-FS255 (Hold Registers)          | 0xF4C0-0xF5BF  (62656-62911)   | 256        | Read/Write | 16Bit,2Byte   |  Various  |

#### **.BIT**

选填，寄存器中的特定 bit，例如：

| 地址        | 数据类型  | 说明                                                |
| ----------- | --------- | ------------------------------- |
| D4.0        | bit       | PLC 数据寄存器 D4，第 0 位。    |
| D10.4       | bit       | PLC 数据寄存器 D4，第 4 位。    |
| D1.15       | bit       | PLC 数据寄存器 D1，第 15 位。   |

#### **#ENDIAN**

选填，字节顺序，适用于 int16/uint16/int32/uint32/float 数据类型，详细说明见下表。

| 符号 | 字节顺序 | 支持的数据类型     | 备注               |
| ---- | -------- | ------------------ | ------------------ |
| #B   | 2,1      | int16/uint16       |                    |
| #L   | 1,2      | int16/uint16       | 不填，默认字节顺序 |
| #LL  | 1,2,3,4  | int32/uint32/float | 不填，默认字节顺序 |
| #LB  | 2,1,4,3  | int32/uint32/float |                    |
| #BL  | 3,4,1,2  | int32/uint32/float |                    |
| #BB  | 4,3,2,1  | int32/uint32/float |                    |

::: tip
字节顺序可能用 ABCD 表示，只需将 1234 对应 ABCD 即可。例如 ABCD 对应默认字节序 1234 (#LL)。
:::

#### .LEN\[H]\[L]\[D]\[E]

当数据类型为 STRING 类型时，**.LEN** 是必填项，表示字符串需要占用的字节长度，每个寄存器中包含**H**，**L**，**D** 和**E** 四种存储方式，如下列表格所示。

| 符号 | 说明                                           |
| ---- | ---------------------------------------------- |
| H    | 一个寄存器存储两个字节，高字节在前低字节在后。 |
| L    | 一个寄存器存储两个字节，低字节在前高字节在后。 |
| D    | 一个寄存器存储一个字节，且存储在低字节。       |
| E    | 一个寄存器存储一个字节，且存储在高字节。       |

#### **.BYTES**

选填，读写bytes类型数据的长度，适用于 bytes 数据类型。

::: tip
Modbus驱动一个寄存器包含2个bytes，在以bytes数据类型读取和写入Modbus寄存器数据时，请保证bytes参数设置为偶数。
:::

### 地址示例

| 地址           | 数据类型  | 说明                                               |
| -------------- | --------- | -------------------------------------------------- |
| 1!D4           | int16     | 指站号为 1，PLC 数据寄存器 D4, 字节顺序为 #L       |
| 1!D4#L         | int16     | 指站号为 1，PLC 数据寄存器 D4, 字节顺序为 #L       |
| 1!D4#B         | uint16    | 指站号为 1，PLC 数据寄存器 D4, 字节顺序为 #B       |
| 1!D4           | int32     | 指站号为 1，PLC 数据寄存器 D4, 字节顺序为 #LL      |
| 1!D4#LB        | uint32    | 指站号为 1，PLC 数据寄存器 D4, 字节顺序为 #LB      |
| 1!D4#BB        | uint32    | 指站号为 1，PLC 数据寄存器 D4, 字节顺序为 #BB      |
| 1!D4#LL        | int32     | 指站号为 1，PLC 数据寄存器 D4, 字节顺序为 #LL      |
| 1!D4#BL        | float     | 指站号为 1，PLC 数据寄存器 D4, 字节顺序为 #BL      |
| 1!D1.10        | String    | 指站号为 1，PLC 数据寄存器 D1, 字符长度为 10，字节顺序为 L，占用 D1 ～ D5 |
| 1!D1.10H       | String    | 指站号为 1，PLC 数据寄存器 D1, 字符长度为 10，字节顺序为 H，占用 D1 ～ D5 |
| 1!D1.10L       | String    | 指站号为 1，PLC 数据寄存器 D1, 字符长度为 10，字节顺序为 L，占用 D1 ～ D5 |
| 1!M8           | bit       | 指站号为 1，PLC 辅助继电器 M8                      |
| 1!X10          | bit       | 指站号为 1，PLC 输入继电器 X10                     |


## 数据监控

完成点位的配置后，您可点击 **监控** -> **数据监控**查看设备信息以及反控设备，具体可参考[数据监控](../../../admin/monitoring.md)。
