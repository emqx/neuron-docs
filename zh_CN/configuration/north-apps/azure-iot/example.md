# 使用 Neuron 将数据桥接到 Azure IoT Hub

本文将介绍如何使用 Neuron 通过公网桥接数据到 Azure IoT Hub ，从而借助 Azure IoT Hub 轻松构建 IoT 应用程序。

## 什么是 Azure IoT Hub

物联网（IoT）使得设备能够连接到互联网并相互通信，改变了我们生活和工作的方式。Azure IoT Hub 是由微软提供的云服务，是一个完全托管的服务，使组织能够管理、监控和控制物联网设备。

此外，Azure IoT Hub 实现了可靠、安全的双向通信，连接了物联网设备和基于云的服务。它允许开发人员从物联网设备接收消息，并向其发送消息，作为通信的中心消息枢纽。它还可以帮助组织利用从物联网设备获取的数据，将物联网数据转化为可操作的洞察力。


## Azure IoT Hub 配置

以下是使用 Azure IoT Hub 的简略步骤。

### 创建 Azure IoT Hub

初始设置过程非常简单。您将需要一个有效的 Azure 订阅。如果您没有，请创建一个免费账户。

订阅后，登录 [Azure portal]。导航到 IoT Hub 标签页，然后点击**创建**按钮。您需要提供订阅、资源组、区域和 IoT Hub 的名称等详细信息。填写完这些信息后，点击**查看 + 创建**按钮来创建您的 IoT Hub。

这里我们创建一个名为 *emqx-hub* 的 IoT Hub，其域名为 *emqx-hub.azure-devices.net* 。

<figure align="center">
  <img src="./assets/azure_emqx_hub.png" style="border:thin solid #E0DCD9; width: 60%" alt="set up Azure IoT Hub">
</figure>

[Azure portal]: https://portal.azure.com/

### 注册设备到 Azure IoT Hub

在创建好 Azure IoT Hub 后，下一步是将设备注册到 Hub 中。

要注册设备，请在 IoT Hub 的 IoT 设备标签页，点击**添加**按钮。为设备提供一个唯一的名称，然后点击**保存**。

在这里，我们为 Neuron 注册了一个名为 *client-005* 的设备。

<figure align="center">
  <img src="./assets/azure_add_device.png" style="border:thin solid #E0DCD9; width: 60%" alt="Azure IoT Hub add device">
</figure>

### 使用 Azure IoT Explorer

一旦您的设备连接到 Azure IoT Hub，它们就可以开始向 Hub 发送消息。这些消息可以是遥测数据，比如传感器读数，或者您希望从设备发送到云端的任何其他数据。 相反的，消息也可以从 Hub 发送到设备。

我们将使用 [Azure IoT Explorer] 来监听 Azure IoT Hub 和 Neuron之间的消息。

第一次运行 Azure IoT Explorer 时，会提示您输入 IoT Hub 的连接字符串。 在 [Azure portal] 中找到*emqx-hub* IoT Hub的连接字符串。

<figure align="center">
  <img src="./assets/azure_hub_connection_string.png" style="border:thin solid #E0DCD9; width: 60%" alt="Azure IoT Hub connection string">
</figure>

在 Azure IoT Explorer 中添加连接字符串后，点击**连接**。

<figure align="center">
  <img src="./assets/azure_iot_explorer.png" style="border:thin solid #E0DCD9; width: 60%" alt="Azure IoT Explorer connect">
</figure>

[Azure IoT Explorer]: https://learn.microsoft.com/en-us/azure/iot/howto-use-iot-explorer

### 设备身份验证

Azure IoT Hub 使用[共享访问签名] (SAS) 令牌对设备和服务进行身份验证，以避免在网络上发送密钥。 可以使用 SAS 令牌向设备和服务授予限时访问 IoT Hub 特定功能的权限。 若要获取授权连接到 IoT Hub，设备和服务必须发送使用共享访问或对称密钥进行签名的 SAS 令牌。

如果不使用 SAS 令牌，Azure IoT Hub 也可以使用 X.509 证书对设备进行身份验证。为此，您首先需要[创建和上传证书]。

为了方便，Azure IoT Explorer 可以帮助生成 SAS 令牌。

<figure align="center">
  <img src="./assets/azure_sas_token.png" style="border:thin solid #E0DCD9; width: 60%" alt="Azure IoT Explorer SAS token">
</figure>

[共享访问签名]: https://learn.microsoft.com/en-us/azure/iot-hub/authenticate-authorize-sas?tabs=node
[创建和上传证书]: https://learn.microsoft.com/en-us/azure/iot-hub/tutorial-x509-test-certs?tabs=linux

## 配置 Neuron

### 创建南向设备

本文使用 [Modbus TCP 插件]创建南向设备，采集数据。

#### 添加 *modbus-tcp* 节点

