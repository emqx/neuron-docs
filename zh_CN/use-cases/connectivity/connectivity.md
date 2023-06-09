# 工业设备连接

Neuron 通常用于工厂数字化改造，将不同的原生协议设备连接到支持 MQTT 或 API 的多个工业信息应用，如 MES、ERP、SCADA、IIoT 平台和分析系统。Neuron 还允许这些工业应用发回命令来监控、管理和控制现场设备。

多个 Neuron 可以部署在地区站点的边缘一侧，用于实时收集各种设备的数据。一些设备是直接连接的，其他的可能是通过 DTU 连接。实时数据通过 EMQX Broker 报告给数据中心。通过规则引擎过滤后，数据被存储或转发到相关的分析系统和应用程序。

![district-site](./assets/district-site.png)

单个 Neuron 可以部署在小型本地站点的边缘一侧。

![small-site](./assets/small-site.png)

Neuron 可以支持多达数千台设备的连接，并将信息转发给数百个工业应用。每个应用都可以在与 EMQX 代理的单点连接中访问所有设备信息。

由于 Neuron 可能包含多达上万个数据标签，必须提供工具来加速部署。因此，Neuron 提供了 Excel 文件配置功能，用户可以导出和导入来定义数据标签。Neuron 还为应用程序提供 API 配置来管理数据标签。

