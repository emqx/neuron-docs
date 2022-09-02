# MQTT API

The following topics are used for read/write interaction between client and neuron.

The **{node_name}** in all topics refers to the actual MQTT northbound application name, which is set in the Neuron UI's northbound application management.

## Upload Data

### Response

*Default topic* **neuron/{node_name}/upload**

#### Body (Tags format)

```json
{
  "node": "modbus-tcp-2",
  "group": "group-1",
  "timestamp": 1647497389075,
  "tags": [
    {
      "value": 123,
      "name": "data1",
    },
    {
      "name": "data2",
      "error": 2014
    }
  ]
}
```

#### Body (Values format)

```json
{
    "node": "opcua-1", 
    "group": "group-1", 
    "timestamp": 1650006388943, 
    "values": 
    {
        "cstr01": "hello!"
    }, 
    "errors": 
    {
        "cstr100": 10002
    }
}
```

::: tip
The value is displayed only when the value is read correctly, when the value is read incorrectly, the error code is displayed, not the value.A group sends a message.
:::

The upload topic can be set in the driver configuration form. Once set to a custom topic, the default topic will be disabled.

There are two message formats for the body. You can choose one of two different formats in the mqtt configuration form.

## Heartbeat

### Response

*Default topic* **neuron/{node_name}/heartbeat**

#### Body

```json
{
  "version": "2.1.0",
  "timestamp": 1658134132237,
  "states": [
    {
      "node": "mqtt-client",
      "link": 2,
      "running": 3
    },
    {
      "node": "fx5u-client",
      "link": 2,
      "running": 3
    }
  ]
}
```

The heartbeat topic can be set in the driver configuration form. Once set to a custom topic, the default topic will be disabled.

Heartbeat messages are currently set to be sent every 3 seconds by default.

## Read Tags

### Request

*Topic*  **neuron/{node_name}/read/req**

#### Body

```json
{
    "uuid": "bca54fe7-a2b1-43e2-a4b4-1da715d28eab",
    "node": "modbus-tcp-1",
    "group": "group-2"
}
```

### Response

*Topic*  **neuron/{node_name}/read/resp**

#### Body

```json
{
  "uuid": "bca54fe7-a2b1-43e2-a4b4-1da715d28eab",
  "tags": [
    {
      "value": 4,
      "name": "data1",
    },
    {
      "name": "data2",
      "error": 2014
    }
  ]
}
```

::: tip
The value is displayed only when the value is read correctly , when the value is read incorrectly, the error code is displayed, not the value.
:::

## Write Tag

### Request

*Topic*  **neuron/{node_name}/write/req**

#### Body

```json
{
    "uuid": "cd32be1b-c8b1-3257-94af-77f847b1ed3e",
    "node": "modbus-tcp-1",
    "group": "group-2",
    "tag": "tag1",
    "value": 1234
}
```

### Response

*Topic*  **neuron/{node_name}/write/resp**

#### Body

```json
{
  "uuid": "cd32be1b-c8b1-3257-94af-77f847b1ed3e",
  "error": 0
}
```
