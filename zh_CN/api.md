# API

Neuron 将为 IIoT 平台提供一系列 API 服务，用于查询基本信息、控制网关行为或设置轮询配置。 IIoT 平台必须通过向 Neuron 发送请求消息来启动通信。 通过返回，Neuron 将返回所需的信息或执行相应的操作。 如果有错误，将返回一个错误代码来说明失败的原因。

## 值

### 数据类型

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

### 点位属性

* READ = 0x01

* WRITE = 0x02

* SUBSCRIBE = 0x04

### Node 类型

* DRIVER = 1
* APP = 2

### 插件类型

* STATIC = 0
* SYSTEM = 1
* CUSTOM = 2

### Node 控制

* START = 0
* STOP = 1

### Node 状态

* IDLE = 0
* INIT = 1
* READY = 2
* RUNNING = 3
* STOPPED = 4

### Node 连接状态

* DISCONNECTED = 0
* CONNECTING = 1
* CONNECTED = 2

## Ping

*POST*  **/api/v2/ping**

### 请求 Headers

**Authorization** Bearer \<token\>

### 响应状态

* 200 OK

## 登录

*POST*   **/api/v2/login**

### 请求 Headers

**Content-Type**          application/json

### 响应状态

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

### 响应

```json
{
    "token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE2MzcyODcxNjMsImlhdCI6MTYzNzIwMDc2MywiaXNzIjoiRU1RIFRlY2hub2xvZ2llcyBDby4sIEx0ZCBBbGwgcmlnaHRzIHJlc2VydmVkLiIsInBhc3MiOiIwMDAwIiwidXNlciI6ImFkbWluIn0.2EZzPC9djErrCeYNrK2av0smh-eKxDYeyu7cW4MyknI"
}
```

## 添加 Node

*POST*  **/api/v2/node**

### 请求 Headers

**Content-Type** application/json

**Authorization** Bearer \<token\>

### 响应状态

* 200 OK
* 400
  * 2001 node 类型无效
* 404
  * 2301 未找到插件库
* 409
  * 2002 node 不存在

### Body

```json
{
    //node name
    "name": "modbus-tcp-node",
    //plugin name
    "plugin_name": "modbus-plugin-tcp"
}
```

### 响应

```json
{
    "error": 0
}
```

## 删除 Node

*Delete* /api/v2/node

### 请求 Headers

**Content-Type**  application/json

**Authorization** Bearer \<token\>

### 响应状态

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

### 响应

```json
{
    "error": 0
}
```

## 更新 Node(未实现)

*PUT* **/api/v2/node**

### 请求 Headers

**Content-Type**  application/json

**Authorization** Bearer \<token\>

### 响应状态

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

### 响应

```json
{
    "error": 0
}
```

## 获取 Node

*GET*  /api/v2/node

### 请求 Params

**type**  必需

### 请求 Headers

**Authorization** Bearer \<token\>

### 响应状态

* 200 OK

### 响应

```json
{
    "nodes": [
        {
            //node name
            "name": "sample-driver-adapter",
            //plugin name
            "plugin_name": "modbus-tcp"
        },
        {
            "name": "modbus-tcp-adapter",
            "plugin_name": "modbus-tcp"
        }
    ]
}
```

## 添加 Group Config

*POST*  /api/v2/gconfig

### 请求 Headers

**Content-Type**  application/json

**Authorization** Bearer \<token\>

