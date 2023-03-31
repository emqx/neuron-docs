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
    //node name
    "node": "modbus-tcp-1",
    //group name
    "group": "config_modbus_tcp_sample_2"
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

*POST*  /api/v2/write

### Request Headers

**Content-Type**  application/json

**Authorization** Bearer \<token\>

### Response Status

* 200 OK

### Body

```json
{
    "node": "modbus-tcp-1",
    "group": "config_modbus_tcp_sample_2",
    "tag": "tag1",
    "value": 1234
}
```

### Response

```json
{
    "error": 0
}
```