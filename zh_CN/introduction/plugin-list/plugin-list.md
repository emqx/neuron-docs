# 模块列表

插件可以分为北向应用和南向驱动程序。北向插件通常用于连接到云平台或像处理引擎这样的外部应用程序。南向插件是实现特定协议以访问外部设备的通信驱动程序。为了实现协议格式转换，至少需要一个北向插件和一个南向插件分别用于数据传递和数据采集。

登录 Neuron 后，您可点击**配置** -> **插件**查看系统的插件列表。您也可点击左上角的**添加插件**按钮安装自定义插件。

## 查看可用插件模块

插件管理页面显示所有可用的可插拔模块和详细信息，包括插件名称、关联节点类型、和描述信息，如下图所示，您可从下拉框中选择北向应用或南向设备的插件。

插件类型包括以下三种模式：

- Static：不可删除
- System：不可删除，软件自带
- Custom：可删除，用户自己开发或者是定制开发的

## 添加新的可插拔模块

在插件页面，点击左上角的**添加插件**按钮，在弹出的对话框中进行如下配置：

1. 填写需要添加的 .so 文件的路径和文件名。

2. 单击**创建**按钮将 .so 文件添加到构建目录。

请确保已将自己编写的 .so 插件文件放置在 neuron/build/plugins 目录下，再进行添加。具体的插件开发教程请参考 [SKD 教程](../../dev-guide/sdk-tutorial/sdk-tutorial.md)。

## 南向插件模块

### 全球标准

| 协议名称                                                      | 连接    | 类型  | 是否可用      | 备注                           |
| ------------------------------------------------------------ | ------ | ---- | ------------ | -------------------------------- |
| <div style="width:220pt">Modbus TCP</div>              | <div style="width:40pt">以太网</div>  | <div style="width:40pt">开源</div> | <div style="width:50pt">是</div>            |  |
| <div style="width:220pt">Modbus RTU</div>              | <div style="width:40pt">串口</div>    | <div style="width:40pt">开源</div> | <div style="width:50pt">是</div>           |  |
| <div style="width:220pt">Modbus RTU over TCP</div>     | <div style="width:40pt">以太网</div>  | <div style="width:40pt">开源</div> | <div style="width:50pt">是</div>            |  |
| <div style="width:220pt">OPC UA</div>                  | <div style="width:40pt">以太网</div>  | <div style="width:40pt">商业</div> | <div style="width:50pt">是</div>            |  |
| <div style="width:220pt">CIP Ethernet/IP</div>         | <div style="width:40pt">以太网</div>  | <div style="width:40pt">商业</div> | <div style="width:50pt">是</div>             | <div style="width:110pt">CIP –通用工业协议</div> |

### PLC 驱动

