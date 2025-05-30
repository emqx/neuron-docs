# OPCDA

Neuron 可以使用 Neuron HUB 驱动和 NEURON HUB Windows 程序，间接访问运行于 Windows 操作系统的 OPC DA 服务器。远程连接的系统配置参考 [NeuOPC 远程访问](../opc-da/remote.md)。


## NEURON HUB Windows 程序参数

| 参数      | 说明                                                                                                                     |
| --------- | ------------------------------------------------------------------------------------------------------------------------ |
| Node Name | 节点名称，必须唯一，用来区分多个节点                                                                                     |
| Host      | 需要连接目标主机标识，可以是目标 IP 或者 Hostname                                                                        |
| UserName  | 用户名                                                                                                                   |
| PassWrod  | 密码                                                                                                                     |
| Domain    | 域                                                                                                                       |
| Server    | DA 服务器的名称，如 `opcda://192.168.10.133/Matrikon.OPC.Simulation`，填写 Host 之后可以点击下拉按钮尝试获取 Server 列表 |


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
* ARRAY_INT8   
* ARRAY_UINT8  
* ARRAY_INT16  
* ARRAY_UINT16  
* ARRAY_INT32   
* ARRAY_UINT32 
* ARRAY_INT64   
* ARRAY_UINT64 
* ARRAY_FLOAT     
* ARRAY_DOUBLE  
* ARRAY_BOOL     
* ARRAY_STRING 


## 地址格式
Neuron HUB 驱动选择 OPCDA 节点类型时，地址格式与 OPCDA 一致，也可以通过`导出`功能导出全部点位信息表格，然后直接导入 NEURON。