### 响应状态

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
    //node name
    "node_name": "modbus-node",
    //read/upload interval(ms)
    "interval": 10000
}
```

### 响应

```json
{
    "error": 0
}
```

## 删除 Group Config

*DELETE*  /api/v2/gconfig

### 请求 Headers

**Content-Type**  application/json

**Authorization** Bearer \<token\>

### 响应状态

* 200 OK
* 412
  * 2102 group config in use
* 404
  * 2003 node not exist
  * 2101 group config not exist

### Body

```json
{
    //node name
    "node_name": "modbus-node",
    //group config name
    "name": "gconfig1"
}
```

### 响应

```json
{
    "error": 0
}
```

## 更新 Group Config(未实现)

*PUT*  /api/v2/gconfig

### 请求 Headers

**Content-Type**  application/json

**Authorization** Bearer \<token\>

### 响应状态

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

### 响应

```json
{
    "error": 0
}
```

## 获取 Group Config

*GET*  /api/v2/gconfig

### 请求 Params

**node_name**  必需

### 请求 Headers

**Authorization** Bearer \<token\>

### 响应状态

* 200 OK

### 响应

````json
{
    "group_configs": [
        {
            //group config name
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

## 添加 Tag

*POST*  /api/v2/tags

### 请求 Headers

**Content-Type**  application/json

**Authorization** Bearer \<token\>

### 响应状态

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
   //node name
    "node_name": "modbus-node",
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

### 响应

```json
{
    "error": 0
}
```

## 获取 Tag

*GET*  /api/v2/tags

### 请求 Params

**node_name**  requred

**group_config_name**  optional

### 请求 Headers

**Authorization** Bearer \<token\>

### 响应状态

* 200 OK
* 404
  * 2003 node not exist

### 响应

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
            "group_config_name": "config_modbus_tcp_sample_2"
        },
        {
            "name": "tag2",
            "type": 14,
            "address": "1!00001",
            "attribute": 3,
            "group_config_name": "config_modbus_tcp_sample_2"
        },
        {
            "name": "tag3",
            "type": 11,
            "address": "1!400009",
            "attribute": 3,
            "group_config_name": "config_modbus_tcp_sample_2"
        }
    ]
}
```

## 更新 Tag

*PUT*  /api/v2/tags

### 请求 Headers

**Content-Type**  application/json

**Authorization** Bearer \<token\>

