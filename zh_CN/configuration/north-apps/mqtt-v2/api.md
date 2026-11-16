# 数据上下行格式

以下介绍 MQTT V2 插件如何上报采集的数据，以及如何通过 MQTT V2 插件写点位。状态消息的格式见 [MQTT V2 概述](./overview.md#状态消息)。

## 数据上报

订阅的组每上报一次，插件就向该组的数据 topic 发布一条消息，默认 topic 为 `{Topic 前缀}/{设备名}/data`。上报的时机由南向组的采集间隔决定；对于设置了订阅属性的点位，只有值发生变化时才会上报。

消息内容由应用配置中的两个 JSON 模板决定：

- **数据模板**：整条消息的结构。
- **点位模板**：数据模板中 `${tags}`、`${tags_kv}`、`${tags[名称]}` 展开时，每个点位的结构。

### 默认模板

数据模板：

```json
{
  "timestamp": "${timestamp}",
  "device": "${device}",
  "group": "${group}",
  "tags": "${tags}"
}
```

点位模板：

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

使用默认模板时，上报的数据如下：

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

`tag0` 没有描述和单位，所以这两个字段没有输出；`tag2` 读取失败，只输出错误码。默认点位模板包含 `${tag.error}`，所以会带上读取失败的点位。如果点位模板里去掉 `${tag.error}`，这些点位不再出现在 `${tags}`、`${tags_kv}` 和 `${tags[名称]}` 中。

### 模板规则

- 模板必须是合法的 JSON，变量写在字符串里，例如 `"${tags}"`。
- 字符串里只有一个变量时，替换为该变量原本的 JSON 类型。例如 `"${timestamp}"` 替换为数字，`"${tags}"` 替换为数组。
- 变量和文字混写时，拼接成字符串。例如 `"${device}-${group}"` 替换为 `"modbus-1-group-1"`。
- key 也可以使用变量。例如点位模板 `{"${tag.name}": "${tag.value}"}` 输出 `{"tag0": 123}`。
- 变量取不到值时，该字段不输出，例如点位没有质量、描述为空，或正常点位的错误码。在数组中取不到值时输出 `null`。
- 点位模板可以是单个变量。例如点位模板为 `"${tag.value}"` 时，`${tags_kv}` 输出 `{"tag0": 123, "tag1": 25.5}`。
- 模板中不允许出现未知变量；点位变量 `${tag.xxx}` 只能用在点位模板中，`${tags}` 等点位集合变量只能用在数据模板中。不符合规则的配置保存时会报错。

### 模板变量

数据模板中可以使用以下变量：

| 变量 | 说明 |
| --- | --- |
| `${app}` | 北向应用名 |
| `${device}` | 南向设备名 |
| `${group}` | 组名 |
| `${sub_topic}` | 该组实际使用的数据 topic |
| `${timestamp}` | 当前时间，Unix 毫秒时间戳 |
| `${TIME_RFC3339}` | RFC 3339 时间，如 `2026-11-16T08:00:00.123+08:00` |
| `${TIME_UTC}` | UTC 时间，如 `2026-11-16T00:00:00.123Z` |
| `${TIME_LOCAL}` | 本地时间，如 `2026-11-16 08:00:00.123` |
| `${TIME_UNIX}` | 当前时间，Unix 秒级时间戳 |
| `${TIME:格式}` | 按 strftime 格式输出时间，如 `${TIME:%Y-%m-%d %H:%M:%S}` |
| `${tags}` | 全部点位，展开为数组 |
| `${tags_kv}` | 全部点位，展开为以点位名为 key 的对象 |
| `${tags[名称]}` | 单个点位，按点位模板展开 |
| `${tags[名称].属性}` | 单个点位的某个属性，属性名同点位模板，如 `${tags[tag0].value}` |
| `${properties}` | 设备的全部属性，展开为对象；没有属性时不输出 |
| `${properties[key]}` | 设备的单个属性 |

点位模板中可以使用以下变量，以及上表中除 `${tags}`、`${tags_kv}`、`${tags[...]}` 以外的所有变量：

| 变量 | 说明 |
| --- | --- |
| `${tag.name}` | 点位名 |
| `${tag.value}` | 点位值 |
| `${tag.timestamp}` | 点位采样时间戳，驱动提供时才有 |
| `${tag.sourceTimestamp}` | 源时间戳，驱动提供时才有 |
| `${tag.serverTimestamp}` | 服务器时间戳，驱动提供时才有 |
| `${tag.quality}` | 点位质量，驱动提供时才有 |
| `${tag.description}` | 点位描述 |
| `${tag.unit}` | 点位单位 |
| `${tag.error}` | 读取失败时的错误码。点位模板使用了它，读取失败的点位才会进入上报 |
| `${tag.type}` | 点位数据类型，如 `INT16` |

::: tip
点位描述和单位修改后，最长约 30 秒在数据消息中生效。
:::

### 模板示例

**带上设备属性**

数据模板：

```json
{
  "timestamp": "${timestamp}",
  "device": "${device}",
  "properties": "${properties}",
  "tags": "${tags}"
}
```

上报的数据：

```json
{"timestamp": 1731744000123, "device": "modbus-1", "properties": {"location": "Building A", "line": 3}, "tags": [{"name": "tag0", "value": 123}]}
```

**扁平结构**

数据模板：

```json
{
  "site": "${properties[location]}",
  "ts": "${timestamp}",
  "values": "${tags_kv}"
}
```

点位模板：

```json
"${tag.value}"
```

上报的数据：

```json
{"site": "Building A", "ts": 1731744000123, "values": {"tag0": 123, "tag1": 25.5}}
```

**只取部分点位**

数据模板：

```json
{
  "device": "${device}",
  "time": "${TIME_RFC3339}",
  "temperature": "${tags[tag1].value}",
  "unit": "${tags[tag1].unit}"
}
```

上报的数据：

```json
{"device": "modbus-1", "time": "2026-11-16T08:00:00.123+08:00", "temperature": 25.5, "unit": "C"}
```

## 写点位

向设备的写请求 topic `{Topic 前缀}/{设备名}/write/request` 发布写请求，插件把写入结果发布到 `{Topic 前缀}/{设备名}/write/response`。

### 写请求

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

| 字段 | 说明 |
| --- | --- |
| `id` | 选填，请求标识，原样带回写响应中，可以是任意 JSON 值。 |
| `version` | 选填，消息格式版本。目前支持 `"1.0"` 和 `"neuron"`，都表示 neuron 原生格式；不填时也按该格式解析。 |
| `params.values` | 必填，要写入的点位名和值，不能为空。值可以是数字、布尔、字符串、元素类型相同的数组，或 JSON 对象（写入 CUSTOM 类型的点位）。 |
| `params.group` | 选填，点位所在的组。多个已订阅的组中有同名点位时需要指定。 |

- 只能写入本应用已订阅的组中的点位。
- 一次请求可以写入同一设备多个组中的点位。

### 写响应

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

| 字段 | 说明 |
| --- | --- |
| `id`、`version` | 与写请求中的值相同，请求中没有时不返回。 |
| `error` | 整体结果。全部成功时为 0，否则为第一个失败点位的错误码。 |
| `tags` | 每个点位的写入结果，0 表示成功，其他值为错误码。 |

请求本身不合法时，例如不是 JSON，所有点位都返回同一个错误码。常见错误码：

| 错误码 | 说明 |
| --- | --- |
| 1002 | 请求不是 JSON，或 `params.values` 缺失或为空 |
| 1003 | `version` 不支持，或 `group`、点位值格式不正确 |
| 2102 | 指定的组未被本应用订阅 |
| 2201 | 已订阅的组中不存在该点位 |
| 3004 | 点位不可写 |
