# Neuron 简介

Neuron 是运行在各类物联网边缘网关硬件上的工业协议商业化网关软件，支持一站式接入和解析数十种工业协议，并转换成 MQTT 协议接入工业物联网平台。用户可以通过基于 Web 的管理控制台可以实现在线的网关配置管理；Neuron 的资源占用很低，并且同时支持 X86、ARM、MIPS 三大 CPU 架构。

- 支持了 Modbus，OPCUA，IEC61850，IEC104 和 BACnet 等众多协议和设备；
- 管理控制台，用户可以在浏览器中进行可视化的配置，实现跨工业设备数据的接入；
- 北向标准 MQTT 数据发送，根据用户指定配置，将数据发送至指定的 MQTT 消息服务器中；
- 南向控制接口，Neuron 监听控制设备的主题，将相关的控制命令转发给设备。结合 EMQ X Kuiper 提供的规则引擎功能，快速实现基于规则的设备控制；
- 本地数据存储，实现设备原始数据的存储和查看；

Neuron 与 EMQ 在边缘的其它产品集成，可以轻松实现一个端到端的[云边协同的工业互联网解决方案](https://www.emqx.cn/blog/emq-industrial-internet-cloud-edge-integrated-solution)。

**以下为本文档内容的基本介绍，读者可以根据情况阅读相关的内容**

## 安装与快速使用

- [安装](getting-started/install.md)：在不同操作系统下的下载和安装过程文档。

- [快速教程](getting-started/quick_start.md)：3分钟 Neuron Docker 使用教程，Neuron 从 Modbus TCP 模拟器中读取数据，并在管理控制台中展示原始数据的过程。

## 管理控制台使用

- Neuron 提供了基于 web 的管理控制台界面，用户可以通过控制台实现在浏览器中进行可视化的配置。

## 驱动列表及使用说明

- [驱动列表](neuron-driver.md)：内包含一系列常见的驱动以及相关的配置信息。
