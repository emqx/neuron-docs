# DataStorage

The Neuron DataStorage plugin is an open-source northbound plugin that writes data to [Datalayers](https://docs.datalayers.cn/datalayers/latest/) using [Arrow Flight SQL](https://arrow.apache.org/docs/format/FlightSql.html#arrow-flight-sql). It extends Neuron's capability to store time-series data.

Upon startup, Neuron creates a singleton *DataStorage* node automatically. Users cannot manually create or delete this node.

You can view the *DataStorage* node in the **North Apps** tab throw the dashboard.

## Application Configuration

The following parameters are available when configuring the DataStorage node:

| Field                       | Description                                                |
| ------------------------------- | ------------------------------------------------------------ |
| **Host**                | IP address of the Datalayers server |
| **Port**                | gRPC service port of the Datalayers server  |
| **Username**            | Datalayers username         |
| **Password**            | Datalayers password           |

## Add Subscription

After plugin configuration, data forwarding can be enabled via southbound device subscriptions.

Click the device card or row on the **North Apps** page, then **Add Subscription** on the **Group List** page. And set the following:

- **South device**: Select the southbound device you want to subscribe to.
- **Group**: Select a group from the southbound device'.

## Data Upload

Neuron DataStorage uses Arrow's columnar format for data transmission, which eliminates serialization and deserialization during transport. This significantly reduces latency and performance overhead, improving system throughput.

## Operation & Maintenance

On the device card or device row, you can click on the **Data Statistics** icon to mreview the application's operation status and track the data received and sent.