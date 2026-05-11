# Kafka

[Apache Kafka] 是一个分布式流处理平台，广泛应用于构建实时数据管道和流式应用。Kafka 具有高吞吐量、低延迟、持久化存储和水平扩展等特点，适用于大规模工业数据采集和传输场景。

Neuron Kafka 插件作为 Kafka **生产者**，将南向设备采集到的数据以 JSON 格式发布到 Kafka Topic，实现工业数据向大数据平台的高效传输。

该插件支持 SASL 认证和 SSL/TLS 加密通讯，确保数据传输的安全性。

[Apache Kafka]: https://kafka.apache.org

## 添加插件

在**配置 -> 北向应用**，点击**添加应用**添加 Kafka 节点。

## 应用配置

| 字段                 | 说明                                                         |
| -------------------- | ------------------------------------------------------------ |
| **Broker 地址**      | Kafka Broker 地址，必填。                                    |
| **默认 Topic**       | 默认 Kafka Topic，当订阅未指定 Topic 时使用，必填。          |
| **上报数据格式**     | 上报数据的 JSON 格式：<br />· **values-format**：数据被分成 `values` 和 `errors` 的子对象。<br />· **tags-format**：数据被放在一个数组中。 |
| **上报点位错误码**   | 点位采集报错时上报错误码，默认开启。关闭后，错误点位将被过滤，若所有点位均为错误则不发送消息。 |
| **压缩算法**         | 消息压缩算法，可选：none（默认）、gzip、snappy、lz4、zstd。 |
| **最大批量消息数**   | 生产者队列中最大缓冲消息数，范围 [1, 1000000]，默认 10000。 |
| **Linger 时间 (ms)** | 生产者批量发送等待时间，范围 [0, 60000]，默认 5。            |
| **消息超时 (ms)**    | 消息投递超时时间，范围 [1000, 300000]，默认 5000。           |
| **Acks**             | 生产者确认模式：-1（all，默认）、0（不确认）、1（leader 确认）。 |
| **客户端 ID**        | Kafka 客户端标识，选填。                                     |
| **安全协议**         | 通信安全协议：<br />· **plaintext**（默认）：不加密不认证。<br />· **sasl_plaintext**：SASL 认证，不加密。<br />· **ssl**：SSL/TLS 加密，不使用 SASL。<br />· **sasl_ssl**：SASL 认证 + SSL/TLS 加密。 |

### SASL 认证

当**安全协议**选择 `sasl_plaintext` 或 `sasl_ssl` 时，需配置以下参数：

| 字段             | 说明                                                         |
| ---------------- | ------------------------------------------------------------ |
| **SASL 机制**    | 认证机制：PLAIN（默认）、SCRAM-SHA-256、SCRAM-SHA-512。      |
| **SASL 用户名**  | SASL 认证用户名，必填。                                      |
| **SASL 密码**    | SASL 认证密码，必填。                                        |

### SSL/TLS

当**安全协议**选择 `ssl` 或 `sasl_ssl` 时，可配置以下参数：

| 字段             | 说明                                                         |
| ---------------- | ------------------------------------------------------------ |
| **CA 证书**      | CA 证书（Base64 编码的 PEM 格式），使用自签发证书时配置。    |
| **客户端证书**   | 客户端证书（Base64 编码的 PEM 格式），使用双向认证时配置。   |
| **客户端私钥**   | 客户端私钥（Base64 编码的 PEM 格式），使用双向认证时配置。   |

## 添加订阅

完成插件的添加和配置后，在**北向应用**页，点击设备卡片/设备列进入**组列表**页。点击**添加订阅**，并进行如下设置：

- **南向设备**：选择要订阅的南向设备；
- **组**：选择南向设备下的某个组；
- **Topic**（可选）：指定该订阅的 Kafka Topic。若不填写，则使用应用配置中的**默认 Topic**。

每个订阅可指定不同的 Topic，实现不同设备/组的数据路由到不同的 Kafka Topic。

## 运行与维护

在设备卡片或设备列，您可点击数据统计图表查看应用运行情况、接受和发送的数据情况。关于统计字段的说明，见[创建北向应用](../north-apps.md)。

如果设备运行出现任何问题，您可点击 DEBUG 日志图表，此时系统将自动打印该节点的 DEBUG 级别日志，十分钟后将切回系统默认级别日志。稍后，您可点击页面顶部功能栏的**系统信息** -> **日志**查看日志，并进行故障诊断。有关系统日志的详细解析，见[管理日志](../../../admin/log-management.md)。

