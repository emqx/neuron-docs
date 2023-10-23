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
    "group": "config_modbus_tcp_sample_2"
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