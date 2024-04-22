# AWS IoT

[AWS IoT Core] provides secure, bi-directional communication for Internet-connected devices to connect to the AWS Cloud over MQTT.

[MQTT] is a messaging protocol designed for IoT devices and applications operating on a publish/subscribe model. It's lightweight, efficient, reliable, and allows for real-time communication. MQTT is well-suited for environments with limited resources, where efficient use of power and bandwidth is necessary.

Neuron supports MQTT as one of its communication protocols. The Neuron AWS IoT plugin is based on the [MQTT plugin] to provide easy access to AWS IoT Core.

[MQTT]: https://mqtt.org
[MQTT plugin]: ../mqtt/overview.md
[AWS IoT Core]: https://docs.aws.amazon.com/iot/

## Add Application

To create a northbound node and connect it to AWS IoT Core to upload data, navigate to **North Apps** and click **Add Application**.

- Name: The name of this application node, for example, "aws-iot".
- Plugin: Select the AWS IoT plugin.

## Configure Application

See the table below for the configuration parameters.

| Parameter                       | Description                                                  |
| ------------------------------- | ------------------------------------------------------------ |
| **Client ID**                   | MQTT client id for communication, a required field.          |
| **QoS Level**                   | MQTT QoS level for message delivery, optional, default QoS 0. |
| **Upload Format**               | JSON format of reported data, a required field: <br /><br /> - *values-format*, data are split into `values` and `errors` sub-objects. <br />- *tags-format*, tag data are put in a single array. <br /><br />Same as the MQTT plugin, see [MQTT Upstream/Downstream Data Format](../mqtt/api.md#write-tag) |
| **Write Request Topic**         | MQTT topic to which the plugin subscribes for write requests. Same as the MQTT plugin, see [MQTT Upstream/Downstream Data Format](../mqtt/api.md#write-tag) (since 2.4.5) |
| **Write Response Topic**        | MQTT topic to which the plugin sends write responses.        |
| **Device Data Endpoint**        | AWS IoT device data endpont.                                 |
| **Root CA Certificate**         | AWS IoT data endpoint root CA certificate.                   |
| **Device Certificate**          | Device Certificate corresponding to a `thing` object in the AWS IoT console. |
| **Private Key**                 | Private Key corresponding to a `thing` object in the AWS IoT console. |


## Add Subscription

After plugin configuration, data forwarding can be enabled via southbound device subscriptions.

Click the device card or row on the **North Apps** page, then **Add Subscription** on the **Group List** page. And set the following:

- **South device**: Select the southbound device you want to subscribe to, for example, 'modbus-tcp-1'.
- **Group**: Select a group from the southbound device, for example, 'group-1'.
- **Topic**: Specify the reporting topic, for example '/neuron/mqtt/upload'.

Select the desired southbound device (e.g., 'modbus-tcp-1') and group (e.g., 'group-1'). Lastly, specify the reporting topic, such as '/neuron/mqtt/upload'.

<figure align="center">
  <img src="./assets/subscribe_topic.png" style="border:thin solid #E0DCD9; width: 60%" alt="Neuron version 2.4.0 MQTT subscribe interface">
</figure>

The exact format of the data reported is controlled by the **Upload Format** parameter, and the behavior is the same as that of the MQTT plugin. For more detailed information, see [MQTT Upstream/Downstream Data Format](../mqtt/api.md#data-upload)

## Tutorial

[Bridging Data to AWS IoT using Neuron](./example.md) demonstrates how to use the AWS IoT plugin to connect to AWS IoT Core.
