# 概览

Neuron MTConnect 插件通过 HTTP 协议访问安装有 MTConnect Agent 的设备。

## 设备设置

| 字段      | 说明                            |
| --------- | ------------------------------- |
| host      | 设备 IP 地址或者绑定地址        |
| port      | 设备端口或者绑定端口, 默认 5000 |
| ns_prefix | 命名空间前缀                    |
| ns_uri    | 命名空间标识                    |

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

## MTConnect Agent 
MTConnect Agent 的安装和使用，详细内容请访问此链接 [cppagent](https://github.com/mtconnect/cppagent)。

## ADDRESS
插件地址为 XML XPATH 形式.

## 地址示例

| 地址                                                                                                                               | 数据类型 | 说明                |
| ---------------------------------------------------------------------------------------------------------------------------------- | -------- | ------------------- |
| //m:Angle[@dataItemId='Babs']                                                                                                      | float    | 旋转轴 B 绝对值角度 |
| //m:DeviceStream[@uuid='Mazak']/m:ComponentStream[@componentId='LYI1']/m:Samples/m:Position[@dataItemId='LYI1actm']                | double   | 线性轴 Y 的机械坐标 |
| //m:DeviceStream[@uuid='Mazak']/m:ComponentStream[@componentId='Lct1']/m:Events/m:InputOutputSignal[@dataItemId='LPlcMonitorIO_1'] | bit      | IO 信号             |