| 协议名称                                                      | 连接    | 类型  | 是否可用      | 备注                           |
| ------------------------------------------------------------ | ------ | ---- | ------------ | -------------------------------- |
| <div style="width:220pt">Siemens 3964R/RK512</div>                                          | <div style="width:40pt">串口</div>    | <div style="width:40pt">商业</div> | <div style="width:50pt">仅 V1.x 可用</div>  | <div style="width:110pt">用于 S5 和 S7</div> |
| <div style="width:220pt">Siemens Industrial Ethernet ISO for S7-200/300/400/1200/1500</div> | <div style="width:40pt">以太网</div>  | <div style="width:40pt">商业</div> | <div style="width:50pt">是</div>            | |
| <div style="width:220pt">Siemens Fetch Write for S7-300/400 and CP443 module</div>          | <div style="width:40pt">以太网</div>  | <div style="width:40pt">商业</div> | <div style="width:50pt">是</div>  | |
| <div style="width:220pt">Allen-Bradley DF1 half-duplex</div>                       | <div style="width:40pt">串口</div>    | <div style="width:40pt">商业</div> | <div style="width:50pt">是</div>  | <div style="width:110pt">用于 PLC2 和 PLC5</div>                |
| <div style="width:220pt">Allen-Bradley CIP EtherNet/IP</div>                                | <div style="width:40pt">以太网</div>  | <div style="width:40pt">商业</div> | <div style="width:50pt">是</div>            | <div style="width:110pt">CIP – 通用工业协议</div> |
| <div style="width:220pt">Schneider PLC Modbus RTU</div>                                     | <div style="width:40pt">串口</div>    | <div style="width:40pt">商业</div> | <div style="width:50pt">是</div>  | |
| <div style="width:220pt">Schneider PLC Modbus TCP</div>                                     | <div style="width:40pt">以太网</div>  | <div style="width:40pt">商业</div> | <div style="width:50pt">是</div>  | |
| <div style="width:220pt">Schneider Telemecanique UNI-TE</div>                               | <div style="width:40pt">串口</div>    | <div style="width:40pt">商业</div> | <div style="width:50pt">仅 V1.x 可用</div>  | |
| <div style="width:220pt">ABB SattControl Comli</div>                                        | <div style="width:40pt">串口</div>    | <div style="width:40pt">商业</div> | <div style="width:50pt">是</div>  | |
| <div style="width:220pt">Omron Host Link</div>                                              | <div style="width:40pt">串口</div>    | <div style="width:40pt">商业</div> | <div style="width:50pt">仅 V1.x 可用</div>  | <div style="width:110pt">用于单连接和多连接</div> |
| <div style="width:220pt">Omron FINS on Host Link</div>                                      | <div style="width:40pt">串口</div>    | <div style="width:40pt">商业</div> | <div style="width:50pt">仅 V1.x 可用</div>  | |
| <div style="width:220pt">Omron FINS on TCP</div>                                            | <div style="width:40pt">以太网</div>  | <div style="width:40pt">商业</div> | <div style="width:50pt">是</div>            | |
| <div style="width:220pt">Omron FINS on UDP</div>                                            | <div style="width:40pt">以太网</div>  | <div style="width:40pt">商业</div> | <div style="width:50pt">是</div>            | |
| <div style="width:220pt">Mitsubishi MC Protocol for Q series and C24 module</div>           | <div style="width:40pt">串口</div>    | <div style="width:40pt">商业</div> | <div style="width:50pt">仅 V1.x 可用</div>  | |
| <div style="width:220pt">Mitsubishi MC Protocol for Q series and E71 module</div>           | <div style="width:40pt">以太网</div>  | <div style="width:40pt">商业</div> | <div style="width:50pt">是</div>            | <div style="width:110pt">3E frame</div> |
| <div style="width:220pt">Mitsubishi FX Series</div>                                         | <div style="width:40pt">串口</div>    | <div style="width:40pt">商业</div> | <div style="width:50pt">仅 V1.x 可用</div>  | |
| <div style="width:220pt">Mitsubishi FX3U-ENET-ADP</div>                                     | <div style="width:40pt">以太网</div>  | <div style="width:40pt">商业</div> | <div style="width:50pt">是</div>            | <div style="width:110pt">1E frame</div>   |
| <div style="width:220pt">Mitsubishi 232ADP/485BD: Serial/RS485</div>                        | <div style="width:40pt">串口</div>    | <div style="width:40pt">商业</div> | <div style="width:50pt">否</div>           | |
| <div style="width:220pt">Panasonic FP series MEWTOCOL-COM</div>                             | <div style="width:40pt">串口</div>    | <div style="width:40pt">商业</div> | <div style="width:50pt">否</div>            | |
| <div style="width:220pt">Panasonic FP series MEWTOCOL-COM</div>                             | <div style="width:40pt">以太网</div>  | <div style="width:40pt">商业</div> | <div style="width:50pt">是</div>            | |
| <div style="width:220pt">Panasonic FP series MEWTOCOL-DAT</div>                             | <div style="width:40pt">以太网</div>  | <div style="width:40pt">商业</div> | <div style="width:50pt">否</div>            | |
| <div style="width:220pt">Beckhoff ADS/AMS TCPIP</div>                                       | <div style="width:40pt">以太网</div>  | <div style="width:40pt">商业</div> | <div style="width:50pt">是</div>            | |
| <div style="width:220pt">Keyence CIP Ethernet/IP</div>                                      | <div style="width:40pt">以太网</div>  | <div style="width:40pt">商业</div> | <div style="width:50pt">是</div>            | <div style="width:110pt">CIP – 通用工业协议</div> |
| <div style="width:220pt">Keyence MC Protocol</div>                                          | <div style="width:40pt">以太网</div>  | <div style="width:40pt">商业</div> | <div style="width:50pt">是</div>            | <div style="width:110pt">三菱 MC 协议</div> |
| <div style="width:220pt">Delta DVP communication protocol</div>                             | <div style="width:40pt">串口</div>    | <div style="width:40pt">商业</div> | <div style="width:50pt">否</div>            | |
| <div style="width:220pt">Delta Modbus TCP</div>                                             | <div style="width:40pt">以太网</div>  | <div style="width:40pt">商业</div> | <div style="width:50pt">是</div>            | |
| <div style="width:220pt">Delta CIP Ethernet/IP</div>                                        | <div style="width:40pt">以太网</div>  | <div style="width:40pt">商业</div> | <div style="width:50pt">是</div>            | <div style="width:110pt">CIP – 通用工业协议</div> |
| <div style="width:220pt">Fatek FACON serial</div>                                           | <div style="width:40pt">串口</div>    | <div style="width:40pt">商业</div> | <div style="width:50pt">否</div>            | |
| <div style="width:220pt">Fatek FACON ethernet</div>                                         | <div style="width:40pt">以太网</div>  | <div style="width:40pt">商业</div> | <div style="width:50pt">否</div>            | |
| <div style="width:220pt">GE FANUC 90-30 SNPX</div>                                          | <div style="width:40pt">串口</div>    | <div style="width:40pt">商业</div> | <div style="width:50pt">否</div>            | |
| <div style="width:220pt">GE FANUC 90-30 Ethernet SRTP</div>                                 | <div style="width:40pt">以太网</div>  | <div style="width:40pt">商业</div> | <div style="width:50pt">否</div>            | |

