# MQTT API

MQTT 客户端和 Neuron 进行交互的所有主题。包括读、写、订阅。

所有主题中的 **{node_name}** 指的是实际的 MQTT 北向应用名称，在 Neuron UI 的北向应用管理中设置。

## 上传数据

### 响应

*默认主题* **/neuron/{node_name}/upload**

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
当数值被正确读取时，将显示读取到的数值。当读点位数值发生错误时，将显示错误码，不再显示数值。一个 Group 发送一条信息。
:::

上传主题可以在驱动配置表单中设置，一旦设置成自定义主题，则默认主题将被停用。

Body 有两种消息格式，您可以在 Neuron UI 中 mqtt 配置表单中选择。

## 心跳数据

### 响应

*默认主题* **/neuron/{node_name}/heartbeat**

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

心跳主题可以在驱动配置表单中设置，一旦设置成自定义主题，则默认主题将被停用。

目前的心跳报文被默认设置为每3秒发送一次。

## 读 Tags

### 请求

*主题*  **/neuron/{node_name}/read/req**

#### Body

```json
{
    "uuid": "bca54fe7-a2b1-43e2-a4b4-1da715d28eab",
    "node": "modbus-tcp-1",
    "group": "group-2"
}
```

### 响应

*主题*  **/neuron/{node_name}/read/resp**

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
当读点位数值发生错时，将显示 **error** 字段，不再显示 **value** 字段。
:::

## 写 Tag

### 请求

*主题*  **/neuron/{node_name}/write/req**

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

### 响应

*主题*  **/neuron/{node_name}/write/resp**

#### Body

```json
{
  "uuid": "cd32be1b-c8b1-3257-94af-77f847b1ed3e",
  "error": 0
}
```
