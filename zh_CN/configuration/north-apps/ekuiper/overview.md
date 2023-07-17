# eKuiper

LF Edge [eKuiper] 是 Golang 实现的轻量级物联网边缘分析、流式处理开源软件，可以运行在各类资源受限的边缘设备上。eKuiper 的主要目标是在边缘端提供一个流媒体软件框架，并通过内置的规则引擎帮助用户在几分钟内创建物联网边缘分析应用。

作为一款工业网关，Neuron 为众多使用不同协议的不同设备提供一站式访问，而 eKuiper 具有数据过滤、聚合、转换和路由的能力。Neuron eKuiper 插件使用户能够将收集到的数据发布到 eKuiper 以进一步处理。二者的组合将能极大降低边缘计算解决方案的资源要求，满足更加丰富的场景需求。

## 方案优势

- <b>扩展的数据分析能力</b>：Neuron可以提供先进的实时数据分析功能，例如异常检测、预测性维护和优化算法，为工业物联网部署提供更全面、更智能的解决方案。
- <b>边缘计算能力</b>：Neuron可以在边缘处理数据，靠近工业设备，减少延迟，实现更快的响应时间。
- <b>无缝的数据处理和转换</b>： Neuron支持数据提取、转换和加载（ETL），可以在数据用于分析之前高效地预处理和清洗数据，确保云端AI/ML分析功能的数据质量和一致性。
- <b>基于数据驱动的边缘决策</b>：Neuron可以在本地分析和处理基于AI的洞察，而不仅仅依赖于基于云的决策系统。

## 添加插件

在**配置 -> 北向应用**，点击 **添加应用** 添加 eKuiper 客户端节点。

## 应用配置

从 Neuron 2.4.0 版本开始，使用 eKuiper 插件时可使用如下参数：

| 字段             | 说明                             |
| ---------------- | -------------------------------- |
| **本地 IP 地址** | 监听 eKuiper 连接的 IP 地址。    |
| **本地端口**     | 监听 eKuiper 连接的 TCP 端口号。 |

## 添加订阅

完成插件的添加和配置后，我们将继续通过订阅南向设备实现数据的转发。

完成设备配置后，在**北向应用**页，点击设备卡片/设备列进入**组列表**页。点击**添加订阅**，并进行如下设置：

- **南向设备**：选择要订阅的南向设备，例如，modbus-tcp-1；
- **组**：选择南向设备下的某个组，例如，group-1。

至此，我们将能通过 Neuron 将数据转发至 eKuiper 进行下一步处理。

有关在 eKuiper 中的操作，见[使用 eKuiper 对 Neuron 采集的数据进行流式处理](https://ekuiper.org/docs/zh/latest/integrations/neuron/neuron_integration_tutorial.html#integration-of-neuron-and-ekuiper)。

## 应用场景

通过 Neuron eKuiper 插件，您可在 Neuron 和 eKuiper 之间建立直接的数据通道，具体步骤，见 [通过 Docker 集成 Neuron 与 eKuiper](./ekuiper.md)。

## 运行与维护

在设备卡片或设备列，您可点击数据统计图表查看及应用运行情况、接受和发送的数据情况。关于统计字段的说明，见[创建北向应用](../north-apps.md)。

如果设备运行出现任何问题，您可点击 DEBUG 日志图表，此时系统将自动打印该节点的 DEBUG 级别日志，十分钟后将切回系统默认级别日志。稍后，您可点击页面顶部功能栏的**系统信息** -> **日志**查看日志，并进行故障诊断。稍后，您可点击页面顶部功能栏的**系统信息** -> **日志**查看日志，并进行故障诊断。有关系统日志的详细解析，见[管理日志](../../../admin/log-management.md)。

<!--这里感觉应该把ekuiper部分的操作也贴进来-->

## 版本兼容性

Neuron 和 eKuiper 之间的交互是双向的，需要两边同时提供支持：
* Neuron 方面，提供 eKuiper 插件以支持向 eKuiper 发布数据并接收命令。
* eKuiper 方面，提供一个 Neuron 源以支持从 Neuron 订阅数据，以及一个 Neuron 动作以支持通过 Neuron 控制设备。

| Neuron 版本       | eKuiper 版本      | 发布历史                                                     | 使用限制                                                     |
| ----------------- | ----------------- | ------------------------------------------------------------ | ------------------------------------------------------------ |
| Neuron 2.0        | eKuiper 1.5       | 1. Neuron 首次引入 eKuiper 插件<br />2. eKuiper 首次添加 Neuron 源和动作 <br />3. Neuron 和 eKuiper 基于 [IPC 传输层]的 [NNG pair0 协议]进行通信<br /> | 1. Neuron 和 eKuiper 应部署在同一个主机（或使用 MQTT 作为双方之间的中继）<br />2. 一对一通信 |
| Neuron 2.4 及以上 | Neuron 1.9 及以上 | 1. Neuron 和 eKuiper 基于 [TCP 传输层] 进行通信 <br />2. 支持多对多连接 | -                                                            |

 传输协议的变化如下图所示：![connection_change](./assets/connection_change.png)

## 拓展阅读

本节描述了 Neuron 和 eKuiper 之间的底层通信细节，可选择跳过。

### 数据上报

Neuron eKuiper 插件连接到 eKuiper 后，将从设备收集的数据以 JSON 形式发布。
发布到 eKuiper 的数据具有以下字段：
* `timestamp`：数据采集时的 UNIX 时间戳。
* `node_name`：被采集的南向节点的名字。
* `group_name`：被采集的南向节点的点位组的名字。
* `values`：存储采集成功的点位值的字典。
* `errors`：存储采集失败的错误码的字典。

以下是一个示例数据。当标签读取成功时，它的值将记录在 *values* 字典中。
如果在读取标签时出错，则将错误代码记录在 *errors* 字典中。

``` json
{
  "timestamp": 1646125996000,
  "node_name": "modbus", 
  "group_name": "grp",
  "values": {
    "tag0": 42,
    "tag1": "string"
  },
  "errors": {
    "tag2": 1011
  }
}
```

### 反向控制

eKuiper 可以通过使用 Neuron 动作发送写命令来控制设备，Neuron 在接收到命令后将向设备写入数据。

写命令应该是一个带有以下字段的 JSON 数据：
* `node_name`：某个南向节点名字。
* `group_name`：南向节点的某个组的名字。
* `tag_name`：要写入的点位名字。
* `value`：要写入的数据值。

以下是一个写命令示例：

``` json
{
    "node_name": "modbus",
    "group_name": "grp",
    "tag_name": "tag0",
    "value": 1234
}
```

## 更多资源

eKuiper 也有一份教程[使用 eKuiper 对 Neuron 采集的数据进行流式处理]。

[eKuiper]: https://ekuiper.org
[NNG pair0 协议]: https://nng.nanomsg.org/man/v1.3.2/nng_pair.7.html
[IPC 传输层]: https://nng.nanomsg.org/man/v1.3.2/nng_ipc.7.html
[TCP 传输层]: https://nng.nanomsg.org/man/v1.3.2/nng_tcp.7.html
[使用 eKuiper 对 Neuron 采集的数据进行流式处理]: https://ekuiper.org/docs/zh/latest/integrations/neuron/neuron_integration_tutorial.html#integration-of-neuron-and-ekuiper
