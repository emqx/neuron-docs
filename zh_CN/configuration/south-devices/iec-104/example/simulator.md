# IEC 60870-5-104 Server 模拟器连接示例

本文将使用 Neuron 的 IEC608750-5-104 插件连接到模拟器 [IEC 60870-5-104 Server Simulator](https://www.freyrscada.com/iec-60870-5-104-Client-Simulator.php)，此模拟器支持多种数据类型的采集以及控制写入。

## 下载 IEC 60870-5-104 Server Simulator

此软件可在 [模拟器](https://sourceforge.net/projects/iec-104-client-simulator/) 处下载，试用版软件每 15 分钟将会自动关闭，及时保存相关配置数据。
下载后解压找到 IEC60870-5-104 Server Simulator 可执行文件后直接点击安装。

### 模拟器点位配置

* 打开 **IEC 60870-4-104 Server Simulator** 模拟器。
* 点击左上角 **Add Server** 创建一个 Server。
* 在选项卡 **IEC104-SERVER_1** 中修改默认 Server 的配置选项。**Source IP Address** 把默认值 127.0.0.1 修改为 0.0.0.0，便于 Neuron 进行连接。
* 切换到 **Configuration_1** 选项卡，点击 **Add Row** 添加一个点位，**IEC 60870-5 Group to Choose** 选择 **Measured Normalized**，**Event Report Type ID** 选择 **M_ME_NA_1=9**。
* 模拟器点位其他值保持默认值即可，**IOA** 默认为 1，**Common Address** 默认为 1。

![simulator-tag](./assets/tag.png)

* 配置完模拟器点位后，点击按钮 **Load Configuration** 进入 **Data_Objects_1** 选项卡，点击 **Start Communication** 即可成功运行模拟器。

### 配置 Neuron

- 进入 Neuron 管理页面，使用 **IEC60870-5-104 插件** 创建一个南向节点。

* 点击按钮 **设备配置** 进入节点配置页面，**设备 IP 地址** 填写安装模拟器的设备 IP 地址，其他参数使用默认值即可，点击 **提交** 即可完成设备参数配置。 
* 进入到节点组配置中，创建一个组后，在组下创建一个点位，点位数据类型选择 **INT16**，地址填写为 **1**，地址值为模拟器点位配置中的 **IOA** 参数。

## 数据监控

完成点位的配置后，您可点击 **监控** -> **数据监控**查看设备信息以及反控设备，具体可参考[数据监控](../../../../usage/monitoring.md)。

