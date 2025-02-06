# Upstream/Downstream Data Format

The following contents describe how the Neuron MQTT plugin publishes collected data, and how to read or write data through MQTT using the plugin.

Note that **{node_name}** in all the following MQTT topics refers to the actual MQTT northbound application name, **{driver_name}** refers to some southbound node name, and **{group_name}** refers to some south node group name.

## Data Upload

The Neuron MQTT plugin publishes collected data in JSON to some user-designated topics. The exact format of the data reported is controlled by the **Upload Format** parameter. There are two formats, *tags-format* and *values-format*.

### Upload Topic

Before Neuron version 2.4.0, the upload topic is specified by the **upload-topic** parameter, and the default one set through the dashboard is **/neuron/{node_name}/upload**.

Since Neuron version 2.4.0, the **upload-topic** parameter is removed. And the upload topic is specified in the group subscription request instead with default as **/neuron/{node_name}/{driver_name}/{group_name}**.

### Tags Format

In *tags-format*, the upload data has the following fields:
* `timestamp`: the Unix timestamp when the data was collected
* `node`: name of the south node from which data was collected
* `group`: name of the south node group that the tags belong to
* `tags`: tags data array where each element corresponds to one tag in the group

The following example data is in *tags-format*, where tag data are stored in an array. Each element has the name of the tag, and the tag value or error code if something went wrong.

