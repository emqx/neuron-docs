# API

以下内容描述 Neuron MQTT 插件如何上报采集的数据，以及如何通过 MQTT 协议读写点位数据。

注意下文中涉及的 MQTT 主题中出现的 **{node_name}** 指代的是实际的 MQTT 北向节点名字， **{driver_name}** 指代南向节点名字，**{group_name}** 指代南向节点下的组的名字。


## 数据上报

Neuron MQTT 插件将采集到的数据以 JSON 形式发布到指定的主题。
上报数据的具体格式由**上报数据格式**参数指定，有 *tags-format* 和 *values-format* 两种格式。

### 上报主题

在 Neuron 2.4.0 版本之前，上报主题由 **upload-topic** 参数指定， 通过仪表板配置时默认为 **/neuron/{node_name}/upload** 。

自 Neuron 2.4.0 版本起，**upload-topic** 参数被删除了。
上报主题改为在群组订阅请求中指定，其默认值为 **/neuron/{node_name}/{driver_name}/{group_name}** 。

### Tags 格式

在 *tags-format* 格式中， 上报的数据由以下字段构成：
* `timestamp` : 数据采集时的 UNIX 时间戳。
* `node` : 被采集的南向节点的名字。
* `group` : 被采集的南向节点的点位组的名字。
* `tags` : 点位数据数组，每个元素对应一个点位。


以下为使用 *tags-format* 格式的数据样例，其中所有点位数据存放在一个数组中，每个数组元素包含点位的名字，采集成功时的数据值或者采集失败时的错误码。

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

### Values 格式

在 *values-format* 格式中， 上报的数据由以下字段构成：
* `timestamp` : 数据采集时的 UNIX 时间戳。
* `node` : 被采集的南向节点的名字。
* `group` : 被采集的南向节点的点位组的名字。
* `values` : 存储采集成功的点位值的字典。
* `errors` : 存储采集失败的错误码的字典。

以下为使用 *values-format* 格式的数据样例，采集成功的点位数据值存放在一个字典中，采集失败的点位错误码存放在另一个字典中。

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

::: tip
当点位采集成功时，返回采集到的数据。当点位采集发生错误时，返回错误码，不再返回数值。
:::

## 读 Tags

### 请求

通过发送 JSON 形式的请求到 MQTT 主题 **/neuron/{node_name}/read/req** ，您可以读取一组点位数据。

#### 请求体

读请求体由以下字段构成：
* `uuid` : 唯一的标志，会在响应中原样返回用以区分对应的请求。
* `node` : 某个南向节点名字。
* `group` : 南向节点的某个组的名字。

以下为一个读请求样例：

```json
{
    "uuid": "bca54fe7-a2b1-43e2-a4b4-1da715d28eab",
    "node": "modbus",
    "group": "grp"
}
```

### 响应

读响应会发布到 MQTT 主题 **/neuron/{node_name}/read/resp** 。

#### 响应体

读响应体由以下字段构成：
* `uuid` : 对应请求中所设置的唯一标志。
* `tags` : 点位数据数组，和 [tags 格式](#tags-格式)中的表示方法一样.

以下为一个读响应样例：

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
当点位采集成功时，返回采集到的数据。当点位采集发生错误时，返回错误码，不再返回数值。
:::

## 写 Tag

### 请求

通过发送 JSON 形式的请求到 MQTT 主题 **/neuron/{node_name}/write/req** ，您可以写一个点位数据。

#### 请求体

写请求体由以下字段构成：
* `uuid` : 唯一的标志，会在响应中原样返回用以区分对应的请求。
* `node` : 某个南向节点名字。
* `group` : 南向节点的某个组的名字。
* `tag` : 要写入的点位名字。
* `value` : 要写入的数据值。

以下为一个写请求样例：

```json
{
    "uuid": "cd32be1b-c8b1-3257-94af-77f847b1ed3e",
    "node": "modbus",
    "group": "grp",
    "tag": "tag0",
    "value": 1234
}
```

### 响应

写响应会发布到 MQTT 主题 **/neuron/{node_name}/write/resp** 。

#### 响应体

写响应体由以下字段构成：
* `uuid` : 对应请求中所设置的唯一标志。
* `error` : 错误码。0 代表成功，非零代表失败。

以下为一个读响应样例：
```json
{
  "uuid": "cd32be1b-c8b1-3257-94af-77f847b1ed3e",
  "error": 0
}
```