在控制面板，点击**南向设备 -> 添加设备**，选择 Modbus TCP 插件添加节点 *modbus-tcp* 。配置节点，连接到位于端口 `60502` 的 Modbus 模拟器。
<figure align="center">
  <img src="./assets/neuron_create_driver.png" style="border:thin solid #E0DCD9; width: 60%" alt="Add modbus node in Neuron dashboard">
</figure>

#### 创建组

点击 *modbus-tcp* 节点，创建组，设置组名为 *group*，间隔为 *1000* 。
<figure align="center">
  <img src="./assets/neuron_driver_group.png" style="border:thin solid #E0DCD9; width: 60%" alt="Add a group to the modbus node in Neuron dashboard">
</figure>

#### 添加点位

添加一个点位，名字为 *tag0*，类型为 *INT16* 。
<figure align="center">
  <img src="./assets/neuron_driver_tags.png" style="border:thin solid #E0DCD9; width: 60%" alt="Add a tag to the modbus node in Neuron dashboard">
</figure>

配置完成后，*modbus-tcp* 节点显示处于连接状态。
<figure align="center">
  <img src="./assets/neuron_driver_list.png" style="border:thin solid #E0DCD9; width: 60%" alt="Neuron dashboard sourth devices tab showing modbus node connected">
</figure>

### 创建北向应用

#### 添加 *azure* 节点

点击**北向应用 -> 添加应用**，选择 Azure IoT 插件。
<figure align="center">
  <img src="./assets/neuron_create_app.png" style="border:thin solid #E0DCD9; width: 60%" alt="Add azure node in Neuron dashboard">
</figure>

在**应用配置**标签页，对 *azure* 节点进行配置。 为了建立与 Azure IoT Hub 的 MQTT 连接，Neuron Azure IoT 插件需要使用**共享访问签名（Shared Access Signature）** 或 **X.509 证书**进行身份验证。在这里，我们提供了一个 **SAS 令牌**。
<figure align="center">
  <img src="./assets/neuron_app_conf.png" style="border:thin solid #E0DCD9; width: 60%" alt="Neuron dashboard north apps tab">
</figure>

配置完成后，*azure* 节点将成功连接 Azure IoT Hub 。
<figure align="center">
  <img src="./assets/neuron_app_list.png" style="border:thin solid #E0DCD9; width: 60%" alt="azure node connected state in Neuron dashboard">
</figure>

#### 订阅 *modbus-tcp* 节点

点击 *azure* 节点，然后点击**添加订阅**，选择 *modbus-tcp* 节点和 *group* 组。

Neuron Azure IoT 连接成功后，使用 MQTT 主题`devices/{device-id}/messages/events/` 将消息发送到 Azure IoT Hub，其中 `{device-id}` 是已注册设备的**设备 ID**。 在我们的情况下，*azure* 节点将向主题 `devices/client-005/messages/events/` 发布南向设备数据。

<figure align="center">
  <img src="./assets/neuron_azure_sub.png" style="border:thin solid #E0DCD9; width: 60%" alt="azure node subscribe to modbus node">
</figure>

<figure align="center">
  <img src="./assets/neuron_azure_sub_list.png" style="border:thin solid #E0DCD9; width: 60%" alt="azure node subscribe list">
</figure>

## 监控数据

订阅 *modbus-tcp* 节点的 *group* 组后，*azure* 节点会将数据推送到 Azure IoT Hub 。点击**数据监控**，选择 *modbus-tcp* 节点和 *group* 组。可以看到 Neuron 报告了 *tag0* 的值为 *0* 。
<figure align="center">
  <img src="./assets/neuron_monitor_1.png" style="border:thin solid #E0DCD9; width: 60%" alt="Neuron dashboard data monitoring tab">
</figure>

在 Azure IoT Explorer 中，点击 **Telemetry -> Start** 以查看设备到云端的消息。我们可以验证 Azure IoT Hub 是否正确接收到数据。
<figure align="center">
  <img src="./assets/azure_neuron_pub_1.png" style="border:thin solid #E0DCD9; width: 60%" alt="Azure IoT Explorer telemetry 1">
</figure>

## 写入数据

在 Azure IoT Explorer 中，点击 **Cloud-to-device message** 向 Neuron 发送写请求，将值 *42* 写入点位 *tag0* 。
<figure align="center">
  <img src="./assets/azure_neuron_write.png" style="border:thin solid #E0DCD9; width: 60%" alt="Azure IoT Explorer write">
</figure>

在**数据监控**标签页，可以看到 Neuron 将点位 *tag0* 的值更新为写入的值 *42* 。
<figure align="center">
  <img src="./assets/neuron_monitor_2.png" style="border:thin solid #E0DCD9; width: 60%" alt="Neuron dashboard data monitoring tab">
</figure>

并且 Azure IoT Hub 也收到了更新后的点位值 *42*。
<figure align="center">
  <img src="./assets/azure_neuron_pub_2.png" style="border:thin solid #E0DCD9; width: 60%" alt="Azure IoT Explorer telemetry 2">
</figure>

[Modbus TCP 插件]: ../../south-devices/modbus-tcp/modbus-tcp.md
