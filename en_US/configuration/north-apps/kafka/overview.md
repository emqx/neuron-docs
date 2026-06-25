# Kafka

[Apache Kafka] is a distributed streaming platform widely used for building real-time data pipelines and streaming applications. Kafka offers high throughput, low latency, durable storage, and horizontal scalability, making it well-suited for large-scale industrial data collection and transmission scenarios.

The Neuron Kafka plugin works as a Kafka **producer**, publishing data collected from southbound devices to Kafka topics in JSON format, enabling efficient data delivery to big data platforms.

The plugin supports SASL authentication and SSL/TLS encrypted communication to ensure data security.

[Apache Kafka]: https://kafka.apache.org

## Add Application

Navigate to **Configuration -> North Apps** and click **Add Application** to add a Kafka node.

## Configure Application

| Parameter              | Description                                                  |
| ---------------------- | ------------------------------------------------------------ |
| **Broker Address**     | Kafka Broker address, required.                              |
| **Default Topic**      | Default Kafka topic, used when a subscription does not specify one, required. |
| **Upload Format**      | JSON format of reported data: <br />- **values-format**: Data split into `values` and `errors` sub-objects. <br />- **tags-format**: Tag data put in a single array. |
| **Upload Tag Error Code** | Report tag error codes on collection errors, default enabled. When disabled, error tags are filtered out; if all tags are errors, no message is sent. |
| **Compression**        | Message compression algorithm: none (default), gzip, snappy, lz4, zstd. |
| **Max Batch Messages** | Maximum number of messages buffered in the producer queue. Range [1, 1000000], default 10000. |
| **Linger Time (ms)**   | Producer batching wait time. Range [0, 60000], default 5.    |
| **Message Timeout (ms)** | Message delivery timeout. Range [1000, 300000], default 5000. |
| **Acks**               | Producer acknowledgment mode: -1 (all, default), 0 (no ack), 1 (leader ack). |
| **Client ID**          | Kafka client identifier, optional.                           |
| **Security Protocol**  | Communication security protocol: <br />- **plaintext** (default): No encryption, no authentication. <br />- **sasl_plaintext**: SASL authentication without encryption. <br />- **ssl**: SSL/TLS encryption without SASL. <br />- **sasl_ssl**: SASL authentication with SSL/TLS encryption. |

### SASL Authentication

When **Security Protocol** is set to `sasl_plaintext` or `sasl_ssl`, configure the following parameters:

| Parameter          | Description                                                  |
| ------------------ | ------------------------------------------------------------ |
| **SASL Mechanism**  | Authentication mechanism: PLAIN (default), SCRAM-SHA-256, SCRAM-SHA-512. |
| **SASL Username**   | SASL authentication username, required.                      |
| **SASL Password**   | SASL authentication password, required.                      |

### SSL/TLS

When **Security Protocol** is set to `ssl` or `sasl_ssl`, the following parameters are available:

| Parameter          | Description                                                  |
| ------------------ | ------------------------------------------------------------ |
| **CA Certificate**  | CA certificate (Base64-encoded PEM), required for self-signed certificates. |
| **Client Certificate** | Client certificate (Base64-encoded PEM), required for mutual TLS. |
| **Client Private Key** | Client private key (Base64-encoded PEM), required for mutual TLS. |

## Add Subscription

After plugin configuration, click the device card or row on the **North Apps** page, then **Add Subscription** on the **Group List** page. Set the following:

- **South device**: Select the southbound device to subscribe to.
- **Group**: Select a group from the southbound device.
- **Topic**: Specify the Kafka topic for this subscription. If not set, the **Default Topic** from application configuration is used.

Each subscription can specify a different topic, enabling data routing from different devices/groups to different Kafka topics.

## Operation and Maintenance

On the device card or device row, you can click the **Data Statistics** icon to review the application's operation status and the data received and sent. For explanations on statistical fields, refer to the [Create a Northbound Application](../north-apps.md) section.

If there are any issues with device operation, you can click the DEBUG log chart. The system will automatically print DEBUG level logs for that node and switch back to the system default log level after ten minutes. Later, you can click **System Information** -> **Logs** at the top of the page to view logs and perform troubleshooting. For a detailed interpretation of system logs, see [Managing Logs](../../../admin/log-management.md).

