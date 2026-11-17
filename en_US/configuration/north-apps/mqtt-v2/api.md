# Upstream/Downstream Data Format

This page describes how the MQTT V2 plugin uploads the collected data, and how to write tags through the MQTT V2 plugin. For the formats of status messages, see [MQTT V2 Overview](./overview.md#status-messages).

## Data Upload

Each time a subscribed group reports, the plugin publishes a message to the data topic of the group, `{topic prefix}/{device name}/data` by default. Reports follow the collection interval of the southbound group, tags with the subscribe attribute are only reported when their values change.

The message content is given by two JSON templates in the application configuration:

- **Data template**: the structure of the whole message.
- **Tag template**: the structure of each tag, when `${tags}`, `${tags_kv}` or `${tags[name]}` in the data template expands.

### Default Templates

Data template:

```json
{
  "timestamp": "${timestamp}",
  "device": "${device}",
  "group": "${group}",
  "tags": "${tags}"
}
```

Tag template:

```json
{
  "name": "${tag.name}",
  "value": "${tag.value}",
  "timestamp": "${tag.timestamp}",
  "quality": "${tag.quality}",
  "description": "${tag.description}",
  "unit": "${tag.unit}",
  "error": "${tag.error}"
}
```

With the default templates, the uploaded data looks like:

```json
{
    "timestamp": 1731744000123,
    "device": "modbus-1",
    "group": "group-1",
    "tags": [
        {"name": "tag0", "value": 123},
        {"name": "tag1", "value": 25.5, "description": "temperature", "unit": "C"},
        {"name": "tag2", "error": 3008}
    ]
}
```

`tag0` has no description or unit, so the two fields are left out; `tag2` fails to be read, only its error code is uploaded. The default tag template contains `${tag.error}`, so failed tags are included. Removing `${tag.error}` from the tag template leaves those tags out of `${tags}`, `${tags_kv}` and `${tags[name]}`.

### Template Rules

- Templates must be valid JSON, with variables in strings, for example `"${tags}"`.
- A string holding a single variable is replaced by the original JSON type of the variable. For example `"${timestamp}"` becomes a number and `"${tags}"` an array.
- Variables mixed with text are joined into a string. For example `"${device}-${group}"` becomes `"modbus-1-group-1"`.
- Keys can use variables as well. For example the tag template `{"${tag.name}": "${tag.value}"}` gives `{"tag0": 123}`.
- A field whose variable has no value is left out, for example a tag without quality, an empty description, or the error code of a tag read successfully. In arrays, such values become `null`.
- A tag template can be a single variable. For example with the tag template `"${tag.value}"`, `${tags_kv}` gives `{"tag0": 123, "tag1": 25.5}`.
- Unknown variables are not allowed; tag variables `${tag.xxx}` are only allowed in the tag template, and tag collection variables such as `${tags}` only in the data template. Saving a configuration breaking these rules fails.

### Template Variables

The data template can use the following variables:

| Variable | Description |
| --- | --- |
| `${app}` | Northbound application name |
| `${device}` | Southbound device name |
| `${group}` | Group name |
| `${sub_topic}` | The data topic actually used by the group |
| `${timestamp}` | Current time, Unix timestamp in milliseconds |
| `${TIME_RFC3339}` | RFC 3339 time, such as `2026-11-16T08:00:00.123+08:00` |
| `${TIME_UTC}` | UTC time, such as `2026-11-16T00:00:00.123Z` |
| `${TIME_LOCAL}` | Local time, such as `2026-11-16 08:00:00.123` |
| `${TIME_UNIX}` | Current time, Unix timestamp in seconds |
| `${TIME:format}` | Time in a strftime format, such as `${TIME:%Y-%m-%d %H:%M:%S}` |
| `${tags}` | All tags, expanded as an array |
| `${tags_kv}` | All tags, expanded as an object keyed by tag names |
| `${tags[name]}` | A single tag, expanded with the tag template |
| `${tags[name].attribute}` | An attribute of a single tag, attributes as in the tag template, such as `${tags[tag0].value}` |
| `${properties}` | All the device properties, expanded as an object; left out when the device has none |
| `${properties[key]}` | A single device property |

The tag template can use the following variables, and all the variables of the table above except `${tags}`, `${tags_kv}` and `${tags[...]}`:

| Variable | Description |
| --- | --- |
| `${tag.name}` | Tag name |
| `${tag.value}` | Tag value |
| `${tag.timestamp}` | Tag sample timestamp, when provided by the driver |
| `${tag.sourceTimestamp}` | Source timestamp, when provided by the driver |
| `${tag.serverTimestamp}` | Server timestamp, when provided by the driver |
| `${tag.quality}` | Tag quality, when provided by the driver |
| `${tag.description}` | Tag description |
| `${tag.unit}` | Tag unit |
| `${tag.error}` | Error code of a tag failing to be read. Failed tags are uploaded only when the tag template uses it |
| `${tag.type}` | Tag data type, such as `INT16` |

::: tip
Changes of tag descriptions and units take up to about 30 seconds to appear in data messages.
:::

### Template Examples

**With device properties**

Data template:

```json
{
  "timestamp": "${timestamp}",
  "device": "${device}",
  "properties": "${properties}",
  "tags": "${tags}"
}
```

Uploaded data:

```json
{"timestamp": 1731744000123, "device": "modbus-1", "properties": {"location": "Building A", "line": 3}, "tags": [{"name": "tag0", "value": 123}]}
```

**Flat structure**

Data template:

```json
{
  "site": "${properties[location]}",
  "ts": "${timestamp}",
  "values": "${tags_kv}"
}
```

Tag template:

```json
"${tag.value}"
```

Uploaded data:

```json
{"site": "Building A", "ts": 1731744000123, "values": {"tag0": 123, "tag1": 25.5}}
```

**Selected tags only**

Data template:

```json
{
  "device": "${device}",
  "time": "${TIME_RFC3339}",
  "temperature": "${tags[tag1].value}",
  "unit": "${tags[tag1].unit}"
}
```

Uploaded data:

```json
{"device": "modbus-1", "time": "2026-11-16T08:00:00.123+08:00", "temperature": 25.5, "unit": "C"}
```

## Write Tags

Publish write requests to the write request topic of the device, `{topic prefix}/{device name}/write/request`, the plugin publishes the write results to `{topic prefix}/{device name}/write/response`.

### Write Request

```json
{
    "id": "123",
    "version": "1.0",
    "params": {
        "group": "group-1",
        "values": {
            "tag0": 40,
            "tag1": true
        }
    }
}
```

| Field | Description |
| --- | --- |
| `id` | Optional, request identifier returned as is in the write response, any JSON value. |
| `version` | Optional, message format version. `"1.0"` and `"neuron"` are supported, both meaning the neuron native format, which is also used when not set. |
| `params.values` | Required, the tag names and values to write, not empty. A value can be a number, boolean, string, array of elements of the same type, or JSON object (for CUSTOM type tags). |
| `params.group` | Optional, the group of the tags. Required when several subscribed groups have tags of the same name. |

- Only tags of the groups subscribed by this application can be written.
- A request can write tags of several groups of the same device.

### Write Response

```json
{
    "id": "123",
    "version": "1.0",
    "error": 0,
    "tags": {
        "tag0": 0,
        "tag1": 0
    }
}
```

| Field | Description |
| --- | --- |
| `id`, `version` | Same as in the write request, left out when not in the request. |
| `error` | Overall result. 0 when all succeed, otherwise the error code of the first failing tag. |
| `tags` | Write result of each tag, 0 for success, otherwise the error code. |

When the request itself is invalid, for example not JSON, all tags get the same error code. Common error codes:

| Error code | Description |
| --- | --- |
| 1002 | The request is not JSON, or `params.values` is missing or empty |
| 1003 | Unsupported `version`, or invalid `group` or tag value |
| 2102 | The group is not subscribed by this application |
| 2201 | The tag does not exist in the subscribed groups |
| 3004 | The tag is not writable |
