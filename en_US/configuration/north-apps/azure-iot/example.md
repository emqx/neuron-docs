# Bridging Data to Microsoft Azure IoT Hub using Neuron

This article will introduce how to use Neuron to bridge data to Microsoft Azure IoT Hub through the public network so that you can easily build IoT applications.

## What is Microsoft Azure IoT Hub?

The internet of things (IoT) enables everyday physical objects to connect to the internet and intercommunicate, changing the way we live and work. Azure IoT Hub, a cloud service provided by Microsoft, is a fully managed service that enables organizations to manage, monitor, and control IoT devices.

In addition, Azure IoT Hub enables reliable, secure bidirectional communications between IoT devices and its cloud-based services. It allows developers to receive messages from, and send messages to, IoT devices, acting as a central message hub for communication. It can also help organizations make use of data obtained from IoT devices, transforming IoT data into actionable insights.


## Getting started with Azure IoT Hub

Here are the general steps for starting to use Azure IoT Hub.

### Setting up Azure IoT Hub

The initial setup process is straightforward. You will need an active Azure subscription. If you do not have one, create a free account.

Once you have an active subscription, log in to the [Azure portal]. Navigate to the IoT Hub section and click on the **Create** button. You will need to provide details like the subscription, resource group, region, and name of the IoT Hub. Once these details are filled in, click on the **Review + Create** button to create your IoT Hub.

Here we create an IoT Hub called *emqx-hub*, and its hostname is *emqx-hub.azure-devices.net*.

<figure align="center">
  <img src="./assets/azure_emqx_hub.png" style="border:thin solid #E0DCD9; width: 60%" alt="set up Azure IoT Hub">
</figure>

[Azure portal]: https://portal.azure.com/

### Registering devices to Azure IoT Hub

Once your Azure IoT Hub is set up, the next step is to register your devices to the Hub.

To register a device, navigate to the IoT devices section in your IoT Hub and click on the **Add** button. Provide a unique name for the device and click on **Save**.

Here, we registered a device *client-005* for Neuron.

<figure align="center">
  <img src="./assets/azure_add_device.png" style="border:thin solid #E0DCD9; width: 60%" alt="Azure IoT Hub add device">
</figure>

### Use Azure IoT Explorer

Once your devices are connected to Azure IoT Hub, they can start sending messages to the Hub. These messages can be telemetry data, like sensor readings, or any other data that you want to send from your devices to the cloud.
In the reverse direction, messages could be sent from the Hub to the devices.

We will use [Azure IoT Explorer] to monitor messages between Azure IoT Hub and Neuron.

The first time you run Azure IoT explorer, you're prompted for your IoT hub's connection string.
Find the *emqx-hub* IoT Hub connection string in [Azure portal].

<figure align="center">
  <img src="./assets/azure_hub_connection_string.png" style="border:thin solid #E0DCD9; width: 60%" alt="Azure IoT Hub connection string">
</figure>

After you add the connection string in Azure IoT Explorer, select **Connect**.

<figure align="center">
  <img src="./assets/azure_iot_explorer.png" style="border:thin solid #E0DCD9; width: 60%" alt="Azure IoT Explorer connect">
</figure>

[Azure IoT Explorer]: https://learn.microsoft.com/en-us/azure/iot/howto-use-iot-explorer

### Device authentication

IoT Hub uses [shared access signature] (SAS) tokens to authenticate devices and services to avoid sending keys on the wire.
You use SAS tokens to grant time-bounded access to devices and services to specific functionality in IoT Hub.
To get authorization to connect to IoT Hub, devices and services must send SAS tokens signed with either a shared access or symmetric key.

Alternatively, Azure IoT Hub can authenticate devices using X.509 certificates. For that to work, you should [create and upload certificates] first.

Azure IoT Explorer could help generate SAS tokens for convenience.

<figure align="center">
  <img src="./assets/azure_sas_token.png" style="border:thin solid #E0DCD9; width: 60%" alt="Azure IoT Explorer SAS token">
</figure>

[shared access signature]: https://learn.microsoft.com/en-us/azure/iot-hub/authenticate-authorize-sas?tabs=node
[create and upload certificates]: https://learn.microsoft.com/en-us/azure/iot-hub/tutorial-x509-test-certs?tabs=linux

## Configure Neuron

### South device

We need some south devices to collect data from. Any Neuron southbound plugin will do for this tutorial, for example, the [Modbus TCP plugin].

#### Add the *modbus-tcp* Node

Click **South Devices -> Add Device** to add a node using the Modbus TCP plugin.
This tutorial will connect to a modbus simulator at port `60502`.
<figure align="center">
  <img src="./assets/neuron_create_driver.png" style="border:thin solid #E0DCD9; width: 60%" alt="Add modbus node in Neuron dashboard">
