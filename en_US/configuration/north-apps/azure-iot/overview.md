# Azure IoT

[Azure IoT Hub] enables reliable, secure bidirectional communications between IoT devices and its cloud-based services. It allows developers to receive messages from, and send messages to, IoT devices, acting as a central message hub for communication. It can also help organizations make use of data obtained from IoT devices, transforming IoT data into actionable insights.

[MQTT] is a messaging protocol designed for IoT devices and applications operating on a publish/subscribe model. It's lightweight, efficient, reliable, and allows for real-time communication. MQTT is well-suited for environments with limited resources, where efficient use of power and bandwidth is necessary.

Neuron supports MQTT as one of its communication protocols. The Neuron Azure IoT plugin is based on the [MQTT plugin] to provide easy access to Azure IoT .

[MQTT]: https://mqtt.org
[MQTT plugin]: ../mqtt/overview.md
[Azure IoT Hub]: https://learn.microsoft.com/en-us/azure/iot/

## Add Application

To create a northbound node and connect it to Azure IoT Hub to upload data, navigate to **North Apps** and click **Add Application**.

- Name: The name of this application node, for example, "azure-iot".
- Plugin: Select the Azure IoT plugin.

## Configure Application

See the table below for the configuration parameters.

| Parameter                       | Description                                                  |
| ------------------------------- | ------------------------------------------------------------ |
| **Device ID**                   | Azure IoT Hub device ID.                                     |
| **QoS Level**                   | MQTT QoS level for message delivery, optional, default QoS 0. |
| **Upload Format**               | JSON format of reported data, a required field: <br /><br /> - *values-format*, data are split into `values` and `errors` sub-objects. <br />- *tags-format*, tag data are put in a single array. <br /><br />Same as the MQTT plugin, see [MQTT Upstream/Downstream Data Format](../mqtt/api.md#write-tag) |
| **IoT Hub Hostname**            | Azure IoT Hub hostname (full CName).                         |
| **Authentication**              | Azure IoT Hub device authentication method, uses either Shared Access Signature or X.509 Certificates. |
| **SAS Token**                   | SAS token, required if using Shared Access Signature authentication.   |
| **Root CA Certificate**         | CA certificate, required if using X.509 authentication.                |
| **Device Certificate**          | Device Certificate, required if using X.509 authentication.            |
| **Private Key**                 | Device Private Key, required if using X.509 authentication.            |


## Add Subscription

After plugin configuration, data forwarding can be enabled via southbound device subscriptions.

Click the north app on the **North Apps** page, then **Add Subscription** on the **Group List** page. And set the following:

- **South device**: Select the southbound device you want to subscribe to, for example, 'modbus-tcp-1'.
- **Group**: Select a group from the southbound device, for example, 'group-1'.

Select the desired southbound device (e.g., 'modbus-tcp-1') and group (e.g., 'group-1').

After the Azure IoT plugin connects successfully,  it will send messages to Azure IoT Hub using the MQTT topic `devices/{device-id}/messages/events/`, where `{device-id}` is the **Device ID**.

The exact format of the data reported is controlled by the **Upload Format** parameter, and the behavior is the same as that of the MQTT plugin. For more detailed information, see [MQTT Upstream/Downstream Data Format](../mqtt/api.md#data-upload)

## Write tags using cloud-to-device messages

The Azure IoT plugin could receive write requests from Azure IoT Hub cloud-to-device messages on the MQTT topic `devices/{device-id}/messages/events/`, where `{device-id}` is the **Device ID**.
The write request data format is the same as the MQTT plugin, see [MQTT Upstream/Downstream Data Format](../mqtt/api.md#write-tag).

## Tutorial

[Bridging Data to Azure IoT Hub using Neuron](./example.md) demonstrates how to use the Azure IoT plugin to connect to Azure IoT Hub.
