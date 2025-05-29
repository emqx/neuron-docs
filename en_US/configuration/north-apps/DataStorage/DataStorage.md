# DataStorage

DataStorage northbound plugin writes data to [Datalayers](https://docs.datalayers.cn/datalayers/latest/) using [Arrow Flight SQL](https://arrow.apache.org/docs/format/FlightSql.html#arrow-flight-sql). It extends NeuronEX's capability to store time-series data.

Upon startup, NeuronEX creates a singleton *DataStorage* node automatically. Users cannot manually create or delete this node.

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

After plugin configuration, data storage can be enabled via southbound device subscriptions.

Click DataStorage node on the **North Apps** page, then **Add Subscription** on the **Group List** page. And set the following:

- **South device**: Select the southbound device you want to subscribe to.
- **Group**: Select a group from the southbound device.

## Data Storage

DataStorage uses Arrow's columnar format for data storage, which eliminates serialization and deserialization during transport. This significantly reduces latency and performance overhead, improving system throughput.

## Operation & Maintenance

You can click on the **Data Statistics** icon to review the application's operation status and track the data received and sent.

Cached Queue Size indicates the value used by the current DataStorage plugin when storing data.

Max Cached Queue Size indicates the historical maximum value used by the DataStorage plugin when storing data.

Discarded Messages indicates the number of data lost when the DataStorage plugin stores data due to excessive data throughput exceeding the maximum value of the cache queue of 1000.
