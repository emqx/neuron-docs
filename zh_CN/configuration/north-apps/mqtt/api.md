# 数据上下行格式

以下内容描述 Neuron MQTT 插件如何上报采集的数据，以及如何通过 MQTT 插件实现读写点位数据。

注意下文中涉及的 MQTT 主题中出现的 **{node_name}** 指代的是实际的 MQTT 北向节点名字， **{driver_name}** 指代南向驱动节点名字，**{group_name}** 指代南向节点下的组的名字。


## 数据上报

Neuron MQTT 插件将采集到的数据以 JSON 形式发布到指定的主题。
上报数据的具体格式由**上报数据格式**参数指定，有多种格式可选。

### 上报主题

上报主题在北向节点订阅中指定，其默认值为 **/neuron/{node_name}/{driver_name}/{group_name}** 

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
* `metas` : 驱动相关的元数据信息。

以下为使用 **values-format** 格式的数据样例，采集成功的点位数据值存放在一个字典中，采集失败的点位错误码存放在另一个字典中。

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
    },
    "metas":{}
}
```

### 自定义格式

在自定义格式中，可以使用内置支持的变量自定义数据上报格式。

#### 内置变量

| *变量名称* | *说明* |
| ------------------ | ---------------------- | 
| `${timestamp}` | 数据采集时的 UNIX 时间戳。 |
| `${node}` | 被采集的南向节点的名字。 |
| `${group}` | 被采集的南向节点的点位组的名字。 |
| `${tags}` | 南向采集点位有效值的数组。 |
| `${tag_values}` | 南向采集点位有效值的数组，Value 格式。 |
| `${tag_errors}` | 南向采集点位报错的数组。 |
| `${tag_error_values}` | 南向采集点位报错的数组，Value 格式。 |
| `${static_tags}` | 订阅时自定义配置的静态点位。 |
| `${static_tag_values}` | 订阅时自定义配置的静态点位，Value 格式。 |

#### 示例

自定义数据格式配置为：
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

数据上报的格式为：
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
当点位采集成功时，返回采集到的数据。当点位采集发生错误时，返回错误码，不再返回数值。
:::

## 读 Tags

### 请求

通过发送 JSON 形式的请求到 MQTT 主题 **/neuron/{node_name}/read/req**，您可以读取一组点位数据。

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
* `tags` : 点位数据数组，和 [tags 格式](#tags-格式)中的表示方法一样。

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

通过发送 JSON 形式的请求到**写请求主题**参数指定的 MQTT 主题，您可以写一个点位数据。可在 MQTT 参数配置中配置写请求的主题，默认为为 **/neuron/{random_str}/write/req**。


#### 请求体

#### 写一个 Tag

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

#### 写多个 Tag

Neuron 提供了对多点位写入的支持。要在一次请求中可以写入多个点位数据, 写请求体应由以下字段构成：
* `uuid` : 唯一的标志，会在响应中原样返回用以区分对应的请求。
* `node` : 某个南向节点名字。
* `group` : 南向节点的某个组的名字。
* `tags` : 点位数据数组，每个元素对应一个点位。

以下为一个写请求样例：

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

### 响应

写响应会发布到**写响应主题**参数指定的 MQTT 主题。默认**写响应主题**参数为 **/neuron/{random_str}//write/resp**。

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

## 驱动状态上报

上报所有南向驱动状态到指定的 MQTT 主题。

### 状态上报主题

上报主题在北向节点配置中指定，其默认值为 **/neuron/{random_str}/state/update** 

### 状态上报间隔

状态上报间隔在北向节点配置中指定，指每条消息之间间隔的秒数，其默认值为 1，允许的范围为 1-3600。

### 上报消息格式

上报的数据由以下字段构成：
* `timestamp` : 数据采集时的 UNIX 时间戳。
* `states` : 节点状态信息的数组。

以下是一个驱动状态上报消息样例。

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