</figure>

#### Create a Group

Click the *modbus-tcp* node to create a group. We set the group name to *group* and the interval to *1000*.
<figure align="center">
  <img src="./assets/neuron_driver_group.png" style="border:thin solid #E0DCD9; width: 60%" alt="Add a group to the modbus node in Neuron dashboard">
</figure>

#### Add tag

Click the created *group* group to create a tag with the name *tag0* and with type *INT16*.
<figure align="center">
  <img src="./assets/neuron_driver_tags.png" style="border:thin solid #E0DCD9; width: 60%" alt="Add a tag to the modbus node in Neuron dashboard">
</figure>

Finally, check that the *modbus-tcp* node is in **Connected** state.
<figure align="center">
  <img src="./assets/neuron_driver_list.png" style="border:thin solid #E0DCD9; width: 60%" alt="Neuron dashboard sourth devices tab showing modbus node connected">
</figure>

### North app

#### Add the *azure* Node

Click **North Apps -> Add Application** to add a node using the Azure IoT plugin.
<figure align="center">
  <img src="./assets/neuron_create_app.png" style="border:thin solid #E0DCD9; width: 60%" alt="Add azure node in Neuron dashboard">
</figure>

In the **Application Configuration** tab, configure the *azure* node.
In order to make MQTT connections to Azure IoT Hub, the Neuron Azure IoT plugin must be provided with either a **Shared Access Signature** or **X.509 Certificates** for authentication. Here, we provides a **SAS Token**.

<figure align="center">
  <img src="./assets/neuron_app_conf.png" style="border:thin solid #E0DCD9; width: 60%" alt="Neuron dashboard north apps tab">
</figure>

Once the configuration is submitted, the *azure* node connects to Azure IoT Hub successfully.
<figure align="center">
  <img src="./assets/neuron_app_list.png" style="border:thin solid #E0DCD9; width: 60%" alt="azure node connected state in Neuron dashboard">
</figure>

#### Subscribe to the *modbus-tcp* Node

Click the *azure* node, then click **Add subscription**, select the *modbus-tcp* node and the *group* group.

After a device connects, it can send messages to Azure IoT Hub using the MQTT topic `devices/{device-id}/messages/events/`, where `{device-id}` is the **Device ID** of the registered device.
In our case, the *azure* node will publish south device data to the topic `devices/client-005/messages/events/`.

<figure align="center">
  <img src="./assets/neuron_azure_sub.png" style="border:thin solid #E0DCD9; width: 60%" alt="azure node subscribe to modbus node">
</figure>

<figure align="center">
  <img src="./assets/neuron_azure_sub_list.png" style="border:thin solid #E0DCD9; width: 60%" alt="azure node subscribe list">
</figure>


## Monitor Data

After subscribing to the *group* group of the *modbus-tcp* node, the *azure* node will begin pushing data to the Azure IoT Hub.
Click **Monitoring**, then select the *modbus-tcp* node and the *group* group. We see that Neuron reports a initial value *0* for *tag0*.

<figure align="center">
  <img src="./assets/neuron_monitor_1.png" style="border:thin solid #E0DCD9; width: 60%" alt="Neuron dashboard data monitoring tab">
</figure>

In Azure IoT Explorer, click **Telemetry -> Start** to view the device to cloud messages. We can check that Azure IoT Hub receives the data correctly.
<figure align="center">
  <img src="./assets/azure_neuron_pub_1.png" style="border:thin solid #E0DCD9; width: 60%" alt="Azure IoT Explorer telemetry 1">
</figure>

## Write Data

In Azure IoT Explorer, click **Cloud-to-device message** to send a write request to Neuron, which writes value *42* to the tag *tag0*.
<figure align="center">
  <img src="./assets/azure_neuron_write.png" style="border:thin solid #E0DCD9; width: 60%" alt="Azure IoT Explorer write">
</figure>

Now we can see that Neuron updates *tag0* correctly in the **Data monitoring** tab.
<figure align="center">
  <img src="./assets/neuron_monitor_2.png" style="border:thin solid #E0DCD9; width: 60%" alt="Neuron dashboard data monitoring tab">
</figure>

And Azure IoT Hub receives the correct tag data, *42*, which is expected.
<figure align="center">
  <img src="./assets/azure_neuron_pub_2.png" style="border:thin solid #E0DCD9; width: 60%" alt="Azure IoT Explorer telemetry 2">
</figure>

[Modbus TCP plugin]: ../../south-devices/modbus-tcp/modbus-tcp.md
