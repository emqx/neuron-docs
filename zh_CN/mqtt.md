# MQTT订阅主题

客户端和神经元之间通过读、写命令进行交互的所有主题。

所有主题中的**client-id**指的是实际的MQTT客户端id，在Neuron UI的北向应用配置中设置。

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

*Node* 正确读取数值时，仅显示数值，仅当读取错误数值时，显示错误码，不显示数值。

## Upload Data

### Response

*Topic* **neuron/{client-id}/upload** 

如果在节点设置中设置了upload-topic，则该topic将用于上传数据，默认topic将不再上传数据。

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

*Node* 正确读取数值时，仅显示数值，仅当读取错误数值时，显示错误码，不显示数值。

正文有两种消息格式。 您可以在 mqtt 配置表单中选择两种不同的格式。

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
