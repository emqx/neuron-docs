# Sparkplug_B 介绍及使用

## 模块描述

Neuron 从设备采集到的数据可以通过Sparkplug_B协议从边缘端传输到Sparkplug_B应用中，用户也可以从应用程序向 Neuron 发送数据修改指令。Sparkplug_B是运行再MQTT之上的应用型协议，所以在Neuron中的设置与MQTT驱动相似。

## 应用配置

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