# Configuration

Neuron provide a series of API services for IIoT platform, to query the basic information, to control gateway behaviors or to setup the polling configuration. IIoT platform can initiate the communication by sending request message to Neuron. By return, Neuron would send back the required information or execute the deserved action. If there is error, a error code would be returned to tell the reason of failure.

## Ping

*POST*  **/api/v2/ping**

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

## Password

*POST*   **/api/v2/password**

### Request Headers

**Content-Type** application/json

**Authorization** Bearer \<token\>

### Response Status

* 200 OK
* 401
  * 1004 missing token
  * 1005 decoding token error
  * 1012 password length too short or too long
  * 1013 duplicate password
* 403
  * 1006 expired token
  * 1007 validate token error
  * 1008 invalid token

### Body

```json
{
    "name": "admin",
    "old_pass": "01234",
    "new_pass": "56789"
}
```

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
  * 2301 library not found
* 409
  * 2002 node exist

### Body

```json
{
    //node name
    "name": "modbus-tcp-node",
    //plugin name
    "plugin": "Modbus TCP"
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
    "name": "modbus-tcp-node"
}
```

### Response

```json
{
    "error": 0
}
```

## Update Node

*PUT* **/api/v2/node**

### Request Headers

**Content-Type**  application/json

**Authorization** Bearer \<token\>

### Response Status

* 200 OK
* 400
  * 2013 node not allow update
  * 2015 node name is empty
* 404
  * 2003 node not exist
* 409
  * 2002 node exist
* 500
  * 1001 internal server error
  * 1010 server is busy

### Body

