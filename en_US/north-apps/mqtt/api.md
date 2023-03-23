# API

The following contents describe how the Neuron MQTT plugin publishes collected
data, and how to read or write data through MQTT using the plugin.

Note that **{node_name}** in all the following MQTT topics refers to the actual
MQTT northbound application name.

## Data upload

The Neuron MQTT plugin publish collected data in JSON to the topic designated
by the **upload-topic** parameter, the default one set through the dashboard
is **/neuron/{node_name}/upload**.

The exact format of the data reported is controlled by the **format** parameter.
There are two formats, *tags-format* and *values-format*.

### Tags format

The following example data is in *tags-format*, where tag data are stored in
a array. Each element has the name of the tag, and the tag value or error code
if something went wrong.

```json
{
  "node": "modbus",
  "group": "grp",
  "timestamp": 1647497389075,
  "tags": [
    {
      "name": "tag0",
      "value": 123,
    },
    {
      "name": "tag1",
      "error": 2014
    }
  ]
}
```

### Values format

The following example data is in *values-format*, where tag values collected
successfully are stored in a dictionary, while error codes in another.

```json
{
    "node": "modbus",
    "group": "grp",
    "timestamp": 1650006388943,
    "values":
    {
        "tag0": 123
    },
    "errors":
    {
        "tag1": 2014
    }
}
```

::: tip
Tag value is returned only when the tag is read successfully. If something goes
wrong when reading a tag, the error code is returned.
:::

## Read tags

### Request

You can read a group of tags by sending requests in JSON to the MQTT topic
**/neuron/{node_name}/read/req**.

#### Body

The read request body should have the following fields:
* "uuid": a unique identifier, which will be echoed back in the response to help identify the corresponding request.
* "node": the name of a southbound node.
* "group": the name of a group to read.

Below is an example read request:

```json
{
    "uuid": "bca54fe7-a2b1-43e2-a4b4-1da715d28eab",
    "node": "modbus",
    "group": "grp"
}
```

### Response

Read response will be publish to the MQTT topic **/neuron/{node_name}/read/resp**.

#### Body

Below is an example read response:

```json
{
  "uuid": "bca54fe7-a2b1-43e2-a4b4-1da715d28eab",
  "tags": [
    {
      "name": "tag0",
      "value": 4,
    },
    {
      "name": "tag1",
      "error": 2014
    }
  ]
}
```

::: tip
Tag value is returned only when the tag is read successfully. If something goes
wrong when reading a tag, the error code is returned.
:::

## Write Tag

### Request

You could write a tag by sending requests in JSON to the MQTT topic
**/neuron/{node_name}/write/req**.

#### Body

The write request body should have the following fields:
* "uuid": a unique identifier, which will be echoed back in the response to help identify the corresponding request.
* "node": the name of a southbound node.
* "group": the name of a group.
* "tag": the name of a tag.
* "value": the value to write.

Below is an example write request:

```json
{
    "uuid": "cd32be1b-c8b1-3257-94af-77f847b1ed3e",
    "node": "modbus",
    "group": "grp",
    "tag": "tag0",
    "value": 1234
}
```

### Response

Write response will be published to the MQTT topic **/neuron/{node_name}/write/resp**.

#### Body

Below is an example write response:

```json
{
  "uuid": "cd32be1b-c8b1-3257-94af-77f847b1ed3e",
  "error": 0
}
```
