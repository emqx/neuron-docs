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
    "group": "config_modbus_tcp_sample_2"
    //tag name substring match (optional)
    "name": "hold_bit",
    //tag description substring match (optional)
    "desc": "switch",
    //synchronous read (optional, default false)
    "sync": false
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