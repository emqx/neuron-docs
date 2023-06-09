# 集成

Neuron 可以通过 MQTT 和 REST 与各种云平台集成，包括 EMQX Cloud、AWS、Google Cloud Platform 和 Microsoft Azure，将实时工业数据直接无缝地流向工业应用，如 MES、ERP、大数据、分析软件等等。

Neuron 还为数据分析 AI/ML 提供了一个集成的 SQL 流处理规则引擎 eKuiper，以利用边缘侧低延迟处理的优势。输出的流数据可以存储在边缘侧的 influxdb 等时间序列数据库中。

![integrations](./assets/integration.png)

Neuron可以与eKuiper集成，提供[边缘处理](./ekuiper/ekuiper.md)能力。
Neuron 集成基于规则的处理引擎 eKuiper，可以通过边缘端的流式 SQL 语句实现 AI/ML 分析、数据过滤、数据操作、设备控制和时间序列数据库中的数据持久化。



Neuron可以与EMQX集成，提供[支持Sparkplug](./sparkplug/sparkplug.md)的工业通信功能。
