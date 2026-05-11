# OPCAE

Neuron 可以使用 Neuron HUB 驱动和 NeuronHUB Windows 程序，间接访问运行于 Windows 操作系统的 OPC AE（Alarms and Events）服务器，支持 Simple，Conditional 和 Tracking。OPC AE 主要用于获取设备的报警和事件信息。


## NEURON HUB Windows 程序参数

| 参数      | 说明                                                                                                                 |
| --------- | -------------------------------------------------------------------------------------------------------------------- |
| Node Name | 节点名称，必须唯一，用来区分多个节点                                                                                 |
| Host      | 需要连接目标主机标识，可以是目标 IP 或者 Hostname                                                                    |
| UserName  | 用户名                                                                                                               |
| PassWrod  | 密码                                                                                                                 |
| Domain    | 域                                                                                                                   |
| Server    | AE 服务器的名称，如 `opcae://192.168.10.133/Matrikon.OPC.Alarms`，填写 Host 之后可以点击下拉按钮尝试获取 Server 列表 |


## 支持的数据类型

* string

数据示例：
```json
{
  "source": "GEAK Source",
  "condition": "",
  "subCondition": "",
  "message": "GEAK",
  "time": "2026-01-06T13:40:25.6375708+08:00",
  "severity": 2,
  "eventType": 1,
  "categoryId": 3,
  "ackRequired": false,
  "activeTime": "0001-01-01T00:00:00",
  "newState": 0,
  "actorId": "",
  "clientHandle": "ae",
  "changeMask": 0,
  "quality": 0,
  "cookie": 0,
  "attributes": [
    100,
    200,
    300
  ]
}
```


## 地址格式
Neuron HUB 驱动选择 OPCAE 节点类型时，地址为 OPC AE 服务器中的事件源路径。可以通过`导出`功能导出全部点位信息表格，然后直接导入 NEURON。


## 报警确认
支持对 Conditional 报警的确认以及 comment 的写入。
