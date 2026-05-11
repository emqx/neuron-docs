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
- **Topic** (optional): Specify the Kafka topic for this subscription. If not set, the **Default Topic** from application configuration is used.

Each subscription can specify a different topic, enabling data routing from different devices/groups to different Kafka topics.

## Operation and Maintenance

On the device card or device row, you can click the **Data Statistics** icon to review the application's operation status and the data received and sent. For explanations on statistical fields, refer to the [Create a Northbound Application](../north-apps.md) section.

If there are any issues with device operation, you can click the DEBUG log chart. The system will automatically print DEBUG level logs for that node and switch back to the system default log level after ten minutes. Later, you can click **System Information** -> **Logs** at the top of the page to view logs and perform troubleshooting. For a detailed interpretation of system logs, see [Managing Logs](../../../admin/log-management.md).
