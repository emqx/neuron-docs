# eKuiper

LF Edge [eKuiper] is a lightweight IoT data analytics and stream processing engine running on resource-constraint edge devices. The major goal for eKuiper is to provide a streaming software framework on the edge side. eKuiper's rule engine allows users to provide either SQL-based or graph-based rules to create IoT edge analytics applications within a few minutes.

The Neuron eKuiper plugin enables users to create northbound nodes publishing collected data to eKuiper for further processing. As an industrial gateway, Neuron provides one-stop access to many different devices speaking many different
protocols, while eKuiper can filter data, aggregate, transform, and route. Combining the two products gives you the best of both worlds, significantly reducing the resource requirements of edge computing solutions and enabling more use cases. 

## Key Benefits

With the integration of eKuiper, Neuron gains the following capabilities:

- <b>Enhanced Data Analytics</b>: Neuron now supports advanced real-time data analytics, which includes anomaly detection, predictive maintenance, and optimization algorithms. This expansion of functionality allows Neuron to offer more comprehensive and intelligent solutions for industrial IoT deployments.

- <b>Edge Computing Proficiency</b>: Neuron can process data closer to the industrial devices at the edge, which reduces latency and enables quicker response times.

- <b>Efficient Data Processing and Transformation</b>: Neuron's support for Extract, Transform, and Load (ETL) processes allows efficient data preprocessing and cleansing before analytics are applied. This ensures data quality and consistency, which are critical for cloud-based AI/ML analytics functions.
- <b>Edge-based Data-Driven Decision Making</b>: Neuron has the capability to locally analyze and process AI-driven insights, reducing the reliance on cloud-based decision-making systems. This allows faster and more informed decision-making at the edge.

## Add Application

Navigate to **Configuration -> North Apps** and click **Add Application** to add an eKuiper client node.

## Configure Application

From Neuron version 2.4.0, these are the available parameters when configuring a node using the eKuiper plugin.

| Parameter           | Description                                                  |
| ------------------- | ------------------------------------------------------------ |
| **Local IP address**| IP address to listen for connections from eKuiper.           |
| **Local port**      | TCP port number to listen for connections from eKuiper.      |

## Add Subscription

After plugin configuration, data forwarding can be enabled via southbound device subscriptions.

Click the device card or row on the **North Apps** page, then **Add Subscription** on the **Group List** page. And set the following:

- **South device**: Select the southbound device you want to subscribe to, for example, 'modbus-tcp-1'.
- **Group**: Select a group from the southbound device, for example, 'group-1'.

Now you can use Neuron to forward the data to eKuiper for further processing. For detailed steps, see [Stream processing of data collected by Neuron using eKuiper](https://ekuiper.org/docs/en/latest/integrations/neuron/neuron_integration_tutorial.html#integration-of-neuron-and-ekuiper)

## Use Case

Through the Neuron eKuiper plugin, you can establish a direct data channel between Neuron and eKuiper. This enables operations like printing data collected by Neuron into eKuiper's logs. For specific steps, refer to the [Best Practices for Integrating Neuron and eKuiper](ekuiper.md)

## Operation and Maintenance

On the device card or device row, you can click on the **Data Statistics** icon to review the application's operation status and track the data received and sent. For explanations on statistical fields, refer to the [Create a Northbound Application](../north-apps.md) section.

If there are any issues with device operation, you can click on the DEBUG log chart. The system will automatically print DEBUG level logs for that node and switch back to the system default log level after ten minutes. Later, you can click on **System Information** -> **Logs** at the top of the page to view logs and perform troubleshooting. For a detailed interpretation of system logs, see [Managing Logs](../../../admin/log-management.md).

## Version Compatibility

Interaction between Neuron and eKuiper is bidirectional, necessitating support from both ends:

On the Neuron side, an eKuiper plugin is provided to publish data to eKuiper and receive commands. From eKuiper, a Neuron source is provided to subscribe to data from Neuron, along with a Neuron action to control devices via Neuron.

| Neuron Version       | eKuiper Version       | Release History                                              | Usage Limitations                                            |
| -------------------- | --------------------- | ------------------------------------------------------------ | ------------------------------------------------------------ |
| Neuron 2.0           | eKuiper 1.5           | 1. Neuron first introduces the eKuiper plugin<br />2. eKuiper first adds the Neuron source and actions <br />3. Neuron and eKuiper communicate using the NNG pair0 protocol based on the IPC transport layer | 1. Neuron and eKuiper should be deployed on the same host (or use MQTT as a relay between them) <br />2. Communication is one-to-one |
| Neuron 2.4 and above | eKuiper 1.9 and above | 1. Neuron and eKuiper communicate using the TCP transport layer <br />2. Support for multiple (many-to-many) connections | None                                                         |

<img src="./assets/connection_change.png" alt="connection_change" style="zoom:50%;" />

## Further Reading

This section encapsulates the underlying details of the Neuron and eKuiper communication, which can be optionally skipped.

### Data Publication

Upon connecting to eKuiper, the Neuron eKuiper plugin publishes data harvested from devices in a JSON format. The data disseminated to eKuiper encompasses:

- `timestamp`: UNIX timestamp at the data harvesting moment.
- `node_name`: Name of the harvested south node.
- `group_name`: Name of the point group within the harvested south node. 
- `values`: A dictionary recording point values from successful harvesting. 
- `errors`: A dictionary recording error codes from unsuccessful harvests. 

The following data sample demonstrates that successful tag readings get recorded in the 'values' dictionary. Conversely, errors during tag reading are documented in the 'errors' dictionary.

```bash
{
  "timestamp": 1646125996000,
  "node_name": "modbus", 
  "group_name": "grp",
  "values": {
    "tag0": 42,
    "tag1": "string"
  },
  "errors": {
    "tag2": 1011
  }
}
```

### Reverse Control

eKuiper can control devices by dispatching write commands through the Neuron action. Upon command reception, Neuron writes data to the designated device.

A write command is a JSON data piece with the following fields:

- `node_name`: A specific south node's name. 
- `group_name`: Name of a group within the south node.
- `tag_name`: Point to be written's name. 
- `value`: The data value to write. 

The following is an example of a write command:

``` json
{
    "node_name": "modbus",
    "group_name": "grp",
    "tag_name": "tag0",
    "value": 1234
}
```

In order to write multiple tags in a single command, the eKuiper plugin also supports write command of the following form.

```
{
    "node_name": "modbus",
    "group_name": "grp",
    "tags": [
        {
            "tag_name": "tag0",
            "value": 1234
        },
        {
            "tag_name": "tag1",
            "value": 4567
        }
    ]
}
```

[eKuiper]: https://ekuiper.org
[NNG pair0 protocol]: https://nng.nanomsg.org/man/v1.3.2/nng_pair.7.html
[IPC transport]: https://nng.nanomsg.org/man/v1.3.2/nng_ipc.7.html
[TCP transport]: https://nng.nanomsg.org/man/v1.3.2/nng_tcp.7.html
[Stream processing of data collected by Neuron using eKuiper]: https://ekuiper.org/docs/en/latest/integrations/neuron/neuron_integration_tutorial.html#integration-of-neuron-and-ekuiper
