# 模块配置

本节主要介绍了北向应用和南向设备的参数配置，南向设备的点位信息配置规范。

::: tip
uint16 对应 word 类型。uint32 对应 dword 类型。
:::

## MQTT

Neuron 从设备采集到的数据可以通过 MQTT 应用程序传输到 MQTT Broker 中，用户也可以通过 MQTT 应用程序向 Neuron 发送指令。

### 应用配置

| 字段                | 说明                                                         |
| ------------------- | ------------------------------------------------------------ |
| **client-id**       | MQTT通信的客户端id，必填。（默认为节点名）                   |
| **upload-topic**    | 订阅数据上报的主题，必填。                                   |
| **format**          | 上报数据的json格式选择，选填，有values模式和tags模式，默认为values模式 |
| **cache-mem-size**  | 通信失败时内存消息缓存大小(MB)限制，必填。范围在[0, 1024], 默认 0。 须不大于*cache-disk-size*。|
| **cache-disk-size** | 通信失败时磁盘消息缓存大小(MB)限制，必填。范围在[0, 10240], 默认 0。设为非零值时, *cache-mem-size*也须为非零值。|
| **host**            | MQTT Broker 主机，必填。                                     |
| **port**            | MQTT Broker 端口号，必填。                                   |
| **username**        | 连接到 Broker 时使用的用户名，选填。                         |
| **password**        | 连接到 Broker 时使用的密码，选填。                           |
| **ssl**             | 是否启用 mqtt ssl，选填，默认 false                          |
| **ca**              | ca文件，只在ssl值为true时启用，这种情况下为必填。            |
| **cert**            | cert文件，只在ssl值为true时启用，选填。                      |
| **key**             | key文件，只在ssl值为true时启用，选填。                       |
| **keypass**         | key文件密码，只有在ssl值为true时启用，选填。                 |

## Sparkplug_B

Neuron 从设备采集到的数据可以通过Sparkplug_B协议从边缘端传输到Sparkplug_B应用中，用户也可以从应用程序向 Neuron 发送数据修改指令。Sparkplug_B是运行再MQTT之上的应用型协议，所以在Neuron中的设置与MQTT驱动相似。

### 应用配置

| 字段          | 说明                                                         |
| ------------- | ------------------------------------------------------------ |
| **client-id** | MQTT 客户端 ID，连接的唯一标识，必填                         |
| **group-id**  | Sparkplug_B 协议中的最顶层逻辑分组，可以代表工厂或车间等实体，必填 |
| **node-id**   | Sparkplug_B 协议中的边缘节点唯一标识，必填                   |
| **ssl**       | 是否启用 mqtt ssl，默认 false                                |
| **host**      | MQTT Broker 主机，必填                                       |
| **port**      | MQTT Broker 端口号，必填                                     |
| **username**  | 连接到 Broker 时使用的用户名，可选填                         |
| **password**  | 连接到 Broker 时使用的密码，可选填                           |
| **ca**        | ca 文件，只在 ssl 值为 true 时启用，这种情况下为必填         |
| **cert**      | cert 文件，只在 ssl 值为 true 时启用，可选填                 |
| **key**       | key 文件，只在 ssl 值为 true 时启用，可选填                  |
| **keypass**   | key 文件密码，只有在 ssl 值为 true 时启用，可选填            |