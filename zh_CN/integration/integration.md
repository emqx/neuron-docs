# 集成

作为物联网（IoT）和工业物联网（IIoT）生态的有机组成部分，Neuron 在设备现场和各种分析平台之间发挥着重要的桥梁作用。本章将深入探讨 Neuron 与不同生态系统组件的集成。

## 连接南向设备

南向设备，如 PLC、远程终端单元（RTU）、智能传感器、数控机床、机器人、电力设备以及建筑自动化系统等，是 IoT 和 IIoT 生态环境中的主要数据来源。Neuron 凭借其对众多通信协议的兼容性，支持连接这些现场设备并进行数据采集，为后续的数据分析和决策提供基础。

## 集成 EMQX/eKuiper

Neuron 收集到的边缘数据，可被转发至 eKuiper 或 EMQX Broker 进一步处理。

eKuiper 是一个实时流数据处理系统，主要用于时间序列数据库的处理。Neuron 与 eKuiper 的集成能够实时分析数据，对数据流的变化做出即时响应，从而充分发挥在边缘侧的低延迟处理等优势。处理后的流数据可存储在边缘侧的时间序列数据库中，如 InfluxDB。

作为一款开源的 MQTT 代理，EMQX Broker 可将数据转发到企业 ERP 系统或 MES 系统中，从而实现有效的资源管理和生产控制。

此外，你还可以利用 [云边协同的企业级 MQTT 物联网管理平台 EMQX ECP](https://www.emqx.com/zh/products/emqx-ecp) 集中管理 Neuron 与 EMQX/eKuiper 的集成。

## 集成云平台

Neuron 可以通过 MQTT 和 REST 与各种云平台集成，包括 EMQX Cloud、AWS、Google Cloud Platform 和 Microsoft Azure，将实时工业数据直接无缝地流向工业应用，如 MES、ERP、大数据、分析软件等等，实现各类复杂的数据处理和存储场景。

![integrations](./assets/integration.png)

本章主要介绍以下场景：

1. [Neuron 集成 eKuiper](./ekuiper/ekuiper.md)，通过边缘端的流式 SQL 语句实现 AI/ML 分析、数据过滤、数据操作、设备控制和时间序列数据库中的数据持久化。
2. [Neuron 集成 EMQX](./sparkplug/sparkplug.md)，提供 Sparkplug 工业通信能力。
