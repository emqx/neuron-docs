# 设置先决条件

数据流引擎中预先定义了一个名为 `neuronStream` 的数据流，其属性为`neuron`。这个数据流收集 neuron 从各个设备采集过来的数据，所有规格都将共享此数据流。

## 第一步，查看数据流处理应用节点

商业版本中，北向应用管理界面中有一个默认的`data-stream-processing`节点卡片，如下图所示。

![data-stream-rules-adapter](./assets/data-stream-rules-adapter.png)

## 第二步，订阅南向标签组

点击 `data-stream-processing` 应用节点任意空白处，进入订阅 Group 的界面，如下图所示。

![data-stream-rules-sub](./assets/data-stream-rules-sub.png)

* 点击右上角`添加订阅`；
* 点击下拉框，选择南向设备，本例中选择已构建的**modbus-plus-tcp-1**；
* 点击下拉框，选择要订阅的 Group，本例中选择已构建的 **group-1**；
* 点击`提交`按键完成订阅。
