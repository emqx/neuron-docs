# 概览

LF Edge [eKuiper] 是 Golang 实现的轻量级物联网边缘分析、流式处理开源软件，可以运行在各类资源受限的边缘设备上。
eKuiper 的主要目标是在边缘端提供一个流媒体软件框架。
eKuiper 的规则引擎允许用户提供基于 SQL 或基于图形的规则，在几分钟内创建物联网边缘分析应用。

Neuron eKuiper 插件使用户能够将收集到的数据发布到 eKuiper 以进一步处理。
作为一款工业网关，Neuron 为众多使用不同协议的不同设备提供一站式访问，而 eKuiper 具有数据过滤、聚合、转换和路由的能力。
将两个产品结合在一起，您将得到双重优势，这极大地降低了边缘计算解决方案的资源要求，并能发掘更多的用例。
更棒的是，Neuron eKuiper 插件是开源的。

## 参数

从 Neuron 2.4.0 版本开始，使用 eKuiper 插件时可使用如下参数。

| 字段                | 说明                                                         |
| ------------------- | ------------------------------------------------------------ |
| **本地 IP 地址**    | 监听来自 eKuiper 的连接的 IP 地址。                          |
| **本地端口**        | 监听来自 eKuiper 的连接的 TCP 端口号                         |

## 集成 eKuiper

Neuron 和 eKuiper 之间的交互是双向的，需要两边同时提供支持：
* Neuron 方面，提供 eKuiper 插件以支持向 eKuiper 发布数据并接收命令。
* eKuiper 方面，提供一个 Neuron 源以支持从 Neuron 订阅数据，以及一个 Neuron 动作以支持通过 Neuron 控制设备。

Neuron 2.0.0 版本首次发布了 eKuiper 插件，而 eKuiper 1.5.0 版本首次添加了 Neuron 源和动作。
双方使用基于 [IPC 传输层]的 [NNG pair0 协议]进行通信，而该协议只允许在同一主机上进行一对一通信。
因此，需要在同一主机上部署 Neuron 和 eKuiper 以达到正常功能。

::: tip
您也可以使用 MQTT 作为 Neuron 和 eKuiper 双方之间的中继。
:::

从 Neuron 2.4.0 版本开始， eKuiper 插件从 IPC 传输层切换到了 [TCP 传输层]，而 eKuiper 1.9.0 版本开始也采用了 TCP 传输层。
使用 TCP 传输层去除了在同一主机上部署 Neuron 和 eKuiper 的限制，并允许 Neuron 和 eKuiper 之间建立多个连接。

::: tip
从 Neuron 2.0 和 eKuiper 1.5 开始，两端使用 IPC 传输层实现一对一的连接。
从 Neuron 2.4 和 eKuiper 1.9 开始，两端使用 TCP 传输层，并支持多对多的连接
:::

### NeuronEX

为了简化部署和更好的用户体验，从 2.3.0 版本起，与 Neuron 一起发布了 NeuronEX。
NeuronEX 在一个包里集成了 Neuron 和 eKuiper，并且使用增强版的仪表板。
NeuronEX 默认提供了一个 **data-stream-processing** 北向节点。
使用 NeuronEX，用户可以直接通过仪表板轻松管理 eKuiper 规则或者执行其他流处理操作。

### 内部实现

本节描述了 Neuron 和 eKuiper 之间的底层通信细节。如果您不关心这些细节，可以跳过本节。

#### 数据上报

Neuron eKuiper 插件连接到 eKuiper 后，将从设备收集的数据以 JSON 形式发布。
发布到 eKuiper 的数据具有以下字段：
* `timestamp` : 数据采集时的 UNIX 时间戳。
* `node_name` : 被采集的南向节点的名字。
* `group_name` : 被采集的南向节点的点位组的名字。
* `values` : 存储采集成功的点位值的字典。
* `errors` : 存储采集失败的错误码的字典。

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

#### 反向控制

eKuiper 可以通过使用 Neuron 动作发送写命令来控制设备，Neuron 在接收到命令后将向设备写入数据。

写命令应该是一个带有以下字段的 JSON 数据：
* `node_name` : 某个南向节点名字。
* `group_name` : 南向节点的某个组的名字。
* `tag_name` : 要写入的点位名字。
* `value` : 要写入的数据值。

以下是一个写命令示例：

``` json
{
    "node_name": "modbus",
    "group_name": "grp",
    "tag_name": "tag0",
    "value": 1234
}
```

## 示例

[eKuiper]: https://ekuiper.org
[NNG pair0 协议]: https://nng.nanomsg.org/man/v1.3.2/nng_pair.7.html
[IPC 传输层]: https://nng.nanomsg.org/man/v1.3.2/nng_ipc.7.html
[TCP 传输层]: https://nng.nanomsg.org/man/v1.3.2/nng_tcp.7.html
[使用 eKuiper 对 Neuron 采集的数据进行流式处理]: https://ekuiper.org/docs/zh/latest/integrations/neuron/neuron_integration_tutorial.html#integration-of-neuron-and-ekuiper
