# 什么是 Neuron？

Neuron 是一款轻量级工业协议网关软件，可运行在各种边缘硬件上。旨在解决工业4.0背景下设备数据难以统一访问的问题。

Neuron 通过将多种工业协议转换成标准统一的物联网 MQTT 消息，进行数据采集和远程控制，实现工业物联网平台与各种设备的互联互通，最终为以数据为中心的自动化和智能制造提供数据支撑。

Neuron 提供以下产品功能。

## 边缘原生

Neuron 的设计基于实时异步事件驱动处理，以充分利用低延迟网络方法实现 100 毫秒响应时间。 它具有非常低的内存占用，最小仅占用 10M 的内存，适合在机器附近的低配置边缘网关上运行。

## 松耦合模块化

基于解耦模块化插件的 Neuron [架构设计](./architecture.md)，通过热插拔更多的服务模块允许更多的功能扩展。每个可插拔模块独立工作，互不干扰，具有自己特定的服务能力。

## 多样化的连接

Neuron 为各个行业提供广泛多样的南向可插拔模块，包括楼宇自动化、CNC 机器、机器人、电力、各种 PLC 甚至智能传感器。 Neuron 支持对 30 多种工业协议的最广泛访问，例如 Modbus、OPCUA、Ethernet/IP、IEC104、BACnet、Siemens、Mitsubishi 等 [更多插件模块](./module-plugins/module-list.md)。北向可插拔模块包括用于云和本地 IIoT 平台连接的 MQTT 和 Websocket。

## 多源聚合

Neuron 可以同时与各种工业设备建立 1000 个或以上的连接。 同时收集所有连接的所有数据并根据用户指定的配置转发到指定的 MQTT 消息代理。也就是说，通过指定的 MQTT 代理向数据消费者提供所有信息的单一入口点，从而简化 IIoT 平台或工业应用程序从各种来源获取这些数据，例如 [统一命名空间](./use_cases.md) 架构 .

## 流式处理引擎

Neuron 集成了 [eKuiper](https://www.lfedge.org/projects/ekuiper) 流式 SQL 处理规则引擎，对采集的工业数据实现边缘侧 AI/ML 分析和控制逻辑，并将过滤后的工业数据存储起在本地时间序列数据库中或快速实现[基于规则的设备控制](./data-processing-engine/device-control.md)。

## 便携式部署

凭借超低的资源消耗，Neuron 可执行文件可以本地部署在各种边缘设备中，如 X86、ARM、RISC-V 和其他资源有限的硬件架构。它还支持容器化部署，在 K8s 和 KubeEdge 环境中与其他位于同一位置的应用程序容器一起运行。

## API 和 MQTT 服务

Neuron 提供 [HTTP-API](./reference/http-api.md) 和 [MQTT-API](./reference/mqtt-api.md) 服务，无需现场操作即可操作 Neuron 和工业设备。这允许云和本地 IIoT 平台将命令传递给连接的机器/设备，根据大数据分析结果更改其参数设置，或修改数据标签配置以适应更多机器/设备。

## 更好的集成

Neuron 通过专用的北向 MQTT 模块将 IIoT 平台、大数据和 AI/ML 分析软件更好地[集成](./integration.md)到私有云、EMQX Cloud、AWS、Google Cloud、Azure 或本地服务器中。

## 统一数据运营

Neuron 支持 SparkplugB 协议，可以通过 EMQX 代理充当 [SparkplugB 统一工业架构](./use_cases.md)的 EoN 节点，为工业应用提供统一的数据操作，消除 ERP、MES、SCADA 和 historian 访问设备数据的复杂性。

## 数据标签优化

重复或连续的数据标签将被合并到单个读/写命令中，以提高数据传输的效率。这种数据标签调节和减少机制可以减少网络和设备的工作量。

## 点位配置导入导出

Neuron 提供配置 [Excel 表导入和导出](./console-management/configuration-import-export.md)功能，以加速数据标签配置设定，并将数据标签信息保存在外部存储中。

## 身份验证和安全性

Neuron 支持加密 TLS、HTTPS 以确保传输中的数据安全，并采用 JWT auth 机制来验证数据所有者。

## 基于 Web 的仪表板

Neuron 为用户提供基于 Web 的管理界面，可以监控数据和设备状态并且可以在浏览器中在线管理连接设定的配置，并在浏览器中提供[反控设备](./console-management/device-control.md)，从而达到跨行业访问设备数据的目的。