## 对接 Microsoft Fabric

以下说明适用于将 NeuronEX 采集的工业数据写入 **Microsoft Fabric** 中与 Kafka 兼容的 **Eventstream** 接入场景。端到端拓扑、Eventstream 画布操作等请以 [Microsoft Fabric 文档](https://learn.microsoft.com/fabric/) 为准。

### 什么是 Microsoft Fabric

**Microsoft Fabric** 是微软提供的统一 SaaS 数据分析平台，将数据集成、数据工程、实时分析与可视化整合在同一产品体系内。**OneLake** 作为统一数据湖承载多类引擎的数据；其中的 **Real-Time Intelligence / Eventstream** 支持以 **Kafka 协议**接入流数据，云上侧无需您自建 Kafka 集群即可扩展消费与入库（例如写入 **Eventhouse**）。对 NeuronEX 而言，只要云端暴露标准 Kafka Producer 可用的 Bootstrap 地址与认证信息，即可用本页所述北向 Kafka 插件对接。

### 为什么选择 NeuronEX + Microsoft Fabric

- **补齐 OT → IT**：NeuronEX 在边缘对接 Modbus、OPC UA、各类 PLC 等工业协议，将现场时序数据规整为结构化 JSON，再由 Kafka 链路进入 Fabric，避免每条业务线单独写采集适配器。
- **边缘与云端分工**：边缘侧重低延迟采集与按需汇聚；Fabric 侧重湖仓一体、SQL/BI、数据科学与跨系统关联（ERP/MES 等），同一套云上数据底座支撑监控大屏与离线分析。
- **实时路径清晰**：Fabric Eventstream 面向秒级采样与持续流写入，和北向 Kafka 生产者模型一致，链路短、运维面相对可控。

上述优势随业务规模与合规要求而异，请以实际架构评审为准。

### NeuronEX 接入 Fabric 的两种方式

NeuronEX 可通过以下路径把数据送至 Fabric Eventstream（Kafka 兼容端点），**可同时存在**，按是否在边缘做 SQL 流处理选型即可。

| 方式 | 说明 |
|------|------|
| **数据处理 → Kafka Sink** | 南向数据先接入**数据处理（流处理）**，由 SQL 规则过滤、映射、聚合后，再通过 **Kafka Sink** 写出到 Eventstream。**适合**需在边缘删减字段、节流或按条件上云的场景。 |
| **北向 Kafka 插件（本文档）** | 南向订阅的数据由北向 Kafka 节点作为 **Kafka 生产者**直接发送至 Broker/Topic。**适合**采集层已与订阅模型对齐、希望独立于流处理控制台调整发送节奏与 Topic 路由的场景。 |

两种方式在 Fabric 侧通常都使用相同的 Eventstream Bootstrap、Topic 与 SASL 凭据；差异主要在 NeuronEX 侧是否在写出前经过数据处理引擎。

### 使用北向 Kafka 插件连接 Eventstream 的配置说明

在 Fabric 中创建 **Eventstream** 并完成 Kafka 自定义接入后，将连接信息与下列 **北向 Kafka 插件**字段对应填写。

| NeuronEX 北向 Kafka 字段 | 说明 | 示例（请以 Azure Fabric 实际内容为准） |
| ------------------------ | ---- | ---------------------------------------- |
| **Broker 地址** | Fabric Eventstream 的 Bootstrap server（含端口）。 | `neuron-eventstream.servicebus.windows.net:9093` |
| **默认 Topic** | Fabric 中为该流配置的 Topic name；若在「添加订阅」里为某条订阅单独指定了 Topic，则以订阅为准，否则用此处默认值。 | `neuron-topic` |
| **安全协议** | 使用 TLS + SASL 连接 Eventstream 时选 **`sasl_ssl`**。 | `sasl_ssl` |
| **SASL 机制** | 与 Kafka Sink 中的 **SASL Auth Type = plain** 对应，插件内选 **`PLAIN`**。 | `PLAIN` |
| **SASL 用户名** | 固定字符串。 | `$ConnectionString` |
| **SASL 密码** | Fabric **Connection string - primary key** 整段，勿截断。 | `Endpoint=sb://...` |

配置完成后，结合 NeuronEX 的运行统计或 DEBUG 日志，以及 Fabric Eventstream **数据预览**（或下游 Eventhouse 查询），确认消息持续到达。