```json
{
  "timestamp": 1647497389075,
  "node": "modbus",
  "group": "grp",
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

### Values Format

In *values-format*, the upload data has the following fields:
* `timestamp`: the Unix timestamp when the data was collected
* `node`: name of the south node from which data was collected
* `group`: name of the south node group that the tags belong to
* `values`: dictionary storing tags with successfully collected values
* `errors`: dictionary storing tags with encountered error codes

The following example data is in *values-format*, where tag values collected successfully are stored in a dictionary, while error codes in another.

```json
{
    "timestamp": 1650006388943,
    "node": "modbus",
    "group": "grp",
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

### Custom Format

In the custom format, use built-in variables to define the data upload format.

#### Variables

| *variable* | *description* |
| ------------------ | ---------------------- | 
| `${timestamp}` | The UNIX timestamp when the data was read. |
| `${node}` | The name of the southbound node. |
| `${group}` | The name of the group. |
| `${tags}` | The array of valid tag values. |
| `${tag_values}` | The array of valid tag values, Value Format |
| `${tag_errors}` | The array of error codes. |
| `${tag_error_values}` | The array of error codes, Value Format |
| `${static_tags}` | The array of static tags. |
| `${static_tag_values}` | The array of static tags, Value Format |

#### Example

The custom format is defined using built-in variables.
```json
{
    "timestamp": "${timestamp}",
    "node": "${node}",
    "group": "${group}",
    "tags": "${tags}",
    "values": "${tag_values}",
    "static_tags": "${static_tags}",
    "static_tag_values": "${static_tag_values}",
    "errors": "${tag_errors}",
    "error_values": "${tag_error_values}"
}
```

The following is an example of the custom format data.
```json
{
    "timestamp": 1650006388943,
    "node": "modbus",
    "group": "group",
    "tags": [
        {
            "name": "tag0",
            "value": 123
        },
        {
            "name": "tag1",
            "value": false 
        }
    ],
    "values": {"tag0": 123, "tag1": false},
    "static_tags": [
        {
            "name": "static_tag1",
            "value": 456
        }
    ],
    "static_tag_values": {"static_tag1": 456},
    "errors": [
        {
            "name": "tag2",
            "error": 2014
        }
    ],
    "error_values": {"tag2": 2014}
}
```

::: tip
Tag value is returned only when the tag is read successfully. If something goes wrong when reading a tag, the error code is returned.
:::

### ECP Format

In *ECP-format*, the upload data has the following fields:
* `timestamp`: the Unix timestamp when the data was collected
* `node`: name of the south node from which data was collected
* `group`: name of the south node group that the tags belong to
* `tags`: tags data array where each element corresponds to one tag in the group

The following example data is in *ECP-format*, where tag data are stored in an array. Each element has the name of the tag, the tag type and the tag value, excluding tags where collection failed.

Data classes are divided into four types: Boolean, Integer, Float, and String.
* type = 1 Boolean
* type = 2 Integer
* type = 3 Float
* type = 4 String

```json
{
  "timestamp": 1647497389075,
  "node": "modbus",
  "group": "grp",
  "tags": [
    {
      "name": "tag_boolean",
      "value": true,
      "type": 1,
    },
    {
      "name": "tag_int32_",
      "value": 123,
      "type": 2,
    },
    {
      "name": "tag_float",
      "value": 1.23,
      "type": 3,
    },
    {
      "name": "tag_string",
      "value": "abcd",
      "type": 4,
    }
  ]
}
```

## Read Tag

### Request

You can read a group of tags by sending requests in JSON to the MQTT topic **/neuron/{node_name}/read/req**.

#### Body

The read request body should have the following fields:
* `uuid`: a unique identifier, which will be echoed back in the response to help identify the corresponding request
* `node`: the name of a southbound node
* `group`: the name of a group to read

Below is an example read request:

```json
{
    "uuid": "bca54fe7-a2b1-43e2-a4b4-1da715d28eab",
    "node": "modbus",
    "group": "grp"
}
```

### Response

Read response will be published to the MQTT topic **/neuron/{node_name}/read/resp**.

#### Body

The read response body has the following fields:
* `uuid`: the same unique identifier which is set by the corresponding request
* `tags`: tags data array, same as that in [tags format](#tags-format)

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
Tag value is returned only when the tag is read successfully. If something goes wrong when reading a tag, the error code is returned.
:::

## Write Tag

### Request

You could write a tag by sending requests in JSON to the MQTT topic designated by the **Write Request Topic** parameter.

::: tip
Before Neuron version 2.4.5, the write request topic was hard-coded to **/neuron/{random_str}/write/req**.
:::

#### Body

#### Write one tag

The write request body should have the following fields:
* `uuid`: a unique identifier, which will be echoed back in the response to help identify the corresponding request
* `node`: the name of a southbound node
* `group`: the name of a group
* `tag`: the name of a tag
* `value`: the value to write

Below is an example of write request:

```json
{
    "uuid": "cd32be1b-c8b1-3257-94af-77f847b1ed3e",
    "node": "modbus",
    "group": "grp",
    "tag": "tag0",
    "value": 1234
}
```

#### Write multiple tags

Since Neuron version 2.6.0, write requests also support writing multiple tags at
a time. To write multiple tags at a time, the request body should have the
following fields:
* `uuid` : a unique identifier, which will be echoed back in the response to help identify the corresponding request.
* `node` : the name of a southbound node.
* `group` : the name of a group.
* `tags` : tags data array where each element corresponds to one tag in the group.

Below is an example write request:

```json
{
    "uuid": "cd32be1b-c8b1-3257-94af-77f847b1ed3e",
    "node": "modbus",
    "group": "grp",
    "tags": [
      {
        "tag": "tag0",
        "value": 1234
      },
      {
        "tag": "tag1",
        "value": 5678
      }
    ]
}
```


### Response

Write response will be published to the MQTT topic designated by the **Write Response Topic** parameter.

::: tip
Before Neuron version 2.4.5, the write response topic was hard-coded to **/neuron/{random_str}//write/resp**.
:::

#### Body

The write response body has the following fields:
* `uuid`: the same unique identifier which is set by the corresponding request.
* `error`: error code if something bad happens, `0` represents success.

Below is an example of write response:

```json
{
  "uuid": "cd32be1b-c8b1-3257-94af-77f847b1ed3e",
  "error": 0
}
```

## Driver Status Report

Reports status of all the southbound nodes to the specified topic.

### Status Report Topic

The status report topic is specified in the northbound node configuration. Its default value is **/neuron/{random_str}/state/update**.

### Status Report Interval

The status report interval is specified in the northbound node configuration, indicating the number of seconds between each message. The default value is 1, with an allowed range of 1-3600.

### Reporting Message Format

The reported data consists of the following fields:
* `timestamp`: The UNIX timestamp when the data was collected.
* `states`: An array of node status information.

Below is an example of a driver status reporting message.

```json
{
  "timestamp": 1658134132237,
  "states": [
    {
      "node": "modbus-tcp",
      "link": 1,
      "running": 3
    },
    {
      "node": "modbus-rtu",
      "link": 1,
      "running": 3
    }
  ]
}
```
