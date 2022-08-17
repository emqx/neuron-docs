# HTTP API

Neuron provide a series of API services for IIoT platform, to query the basic information, to control gateway behaviors or to setup the polling configuration. IIoT platform can initiate the communication by sending request message to Neuron. By return, Neuron would send back the required information or execute the deserved action. If there is error, a error code would be returned to tell the reason of failure.

## Value

### Baud

* 115200 = 0
* 57600  = 1
* 38400  = 2
* 19200  = 3
* 9600   = 4

### Parity

* NONE   = 0
* ODD    = 1
* EVEN   = 2
* MARK   = 3
* SPACE  = 4

### Stop

* Stop_1 = 0
* Stop_2 = 1

### Data

* Data_5 = 0
* Data_6 = 1
* Data_7 = 2
* Data_8 = 3

### Data Type

* INT8   = 1
* UINT8  = 2
* INT16  = 3
* UINT16 = 4
* INT32  = 5
* UINT32 = 6
* INT64  = 7
* UINT64 = 8
* FLOAT  = 9
* DOUBLE = 10
* BIT    = 11
* BOOL   = 12
* STRING = 13
* BYTES  = 14

### Data Attribute

* READ = 0x01

* WRITE = 0x02

* SUBSCRIBE = 0x04

### Node Type

* DRIVER = 1
* APP = 2

### Plugin Kind

* STATIC = 0
* SYSTEM = 1
* CUSTOM = 2

### Node CTL

* START = 0
* STOP = 1

### Node State

* IDLE = 0
* INIT = 1
* READY = 2
* RUNNING = 3
* STOPPED = 4

### Node Link State

* DISCONNECTED = 0
* CONNECTED = 1

## Ping

*POST*  **/api/v2/ping**

### Request Headers

**Authorization** Bearer \<token\>

### Response Status

* 200 OK

## Login

*POST*   **/api/v2/login**

### Request Headers

**Content-Type**          application/json

### Response Status

* 200 OK
* 401
  * 1004, 缺少令牌
  * 1005, 解码令牌错误
* 403
  * 1006, 令牌过期
  * 1007, 验证令牌错误
  * 1008, 无效令牌

### Body

```json
{
    "name": "admin",
    "pass": "0000"
}
```

### Response

```json
{
    "token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE2MzcyODcxNjMsImlhdCI6MTYzNzIwMDc2MywiaXNzIjoiRU1RIFRlY2hub2xvZ2llcyBDby4sIEx0ZCBBbGwgcmlnaHRzIHJlc2VydmVkLiIsInBhc3MiOiIwMDAwIiwidXNlciI6ImFkbWluIn0.2EZzPC9djErrCeYNrK2av0smh-eKxDYeyu7cW4MyknI"
}
```

## Add Node

*POST*  **/api/v2/node**

### Request Headers

**Content-Type** application/json

**Authorization** Bearer \<token\>

### Response Status

* 200 OK
* 400
  * 2001 node type invalid
* 404
  * 2301 library not found
* 409
  * 2002 node exist

### Body

```json
{
    //node name
    "name": "modbus-tcp-node",
    //plugin name
    "plugin": "modbus-plugin-tcp"
}
```

### Response

```json
{
    "error": 0
}
```

## Del Node

*Delete* /api/v2/node

### Request Headers

**Content-Type**  application/json

**Authorization** Bearer \<token\>

### Response Status

* 200 OK
* 404
  * 2003 node not exist

### Body

```json
{
     //node name
    "name": "modbus-tcp-test"
}
```

### Response

```json
{
    "error": 0
}
```

## Update Node(Not Implemented)

*PUT* **/api/v2/node**

### Request Headers

**Content-Type**  application/json

**Authorization** Bearer \<token\>

### Response Status

* 200 OK
* 404
  * 2003 node exist

### Body

```json
{
    //node id
    "id": 1,
    //node name
    "name": "modbus-tcp-node"
}
```

### Response

```json
{
    "error": 0
}
```

## Get Node

*GET*  /api/v2/node

### Request Params

**type**  required

### Request Headers

**Authorization** Bearer \<token\>

### Response Status

* 200 OK

### Response

```json
{
    "nodes": [
        {
            //node name
            "name": "sample-driver-adapter",
            //plugin name
            "plugin": "modbus-tcp"
        },
        {
            "name": "modbus-tcp-adapter",
            "plugin": "modbus-tcp"
        }
    ]
}
```

