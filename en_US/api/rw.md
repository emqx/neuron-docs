# Read & Write

## Read Tag

*POST*  /api/v2/read

### Request Headers

**Content--Type**  application/json

**Authorization** Bearer \<token\>

### Response Status

* 200

### Body

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

### Response

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
The value is displayed only when the value is read correctly, when the value is read incorrectly, the error code is displayed, not the value.
:::

## Read Tag(pagination)

*POST*  /api/v2/read/paginate

### Request Headers

**Content--Type**  application/json

**Authorization** Bearer \<token\>

### Response Status

* 200

### Body

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

### Response

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

::: tip
The **value** is displayed only when the value is read correctly, when the value is read incorrectly, the error code is displayed with **error**.
:::


## TEST Reading Tag

*POST*  /api/v2/read/test

### Request Headers

**Content--Type**  application/json

**Authorization** Bearer \<token\>

### Response Status

* 200

### Body

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

### Response

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

::: tip
Only perform reading tests, no need to actually add the tag.
Not compatible with tag and node byte order, does not calculate decimal and offset.
:::

## Write Tag

### Write One Tag

*POST*  /api/v2/write

#### Request Headers

**Content-Type**  application/json

**Authorization** Bearer \<token\>

#### Response Status

* 200 OK

#### Body

```json
{
    "node": "modbus-tcp-1",
    "group": "config_modbus_tcp_sample_2",
    "tag": "tag1",
    "value": 1234
}
```

#### Response

```json
{
    "error": 0
}
```

### Write Multiple Tags

*POST*  /api/v2/write/tags

:::tip 

Multiple tags writing currently only supports Mitsubishi 3E, Beckhoff ADS, Modbus TCP, Modbus RTU, Siemens S7 ISOTCP, Omron FINS TCP, OPC UA, BACnet/IP drivers.

:::

#### Request Headers

**Content-Type**  application/json

**Authorization** Bearer \<token\>

#### Response Status

* 200 OK

#### Body

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

#### Response

```json
{
    "error": 0
}
```