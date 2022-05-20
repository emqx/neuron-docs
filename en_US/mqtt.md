# MQTT Topics

The following topics are used for read/write interaction between client and neuron.

The **{client-id}** in all topics refers to the actual MQTT client id, which is set in the northbound application configuration in the Neuron UI.

## Read Tags

### Request

*Topic*  **neuron/{client-id}/read/req**

#### Body

```json
{
    "uuid": "E21AEE51-1269-B228-E9E5-CD252CE10877",
    "node_name": "modbus-tcp-1",
    "group_name": "group-2"
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

*Note* The value is displayed only when the value is read correctly , when the value is read incorrectly, the error code is displayed, not the value.

## Upload Data

### Response

*Topic* **neuron/{client-id}/upload**

#### Body (Tags format)

```json
{
  "node_name": "modbus-tcp-2",
  "group_name": "group-1",
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
    "node_name": "opcua-1", 
    "group_name": "group-1", 
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

*Note* The value is displayed only when the value is read correctly, when the value is read incorrectly, the error code is displayed, not the value.A group sends a message.

There are two message formats for the body. You can choose one of two different formats in the mqtt configuration form.

## Write Tag

### Request

*Topic*  **neuron/{client-id}/write/req**

#### Body

```json
{
    "uuid": "E21AEE51-1269-B228-E9E5-CD252CE10877",
    "node_name": "modbus-tcp-1",
    "group_name": "group-2",
    "tag_name": "tag1",
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