## Add Group

*POST*  /api/v2/group

### Request Headers

**Content-Type**  application/json

**Authorization** Bearer \<token\>

### Response Status

* 200 OK
* 404
  * 2003 node not exist
* 409
  * 2103 group not allow

### Body

```json
{
    //group name
    "name": "gconfig1",
    //node name
    "node": "modbus-node",
    //read/upload interval(ms)
    "interval": 10000
}
```

### Response

```json
{
    "error": 0
}
```

## Del Group

*DELETE*  /api/v2/group

### Request Headers

**Content-Type**  application/json

**Authorization** Bearer \<token\>

### Response Status

* 200 OK
* 412
  * 2101 group already subscribed
* 404
  * 2003 node not exist
  * 2106 group not exist

### Body

```json
{
    //node name
    "node": "modbus-node",
    //group name
    "group": "gconfig1"
}
```

### Response

```json
{
    "error": 0
}
```

## Update Group

*PUT*  /api/v2/group

### Request Headers

**Content-Type**  application/json

**Authorization** Bearer \<token\>

### Response Status

* 200 OK
* 404
  * 2106 group not exist

### Body

```json
{
    //group name
    "group": "gconfig1",
    //node name
    "node": "modbus-node",
    //read/upload interval(ms)
    "interval": 10000
}
```

### Response

```json
{
    "error": 0
}
```

## Get Group

*GET*  /api/v2/group

### Request Params

**node**  required

### Request Headers

**Authorization** Bearer \<token\>

### Response Status

* 200 OK

### Response

````json
{
    "groups": [
        {
            //group name
            "name": "config_modbus_tcp_sample_2",
            //read/upload interval(ms)
            "interval": 2000,
            //tag count
            "tag_count": 0
        },
        {
            "name": "gconfig1",
            "interval": 10000,
            "tag_count": 0
        }
    ]
}
````

## Add Tag

*POST*  /api/v2/tags

### Request Headers

**Content-Type**  application/json

**Authorization** Bearer \<token\>

### Response Status

* 200 OK
* 206
  * 2202 tag name conflict
  * 2203 tag attribute not support
  * 2204 tag type not support
  * 2205 tag address format invalid
* 404
  * 2003 node not exist

### Body

```json
{
   //node name
    "node": "modbus-node",
   //group name
    "group": "config_modbus_tcp_sample_2",
    "tags": [
        {
           //tag name
            "name": "tag1",
           //tag address
            "address": "1!400001",
           //tag attribute
            "attribute": 1,
           //tag type
            "type": 4,
           //float/double precision, optional(0-17)
            "precision": 3,
           //decimal
            "decimal": 1
        },
        {
            "name": "tag2",
            "address": "1!00001",
            "attribute": 3,
            "type": 14
        },
        {
            "name": "tag3",
            "address": "1!400009",
            "attribute": 3,
            "type": 11
        }
    ]
}
```

### Response

```json
{
    "index": 1,
    "error": 0
}
```

## Get Tag

*GET*  /api/v2/tags

### Request Params

**node**  required

**group**  required

### Request Headers

**Authorization** Bearer \<token\>

### Response Status

* 200 OK
* 404
  * 2003 node not exist

### Response

```json
{
    "tags": [
        {
            //tag name
            "name": "tag1",
            //tag type
            "type": 4,
            //tag address
            "address": "1!400001",
            //tag attribute
            "attribute": 1,
            //float/double precision
            "precision": 1,
            //decimal
            "decimal": 0.1
        },
        {
            "name": "tag2",
            "type": 14,
            "address": "1!00001",
            "attribute": 3
        },
        {
            "name": "tag3",
            "type": 11,
            "address": "1!400009",
            "attribute": 3
        }
    ]
}
```

## Update Tag

*PUT*  /api/v2/tags

### Request Headers

**Content-Type**  application/json

**Authorization** Bearer \<token\>

### Response status

* 200 OK
* 206
  * 2201 tag not exist
  * 2202 tag name conflict
  * 2203 tag attribute not support
  * 2204 tag type not support
  * 2205 tag address format invalid
* 404
  * 2003 node not exist
  * 2106 group not exist

### Body

