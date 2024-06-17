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
    //node name (required)
    "node": "modbus-tcp-1",
    //group name (required)
    "group": "config_modbus_tcp_sample_2",
    //synchronous read (optional, default false)
    "sync": false,
    //filter (optional)
    "query": {
        //tag name substring match (optional)
        "name": "data",
        //tag description substring match (optional)
        "description": "switch"
    }
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

::: tip 注意
当某个点位读数值出错时，将显示 **error** 字段，不再显示 **value** 字段。
:::

## 读 Tag(分页)

*POST*  /api/v2/read/paginate

### 请求头部

**Content--Type**  application/json

**Authorization** Bearer \<token\>

### 响应状态

* 200

### 请求体

```json
{
    //node name (required)
    "node": "modbus-tcp-1",
    //group name (required)
    "group": "config_modbus_tcp_sample_2",
    //synchronous read (optional, default false)
    "sync": false,
    //filter (optional)
    "query": {
        //tag name substring match (optional)
        "name": "data",
        //tag description substring match (optional)
        "description": "switch",
        //current page (optional)
        "currentPage": 1,
        //number of tags per page (optional)
        "pageSize": 10,
        //response error tags only (optional)
        "isError": true
    }
}
```

### 响应

```json
{
   "meta": {"currentPage": 1, "pageSize": 10, "total": 1},
   "items": [ {
            "name": "tag1",
            "type": 4,
            "address": "1!400001",
            "attribute": 8,
            "description": "",
            "precison": 0,
            "decimal": 0,
            "bias": 0,
            "error": 3002 // "value": 123
        } ]
}
```

::: tip 注意
当某个点位读数值出错时，显示 **error** 字段；读取正常时显示 **value** 字段。
:::


## 测试读 Tag

*POST*  /api/v2/read/test

### 请求头部

**Content--Type**  application/json

**Authorization** Bearer \<token\>

### 响应状态

* 200

### 请求体

```json
{
    "driver": "1",
    "group": "1",
    "tag": "tag1",
    "address": "1!400002",
    "attribute": 8,
    "type": 3,
    "precision": 0,
    "decimal": 0,
    "bias": 0.0
}
```

### 响应

```json
{
    "value": 29540
}
```

```json
{
    "error": 3022
}
```

::: tip 注意
仅做读取测试，无需实际添加点位。
不适配点位和节点字节序，不计算乘系数，偏移量。
:::


## 写 Tag

### 写一个 Tag

*POST*  /api/v2/write

#### 请求头部

**Content-Type**  application/json

**Authorization** Bearer \<token\>

#### 响应状态

* 200 OK

#### 请求体

```json
{
    "node": "modbus-tcp-1",
    "group": "config_modbus_tcp_sample_2",
    "tag": "tag1",
    "value": 1234
}
```

#### 响应

```json
{
    "error": 0
}
```

### 写多个 Tag

*POST*  /api/v2/write/tags

:::tip 注意

多点位写入，目前仅支持Mitsubishi 3E, Beckhoff ADS, Modbus TCP, Modbus RTU, Siemens S7 ISOTCP, Omron FINS TCP, OPC UA, BACnet/IP 驱动。

:::

#### 请求头部

**Content-Type**  application/json

**Authorization** Bearer \<token\>

#### 响应状态

* 200 OK

#### 请求体

```json
{
    "node": "modbus-tcp-1",
    "group": "group1",
    "tags": [

        {
            "tag": "tag1",
            "value": 123
        },
        {
            "tag": "tag2",
            "value": 1233
        },
        {
            "tag": "tag3",
            "value": 7788
        },
        {
            "tag": "tag4",
            "value": 1
        },
        {
            "tag": "tag5",
            "value": "asdfda"
        }
    ]
}
```

#### 响应

```json
{
    "error": 0
}
```