### 电力

| 协议名称             | 连接    | 类型       | 是否可用   | 备注     |
| ------------------- | ------ | --------- | --------- | ---------- |
| <div style="width:220pt">DL/T645-1997</div>          | <div style="width:40pt">串口</div>    | <div style="width:40pt">商业</div>       | <div style="width:50">是</div>       | <div style="width:110pt">中国电力仪表标准</div>  |
| <div style="width:220pt">DL/T645-2007</div>          | <div style="width:40pt">串口</div>    | <div style="width:40pt">商业</div>       | <div style="width:50">是</div>       | <div style="width:110pt">中国电力仪表标准</div>  |
| <div style="width:220pt">IEC 60870-5-101</div>     | <div style="width:40pt">串口</div>     | <div style="width:40pt">商业</div>      | <div style="width:50">否</div>         | |
| <div style="width:220pt">IEC 60870-5-102</div>     | <div style="width:40pt">串口</div>     | <div style="width:40pt">商业</div>      | <div style="width:50">否</div>         | |
| <div style="width:220pt">IEC 60870-5-103</div>     | <div style="width:40pt">串口</div>     | <div style="width:40pt">商业</div>      | <div style="width:50">否</div>         | |
| <div style="width:220pt">IEC 60870-5-104</div>     | <div style="width:40pt">以太网</div>  | <div style="width:40pt">商业</div>       | <div style="width:50">是</div>        | |
| <div style="width:220pt">IEC 61850</div>           | <div style="width:40pt">以太网</div>  | <div style="width:40pt">商业</div>       | <div style="width:50">是</div>        | |
| <div style="width:220pt">DNP3</div>                | <div style="width:40pt">以太网</div>  | <div style="width:40pt">商业</div>       | <div style="width:50">否</div>        | |

### 楼宇自动化

