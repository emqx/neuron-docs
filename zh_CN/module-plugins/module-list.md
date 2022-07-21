# 模块列表

## 南向插件模块

### PLC 驱动

| 协议名称                                                      | 连接    | 类型  | 是否可用      | 备注                           |
| ------------------------------------------------------------ | ------ | ---- | ------------ | -------------------------------- |
| Allen-Bradley DF1 half-duplex for PLC2                       | 串口    | 商业 | 仅 V1.x 可用  | 用于 PLC2 和 PLC5                |
| Allen-Bradley CIP EtherNet/IP                                | 以太网  | 商业 | 否            | CIP – 通用工业协议 |
| Schneider PLC Modbus RTU                                     | 串口    | 商业 | 仅 V1.x 可用  | |
| Schneider PLC Modbus TCP                                     | 以太网  | 商业 | 仅 V1.x 可用  | |
| Schneider Telemecanique UNI-TE                               | 串口    | 商业 | 仅 V1.x 可用  | |
| ABB SattControl Comli                                        | 串口    | 商业 | 仅 V1.x 可用  | |
| Omron Host Link                                              | 串口    | 商业 | 仅 V1.x 可用  | 用于单连接和多连接 |
| Omron FINS on Host Link                                      | 串口    | 商业 | 仅 V1.x 可用  | |
| Omron FINS on TCP                                            | 以太网  | 商业 | 是            | |
| Siemens 3964R/RK512                                          | 串口    | 商业 | 仅 V1.x 可用  | 用于 S5 和 S7 |
| Siemens Fetch Write for S7-300/400 and CP443 module          | 以太网  | 商业 | 仅 V1.x 可用  | |
| Siemens Industrial Ethernet ISO for S7-200/300/400/1200/1500 | 以太网  | 商业 | 是            | |
| Mitsubishi FX Series                                         | 串口    | 商业 | 仅 V1.x 可用  | |
| Mitsubishi 232ADP/485BD: Serial/RS485                        | 串口    | 商业 | 否           | |
| Mitsubishi MC Protocol for Q series and C24 module           | 串口    | 商业 | 仅 V1.x 可用  | |
| Mitsubishi MC Protocol for Q series and E71 module           | 以太网  | 商业 | 是            | |
| Mitsubishi FX3U-ENET-ADP                                     | 以太网  | 商业 | 否            | 只用于 FX   |
| Panasonic FP series MEWTOCOL-COM                             | 串口    | 商业 | 否            | |
| Panasonic FP series MEWTOCOL-COM                             | 以太网  | 商业 | 否            | |
| Panasonic FP series MEWTOCOL-DAT                             | 以太网  | 商业 | 否            | |
| Beckhoff ADS/AMS TCPIP                                       | 以太网  | 商业 | 否            | |
| Keyence CIP Ethernet/IP                                      | 以太网  | 商业 | 否            | CIP – 通用工业协议 |
| Keyence MC Protocol                                          | 以太网  | 商业 | 否            | 三菱 MC 协议 |
| Delta DVP communication protocol                             | 串口    | 商业 | 否            | |
| Delta Modbus TCP                                             | 以太网  | 商业 | 否            | |
| Delta CIP Ethernet/IP                                        | 以太网  | 商业 | 否            | |
| Fatek FACON serial                                           | 串口    | 商业 | 否            | |
| Fatek FACON ethernet                                         | 以太网  | 商业 | 否            | |
| GE FANUC 90-30 SNPX                                          | 串口    | 商业 | 否            | |
| GE FANUC 90-30 Ethernet SRTP                                 | 以太网  | 商业 | 否            | |

### 全球标准

| 协议名称                  | 连接   | 类型   | 是否可用 | 备注 |
| ----------------------- | ------ | ----- | ------- | -------------------------------- |
| Modbus RTU              | 串口    | 商业  | 是       |  |
| Modbus RTU over TCP     | 以太网  | 商业  | 是       |  |
| Modbus TCP              | 以太网  | 开源  | 是       |  |
| OPC UA                  | 以太网  | 商业  | 是       |  |
| CIP Ethernet/IP         | 以太网  | 商业  | 否       | CIP – 通用工业协议 |

### 电力

| 协议名称             | 连接    | 类型       | 是否可用   | 备注     |
| ------------------- | ------ | --------- | --------- | ---------- |
| IEC 60870-5-101     | 串口    | 商业       | 否        | |
| IEC 60870-5-104     | 以太网  | 商业       | 是        | |
| IEC 61850           | 以太网  | 商业       | 否        | |
| DNP3                | 以太网  | 商业       | 否        | |
| DL/T645-07          | 串口    | 商业       | 是       | 中国电力仪表标准 |

### 楼宇自动化

| 协议名称        | 连接      | 类型       | 是否可用  |
| -------------- | ------- | ---------- | -------- |
| BACnet MS/TP   | 串口    | 商业        | 否        |
| BACnet IP      | 以太网  | 商业        | 是        |
| KNXnet IP      | 以太网  | 商业        | 是        |
| LON            | 以太网  | 商业        | 否        |

### 数控机床和机器人

| 协议名称       | 连接     | 类型   | 是否可用   |
| ------------- | ------- | ----- | --------- |
| MTConnect     | 以太网   | 商业   | 否        |

## 北向插件模块

### 云连接

| 协议名称                | 类型  | 是否可用 |
| --------------------- | ----- | --------- |
| MQTT                  | 开源  | 是      |
| MQTT + Sparkplug B    | 商业  | 是      |
| Websocket             | 商业  | 否      |
| RESTful API           | 开源  | 是      |

### 应用程序

| 协议名称                           | 类型      | 是否可用   |
| --------------------------------- | -------- | --------- |
| eKuiper Stream Processing Engine  | 开源      | 是        |

## 商业模块的 EMQ 许可证

* 必须安装试用 EMQ 许可证或官方 EMQ 许可证才能运行 Neuron 商业插件模块。

* 试用 EMQ 许可证可从网站 [https://www.emqx.com/zh/apply-licenses/neuron](https://www.emqx.com/zh/apply-licenses/neuron) 下载。所有可用的模块都可以无限制地使用 15 天。

* 核心框架，部分插件模块在 LGPLv3 许可下开源。

* 每个插件模块都可以在 EMQ 许可文件中独立授权。
