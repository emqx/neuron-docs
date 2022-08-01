# MQTT API

The following topics are used for read/write interaction between client and neuron.

The **{client-id}** in all topics refers to the actual MQTT client id, which is set in the northbound application configuration in the Neuron UI.

## Upload Data

### Response

*Default topic* **neuron/{client-id}/upload**

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

*Default topic* **neuron/{client-id}/heartbeat**

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

*Topic*  **neuron/{client-id}/read/req**

#### Body

```json
{
    "uuid": "E21AEE51-1269-B228-E9E5-CD252CE10877",
    "node": "modbus-tcp-1",
    "group": "group-2"
}
```

### Response

*Topic*  **neuron/{client-id}/read/resp**

#### Body

```json
{
  "uuid": "E21AEE51-1269-B228-E9E5-CD252CE10877",
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

*Topic*  **neuron/{client-id}/write/req**

#### Body

```json
{
    "uuid": "E21AEE51-1269-B228-E9E5-CD252CE10877",
    "node": "modbus-tcp-1",
    "group": "group-2",
    "tag": "tag1",
    "value": 1234
}
```

### Response

*Topic*  **neuron/{client-id}/write/resp**

#### Body

```json
{
  "uuid": "E21AEE51-1269-B228-E9E5-CD252CE10877",
  "error": 0
}
```