## Integrating with Microsoft Fabric

The following applies when delivering industrial data collected by NeuronEX to **Eventstream** in **Microsoft Fabric** using a Kafka-compatible endpoint. For end-to-end topology and Eventstream canvas steps, refer to [Microsoft Fabric documentation](https://learn.microsoft.com/fabric/).

### What is Microsoft Fabric

**Microsoft Fabric** is Microsoft's unified SaaS analytics platform that brings data integration, data engineering, real-time analytics, and visualization into one product family. **OneLake** is the unified lake that holds data for multiple engines; **Real-Time Intelligence / Eventstream** can ingest streaming data over the **Kafka protocol**, so you do not need to operate a self-managed Kafka cluster in the cloud to scale consumption and persistence (for example into **Eventhouse**). For NeuronEX, if the cloud exposes a standard Kafka producer bootstrap address and credentials, you can use the northbound Kafka plugin described on this page.

### Why NeuronEX + Microsoft Fabric

- **Close the OT → IT gap**: NeuronEX connects to Modbus, OPC UA, PLCs, and other industrial protocols at the edge, shapes time-series data into structured JSON, and sends it over Kafka into Fabric—without ad-hoc collectors per business line.
- **Clear edge and cloud roles**: the edge focuses on low-latency acquisition and optional aggregation; Fabric focuses on lakehouse-style analytics, SQL/BI, data science, and cross-system correlation (e.g. ERP/MES) on a shared cloud data foundation for dashboards and offline analysis.
- **Straightforward real-time path**: Fabric Eventstream is built for sustained streaming and second-level sampling, which aligns with the northbound Kafka producer model—short path and predictable operations.

Actual benefits depend on deployment scale and compliance; validate in your own architecture review.

### Two ways for NeuronEX to reach Fabric

NeuronEX can send data to Fabric Eventstream (Kafka-compatible endpoint) via the paths below. **Both can coexist**; choose based on whether you need SQL stream processing at the edge.

| Approach | Description |
| -------- | ----------- |
| **Data processing → Kafka Sink** | Southbound data enters **Data processing (stream processing)** first. SQL rules filter, map, and aggregate; a **Kafka Sink** writes to Eventstream. **Suited to** trimming fields, throttling, or conditional upload at the edge. |
| **Northbound Kafka plugin (this page)** | Data from subscriptions is sent by the northbound Kafka node as a Kafka **producer** straight to the broker/topic. **Suited to** models that already align with subscriptions, with send cadence and topic routing controlled outside the stream-processing console. |

On the Fabric side both paths often reuse the same Eventstream bootstrap, topic, and SASL credentials; the difference is whether data goes through the data processing engine before send.

### Configuring the northbound Kafka plugin for Eventstream

After you create **Eventstream** in Fabric and complete the Kafka custom endpoint setup, map the connection details to the **northbound Kafka** fields below.

| NeuronEX northbound Kafka field | Description | Example (must match your **Microsoft Fabric** / **Azure** portal) |
| ------------------------------- | ------------ | ----------------------------------------------------------------- |
| **Broker Address** | Fabric Eventstream **bootstrap server** (including port). | `neuron-eventstream.servicebus.windows.net:9093` |
| **Default Topic** | Topic name configured for that stream in Fabric; if **Add Subscription** sets a **Topic** for a subscription, that value takes precedence; otherwise use this default. | `neuron-topic` |
| **Security Protocol** | Use **`sasl_ssl`** when connecting to Eventstream with TLS and SASL. | `sasl_ssl` |
| **SASL Mechanism** | Matches Kafka Sink **SASL Auth Type = plain**; select **`PLAIN`** in the plugin. | `PLAIN` |
| **SASL Username** | Fixed string. | `$ConnectionString` |
| **SASL Password** | Full Fabric **Connection string - primary key**; do not truncate. | `Endpoint=sb://...` |

After configuration, confirm delivery using NeuronEX runtime statistics or DEBUG logs, and Fabric Eventstream **Data preview** (or downstream Eventhouse queries) to verify that messages keep arriving.