### 响应状态

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
    //node name
    "node_name": 4,
    "tags": [
        {
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
            "name": "tag2",
            "type": 6,
            "attribute": 0,
            "address": "1!400002"
        }
    ]
}
```

### 响应

```json
{
    "error": 0
}
```

## 删除 Tag

*DELETE*  /api/v2/tags

### 请求 Headers

**Content-Type**  application/json

**Authorization** Bearer \<token\>

### 响应状态

* 200 OK
* 404
  * 2003 node not exist

### Body

```json
{
    //group config name
    "group_config_name": "config_modbus_tcp_sample_2",
    //node name
    "node_name": "modbus-node",
    //tag ids
    "names": [
        "tag1",
        "tag2"
    ]
}
```

### 响应

```json
{
    "error": 0
}
```

## 添加插件

*POST*  /api/v2/plugin

### 请求 Headers

**Content-Type**  application/json

**Authorization** Bearer \<token\>

### 响应状态

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

### 响应

```json
{
    "error": 0
}
```

## 删除插件

*DELETE*  /api/v2/plugin

### 请求 Headers

**Content-Type**  application/json

**Authorization** Bearer \<token\>

### 响应状态

* 200 OK

### Body

```json
{
    //plugin name
    "name": "modbus-tcp"
}
```

### 响应

```json
{
    "error": 0
}
```

## 获取插件

*GET*  /api/v2/plugin

### 请求 Params

**plugin_id**  optional

### 请求 Headers

**Authorization** Bearer \<token\>

### 响应状态

* 200 OK

### 响应

```json
{
    "plugin_libs": [
        {
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

## 订阅

*POST*  /api/v2/subscribe

### 请求 Headers

**Content-Type**  application/json

**Authorization** Bearer \<token\>

### 响应状态

* 200 OK
* 404
  * 2101 group config not exist

### Body

```json
{
    //app name
    "app_name": "mqtt-node",
    //driver name
    "driver_name": "modbus-node",
    //driver node group config name
    "name": "gconfig1"
}
```

### 响应

```json
{
    "error": 0
}
```

## 取消订阅

*DELETE*  /api/v2/subscribe

### 请求 Headers

**Content-Type**  application/json

**Authorization** Bearer \<token\>

### 响应状态

* 200 OK
* 404
  * 2101 group config not exist

### Body

```json
{
    //app name
    "app name": "mqtt-node",
    //driver name
    "driver name": "driver-node",
    //driver node group config name
    "name": "gconfig1"
}
```

### 响应

```json
{
    "error": 0
}
```

## 读点位

*POST*  /api/v2/read

### 请求 Headers

**Content--Type**  application/json

### 响应状态

* 200

### Body

```json
{
    //node name
    "node_name": "modbus-tcp-1",
    //group config name
    "group_name": "config_modbus_tcp_sample_2"
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

*注意* 当某个点位读数值出错时，将显示 **error** 字段，不再显示 **value** 字段。

## 写点位

*POST*  /api/v2/write

### 请求 Headers

**Content-Type**  application/json

**Authorization** Bearer \<token\>

### 响应状态

* 200 OK

### Body

```json
{
    "node_name": "modbus-tcp-1",
    "group_name": "config_modbus_tcp_sample_2",
    "tag_name": "tag1",
    "value": 1234
}
```

### 响应

```json
{
    "error": 0
}
```

## 获取插件 Schema

*GET*  /api/v2/schema

### 请求 Params

**plugin_name**  required

### 响应状态

* 200 OK

### 响应

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

## Node 配置

*POST*  /api/v2/node/setting

### 请求 Headers

**Content-Type**  application/json

**Authorization** Bearer \<token\>

### 响应状态

* 200 OK
* 400
  * 2003 node not exist
  * 2004 node setting invalid

### Body

```json
//The parameter fields in json fill in different fields according to different plugins
{
    //node name
    "node_name": "modbus-node",
    "params": {
        "param1": 1,
        "param2": "1.1.1.1",
        "param3": true,
        "param4": 11.22
    }
}
```

### 响应

```json
{
    "error": 0
}
```

## 获取 Node 配置

*GET*  /api/v2/node/setting

### 请求 Params

**node_name**  必需

### 请求 Headers

**Authorization** Bearer \<token\>

### 响应状态

* 200 OK
  * 2005 node setting not found
* 404
  * 2003 node not exist

### 响应

```json
//The parameter fields in json fill in different fields according to different plugins
{
    "node_name": "modbus-node",
    "params": {
        "param1": "1.1.1.1",
        "param2": 502
    }
}
```

## Node 控制

*POST*  /api/v2/node/ctl

### 请求 Headers

**Content-Type**  application/json

**Authorization** Bearer \<token\>

### 请求状态

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
    "name": "modbus-node",
    //0 start, 1 stop
    "cmd": 0
}
```

### 响应

```json
{
    "error": 0
}
```

## 获取 Node 状态

*GET*  /api/v2/node/state

### 请求 Params

**node_name**  required

### 请求 Headers

**Authorization** Bearer \<token\>

### 响应状态

* 200 OK

### 响应

```json
{
    //running state
    "running": 2,
    //link state
    "link": 1
}
```

## 获取订阅的 Group Config

*GET*  /api/v2/subscribe

### 请求 Params

**node_name**  required

### 请求 Headers

**Authorization** Bearer \<token\>

### 响应状态

* 200
* 400

### 响应

```json
{
    "groups": [
        {
            //node name
            "node_name": "modbus-node",
            //group config name
            "group_config_name": "g1name"
        },
        {
            "node_name": "modbus-node",
            "group_config_name": "g2name"
        }
    ]
}
```

## 获取日志

*GET*  /api/v2/log

### 请求 Params

**since**       必需， UTC 时间戳

**until**       必需， UTC timestamp, with `since` forms the interval [since, until)

**level**       选填， log level, should be one of trace, debug, info, warn, error, fatal

**page**        必需

**page_size**   必需，范围应在 200 ～ 10000

### 请求 Headers

**Authorization** Bearer \<token\>

### 响应状态

* 200
* 400
  * 1003 错误参数

### 响应

```json
{
    "error": 0,
    "rows": [
        "2022-02-11 15:30:57 WARN  [neuron] src/main.c:90: recv sig: 2"
    ]
}
```

## 获取版本信息

*GET*  /api/v2/version

### 请求头部

**Authorization** Bearer \<token\>

### 响应状态

* 200
* 500
  * 1001 服务器内部错误

### 响应

```json
{
    "build_date": "2022-06-01",
    "revision": "99e2184+dirty", // dirty 表示有未提交的更改
    "version": "2.0.1"
}
```
