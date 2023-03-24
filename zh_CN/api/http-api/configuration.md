# 配置

## 概念解析

### Node 节点

在 Neuron 中每个节点都可以与一台设备或一个北向应用建立连接。
* 在设备节点中，可以添加和管理设备点位。
* 在北向节点中，可以选择需要订阅的数据组。

### Group 组

每个节点底下都可以创建多个数据组，对点位进行分类。例如，一台设备连接多个温度传感器和多个湿度传感器，可以创建温度和湿度两个数据组对采集的点位进行分类。Neuron 按组为单位，将采集数据上传到北向应用。
### Tag 点位

在每个组底下可以创建多个采集点位，例如，一台温度传感器采集多个温度值，一个温度值作为一个点位。

### Plugin 插件

在 Neuron 中，每个插件对应一种协议的实现。例如，一种 modbus tcp 协议对应一个插件，mqtt 协议对应一个插件。

## Ping

*POST*  **/api/v2/ping**

### 请求头部

**Authorization** Bearer \<token\>

### 响应状态

* 200 OK

## 登录

*POST*   **/api/v2/login**

### 请求头部

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

### 请求体

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

## 更改密码

*POST*   **/api/v2/password**

### 请求头部

**Content-Type** application/json

**Authorization** Bearer \<token\>

### 响应状态

* 200 OK
* 401
  * 1004, 缺少令牌
  * 1005, 解码令牌错误
  * 1012, 密码长度太短或太长
  * 1013, 密码重复
* 403
  * 1006, 令牌过期
  * 1007, 验证令牌错误
  * 1008, 无效令牌

### 请求体

```json
{
    "name": "admin",
    "old_pass": "01234",
    "new_pass": "56789"
}
```

### 响应

```json
{
    "error": 0
}
```

## 添加 Node

*POST*  **/api/v2/node**

### 请求头部

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

### 请求体

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

### 请求头部

**Content-Type**  application/json

**Authorization** Bearer \<token\>

### 响应状态

* 200 OK
* 404
  * 2003 node not exist

### 请求体

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

### 请求头部

**Content-Type**  application/json

**Authorization** Bearer \<token\>

### 响应状态

* 200 OK
* 404
  * 2003 node exist

### 请求体

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

### 请求参数

**type**  必需

**plugin** 可选

**node** 可选

### 请求头部

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

## 配置 Node

*POST*  /api/v2/node/setting

### 请求头部

**Content-Type**  application/json

**Authorization** Bearer \<token\>

### 响应状态

* 200 OK
* 400
  * 2003 node 不存在
  * 2004 node 配置无效

### 请求体

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
每个插件的配置参数具体可参考 [插件设置](./plugin-setting.md)。
:::

### 响应

```json
{
    "error": 0
}
```

## 获取 Node 配置

*GET*  /api/v2/node/setting

### 请求参数

**node**  必需

### 请求头部

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

## 控制 Node

*POST*  /api/v2/node/ctl

### 请求头部

**Content-Type**  application/json

**Authorization** Bearer \<token\>

### 请求状态

* 200 OK
* 409
  * 2006 node not ready
  * 2007 node is running
  * 2008 node not running
  * 2009 node is stopped

### 请求体

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

### 请求参数

**node**  optional

### 请求头部

**Authorization** Bearer \<token\>

### 响应状态

* 200 OK

### 响应

```json
{
    //running state
    "running": 2,
    //link state
    "link": 1,
    //average round trip time communicating with devices
    "average_rtt": 100
}

{
    "states": [
        {
            "node": "modbus-node1",
            "running": 2,
            "link": 1,
            "average_rtt": 100
        },
        {
            "node": "modbus-node2",
            "running": 1,
            "link": 0,
            "average_rtt": 9999
        }
    ]
}
```

## 添加 Group

*POST*  /api/v2/group

### 请求头部

**Content-Type**  application/json

**Authorization** Bearer \<token\>

### 响应状态

* 200 OK
* 404
  * 2003 node not exist
* 409
  * 2103 group not allow

### 请求体

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

### 请求头部

**Content-Type**  application/json

**Authorization** Bearer \<token\>

### 响应状态

* 200 OK
* 412
  * 2101 group already subscribed
* 404
  * 2003 node not exist
  * 2101 group not exist

### 请求体

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

## 更新 Group

*PUT*  /api/v2/group

### 请求头部

**Content-Type**  application/json

**Authorization** Bearer \<token\>

### 响应状态

* 200 OK
* 404
  * 2106 group not exist

### 请求体

```json
{
    //node name
    "node": "node1",
    //group name
    "group": "group",
    //read/upload interval(ms)
    "interval": 20000
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

### 请求参数

**node**  可选

### 请求头部

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

```json
{
    "groups": [
        {
            //node name
            "driver": "modbus",
            //group name
            "group": "group1",
            "tag_count": 1,
            "interval": 1000
        },
        {
            "driver": "modbus",
            "group": "group2",
            "tag_count": 0,
            "interval": 100
        },
        {
            "driver": "modbus1",
            "group": "group",
            "tag_count": 0,
            "interval": 10001
        }
    ]
}
```

## 添加 Tag

*POST*  /api/v2/tags

### 请求头部

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

### 请求体

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
           //floag precision, optional(0-17)
            "precision": 3,
           //decimal, optional
            "decimal": 0.1
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

### 请求参数

**node**  必需

**group**  必需

**name** 可选

### 请求头部

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
            "attribute": 1,
            //float/double precision
             "precison": 1,
            //decimal
             "decimal": 0
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

### 请求头部

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

### 请求体

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
            //float/double precision
            "precison": 1,
            //decimal
            "decimal": 1
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

### 请求头部

**Content-Type**  application/json

**Authorization** Bearer \<token\>

### 响应状态

* 200 OK
* 404
  * 2003 node 不存在

### 请求体

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

### 请求头部

**Content-Type**  application/json

**Authorization** Bearer \<token\>

### 响应状态

* 200 OK

* 400
  
  * 2302 库信息无效

### 请求体

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

### 请求头部

**Content-Type**  application/json

**Authorization** Bearer \<token\>

### 响应状态

* 200 OK

### 请求体

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

### 请求参数

**plugin**  optional

### 请求头部

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
            "description": "description",
            "description_zh": "描述"
        }
    ]
}
```

