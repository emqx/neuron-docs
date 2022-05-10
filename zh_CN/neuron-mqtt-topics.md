# Neuron MQTT Topics

All topics for interaction between client and neuron with read, write command.

The **client-id** in all topics refers to the actual MQTT client id, which is set in the northbound application configuration in the Neuron UI.

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

*Node* When the value is read correctly, only the value is displayed, only when the value is read incorrectly, the error code is displayed, not the value.

## Upload Data

### Response

*Topic* **neuron/{client-id}/upload** 

If the upload-topic is set in the node setting, the topic will be used to upload data, and the default topic will no longer upload data.

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

*Node* When the value is read correctly, only the value is displayed, only when the value is read incorrectly, the error code is displayed, not the value.

There are two message formats for the body. You can choose two different formats in the mqtt configuration form.

**Node:**  A group sends a message.

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
