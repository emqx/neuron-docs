# 读写

## 读 Tag

*POST*  /api/v2/read

### 请求头部

**Content--Type**  application/json

**Authorization** Bearer \<token\>

### 响应状态

* 200

### 请求体

```json
{
    //node name
    "node": "modbus-tcp-1",
    //group name
    "group": "config_modbus_tcp_sample_2",
    //synchronous read (optional, default false)
    "sync": false
}
```

### 响应

```json
{
    "tags": [
        {
            //tag nmae
            "name": "data1",
            //tag value
            "value": 1,
        },
        {
            "name": "data2",
            "error": 2014
        },
        {
            "name": "data3",
            "value": true,
        }
    ]
}
```

::: tip
当某个点位读数值出错时，将显示 **error** 字段，不再显示 **value** 字段。
:::

## 写 Tag

*POST*  /api/v2/write

### 请求头部

**Content-Type**  application/json

**Authorization** Bearer \<token\>

### 响应状态

* 200 OK

### 请求体

```json
{
    "node": "modbus-tcp-1",
    "group": "config_modbus_tcp_sample_2",
    "tag": "tag1",
    "value": 1234
}
```

### 响应

```json
{
    "error": 0
}
```