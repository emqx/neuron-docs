# Azure IoT

[Azure IoT Hub] 实现了可靠、安全的双向通信，将物联网设备与基于云的服务连接起来。作为通信的中心消息枢纽，它允许开发人员从物联网设备接收消息，并向其发送消息。

[MQTT] 是一种轻量级的消息传输协议，专为物联网设备和应用程序设计。它采用发布与订阅模型，允许设备和应用程序通过中间代理（Broker）进行通信。MQTT拥有轻量级、高效率和可靠性等诸多优点，特别适用于边缘硬件资源有限，需要高效地传输实时数据，以及对通信延迟和带宽占用有要求的场景。
MQTT协议在工业互联网中得到广泛选择和应用，它为工业互联网带来了实时数据交换、设备互通性、资源节约和稳定可靠等诸多价值，成为工业互联网通信的重要基石。

Neuron 支持 MQTT 插件作为其数据汇聚上报的方式之一。 Neuron Azure IoT 插件基于 [MQTT 插件]，提供对 Azure IoT Hub 的便捷接入。

[MQTT]: https://mqtt.org
[MQTT 插件]: ../mqtt/overview.md
[Azure IoT Hub]: https://learn.microsoft.com/en-us/azure/iot/

## 添加插件

在**北向应用**标签页，点击 **添加应用** 添加节点。

## 应用配置

以下是使用 Azure IoT 插件配置节点时可用的参数：

| 字段               | 说明                                                         |
| ------------------ | ------------------------------------------------------------ |
| **设备 ID**        | Azure IoT Hub 的设备 ID，必填。                              |
| **QoS 等级**       | MQTT 通信的服务质量等级，可选，默认为 QoS 0 。               |
| **上报数据格式**   | 上报数据的 JSON 格式：<br />· *values-format*：数据被分成 `values` 和 `errors` 的子对象。<br />· *tags-format*：数据被放在一个数组中。关于通信数据格式，见 [数据上下行格式](../mqtt/api.md#数据上报) |
| **IoT 中心域名**   | Azure IoT 中心域名。                                         |
| **身份验证**       | 设备身份验证方式，使用 Shared Access Signature 或者 X.509 证书。|
| **SAS 令牌**       | 使用 Shared Access Signature 身份验证方式时，需要提供 SAS 令牌。|
| **CA 证书**        | 使用 X.509 证书身份验证方式时，需要提供 CA 证书。               |
| **设备证书**       | 使用 X.509 证书身份验证方式时，需要提供设备证书。               |
| **设备私钥**       | 使用 X.509 证书身份验证方式时，需要提供设备私钥。               |

## 添加订阅

完成插件的添加和配置后，我们将继续通过订阅南向设备实现数据的转发。

完成设备配置后，在**北向应用**页，点击设备卡片/设备列进入**组列表**页。点击**添加订阅**，并进行如下设置：

- **南向设备**：选择要订阅的南向设备，例如，modbus-tcp-1；

- **组**：选择南向设备下的某个组，例如，group-1。

在 Azure IoT 插件成功连接后，它将通过 MQTT 主题 `devices/{device-id}/messages/events/` 向 Azure IoT Hub 发送数据，其中 `{device-id}` 是设备的**设备 ID**。

上报数据的确切格式由**上报数据格式**参数控制，行为与 MQTT 插件一样。更多详细信息，请参阅 [数据上下行格式](../mqtt/api.md#data-upload)。

## Write tags using cloud-to-device messages

Azure IoT 插件通过 MQTT 主题 `devices/{device-id}/messages/events/` 接收来自 Azure IoT Hub 的写入请求，其中 `{device-id}` 是设备的**设备 ID**。
写入请求的数据格式与 MQTT 插件一致，见[数据上下行格式](../mqtt/api.md#写-tag)。

## 教程

[使用 Neuron 将数据桥接到 Azure IoT Hub](./example.md) 教程演示了如何使用 Azure IoT 插件连接 Azure IoT Hub 。
