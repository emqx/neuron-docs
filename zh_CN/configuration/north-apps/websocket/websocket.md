# Overview

[WebSocket] 是一种网络协议，它可以在单个 TCP 连接上提供双向通信通道。
WebSocket 协议于 2011 年由 IETF 标准化为 [RFC 6455] 。
其规范定义了两种方案，即 **ws**（WebSocket）和 **wss**（WebSocket Secure），分别用于非安全的和安全的连接。
WebSocket 相对传统的轮询技术具有许多优点，包括较低的延迟、较少的网络流量和更好的可伸缩性。

Neuron WebSocket 插件是一款商用的北向插件，使用户可以将采集的数据推送到 WebSocket 服务器上。

## Parameters

以下是使用 WebSocket 插件配置节点时可用的参数：

| Parameter                       | Description                                                  |
| ------------------------------- | ------------------------------------------------------------ |
| **上报数据格式**                | 上报数据的 JSON 格式。有 *values-format* 和 *tags-format* 两种格式。在 *values-format* 格式中，数据被分成 `values` 和 `errors` 的子对象。在 *tags-format* 格式中，数据被放在一个数组中。|
| **服务器 URL**                  | Websocket 服务器 URL。例如，`ws://localhost:8000` ， `wss://example.io` 。|
| **CA 证书**                     | 签发服务器证书的 CA 的证书。使用 `wss` 协议和自签发证书时，必填。         |
| **客户端证书**                  | 客户端的证书。使用 `wss` 协议且使用双向认证时，必填。                     |
| **客户端私钥**                  | 客户端的私钥。使用 `wss` 协议且使用双向认证时，必填。                     |
| **客户端私钥密码**              | 客户端的私钥密码。当提供了被加密过的**客户端私钥密码**时，必填。          |

## Data upload

Neuron WebSocket 插件作为客户端， 将从设备采集到的数据作以 JSON 形式推送到由**服务器 URL** 参数指定的 WebSocket 服务器上。

上报数据的格式由**上报数据格式**参数控制。有两种格式，即 *tags-format* 和 *values-format* 。
这两种格式与 [MQTT 插件]的相同，请参阅 [MQTT API tags 格式]。


[WebSocket]: https://en.wikipedia.org/wiki/WebSocke://en.wikipedia.org/wiki/WebSocket
[RFC 6455]: https://datatracker.ietf.org/doc/html/rfc6455
[MQTT 插件]: ../mqtt/overview.md
[MQTT API tags 格式]: ../mqtt/api.md#tags-format
