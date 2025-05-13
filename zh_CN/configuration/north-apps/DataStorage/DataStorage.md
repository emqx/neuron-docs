# DataStorage

Neuron DataStorage 插件是一款开源的北向插件，使用 [Arrow Flight SQL](https://arrow.apache.org/docs/format/FlightSql.html#arrow-flight-sql) 写入数据到 [Datalayers](https://docs.datalayers.cn/datalayers/latest/)，它为 neuron 增加了时序数据的存储能力。

Neuron 会在启动时创建一个 *DataStorage* 单例节点，用户不能直接使用该插件创建或删除节点。
您可以在仪表板的**北向应用**页签中看到 *DataStorage* 节点。

## 应用配置

以下是使用 DataStorage 插件配置节点时可用的参数：

| 字段                       | 说明                                                  |
| ------------------------------- | ------------------------------------------------------------ |
| **服务器地址**                | Datalayers 服务器的 ip 地址 |
| **服务器端口**                | Datalayers gRPC 服务的端口  |
| **用户名**                    | Datalayers 用户名          |
| **密码**                      | Datalayers 密码            |

:::tip
提交配置时，将验证与 Datalayers 的连接，如果连接失败，配置将被拒绝。
:::

## 添加订阅

完成插件的添加和配置后，我们将继续通过订阅南向设备实现数据的转发。

完成设备配置后，在**北向应用**页，点击设备卡片/设备列进入**组列表**页。点击**添加订阅**，完成南向设备和组的设置。订阅完成后，DataStorage 节点将开始接收南向数据。

## 数据上传

Neuron DataStorage 在传输过程中使用 Arrow 的列存格式，在数据传输过程将完全避免序列化/反序列化操作，可彻底消除序列化/反序列化带来时间及性能损耗、提升系统的吞吐能力。

## 运行与维护

在设备卡片或设备列，您可点击数据统计图表查看及应用运行情况、接受和发送的数据情况。
