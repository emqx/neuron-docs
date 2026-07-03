# MTConnect

Neuron MTConnect 插件通过 HTTP 协议访问安装有 MTConnect Agent 的设备。

## 设备设置

| 字段      | 说明                |
| --------- | ------------------- |
| host      | 设备 IP 地址        |
| port      | 设备端口, 默认 5000 |
| ns_prefix | 命名空间前缀        |
| ns_uri    | 命名空间标识        |

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

### node-name: 前缀

对于自闭合标签（元素值由标签名表示，如 CONDITION 类型数据项），可在地址前添加 `node-name:` 前缀。使用此前缀且匹配到的元素无子内容时，插件将提取元素的标签名而非文本内容。

| 地址前缀 | 行为 |
| ---------- | -------------------------------------- |
| `node-name:` | 从自闭合标签中提取元素标签名。 |
| （无前缀） | 提取元素文本内容（默认）。 |

## 地址示例

| 地址                                                                                                                               | 数据类型 | 说明                |
| ---------------------------------------------------------------------------------------------------------------------------------- | -------- | ------------------- |
| //m:Angle[@dataItemId='Babs']                                                                                                      | float    | 旋转轴 B 绝对值角度 |
| //m:DeviceStream[@uuid='Mazak']/m:ComponentStream[@componentId='LYI1']/m:Samples/m:Position[@dataItemId='LYI1actm']                | double   | 线性轴 Y 的机械坐标 |
| //m:DeviceStream[@uuid='Mazak']/m:ComponentStream[@componentId='Lct1']/m:Events/m:InputOutputSignal[@dataItemId='LPlcMonitorIO_1'] | bit      | IO 信号             |
| node-name://m:*[@dataItemId='DMGlogic1']                                                                                            | string   | 自闭合标签的元素名（如 Normal, Warning, Fault） |