| 协议名称        | 连接      | 类型       | 是否可用  | 备注 |
| -------------- | ------- | ---------- | -------- | ------ |
| <div style="width:220pt">BACnet IP</div>      | <div style="width:40pt">以太网</div>  | <div style="width:40pt">商业</div>        | <div style="width:50pt">是</div>        | |
| <div style="width:220pt">KNXnet IP</div>      | <div style="width:40pt">以太网</div>  | <div style="width:40pt">商业</div>        | <div style="width:50pt">是</div>        | |
| <div style="width:220pt">BACnet MS/TP</div>    | <div style="width:40pt">串口</div>   | <div style="width:40pt">商业</div>       | <div style="width:50pt">否</div>         | <div style="width:110pt"> </div> |
| <div style="width:220pt">LON</div>            | <div style="width:40pt">以太网</div>  | <div style="width:40pt">商业</div>        | <div style="width:50pt">否</div>        | |

### 数控机床和机器人

| 协议名称       | 连接     | 类型   | 是否可用   | 备注     |
| ------------- | ------- | ----- | --------- | ------- |
| <div style="width:220pt">MTConnect</div>      | <div style="width:40pt">以太网</div>    | <div style="width:40pt">商业</div>    | <div style="width:50pt">否</div>         | <div style="width:110pt"> </div> |
| <div style="width:220pt">Fanuc 0i, 30i, 31i, 32i and 35i</div>      | <div style="width:40pt">以太网</div>    | <div style="width:40pt">商业</div>    | <div style="width:50pt">是</div>         | <div style="width:110pt"> </div> |
| <div style="width:220pt">Mitsubishi M800/M80</div>      | <div style="width:40pt">以太网</div>    | <div style="width:40pt">商业</div>    | <div style="width:50pt">否</div>         | <div style="width:110pt"> </div> |
| <div style="width:220pt">Siemens 840D、810、828D</div>      | <div style="width:40pt">以太网</div>    | <div style="width:40pt">商业</div>    | <div style="width:50pt">否</div>         | <div style="width:110pt"> </div> |

## 北向插件模块

### 云连接

| 协议名称                                 | 类型                                 | 是否可用                                | 备注                  |
| --------------------------------------- | ----------------------------------- | -------------------------------------- | -------------------- |
| <div style="width:285pt">RESTful API</div>            | <div style="width:40pt">开源</div>   | <div style="width:50pt">是</div>       |  |
| <div style="width:285pt">MQTT</div>                   | <div style="width:40pt">开源</div>   | <div style="width:50pt">是</div>       | <div style="width:110pt"> </div> |
| <div style="width:285pt">MQTT Sparkplug B</div>     | <div style="width:40pt">商业</div>   | <div style="width:50pt">是</div>       |  |
| <div style="width:285pt">Websocket</div>              | <div style="width:40pt">商业</div>   | <div style="width:50pt">是</div>       |  |

### 应用程序

| 协议名称                                                            | 类型                                  | 是否可用                                 | 备注 |
| ----------------------------------------------------------------- | ------------------------------------- | --------------------------------------- | ------ |
| <div style="width:285pt">eKuiper Stream Processing</div>   | <div style="width:40pt">开源</div>    | <div style="width:50pt">是</div>         | <div style="width:110pt"> </div>  |

## 许可证政策

核心框架，仪表板以及 modbus、mqtt 和 eKuiper 可插拔模块在 LGPLv3 许可下开源。 Neuron 可以在没有安装许可证的情况下运行这些模块。 

对于商业模块，Neuron 提供了 30 个点（30 个连接和 30 个数据标签）的免费额度。您可在不安装 EMQ 许可证的情况下，运行这些商业模块。超出免费额度后，则必须安装有效的试用版或官方 EMQ 许可证。

::: tip

Fanuc Focas Ethernet 和 Mitsubishi CNC 不在 30 个点免费的额度内。

:::

### 申请许可证

试用 EMQ 许可证可从 [EMQ 网站](https://www.emqx.com/zh/apply-licenses/neuron) 下载。所有可用的模块都可以在 100 个连接和 1000 个数据标签的限制下使用 15 天。 如果试用 EMQ 许可证过期，您可以通过我们的官网重新申请试用 EMQ 许可证。 但是，一个邮箱最多只能申请两次试用许可证。

官网申请试用许可证时，必须使用硬件标识进行设备的绑定。您可直接[联系我们](https://www.emqx.com/zh/contact?product=neuron)申请不需要硬件标识绑定设备的许可证，或申请正式许可证。