```json
{
    //node name
    "node": "modbus-tcp-test",
    //group name
    "group": "group1",
    "tags": [
        {
            //tag name
            "name": "tag1",
            //tag type
            "type": 6,
            //tag attribute
            "attribute": 0,
            //tag address
            "address": "1!400001",
            //float/double precison
            "precision": 1,
            //decimal
            "decimal": 0.001
        },
        {
            "name": "tag2",
            "type": 6,
            "attribute": 0,
            "address": "1!400002"
        }
    ]
}
```

### Response

```json
{
    "error": 0
}
```

## Del Tag

*DELETE*  /api/v2/tags

### Request Headers

**Content-Type**  application/json

**Authorization** Bearer \<token\>

### Response Status

* 200 OK
* 404
  * 2003 node not exist

### Body

```json
{
    //group name
    "group": "config_modbus_tcp_sample_2",
    //node name
    "node": "modbus-node",
    //tag name
    "tags": [
        "tag1",
        "tag2"
    ]
}
```

### Response

```json
{
    "error": 0
}
```

## Add Plugin

*POST*  /api/v2/plugin

### Request Headers

**Content-Type**  application/json

**Authorization** Bearer \<token\>

### Response Status

* 200 OK

* 400
  
  * 2302 library info invalid

### Body

```json
{
    //plugin library name
    "library": "plugin_name.so"
}
```

### Response

```json
{
    "error": 0
}
```

## Del Plugin

*DELETE*  /api/v2/plugin

### Request Headers

**Content-Type**  application/json

**Authorization** Bearer \<token\>

### Response Status

* 200 OK

### Body

```json
{
    //plugin name
   "plugin": "modbus-tcp"
}
```

### Response

```json
{
    "error": 0
}
```

## Get Plugin

*GET*  /api/v2/plugin

### Request Params

**plugin**  optional

### Request Headers

**Authorization** Bearer \<token\>

### Response Status

* 200 OK

### Response

```json
{
    "plugins": [
        {
            //plugin kind
            "kind": 1,
            //node type
            "node_type": 1,
            //plugin name
            "name": "plugin_name",
            //plugin library name
            "library": "plugin_lib_name",
            "description": "description"
        }
    ]
}
```

## Subscribe

*POST*  /api/v2/subscribe

### Request Headers

**Content-Type**  application/json

**Authorization** Bearer \<token\>

### Response Status

* 200 OK
* 404
  * 2106 group not exist

### Body

```json
{
    //app name
    "app": "mqtt-node",
    //driver name
    "driver": "modbus-node",
    //driver node group name
    "group": "gconfig1"
}
```

### Response

```json
{
    "error": 0
}
```

## UnSubscribe

*DELETE*  /api/v2/subscribe

### Request Headers

**Content-Type**  application/json

**Authorization** Bearer \<token\>

### Response Status

* 200 OK
* 404
  * 2106 group not exist

### Body

```json
{
    //app name
    "app": "mqtt-node",
    //driver name
    "driver": "driver-node",
    //driver node group name
    "group": "gconfig1"
}
```

### Response

```json
{
    "error": 0
}
```

## Read Tag

*POST*  /api/v2/read

### Request Headers

**Content--Type**  application/json

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

## Get Plugin Schema

*GET*  /api/v2/schema

### Request Params

**plugin_name**  required

### Response Status

* 200 OK

### Response

```json
{
 "tag_type": [
  4,
  5,
  6,
  7,
  8,
  9,
  10,
  11,
  14
 ],
 "params": [
  "host",
  "port",
  "mode",
  "baud_rate",
  "real_param"
 ],
 "host": {
  "name": "host",
  "description": "host",
  "type": "string",
  "default": "127.0.0.1",
  "valid": {
   "length": 30
  }
 },
 "port": {
  "name": "port",
  "description": "port",
  "type": "int",
  "default": 502,
  "valid": {
   "min": 1024,
   "max": 65535
  }
 },
 "mode": {
  "name": "mode",
  "description": "mode",
  "type": "bool",
  "default": false,
  "valid": {}
 },
 "baud_rate": {
  "name": "baud rate",
  "description": "port",
  "type": "int",
  "default": 9600,
  "valid": {
   "value": [
    9600,
    112800
   ]
  }
 },
 "real_param": {
  "name": "real param",
  "description": "real",
  "type": "real",
  "default": 11.22,
  "valid": {
   "min": 1.1,
   "max": 20.2
  }
 },
 "ca": {
  "name": "ca",
  "description": "",
  "attribute": "optional",
  "type": "file",
  "condition": {
   "field": "mode",
   "value": true
  },
  "valid": {
   "length": 1024
  }
 }
}
```

