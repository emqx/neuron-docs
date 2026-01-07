# GE Historian

Neuron 可以使用 Neuron HUB 驱动和 NeuronHUB Windows 程序，间接访问运行于 Windows 操作系统的 GE Historian 服务器。GE Historian 是一款工业历史数据库，用于存储和检索工业过程数据。


## NEURON HUB Windows 程序参数

| 参数            | 说明                                              |
| --------------- | ------------------------------------------------- |
| Node Name       | 节点名称，必须唯一，用来区分多个节点              |
| Server          | 需要连接目标主机标识，可以是目标 IP 或者 Hostname |
| UserName        | 用户名                                            |
| PassWrod        | 密码                                              |
| update interval | 缓存更新周期，默认 1000 毫秒                      |


## 支持的数据类型

* uint8
* int8
* uint16
* int16
* uint32
* int32
* uint64
* int64
* float
* double
* bool
* string


## 地址格式
Neuron HUB 驱动选择 GE Historian 节点类型时，地址为 GE Historian 服务器中的标签名称（Tag Name）。可以通过`导出`功能导出全部点位信息表格，然后直接导入 NEURON。


## NOTE
使用 NeuronHUB Windows 程序采集数据之前，需要使用 GE Historian 安装包安装 Historian OLE DB Provider Components 。
