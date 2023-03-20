# MQTT 介绍及使用

## 模块描述

Neuron 从设备采集到的数据可以通过 MQTT 应用程序传输到 MQTT Broker 中，用户也可以通过 MQTT 应用程序向 Neuron 发送指令。

## 应用配置

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