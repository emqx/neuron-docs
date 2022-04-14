# Neuron 2.x api

Neuron would provide a series of API services for IIoT platform, to query the basic information, to control gateway behaviors or to setup the polling configuration. IIoT platform must initiate the communication by sending request message to Neuron. By return, Neuron would send back the required information or execute the deserved action. If there is error, a error code would be returned to tell the reason of failure.

## Value

### Data Type

* BYTE = 2
* INT8 = 3
* INT16 = 4
* INT32 = 5
* INT64 = 6
* UINT8 = 7
* UINT16 = 8
* UINT32 = 9
* UINT64 = 10
* FLOAT = 11
* DOUBLE = 12
* BOOL = 13
* BIT = 14
* STRING = 15

### Data Attribute

* READ = 0x01

* WRITE = 0x02

* SUBSCRIBE = 0x04

### Node Type

* DRIVER = 1
* WEB = 2
* MQTT = 3
* DRIVERX = 4
* APP = 5

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
* CONNECTING = 1
* CONNECTED = 2

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

| Error code    | Type of error                |
| :-----------: | :--------------------------- |
| 401           | 1004, Missing token           |
| 401           | 1005, Decoding token error    |
| 401           | 1009, User or password error  |
| 403           | 1006, Expired token           |
| 403           | 1007, Validate token error    |
| 403           | 1008, Invalid token           |

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

## Logout

*POST*  **/api/v2/logout**

### Request Headers

**Content-Type** application/json

**Authorization** Bearer \<token\>

### Reponse Status

* 200 OK

### Response

