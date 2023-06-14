# Sparkplug 解决方案

Sparkplug B 是一个基于 MQTT 的扩展开放互操作性协议。它使设备和应用程序能够以一种有状态的方式通过 MQTT 发送和接收消息。MQTT 并不能确保设备或应用程序收到的所有消息都是有效的和最新的。Sparkplug 通过使用 "最后意愿 "机制来确保消息是有效和最新的，从而得到改善。这使得在工业环境中使用 MQTT 成为可能。

MQTT SparkplugB 具有以下优势。
* 即插即用的 IIoT 解决方案
* 高可扩展性
* 统一的基础设施

![sparkplugB](./assets/sparkplug.png)

Neuron 是 Sparkplug 解决方案的基础设施中的 EoN 节点。它的作用是实现 EoN 节点网关，将各种不同的工业数据转换为 Sparkplug 消息，并通过 EMQX Broker or Cluster 传递给工业应用。在 Sparkplug 解决方案中使用 Neuron 的第二个原因是协助一些 "数据轮询 "设备变得更聪明，并以异步方式报告数据。