## 获取插件 Schema

*GET*  /api/v2/schema

### 请求参数

**plugin_name**  必需

### 请求头部

**Authorization** Bearer \<token\>

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

## 订阅

*POST*  /api/v2/subscribe

### 请求头部

**Content-Type**  application/json

**Authorization** Bearer \<token\>

### 响应状态

* 200 OK
* 404
  * 2106 group 不存在

### 请求体

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

### 请求头部

**Content-Type**  application/json

**Authorization** Bearer \<token\>

### 响应状态

* 200 OK
* 404
  * 2106 group 不存在

### 请求体

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

## 获取订阅的 Group

*GET*  /api/v2/subscribe

### 请求参数

**app**  必需

### 请求头部

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

## 上传 License

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

## 获取 License 信息

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

## 下载日志文件

*GET*  /api/v2/logs

### 请求头部

**Authorization** Bearer \<token\>

### 响应状态

* 200 OK
* 404
  * 1011 文件不存在
  * 1014 执行指令失败
* 500
  * 1001 内部错误

### 响应

如果有错误返回时响应：

```json
{
    "error": 1014
}
```

## 修改节点日志等级

*PUT*  /api/v2/log/level

### 请求头部

**Authorization** Bearer \<token\>

### 响应状态

* 200 OK
* 404
  * 2003 node 不存在
* 500
  * 1001 内部错误
  * 1010 程序繁忙

### 请求体

```json
{
    // node name
    "node": "modbus-tcp"
}
```

### 响应

```json
{
    "error": 0
}
```

:::tip
调用接口修改节点的日志等级为 debug，十分钟左右自动切回默认等级。
:::

## 获取统计信息

*GET*  /api/v2/metrics

### 请求头部

**Authorization** Bearer \<token\>

### 请求参数

**category**  可选, 取值为`global`, `driver` and `app`之一
**node**      可选, 用节点名过滤, 且必须指定`category=driver`或`category=app`

### 响应状态

* 200 OK
* 400 请求错误
* 500 服务器内部错误

### 响应

```text
# HELP core_dumped Whether there is any core dump
# TYPE core_dumped gauge
core_dumped 0
# HELP uptime_seconds Uptime in seconds
# TYPE uptime_seconds counter
uptime_seconds 314
# HELP north_nodes_total Number of north nodes
# TYPE north_nodes_total gauge
north_nodes_total 1
# HELP north_running_nodes_total Number of north nodes in running state
# TYPE north_running_nodes_total gauge
north_running_nodes_total 1
# HELP north_disconnected_nodes_total Number of north nodes disconnected
# TYPE north_disconnected_nodes_total gauge
north_disconnected_nodes_total 1
# HELP south_nodes_total Number of south nodes
# TYPE south_nodes_total gauge
south_nodes_total 1
# HELP south_running_nodes_total Number of south nodes in running state
# TYPE south_running_nodes_total gauge
south_running_nodes_total 0
# HELP south_disconnected_nodes_total Number of south nodes disconnected
# TYPE south_disconnected_nodes_total gauge
south_disconnected_nodes_total 1
# HELP send_msgs_total Total number of messages sent
# TYPE send_msgs_total counter
send_msgs_total{node="data-stream-processing"} 0
# HELP send_msg_errors_total Total number of errors sending messages
# TYPE send_msg_errors_total counter
send_msg_errors_total{node="data-stream-processing"} 0
# HELP recv_msgs_total Total number of messages received
# TYPE recv_msgs_total counter
recv_msgs_total{node="data-stream-processing"} 0
# HELP last_rtt_ms Last request round trip time in milliseconds
# TYPE last_rtt_ms gauge
last_rtt_ms{node="modbus"} 9999
# HELP send_bytes Total number of bytes sent
# TYPE send_bytes gauge
send_bytes{node="modbus"} 0
# HELP recv_bytes Total number of bytes received
# TYPE recv_bytes gauge
recv_bytes{node="modbus"} 0
# HELP tag_reads_total Total number of tag reads including errors
# TYPE tag_reads_total counter
tag_reads_total{node="modbus"} 0
# HELP tag_read_errors_total Total number of tag read errors
# TYPE tag_read_errors_total counter
tag_read_errors_total{node="modbus"} 0
# HELP group_tags_total Total number of tags in the group
# TYPE group_tags_total gauge
group_tags_total{node="modbus",group="grp"} 1
# HELP group_last_send_msgs Number of messages sent on last group timer invocation
# TYPE group_last_send_msgs gauge
group_last_send_msgs{node="modbus",group="grp"} 0
# HELP group_last_timer_ms Time in milliseconds consumed on last group timer invocation
# TYPE group_last_timer_ms gauge
group_last_timer_ms{node="modbus",group="grp"} 0
```