```json
{
    "error": 0
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
  * 2301 plugin library not found
* 409
  * 2002 node exist

### Body

```json
{
    //node type
    "type": 1,
    //node name
    "name": "modbus-tcp-node",
    //plugin name
    "plugin_name": "modbus-plugin-tcp"
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
    //node id
    "id": 7
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
            //node id
            "id": 1,
            "plugin_id": 1
        },
        {
            "name": "modbus-tcp-adapter",
            "id": 4,
            "plugin_id": 2
        },
        {
            "name": "opcua-adapter",
            "id": 6,
            "plugin_id": 3
        },
        {
            "name": "modbus-tcp-test",
            "id": 7,
            "plugin_id": 4
        }
    ]
}
```

## Add Group Config

*POST*  /api/v2/gconfig

### Request Headers

**Content-Type**  application/json

**Authorization** Bearer \<token\>

### Response Status

* 200 OK
* 404
  * 2003 node not exist
* 409
  * 2103 group config conflict

### Body

```json
{
    //group config name
    "name": "gconfig1",
    //node id
    "node_id": 4,
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

## Del Group Config

*DELETE*  /api/v2/gconfig

### Request Headers

**Content-Type**  application/json

**Authorization** Bearer \<token\>

### Response Status

* 200 OK
* 412
  * 2102 group config in use
* 404
  * 2003 node not exist
  * 2101 group config not exist

### Body

```json
{
    //node id
    "node_id": 4,
    //group config name
    "name": "gconfig1"
}
```

### Response

```json
{
    "error": 0
}
```

## Update Group Config(Not Implemented)

*PUT*  /api/v2/gconfig

### Request Headers

**Content-Type**  application/json

**Authorization** Bearer \<token\>

### Response Status

* 200 OK
* 404
  * 2101 group config not exist

### Body

```json
{
    //group config name
    "name": "modbus-tcp-config1",
    //read/upload interval(ms)
    "interval": 20000,
    //node id
    "node_id": 4
}
```

### Response

```json
{
    "error": 0
}
```

## Get Group Config

*GET*  /api/v2/gconfig

### Request Params

**node_id**  required

### Request Headers

**Authorization** Bearer \<token\>

### Response Status

* 200 OK

### Response

````json
{
    "group_configs": [
        {
            //group config name
            "name": "config_modbus_tcp_sample_2",
            //read/upload interval(ms)
            "interval": 2000,
            //pipe count
            "pipe_count": 1,
            //tag count
            "tag_count": 0
        },
        {
            "name": "gconfig1",
            "interval": 10000,
            "pipe_count": 0,
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
  * 2202  tag name conflict
  * 2203 tag attribute not support
  * 2204 tag type not support
  * 2205 tag address format invalid
* 404
  * 2003 node not exist

### Body

```json
{
   //node id
    "node_id": 4,
   //group config name
    "group_config_name": "config_modbus_tcp_sample_2",
    "tags": [
        {
           //tag name
            "name": "tag1",
           //tag address
            "address": "1!400001",
           //tag attribute
            "attribute": 1,
           //tag type
            "type": 4
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
    "error": 0
}
```

## Get Tag

*GET*  /api/v2/tags

### Request Params

**node_id**  requred

**group_config_name**  optional

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
            //tag group config name
            "group_config_name": "config_modbus_tcp_sample_2",
            //tag id
            "id": 1
        },
        {
            "name": "tag2",
            "type": 14,
            "address": "1!00001",
            "attribute": 3,
            "group_config_name": "config_modbus_tcp_sample_2",
            "id": 4
        },
        {
            "name": "tag3",
            "type": 11,
            "address": "1!400009",
            "attribute": 3,
            "group_config_name": "config_modbus_tcp_sample_2",
            "id": 5
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
  * 2101 group config not exist

### Body

```json
{
    //node id
    "node_id": 4,
    "tags": [
        {
            //tag id
            "id": 4,
            //tag name
            "name": "tag1",
            //tag type
            "type": 6,
            //tag attribute
            "attribute": 0,
            //tag address
            "address": "1!400001"
        },
        {
            "id": 5,
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
    //group config name
    "group_config_name": "config_modbus_tcp_sample_2",
    //node id
    "node_id": 4,
    //tag ids
    "ids": [
        4,
        5
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
  
* 404

  * 2201 library not found

* 409
  * 2203 library name conflict

### Body

```json
{
    //plugin library name
    "lib_name": "plugin_name.so"
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
    //plugin id
    "id": 1
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

**plugin_id**  optional

### Request Headers

**Authorization** Bearer \<token\>

### Response Status

* 200 OK

### Response

```json
{
    "plugin_libs": [
        {
            //plugin id
            "id": 1,
            //plugin kind
            "kind": 1,
            //node type
            "node_type": 1,
            //plugin name
            "name": "plugin_name",
            //plugin library name
            "lib_name": "plugin_lib_name"
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
  * 2101 group config not exist

### Body

```json
{
    //src node id
    "src_node_id": 4,
    //dst node id
    "dst_node_id": 5,
    //src node group config name
    "name": "gconfig1"
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
  * 2101 group config not exist

### Body

```json
{
    //src node id
    "src_node_id": 4,
    //dst node id
    "dst_node_id": 5,
    //src node group config name
    "name": "gconfig1"
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
    "node_name": "modbus-tcp-1",
    //group config name
    "group_config_name": "config_modbus_tcp_sample_2"
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

*Node* When the value is read correctly, only the value is displayed, only when the value is read incorrectly, the error code is displayed, not the value.

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
    "node_name": "modbus-tcp-1",
    "group_config_name": "config_modbus_tcp_sample_2",
    "tag_name": "tag1",
    "value": 1234
}
```

### Response

```json
{
    "error": 0
}
```

## Get TTY

*GET*  /api/v2/tty

### Response Status

* 200 OK

### Response

```json
{
    "ttys": [
        "/dev/tty0",
        "/dev/tty1"
    ]
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
    //node id
    "node_id": 123,
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

**node_id**  required

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
    "node_id": 4,
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
    //node id
    "id": 4,
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

**node_id**  required

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
```

## Get Subscribe Group Config

*GET*  /api/v2/subscribe

### Request Params

**node_id**  required

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
            //node id
            "node_id": 1,
            //group config name
            "group_config_name": "g1name"
        },
        {
            "node_id": 2,
            "group_config_name": "g2name"
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
  * 1003 param is wrong

### Response

```json
{
    "error": 0,
    "rows": [
        "2022-02-11 15:30:57 WARN  [neuron] src/main.c:90: recv sig: 2"
    ]
}
```
