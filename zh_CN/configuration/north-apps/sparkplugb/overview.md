# SparkPlugB

Sparkplug B 是一种建立在 MQTT 3.1.1 基础上的工业物联网数据传输规范。Sparkplug B 在保证灵活性和效率的前提下，使 MQTT 网络具备状态感知和互操作性，为设备制造商和软件提供商提供了统一的数据共享方式。

Neuron 从设备采集到的数据可以通过 Sparkplug B 协议从边缘端传输到 Sparkplug B 应用中，用户也可以从应用程序向 Neuron 发送数据修改指令。

Sparkplug B 是运行在 MQTT 之上的应用型协议，所以在 Neuron 中的设置与 MQTT 驱动相似。

## 添加插件

在**配置 -> 北向应用**，点击 **添加应用** 添加 SparkPlugB 客户端节点。

## 应用配置

Sparkplug B 是运行在 MQTT 之上的应用型协议，所以在 Neuron 中的设置与 MQTT 驱动相似。

|  参数         | 说明                                                         |
| ------------- | ------------------------------------------------------------ |
| **客户端 ID** | MQTT 客户端 ID，连接的唯一标识                                 |
| **组 ID**  | Sparkplug B 协议中的最顶层逻辑分组，可以代表工厂或车间等实体     |
| **节点 ID**   | Sparkplug B 协议中的边缘节点唯一标识                           |
| **SSL**       | 是否启用 mqtt ssl，默认 false                                 |
| **服务器地址**      | MQTT Broker 主机                                             |
| **服务器端口**      | MQTT Broker 端口号                                           |
| **用户名**  | 连接到 Broker 时使用的用户名                                  |
| **密码**  | 连接到 Broker 时使用的密码                                    |
| **CA 证书**        | ca 文件，只在 ssl 值为 true 时启用                            |
| **客户端证书**      | cert 文件，只在 ssl 值为 true 时启用                          |
| **客户端私钥**       | key 文件，只在 ssl 值为 true 时启用                           |
| **私钥密码**   | key 文件密码，只有在 ssl 值为 true 时启用                     |

:::tip
以上参数中只有 **组 ID** 和 **节点 ID** 来源于 Sparkplug B 规范，其余均为 MQTT Broker 的连接参数，可以参阅 [MQTT 概览](../mqtt/overview.md)。
:::

## 订阅南向数据

采集点位是以组为单位进行数据上传的，订阅选择要上传的点位组。

点击 SparkPlugB 节点卡片，进入**组列表**页，点击 **添加订阅** 选择要订阅的点位组，订阅南向设备的点位组。完成订阅后，我们的北向 SparkPlug B 应用将开始接受南向数据。

## 应用场景

您可通过 Neuron Sparkplug B 插件将数据上报到 EMQX，并通过 EMQX 的编解码功能得到正确完整的数据结果，具体结果，见 [集成 EMQX](./sparkplug.md)。

您可通过 Neuron SparkPlugB 插件连接 Ignition 平台，具体步骤，见 [Ignition](./ignition.md)。

您也可通过 Neuron SparkPlugB 插件连接 Cogent DataHub，具体步骤，见 [Cogent](./cogent.md)。

## 运行与维护

在设备卡片或设备列，您可点击数据统计图表查看及应用运行情况、接受和发送的数据情况。关于统计字段的说明，见[创建北向应用](../north-apps.md)。

如果设备运行出现任何问题，您可点击 DEBUG 日志图表，此时系统将自动打印该节点的 DEBUG 级别日志，十分钟后将切回系统默认级别日志。稍后，您可点击页面顶部功能栏的**系统信息** -> **日志**查看日志，并进行故障诊断。稍后，您可点击页面顶部功能栏的**系统信息** -> **日志**查看日志，并进行故障诊断。有关系统日志的详细解析，见[管理日志](../../../admin/log-management.md)。
