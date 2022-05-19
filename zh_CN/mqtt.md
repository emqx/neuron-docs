# MQTT订阅主题

客户端和 Neuron 进行交互的所有主题。包括读、写、订阅。

所有主题中的**{client-id}**指的是实际的 MQTT 客户端 id，在 Neuron UI 的北向应用配置中设置。

## 读 Tags

### 请求

*主题*  **neuron/{client-id}/read/req**

#### Body

```json
{
    "uuid": "E21AEE51-1269-B228-E9E5-CD252CE10877",
    "node_name": "modbus-tcp-1",
    "group_name": "group-2"
}
```

### 响应

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

*注意* 当点位读数值出错时，将显示 **error** 字段，不再显示 **value** 字段。

## 上传数据

### 响应

*主题* **neuron/{client-id}/upload**

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

*注意* 正确读取数值时，仅显示数值，仅当读取错误数值时，显示错误码，不显示数值。一个 Group 发送一条信息。

Body 有两种消息格式，您可以在 Neuron UI 中 mqtt 配置表单中选择。

## 写 Tag

### 请求

*主题*  **neuron/{client-id}/write/req**

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

### 响应

*主题*  **neuron/{client-id}/write/resp**

#### Body

```json
{
  "uuid": "E21AEE51-1269-B228-E9E5-CD252CE10877",
  "error": 0
}
```