## Node Setting

*POST*  /api/v2/node/setting

### Request Headers

**Content-Type**  application/json

**Authorization** Bearer \<token\>

### Response Status

* 200 OK
* 400
  * 2003 node not exist
  * 2004 node setting invalid

### Body

```json
//The parameter fields in json fill in different fields according to different plugins
{
    //node name
    "node": "modbus-node",
    "params": {
        "param1": 1,
        "param2": "1.1.1.1",
        "param3": true,
        "param4": 11.22
    }
}
```

### Response

```json
{
    "error": 0
}
```

## Get Node Setting

*GET*  /api/v2/node/setting

### Request Params

**node**  required

### Request Headers

**Authorization** Bearer \<token\>

### Response Status

* 200 OK
  * 2005 node setting not found
* 404
  * 2003 node not exist

### Response

```json
//The parameter fields in json fill in different fields according to different plugins
{
    "node": "modbus-node",
    "params": {
        "param1": "1.1.1.1",
        "param2": 502
    }
}
```

## Node CTL

*POST*  /api/v2/node/ctl

### Request Headers

**Content-Type**  application/json

**Authorization** Bearer \<token\>

### Request Status

* 200 OK
* 409
  * 2006 node not ready
  * 2007 node is running
  * 2008 node not running
  * 2009 node is stopped

### Body

```json
{
    //node name
    "node": "modbus-node",
    //0 start, 1 stop
    "cmd": 0
}
```

### Response

```json
{
    "error": 0
}
```

## Get Node State

*GET*  /api/v2/node/state

### Request Params

**node**  optional

### Request Headers

**Authorization** Bearer \<token\>

### Response Status

* 200 OK

### Response

```json
{
    //running state
    "running": 2,
    //link state
    "link": 1
}

{
    "states": [
        {
            "node": "modbus-node1",
            "running": 2,
            "link": 1
        },
        {
            "node": "modbus-node2",
            "running": 1,
            "link": 0
        }
    ]
}
```

## Get Subscribe Group

*GET*  /api/v2/subscribe

### Request Params

**app**  required

### Request Headers

**Authorization** Bearer \<token\>

### Response Status

* 200
* 400

### Response

```json
{
    "groups": [
        {
            //driver name
            "driver": "modbus-node",
            //group name
            "group": "g1name"
        },
        {
            "driver": "modbus-node",
            "group": "g2name"
        }
    ]
}
```

## Get Log

*GET*  /api/v2/log

### Request Params

**since**       required, UTC timestamp

**until**       required, UTC timestamp, with `since` forms the interval [since, until)

**level**       optional, log level, should be one of trace, debug, info, warn, error, fatal

**page**        required

**page_size**   required, should be in range [200, 10000]

### Request Headers

**Authorization** Bearer \<token\>

### Response Status

* 200
* 400
  * 1003 request param invalid

### Response

```json
{
    "error": 0,
    "rows": [
        "2022-02-11 15:30:57 WARN  [neuron] src/main.c:90: recv sig: 2"
    ]
}
```

## Get Version

*GET*  /api/v2/version

### Request Headers

**Authorization** Bearer \<token\>

### Response Status

* 200
* 500
  * 1001 internal error

### Response

```json
{
    "build_date": "2022-06-01",
    "revision": "99e2184+dirty", // dirty indicates uncommit changes
    "version": "2.0.1"
}
```

## Upload License

*POST*  /api/v2/license

### Request Headers

**Authorization** Bearer \<token\>

### Response Status

* 200
  * 0    OK
  * 2402 license expired
* 400
  * 2401 license invalid
* 500
  * 1001 internal error

### Body

```json
{
    "license": "-----BEGIN CERTIFICATE-----\nMIID2TCCAsGgAwIBAgIEATSJqjA....."
}
```

### Response

```json
{
    "error": 2401
}
```

## Get License Info

*GET*  /api/v2/license

### Request Headers

**Authorization** Bearer \<token\>

### Response Status

* 200 OK
* 404
  * 2400 license not found
* 500
  * 1001 internal error

### Response

```json
{
    "error": 0,
    "license_type": "trial",
    "max_nodes": 1000,
    "max_node_tags": 20000,
    "valid": true,
    "valid_since": "2022-03-30 09:10:40",
    "valid_until": "2023-03-30 09:10:40",
    "enabled_plugins": ["modbus-rtu", "opcua", "s7comm"]
}
```
