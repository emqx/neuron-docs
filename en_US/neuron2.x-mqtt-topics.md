# Neuron 2.0 MQTT topics

All topics for interaction between client and neuron with login, logout, ping, config, read, write command.

The xxx in all topics refers to the Client-id, which is set in the northbound application configuration in the Neuron UI.

## Basic Status Topic

### Request/Response

A request/response topic, it will return basic status information of neuron.

*topic:*  **neuron/xxx/status**

#### Body

```json
{
    "command": "",
    "uuid": "E21AEE51-1269-B228-E9E5-CD252CE10877"
}
```

---

## Ping Topic

### Request/Response

A request/response topic, ping command for get current Neuron status.

*topic:*  **neuron/xxx/ping**

#### Body

```json
{
    "command": "",
    "uuid": "E21AEE51-1269-B228-E9E5-CD252CE10877"
}
```

---

## Manipulate Node

### Request

A request topic, manipulate node interface for add/del/update/get node.

*topic:*  **neuron/xxx/node/req**
*req command:*  **add/del/update/get**

#### Add Body

```json
{
    "command": "add",
    "uuid": "E21AEE51-1269-B228-E9E5-CD252CE10877",
    "type": 1,
    "name": "modbus-tcp-node",
    "plugin_name": "modbus-tcp-plugin"
}
```

### Response

A response topic, return result of manipulating node.

*topic:*  **neuron/xxx/node/resp**

*resp command:*  **add/del/update/get**

#### Add Body

```json
{
  "uuid": "E21AEE51-1269-B228-E9E5-CD252CE10877",
  "command": "add",
  "error": 0
}
```

*Node:* Other commands are similar to api, add "command" and "uuid" fields.

---

## Manipulate Group Config

### Request

A request topic, manipulate group config interface for add/del/update/get group config.

*topic:*  **neuron/xxx/gconfig/req**

*req command:*  **add/del/update/get**

#### Get Body

```json
{
    "command": "get",
    "uuid": "E21AEE51-1269-B228-E9E5-CD252CE10877",
    "node_id": 3
}
```

A response topic, return result of manipulating group config.

*topic:*  **neuron/xxx/gconfig/resp**

#### Get Body

```json
{
  "uuid": "E21AEE51-1269-B228-E9E5-CD252CE10877",
  "command": "get",
  "group_configs": [
    {
      "tag_count": 3,
      "pipe_count": 1,
      "name": "group-1",
      "interval": 1500
    },
    {
      "tag_count": 2,
      "pipe_count": 1,
      "name": "group-2",
      "interval": 1500
    }
  ]
}
```

*Node:* Other commands are similar to api, add "command" and "uuid" fields.

---

## Manipulate Data Tags

### Request

A request topic, manipulate data tag interface for add/del/update/get data tag.

*topic:*  **neuron/xxx/tags/req**

*req command*  **add/del/update/get**

#### Get Body

```json
{
    "command": "get",
    "uuid": "E21AEE51-1269-B228-E9E5-CD252CE10877",
    "node_id": 5,
    "group_config_name": "group-1"
}
```

### Response

A response topic, return result of manipulating data tag.

*topic:*  **neuron/xxx/tags/resp**

#### Get Body

```json
{
  "uuid": "E21AEE51-1269-B228-E9E5-CD252CE10877",
  "command": "get",
  "tags": [
    {
      "type": 4,
      "name": "data1",
      "id": 1,
      "group_config_name": "group-1",
      "attribute": 1,
      "address": "1!400001"
    },
    {
      "type": 4,
      "name": "data2",
      "id": 2,
      "group_config_name": "group-1",
      "attribute": 1,
      "address": "1!400002"
    }
  ]
}
```

*Node:* Other commands are similar to api, add "command" and "uuid" fields.

---

## Manipulate Plugin Libs

### Request

A request topic, manipulate plugin lib interface for add/del/update/get plugin lib.

*topic:*  **neuron/xxx/plugin/req**

*req command:*  **add/del/update/get**

#### Get Body

```json
{
    "command": "get",
    "uuid": "E21AEE51-1269-B228-E9E5-CD252CE10877",
    "id": 4
}
```

### Response

A response topic, return result of manipulating plugin lib.

*topic:*  **neuron/xxx/plugin/resp**

#### Body

```json
{
  "uuid": "E21AEE51-1269-B228-E9E5-CD252CE10877",
  "command": "get",
  "plugin_libs": [
    {
      "node_type": 1,
      "name": "modbus-tcp-plugin",
      "lib_name": "libplugin-modbus-tcp.so",
      "kind": 1,
      "id": 4
    }
  ]
}
```

---

## Subscribe Group Config

### Request

A request topic, subscribe or unsubscribe a group config, or get group configs that subcribed by a node.

*topic:*  **neuron/xxx/subscribe/req**

*req command:*  **add/del/get**

#### Body

```json
{
    "command": "get",
    "uuid": "E21AEE51-1269-B228-E9E5-CD252CE10877",
    "node_id": 3
}
```

### Response

A response topic, return result of subscribing or unsubscribing a group config.

*topic:*  **neuron/xxx/subscribe/resp**

#### Body

