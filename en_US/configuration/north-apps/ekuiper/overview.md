# LF Edge eKuiper

LF Edge [eKuiper] is a lightweight IoT data analytics and stream processing
engine running on resource-constraint edge devices. The major goal for eKuiper
is to provide a streaming software framework in edge side. eKuiper's rule engine
allows user to provide either SQL based or graph based rules to create IoT edge
analytics applications within few minutes.

The Neuron eKuiper plugin enables users to create north bound nodes publishing
collected data to eKuiper for further processing. As an industrial gateway
Neuron provides one-stop access to many different devices speaking many different
protocols, while eKuiper has the ability of data filtering, aggregation,
transformation, and routing. Combining the two products gives you the best of
both worlds, which significantly reduces the resource requirements of edge
computing solutions and enables more use cases.
Better yet, the Neuron eKuiper plugin is open source.

## Parameters

From Neuron version 2.4.0, these are the available parameters when configuring a
node using the eKuiper plugin.

| Parameter           | Description                                                  |
| ------------------- | ------------------------------------------------------------ |
| **Local IP address**| IP address to listen for connections from eKuiper.           |
| **Local port**      | TCP port number to listen for connections from eKuiper.      |

## eKuiper integration

The interaction between Neuron and eKuiper is bidirectional and needs support
from both sides:
* on the Neuron side, the eKuiper plugin is provided to support publishing data
to and receiving commands from eKuiper.
* on the eKuiper side, a Neuron source is provided to support data subscription
from Neuron, and a Neuron sink is provided to support device control via Neuron.

Neuron version 2.0.0 first released the eKuiper plugin, while eKuiper 1.5.0 first
added the Neuron source and sink.
The two sides use the [NNG pair0 protocol] based on the [IPC transport], which
only allows one-to-one communication in the same host. Thus you need to deploy
Neuron and eKuiper in the same host to achieve correct functionality.

::: tip
You may also use MQTT as a relay between Neuron and eKuiper.
:::

Since Neuron version 2.4.0 the eKuiper plugin switches from the IPC transport to
the [TCP transport], and eKuiper version 1.9.0 adopts the TCP transport.
Using the TCP transport eliminate the requirement that you deploy Neuron and
eKuiper in the same host, and allows multiple connections between Neuron and
eKuiper.

::: tip
Neuron 2.0 and eKuiper 1.5 onwards, the two sides use the IPC transport for
one-to-one connectivity.
Neuron 2.4 and eKuiper 1.9 onwards, the two sides use TCP transport and can
support many-to-many connections.
:::

### NeuronEX

To ease deployment and for better user experience, NeuronEX is released alongside
Neuron since version 2.3.0. NeuronEX is a package of Neuron integrated with
eKuiper and an augmented dashboard. NeuronEX comes with a default north node
**data-stream-processing** created for you. Using NeuronEX, users can easily manage
eKuiper rules directly through the dashboard and perform other stream processing
operations.

### Internals

This section describes low level communication details between Neuron and
eKuiper. You may skip this section without problem.

#### Data upload

The Neuron eKuiper plugin publishes data collected from devices as JSON once
connected to the eKuiper.
Data published to eKuiper have the following fields:
* `timestamp` : the Unix timestamp when the data was collected.
* `node_name` : name of the south node from which data was collected.
* `group_name` : name of the south node group that the tags belong to.
* `values` : dictionary storing tags with successfully collected values
* `errors` : dictionary storing tags with encountered error codes

Following is an example data. When a tag is read successfully, its value is
recorded in the *values* dictionary. If something goes wrong when reading a tag,
the error code is recorded instead in the *errors* dictionary.

``` json
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

#### Device control

eKuiper may control devices via Neuron by sending *write commands* using the
Neuron sink, and Neuron will write data to the devices upon receiving the
commands.

The *write command* should be JSON data with the following fields:
* `node_name` : the name of a southbound node.
* `group_name` : the name of a group.
* `tag_name` : the name of a tag.
* `value` : the value to write.

Below is an example write command:

``` json
{
    "node_name": "modbus",
    "group_name": "grp",
    "tag_name": "tag0",
    "value": 1234
}
```

## Examples

See the [Data Streaming](../../../data-streaming/data-streaming.md) chapter.
Also there is an eKuiper tutorial [Stream processing of data collected by Neuron using eKuiper]

[eKuiper]: https://ekuiper.org
[NNG pair0 protocol]: https://nng.nanomsg.org/man/v1.3.2/nng_pair.7.html
[IPC transport]: https://nng.nanomsg.org/man/v1.3.2/nng_ipc.7.html
[TCP transport]: https://nng.nanomsg.org/man/v1.3.2/nng_tcp.7.html
[Stream processing of data collected by Neuron using eKuiper]: https://ekuiper.org/docs/en/latest/integrations/neuron/neuron_integration_tutorial.html#integration-of-neuron-and-ekuiper
