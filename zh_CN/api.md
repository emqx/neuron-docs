# API

Neuron 将为 IIoT 平台提供一系列 API 服务，用于查询基本信息、控制网关行为或设置轮询配置。 IIoT 平台必须通过向 Neuron 发送请求消息来启动通信。 通过返回，Neuron 将返回所需的信息或执行相应的操作。 如果有错误，将返回一个错误代码来说明失败的原因。

## 值

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

### 数据类型

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
    "plugin": "modbus-plugin-tcp"
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
            "plugin": "modbus-tcp"
        },
        {
            "name": "modbus-tcp-adapter",
            "plugin": "modbus-tcp"
        }
    ]
}
```

## 添加 Group

*POST*  /api/v2/group

### 请求 Headers

**Content-Type**  application/json

**Authorization** Bearer \<token\>

### 响应状态

* 200 OK
* 404
  * 2003 node not exist
* 409
  * 2103 group not allow

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

### 响应

```json
{
    "error": 0
}
```

## 删除 Group

*DELETE*  /api/v2/group

### 请求 Headers

**Content-Type**  application/json

**Authorization** Bearer \<token\>

### 响应状态

* 200 OK
* 412
  * 2101 group already subscribed
* 404
  * 2003 node not exist
  * 2101 group not exist

### Body

```json
{
    //node name
    "node": "modbus-node",
    //group name
    "group": "gconfig1"
}
```

### 响应

```json
{
    "error": 0
}
```

## 更新 Group(未实现)

*PUT*  /api/v2/group

### 请求 Headers

**Content-Type**  application/json

**Authorization** Bearer \<token\>

### 响应状态

* 200 OK
* 404
  * 2106 group not exist

### Body

```json
{
    //group name
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

## 获取 Group

*GET*  /api/v2/group

### 请求 Params

**node**  必需

### 请求 Headers

**Authorization** Bearer \<token\>

### 响应状态

* 200 OK

### 响应

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

## 添加 Tag

*POST*  /api/v2/tags

### 请求 Headers

**Content-Type**  application/json

**Authorization** Bearer \<token\>

### 响应状态

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
    "index": 1,
    "error": 0
}
```

## 获取 Tag

*GET*  /api/v2/tags

### 请求 Params

**node**  必需

**group**  必需

### 请求 Headers

**Authorization** Bearer \<token\>

### 响应状态

* 200 OK
* 404
  * 2003 node 不存在

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
            "attribute": 1
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

## 更新 Tag

*PUT*  /api/v2/tags

### 请求 Headers

**Content-Type**  application/json

**Authorization** Bearer \<token\>

### 响应状态

* 200 OK
* 206
  * 2201 tag 不存在
  * 2202 tag 名字冲突
  * 2203 tag 属性不支持
  * 2204 tag 类型不支持
  * 2205 tag 地址格式无效
* 404
  * 2003 node 不存在
  * 2106 group 不存在

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
  * 2003 node 不存在

### Body

```json
{
    //group name
    "group": "config_modbus_tcp_sample_2",
    //node name
    "node": "modbus-node",
    //tag names
    "tags": [
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
  
  * 2302 库信息无效

### Body

```json
{
    //plugin library name
    "library": "plugin_name.so"
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
    "plugin": "modbus-tcp"
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

**plugin**  optional

### 请求 Headers

**Authorization** Bearer \<token\>

### 响应状态

* 200 OK

### 响应

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

## 订阅

*POST*  /api/v2/subscribe

### 请求 Headers

**Content-Type**  application/json

**Authorization** Bearer \<token\>

### 响应状态

* 200 OK
* 404
  * 2106 group 不存在

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
  * 2106 group 不存在

### Body

```json
{
    //app name
    "app": "mqtt-node",
    //driver name
    "driver": "driver-node",
    //driver node group config name
    "group": "gconfig1"
}
```

### 响应

```json
{
    "error": 0
}
```

## 读 Tag

*POST*  /api/v2/read

### 请求 Headers

**Content--Type**  application/json

### 响应状态

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

### 请求 Headers

**Content-Type**  application/json

**Authorization** Bearer \<token\>

### 响应状态

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

### 响应

```json
{
    "error": 0
}
```

## 获取插件 Schema

*GET*  /api/v2/schema

### 请求 Params

**plugin_name**  必需

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
  * 2003 node 不存在
  * 2004 node 配置无效

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

### 响应

```json
{
    "error": 0
}
```

## 获取 Node 配置

*GET*  /api/v2/node/setting

### 请求 Params

**node**  必需

### 请求 Headers

**Authorization** Bearer \<token\>

### 响应状态

* 200 OK
  * 2005 node 配置未发现
* 404
  * 2003 node 不存在

### 响应

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
    "node": "modbus-node",
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

**node**  required

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

## 获取订阅的 Group

*GET*  /api/v2/subscribe

### 请求 Params

**app**  必需

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

## 上传License

*POST*  /api/v2/license

### 请求头部

**Authorization** Bearer \<token\>

### 响应状态

* 200
  * 0    OK
  * 2402 license过期
* 400
  * 2401 license无效
* 500
  * 1001 服务器内部错误

### 请求体

```json
{
    "license": "-----BEGIN CERTIFICATE-----\nMIID2TCCAsGgAwIBAgIEATSJqjA....."
}
```

### 响应

```json
{
    "error": 2401
}
```

## 获取License信息

*GET*  /api/v2/license

### 请求头部

**Authorization** Bearer \<token\>

### 响应状态

* 200 OK
* 404
  * 2400 license未找到
* 500
  * 1001 服务器内部错误

### 响应

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