```json
{
  "uuid": "E21AEE51-1269-B228-E9E5-CD252CE10877",
  "command": "get",
  "groups": [
    {
      "node_id": 5,
      "group_config_name": "group-1"
    },
    {
      "node_id": 4,
      "group_config_name": "group-1-1"
    },
    {
      "node_id": 5,
      "group_config_name": "group-2"
    }
  ]
}
```

---

## Read Tags with Group Config

### Request

A request topic, read tags in group config.

*topic:*  **neuron/xxx/read/req**

#### Body

```json
{
    "command": "",
    "uuid": "E21AEE51-1269-B228-E9E5-CD252CE10877",
    "node_id": 5,
    "group_config_name": "group-2"
}
```

A response topic, return result of reading tags in group config.

*topic:*  **neuron/xxx/read/resp**

#### Body

```json
{
  "uuid": "E21AEE51-1269-B228-E9E5-CD252CE10877",
  "command": "",
  "tags": [
    {
      "value": 4,
      "id": 3,
      "error": 0
    },
    {
      "value": 5,
      "id": 4,
      "error": 0
    }
  ]
}
```

---

## Cycle Reading

### Response

A response topic, manipulate tag cycle to read tags of subscribed groups.

topic: **neuron/xxx/read/resp**

#### Body

```json
{
  "node_id": 5,
  "node_name": "modbus-tcp-2",
  "group_config_name": "group-1",
  "timestamp": 1647497389075,
  "tags": [
    {
      "value": 123,
      "id": 1,
      "error": 0
    },
    {
      "value": 0,
      "id": 2,
      "error": 0
    }
  ]
}
```

*Node* A group sends a message.

---

## Write Tags with Group Config

### Request

A request topic, write tags in group config.

*topic:*  **neuron/xxx/write/req**

#### Body

```json
{
    "command": "",
    "uuid": "E21AEE51-1269-B228-E9E5-CD252CE10877",
    "node_id": 5,
    "group_config_name": "group-2",
    "tags": [
      {
        "value": 6,
        "id": 3
      },
      {
        "value": 6,
        "id": 4
      }
    ]
}
```

### Response

A response topic, return result of writing tags in group config.

*topic:*  **neuron/xxx/write/resp**

#### Body

```json
{
  "uuid": "E21AEE51-1269-B228-E9E5-CD252CE10877",
  "command": "",
  "tags": [
    {
      "value": 6,
      "id": 3,
      "error": 0
    },
    {
      "value": 6,
      "id": 4,
      "error": 0
    }
  ]
}
```

---

## Manipulate TTY

### Request

A request topic, manipulate tty interface for get tty device.

*topic:*  **neuron/xxx/ttys/req**

*req command:*  **get**

#### Body

```json
```

### Response

A response topic, return result of manipulating tty.

*topic*  **neuron/xxx/ttys/resp**

#### Body

```json
```

---

## Manipulate Plugin Schema

### Request

A request topic, manipulate plugin schema interface for get plugin schema.

*topic:*  **neuron/xxx/schema/plugin/req**

*req command:*  **get**

#### Body

```json
```

### Response

A response topic, return result of manipulating plugin schema.

*topic:*  **neuron/xxx/schema/plugin/resp**

#### Body

```json
```

---

## Manipulate Node Setting

### Request

A request topic, manipulate node setting for set/get node setting.

*topic:*  **neuron/xxx/node/setting/req**

*req command:*  **set/get**

#### Get Body

```json
{
    "command": "get",
    "uuid": "E21AEE51-1269-B228-E9E5-CD252CE10877",
    "node_id": 5
}
```

### Response

A response topic, return result of manipulating node setting.

*topic:*  **neuron/xxx/node/setting/resp**

#### Body

```json
{
  "node_id": 5,
  "uuid": "E21AEE51-1269-B228-E9E5-CD252CE10877",
  "command": "get",
  "params": {
    "host": "192.168.10.143",
    "port": 502
  },
  "error": 0
}
```

---

## Control the Node

### Request

A request topic, control a node interface for start/stop a node. The control command is represent in json message.

*topic:*  **neuron/xxx/node/ctl/req**

*req command:*  **0(start)/1(stop)**

#### Body

```json
{
    "command": "",
    "uuid": "E21AEE51-1269-B228-E9E5-CD252CE10877",
    "id": 5,
    "cmd": 1
}
```

### Response

A response topic, return result of control a node.

*topic:*  **neuron/xxx/node/ctl/resp**

#### Body

```json
{
  "uuid": "E21AEE51-1269-B228-E9E5-CD252CE10877",
  "command": "",
  "error": 0
}
```

---

## Manipulate Node State

### Request

A request topic, manipulate node state for get node state.

*topic:*  **neuron/xxx/node/state/req**

*req command:*  **get**

#### Body

```json
{
    "command": "get",
    "uuid": "E21AEE51-1269-B228-E9E5-CD252CE10877",
    "node_id": 5
}
```

A response topic, return result of manipulating node setting.

*topic:*  **neuron/xxx/node/state/resp**

#### Body

```json
{
  "uuid": "E21AEE51-1269-B228-E9E5-CD252CE10877",
  "command": "get",
  "running": 4,
  "link": 2
}
```

---