```json
{
    "name": "modbus-node",
    "new_name": "modbus-tcp-node"
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

**plugin** optional

**node** optional

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
            "plugin": "Modbus TCP"
        },
        {
            "name": "modbus-tcp-adapter",
            "plugin": "Modbus TCP"
        }
    ]
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

:::tip
Please refer to [Plugin Setting](./plugin-setting.md) for the configuration parameters of each plugin.
:::

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
    "states": [
        {
            // node name
            "node": "modbus-node1",
            //running state
            "running": 2,
            //link state
            "link": 1,
            //average round trip time communicating with devices
            "rtt": 100
        },
        {
            "node": "modbus-node2",
            "running": 1,
            "link": 0,
            "rtt": 9999
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
  * 2003 node not exist
  * 2106 group not exist
* 409
  * 2104 group exist

### Body

To update group name:
```json
{
    //node name
    "node": "modbus-node",
    //group name
    "group": "gconfig1",
    //group new name
    "new_name": "group1"
}
```

To update group interval:
```json
{
    //node name
    "node": "modbus-node",
    //group name
    "group": "gconfig1",
    //read/upload interval(ms)
    "interval": 10000
}
```

To update both group name and interval:
```json
{
    //node name
    "node": "modbus-node",
    //group name
    "group": "gconfig1",
    //group new name
    "new_name": "group1",
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

**node**  optional

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
            "attribute": 8,
           //tag type
            "type": 4,
           //optional, float/double precision, optional(0-17)
            "precision": 0,
           //optional, decimal
            "decimal": 0,
           //optional, description
           "description": "",
           //optional, when the attribute is static,the value field needs to be added.
           "value": 12
        },
        {
            "name": "tag2",
            "address": "1!00001",
            "attribute": 3,
            "type": 3,
            "decimal": 0.01
        },
        {
            "name": "tag3",
            "address": "1!400009",
            "attribute": 3,
            "type": 9,
            "precision": 3
        },
        {
            "name": "static_tag",
            "address": "",
            "attribute": 10,
            "type": 1,
            "description": "It is a static tag",
            "value": 42
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

## Add Tag across multiple groups

*POST*  /api/v2/gtags

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
  * 2106 group not exist

### Body

```json
{
    //node name
    "node": "modbus-node",
    "groups": [
        {
            //group name
            "group": "group_1",
            //group interval
            "interval": 3000,
            "tags": [
                {
                    //tag name
                    "name": "tag1",
                    //tag address
                    "address": "1!400001",
                    //tag attribute
                    "attribute": 3,
                    //tag type
                    "type": 3,
                    //optional, float/double precision, optional(0-17)
                    "precision": 0,
                    //optional, decimal
                    "decimal": 0,
                    //optional, description
                    "description": "",
                    //optional, when the attribute is static,the value field needs to be added.
                    "value": 12
                },
                {
                    "name": "tag2",
                    "address": "1!400002",
                    "attribute": 3,
                    "type": 9,
                    "precision": 3
                }
            ]
        },
        {
            "group": "group_2",
            "interval": 3000,
            "tags": [
                {
                    "name": "tag1",
                    "address": "1!400003",
                    "attribute": 3,
                    "type": 9,
                    "precision": 3
                },
                {
                    "name": "tag2",
                    "address": "1!400004",
                    "attribute": 3,
                    "type": 9,
                    "precision": 3
                }
            ]
        }
    ]
}

```


### Response

```json
{
    //tags count
    "index": 4,
    "error": 0
}
```

## Get Tag

*GET*  /api/v2/tags

### Request Params

**node**  required

**group**  required

**name** optional

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
            "attribute": 8,
            //description
            "description": "",
            //float/double precision
            "precision": 0,
            //decimal
            "decimal": 0,
            //optional, when the attribute is static
            "value": 12
        },
        {
            "name": "tag2",
            "type": 14,
            "address": "1!00001",
            "attribute": 3,
            "description": "",
            "precison": 0,
            "decimal": 0,
        },
        {
            "name": "tag3",
            "type": 11,
            "address": "1!400009",
            "attribute": 3,
            "description": "",
            "precison": 0,
            "decimal": 0,
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
            "type": 8,
            //tag attribute
            "attribute": 0,
            //tag address
            "address": "1!400001",
            //description
            "description":"",
            //float/double precison
            "precision": 0,
            //decimal
            "decimal": 0,
            //optional, when the attribute is static,the value field needs to be added.
            "value": 12
        },
        {
            "name": "tag2",
            "type": 6,
            "attribute": 0,
            "address": "1!400002",
            "description":"",
            "precison": 0,
            "decimal": 0,
        },
        {
            "name": "static_tag",
            "address": "",
            "attribute": 10,
            "type": 8,
            "description":"",
            "precison": 0,
            "decimal": 0,
            "value": 42
        }
    ]
}
```

### Response

```json
{
    "error": 0,
    "index": 1
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
  * 2303 library name conflict
  * 2304 library open fail
  * 2305 library module invalid
  * 2307 library instance fail
  * 2308 library arch no support
  * 2310 library add fail
  * 2311 library module exist
  * 2313 library module kind no support

### Body

```json
{
    //plugin library name
    "library": "plugin_name.so",
    // base64 content of schema json file
    "schema_file":"...",
    // base64 content of library file
    "so_file":"..."
}
```

### Response

```json
{
    "error": 0
}
```


## Update Plugin

*PUT*  /api/v2/plugin

### Request Headers

**Content-Type**  application/json

**Authorization** Bearer \<token\>

### Response Status

* 200 OK

* 400
  
  * 2302 library no found
  * 2302 library info invalid
  * 2304 library open fail
  * 2305 library module invalid
  * 2307 library instance fail
  * 2308 library arch no support
  * 2312 library module no exist
  * 2313 library module kind no support

### Body

```json
{
    //plugin library name
    "library": "plugin_name.so",
    // base64 content of schema json file
    "schema_file":"...",
    // base64 content of library file
    "so_file":"..."
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

* 400
* 
  * 2306 library of system no allow delete
  * 2309 library in using


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
            "name": "Modbus TCP",
            //plugin library name
            "library": "libplugin-modbus-tcp.so",
            "description": "description",
            "description_zh": "描述",
            "schema": "modbus-tcp"
        },
        {
            "kind": 1,
            "node_type": 2,
            "name": "MQTT",
            "library": "libplugin-mqtt.so",
            "description": "Neuron northbound MQTT plugin bases on NanoSDK.",
            "description_zh": "基于 NanoSDK 的 Neuron 北向应用 MQTT 插件",
            "schema": "mqtt"
        }
    ]
}
```

## Get Plugin Schema

*GET*  /api/v2/schema

### Request Params

**schema_name**  required

### Request Headers

**Authorization** Bearer \<token\>

### Response Status

* 200 OK

### Response

```json
{
    "tag_regex": [
        {
            "type": 3,
            "regex": "^[0-9]+![3-4][0-9]+(#B|#L|)$"
        },
        {
            "type": 4,
            "regex": "^[0-9]+![3-4][0-9]+(#B|#L|)$"
        },
        {
            "type": 5,
            "regex": "^[0-9]+![3-4][0-9]+(#BB|#BL|#LL|#LB|)$"
        },
        {
            "type": 6,
            "regex": "^[0-9]+![3-4][0-9]+(#BB|#BL|#LL|#LB|)$"
        },
        {
            "type": 7,
            "regex": "^[0-9]+![3-4][0-9]+(#B|#L|)$"
        },
        {
            "type": 8,
            "regex": "^[0-9]+![3-4][0-9]+(#B|#L|)$"
        },
        {
            "type": 9,
            "regex": "^[0-9]+![3-4][0-9]+(#BB|#BL|#LL|#LB|)$"
        },
        {
            "type": 10,
            "regex": "^[0-9]+![3-4][0-9]+(#B|#L|)$"
        },
        {
            "type": 11,
            "regex": "^[0-9]+!([0-1][0-9]+|[3-4][0-9]+\\.([0-9]|[0-1][0-5]))$"
        },
        {
            "type": 13,
            "regex": "^[0-9]+![3-4][0-9]+\\.[0-9]+(H|L|)$"
        }
    ],
    "group_interval": 1000,
    "connection_mode": {
        "name": "Connection Mode",
        "name_zh": "连接模式",
        "description": "Neuron as the client, or as the server",
        "description_zh": "Neuron 作为客户端或服务端",
        "attribute": "required",
        "type": "map",
        "default": 0,
        "valid": {
            "map": [
                {
                    "key": "Client",
                    "value": 0
                },
                {
                    "key": "Server",
                    "value": 1
                }
            ]
        }
    },
    "interval": {
        "name": "Send Interval",
        "name_zh": "指令发送间隔",
        "description": "Send reading instruction interval(ms)",
        "description_zh": "发送读指令时间间隔，单位为毫秒",
        "attribute": "required",
        "type": "int",
        "default": 20,
        "valid": {
            "min": 0,
            "max": 3000
        }
    },
    "host": {
        "name": "IP Address",
        "name_zh": "IP地址",
        "description": "Local IP in server mode, remote device IP in client mode",
        "description_zh": "服务端模式中填写本地 IP，客户端模式中填写目标设备 IP",
        "attribute": "required",
        "type": "string",
        "valid": {
            "regex": "/^((2[0-4]\\d|25[0-5]|[01]?\\d\\d?)\\.){3}(2[0-4]\\d|25[0-5]|[01]?\\d\\d?)$/",
            "length": 30
        }
    },
    "port": {
        "name": "Port",
        "name_zh": "端口号",
        "description": "Local port in server mode, remote device port in client mode",
        "description_zh": "服务端模式中填写本地端口号，客户端模式中填写远程设备端口号",
        "attribute": "required",
        "type": "int",
        "default": 502,
        "valid": {
            "min": 1,
            "max": 65535
        }
    },
    "timeout": {
        "name": "Connection Timeout",
        "name_zh": "连接超时时间",
        "description": "Connection timeout(ms)",
        "description_zh": "连接超时时间，单位为毫秒",
        "attribute": "required",
        "type": "int",
        "default": 3000,
        "valid": {
            "min": 1000,
            "max": 65535
        }
    }
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
    "app": "mqtt",
    //driver name
    "driver": "modbus-tcp",
    //driver node group name
    "group": "group-1",
    //optional, when using the MQTT plugin, the topic field needs to be added
    "params": {
        "topic": "/neuron/mqtt/group-1"
    }
}
```

### Response

```json
{
    "error": 0
}
```

## Subscribe Multiple Groups

*POST*  /api/v2/subscribes

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
  "app": "mqtt",
  "groups": [
    {
      //driver name
      "driver": "modbus1",
      //group name
      "group": "group1",
      //optional, depends on plugins
      "params": {
        //when using the MQTT plugin, the topic key is the upload topoic
        "topic": "/neuron/mqtt/modbus1/group1"
      }
    },
    {
      "driver": "modbus2",
      "group": "group2",
      "params": {
        "topic": "/neuron/mqtt/modbus2/group2"
      }
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

## Update Subscribe Parameters

*PUT*  /api/v2/subscribe

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
    "app": "mqtt",
    //driver name
    "driver": "modbus-tcp",
    //driver node group name
    "group": "group-1",
    "params": {
        //when using the MQTT plugin, the topic key is the upload topic
        "topic": "/neuron/mqtt/group-1"
    }
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
    "app": "mqtt",
    //driver name
    "driver": "modbus-tcp",
    //driver node group name
    "group": "group-1",
    //optional, when using the MQTT plugin, the topic field needs to be added
    "params": {
        "topic": "/neuron/mqtt/group-1"
    }
}
```

### Response

```json
{
    "error": 0
}
```

## Get Subscribe Group

*GET*  /api/v2/subscribe

### Request Params

**app**  required
**driver**  optional, substring match against driver name
**group**  optional, substring match against group name

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
            "driver": "modbus-tcp",
            //group name
            "group": "group-1",
            //when using the MQTT plugin, the topic field needs to be added
            "params": {
                "topic": "/neuron/mqtt/group-1"
            }
        },
        {
            //driver name
            "driver": "modbus-tcp",
            //group name
            "group": "group-2",
            //when using the MQTT plugin, the topic field needs to be added
            "params": {
                "topic": "/neuron/mqtt/group-2"
            }
        }
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
    "version": "2.4.0"
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
    "valid_until": "2023-03-15 08:11:19",
    "valid_since": "2022-03-15 08:11:19",
    "valid": false,
    "max_nodes": 1,
    "max_node_tags": 1,
    "used_nodes": 12,
    "used_tags": 846,
    "license_type": "retail",
    "error": 0,
    "enabled_plugins": [
        "MODBUS TCP Advance",
        "OPC UA"
    ],
    "hardware_token": "I+kZidSifiyVSbz0/EgcM6AcefnlfR4IU19ZZUnTS18=",
    "object": "emq",
    "email_address": "emq@emqx.io"
}
```

## Update node log level

*PUT*  /api/v2/log/level

### Request Headers

**Authorization** Bearer \<token\>

### Response Status

* 200 OK
* 404
  * 2003 node not exist
* 500
  * 1001 internal error
  * 1010 is busy

### Body

```json
{
    "node_name": "modbus-tcp"
}
```

### Response

```json
{
    "error": 0
}
```

:::tip
Call the api to modify the log level of the node to debug, and automatically switch to the default level in about ten minutes.
:::

## Download File

*GET* /api/v2/file

### Request Headers

**Authorization** Bearer \<token\>

### Request Params

**file_path** Required, absolute path of the file

### Response Status

* 404
    * 1011 file not exist
    * 4101 file open failure
    * 4102 file read failure

### Response

Return the contents of the file and download the file, when responding correctly.

Return the error code, when an error response occurs.

```json
{
    "error": 1011
}
```

## Get file list information

*GET* /api/v2/file/info

### Request Headers

**Authorization** Bearer \<token\>

### Request Params

**dir_path** Required, absolute path of the directory.

### Response Status

* 404
    * 1011 file not exist
    * 4101 file open failure

### Response

Response to the file name, size, creation time and update time, when responding correctly.

```json
{
    "files": [
        {
            "name": "neuron",
            "size": 4096,
            "ctime": "Wed Jan  4 02:38:12 2023",
            "mtime": "Mon Dec 26 09:48:42 2022"
        },
        {
            "name": "test.txt",
            "size": 13,
            "ctime": "Wed Jan  4 02:38:12 2023",
            "mtime": "Mon Dec 26 09:48:42 2022"
        }
    ]
}
```

Response to the error code, when an error response occurs.

```json
{
    "error": 1011
}
```

## Add Template

*POST* /api/v2/template

### Request Headers

**Content-Type**  application/json

**Authorization** Bearer \<token\>

### Response Status

* 200 OK
* 206
    * 2203    tag attribute not support
    * 2204    tag type not support
    * 2205    tag address format invalid
    * 2206    tag name too long
    * 2207    tag address too long
    * 2208    tag description too long
    * 2209    tag precision invalid
* 400
    * 2105    group parameter invalid
    * 2107    group name too long
    * 2502    template name too long
    * 3013    plugin name too long
    * 3016    plugin does not support template
* 404
    * 3014    plugin not found
* 409
    * 2104    group exist
    * 2202    tag name conflict
    * 2500    template already exists
* 500
    * 1010    server is busy
    * 1001    internal error

### Body

```json
{
    "name": "rtu template",
    "plugin": "Modbus RTU",
    "groups": [
        {
            "name": "group1",
            "interval": 2000,
            "tags": [
                {
                    "name": "tag1",
                    "type": 4,
                    "address": "1!400001",
                    "attribute": 1,
                    "precison": 1,
                    "decimal": 0
                },
                {
                    "name": "tag2",
                    "type": 11,
                    "address": "1!400009",
                    "attribute": 3
                }
            ]
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

## Delete Template

*DELETE*  /api/v2/template

### Request Headers

**Content-Type**  application/json

**Authorization** Bearer \<token\>

### Request Params

**name** optional, name of the template to delete. If not specified, then delete all templates.

### Response Status

* 200 OK
* 404
    * 2501    template not found
* 500
    * 1010    server is busy

### Response

```json
{
    "error": 0
}
```

## Get Template

*GET*  /api/v2/template

### Request Headers

**Content-Type**  application/json

**Authorization** Bearer \<token\>

### Request Params

**name** optional, name of a particular template.

### Response Status

* 200 OK
* 400
    * 1003    request param invalid
* 404
    * 2501    template not found
* 500
    * 1001    internal error
    * 1010    server is busy

### Response

Without the **name** request parameter, return all templates.

```json
{
    "templates": [
        {
            "name": "template1",
            "plugin": "modbus tcp"
        },
        {
            "name": "template2",
            "plugin": "opc ua"
        }
    ]
}
```

When the **name** request parameter is specified, return detail information of the template
of the given name.

```json
{
    "name": "rtu template",
    "plugin": "Modbus RTU",
    "groups": [
        {
            "name": "group1",
            "interval": 2000,
            "tags": [
                {
                    "name": "tag1",
                    "type": 4,
                    "address": "1!400001",
                    "attribute": 1,
                    "precison": 1,
                    "decimal": 0
                },
                {
                    "name": "tag2",
                    "type": 11,
                    "address": "1!400009",
                    "attribute": 3
                }
            ]
        }
    ]
}
```

## Template Instantiation

*POST* /api/v2/template/inst

### Request Headers

**Content-Type**  application/json

**Authorization** Bearer \<token\>

### Response Status

* 200 OK
* 400
    * 2304    library failed to open
    * 2502    template name too long
* 404
    * 2301    library not found
    * 2501    template not found
* 409
    * 2002    node exist
    * 2307    library not allow create instance
* 500
    * 1001    internal error
    * 1010    server is busy

### Body

```json
{
    "name": "rtu template",
    "node": "modbus-rtu",
}
```

### Response

```json
{
    "error": 0
}
```

## Template Multi Node Instantiation

*POST* /api/v2/template/instances

### Request Headers

**Content-Type**  application/json

**Authorization** Bearer \<token\>

### Response Status

* 200 OK
* 400
    * 2304    library failed to open
    * 2502    template name too long
* 404
    * 2301    library not found
    * 2501    template not found
* 409
    * 2002    node exist
    * 2307    library not allow create instance
* 500
    * 1001    internal error
    * 1010    server is busy

### Body

```json
{
    "nodes": [
      {
        "name": "rtu template",
        "node": "node1"
      },
      {
        "name": "tcp template",
        "node" "node2"
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

## Add Template Group

*POST*  /api/v2/template/group

### Request Headers

**Content-Type**  application/json

**Authorization** Bearer \<token\>

### Response Status

* 200 OK
* 400
    * 2105    group parameter invalid
    * 2107    group name too long
    * 2502    template name too long
* 404
    * 2501    template not found
* 409
    * 2104    group exist
* 500
    * 1001    internal server error
    * 1010    server is busy

### Body

```json
{
    "template": "modbus-template",
    "group": "group1",
    "interval": 10000
}
```

### Response

```json
{
    "error": 0
}
```

## Del Template Group

*DELETE*  /api/v2/template/group

### Request Headers

**Content-Type**  application/json

**Authorization** Bearer \<token\>

### Response Status

* 200 OK
* 400
    * 2107    group name too long
    * 2502    template name too long
* 404
    * 2106    group not exist
    * 2501    template not found
* 500
    * 1001    internal server error
    * 1010    server is busy

### Body

```json
{
    "template": "modbus-template",
    "group": "group1"
}
```

### Response

```json
{
    "error": 0
}
```

## Update Group

*PUT*  /api/v2/template/group

### Request Headers

**Content-Type**  application/json

**Authorization** Bearer \<token\>

### Response Status


* 200 OK
* 400
    * 2105    group parameter invalid
    * 2107    group name too long
    * 2502    template name too long
* 404
    * 2106    group not exist
    * 2501    template not found
* 500
    * 1001    internal server error
    * 1010    server is busy

### Body

To update group name:
```json
{
    //template name
    "template": "modbus-template",
    //group name
    "group": "gconfig1",
    //group new name
    "new_name": "group1"
}
```

To update group interval:
```json
{
    //template name
    "template": "modbus-template",
    //group name
    "group": "gconfig1",
    //interval(ms)
    "interval": 10000
}
```

To update both group name and interval:
```json
{
    //template name
    "template": "modbus-template",
    //group name
    "group": "gconfig1",
    //group new name
    "new_name": "group1",
    //interval(ms)
    "interval": 10000
}
```

### Response

```json
{
    "error": 0
}
```

## Get Template Group

*GET*  /api/v2/template/group

### Request Params

**name**  required, name of the template.

### Request Headers

**Authorization** Bearer \<token\>

### Response Status

* 200 OK
* 400
    * 1003    request param invalid
* 404
    * 2501    template not found
* 500
    * 1001    internal server error
    * 1010    server is busy

### Response

````json
{
    "groups": [
        {
            "name": "group1",
            "interval": 2000,
            "tag_count": 2
        }
    ]
}
````

## Add Template Tag

*POST*  /api/v2/template/tag

### Request Headers

**Content-Type**  application/json

**Authorization** Bearer \<token\>

### Response Status

* 200 OK
* 206
    * 2203    tag attribute not support
    * 2204    tag type not support
    * 2205    tag address format invalid
    * 2206    tag name too long
    * 2207    tag address too long
    * 2208    tag description too long
    * 2209    tag precision invalid
* 400
    * 2107    group name too long
    * 2502    template name too long
* 404
    * 2106    group not exist
    * 2501    template not found
* 409
    * 2202    tag name conflict
* 500
    * 1001    internal server error
    * 1010    server is busy

### Body

```json
{
    "template": "modbus-template",
    "group": "group1",
    "tags": [
        {
            "name": "tag1",
            "address": "1!400001",
            "attribute": 8,
            "type": 4,
            "precision": 0,
            "decimal": 0,
            "description": "",
            "value": 12
        },
        {
            "name": "tag2",
            "address": "1!00001",
            "attribute": 3,
            "type": 3,
            "decimal": 0.01
        }
    ]
}
```

### Response

```json
{
    "index": 2,
    "error": 0
}
```

## Update Template Tag

*PUT*  /api/v2/template/tag

### Request Headers

**Content-Type**  application/json

**Authorization** Bearer \<token\>

### Response status

* 200 OK
* 206
    * 2201    tag not exist
    * 2203    tag attribute not support
    * 2204    tag type not support
    * 2205    tag address format invalid
    * 2206    tag name too long
    * 2207    tag address too long
    * 2208    tag description too long
    * 2209    tag precision invalid
* 400
    * 2107    group name too long
    * 2502    template name too long
* 404
    * 2106    group not exist
    * 2501    template not found
* 500
    * 1001    internal server error
    * 1010    server is busy

### Body

```json
{
    "template": "modbus-template",
    "group": "group1",
    "tags": [
        {
            "name": "tag1",
            "address": "1!400001",
            "attribute": 8,
            "type": 4,
            "precision": 0,
            "decimal": 0,
            "description": "",
            "value": 12
        },
        {
            "name": "tag2",
            "address": "1!00001",
            "attribute": 3,
            "type": 3,
            "decimal": 0.01
        }
    ]
}
```

### Response

```json
{
    "index": 2,
    "error": 0
}
```

## Del Template Tag

*DELETE*  /api/v2/template/tag

### Request Headers

**Content-Type**  application/json

**Authorization** Bearer \<token\>

### Response Status

* 200 OK
* 206
    * 2206    tag name too long
* 400
    * 2107    group name too long
    * 2502    template name too long
* 404
    * 2106    group not exist
    * 2501    template not found
* 500
    * 1001    internal server error
    * 1010    server is busy

### Body

```json
{
    "template": "modbus-template",
    "group": "group1",
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

## Get Template Tag

*GET*  /api/v2/template/tag

### Request Params

**template**  required, name of the template.

**group**  required, name of the group.

**name** optional, to filter by tag name.

### Request Headers

**Authorization** Bearer \<token\>

### Response Status

* 200 OK
* 400
    * 1003    request param invalid
* 404
    * 2106    group not exist
    * 2501    template not found
* 500
    * 1001    internal server error
    * 1010    server is busy

### Response

```json
{
    "tags": [
        {
            "name": "tag1",
            "type": 4,
            "address": "1!400001",
            "attribute": 8,
            "description": "",
            "precision": 0,
            "decimal": 0,
            "value": 12
        },
        {
            "name": "tag2",
            "type": 14,
            "address": "1!00001",
            "attribute": 3,
            "description": "",
            "precison": 0,
            "decimal": 0,
        }
    ]
}
```
