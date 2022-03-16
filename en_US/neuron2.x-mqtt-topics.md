# Neuron 2.0 MQTT topics

All topics for interaction between client and neuron with login, logout, ping, config, read, write command.

## Basic Status Topic

A response topic, it will return basic status information of neuron. 

*topic*  **neuron/xxx/status**

## Ping Topic

A request topic, ping command for get current Neuron status.

*topic*  **neuron/xxx/ping**

## Manipulate Node

A request topic, manipulate node interface for add/del/update/get node.

*topic*  **neuron/xxx/node/req**

*req command*  **add/del/update/get**

A response topic, return result of manipulating node.

*topic*  **neuron/xxx/node/resp**

## Manipulate Group Config

A request topic, manipulate group config interface for add/del/update/get group config.

*topic*  **neuron/xxx/gconfig/req**

*req command*  **add/del/update/get**

A response topic, return result of manipulating group config.

*topic*  **neuron/xxx/gconfig/resp**

## Manipulate Data Tags

A request topic, manipulate data tag interface for add/del/update/get data tag.

*topic*  **neuron/xxx/tags/req**

*req command*  **add/del/update/get**

A response topic, return result of manipulating data tag.

*topic*  **neuron/xxx/tags/resp**

## Manipulate Plugin Libs

A request topic, manipulate plugin lib interface for add/del/update/get plugin lib.

*topic*  **neuron/xxx/plugin/req**

*req command*  **add/del/update/get**

A response topic, return result of manipulating plugin lib.

*topic*  **neuron/xxx/plugin/resp**

## Subscribe Group Config

A request topic, subscribe or unsubscribe a group config, or get group configs that subcribed by a node.

*topic*  **neuron/xxx/subscribe/req**

*req command*  **add/del/get**

A response topic, return result of subscribing or unsubscribing a group config.

*topic*  **neuron/xxx/subscribe/resp**

## Read Tags with Group Config

A request topic, read tags in group config.

*topic*  **neuron/xxx/read/req**

A response topic, return result of reading tags in group config.

*topic*  **neuron/xxx/read/resp**

## Write Tags with Group Config

A request topic, write tags in group config.

*topic*  **neuron/xxx/write/req**

A response topic, return result of writing tags in group config.

*topic*  **neuron/xxx/write/resp**

## Manipulate TTY

A request topic, manipulate tty interface for get tty device.

*topic*  **neuron/xxx/ttys/req**

*req command*  **get**

A response topic, return result of manipulating tty.

*topic*  **neuron/xxx/ttys/resp**

## Manipulate Plugin Schema

A request topic, manipulate plugin schema interface for get plugin schema.

*topic*  **neuron/xxx/schema/plugin/req**

*req command*  **get**

A response topic, return result of manipulating plugin schema.

*topic*  **neuron/xxx/schema/plugin/resp**

## Manipulate Node Setting

A request topic, manipulate node setting for set/get node setting.

*topic*  **neuron/xxx/node/setting/req**

*req command*  **set/get**

A response topic, return result of manipulating node setting.

*topic*  **neuron/xxx/node/setting/resp**

## Control the Node

A request topic, control a node interface for start/stop a node. The control command is represent in json message.

*topic*  **neuron/xxx/node/ctl/req**

*req command*  **start/stop**

A response topic, return result of control a node.

*topic*  **neuron/xxx/node/ctl/resp**

## Manipulate Node State

A request topic, manipulate node state for get node state.

*topic*  **neuron/xxx/node/state/req**

*req command*  **get**

A response topic, return result of manipulating node setting.

*topic*  **neuron/xxx/node/state/resp**
