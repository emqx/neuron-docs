# 管理日志

## 下载日志

Neuron 在 2.3 版本中已支持在 web 页面一键下载所有日志文件的功能，如下图所示。

![download_log](./assets/download_log.png)

下载日志的功能将把 /neuron/build/logs 的文件夹打包成 neuron_logs.tar.gz 文件并下载到网页上。文件包含所有已创建的驱动及 neuron 的日志文件，文件目录级别示例，如下图所示。

![neuron_logs](./assets/neuron_logs.png)

* data-stream-processing.log：数据处理配置；
* dlt645.log：北向应用配置；
* modbus-plus-tcp.log：南向设备配置；
* neuron.log：Neuron日志

## 设置打印节点 debug 日志

Neuron 支持设置打印某个节点的 debug 日志，并在大致十分钟后自动切回默认的日志等级。每个节点之间的设置相互独立。

每个节点的 `更多` 操作按键中都有一个 `DEBUG 日志` 的操作按键，如下图所示。

![debug_log](./assets/debug_log.png)

点击此按键后，页面将跳出如下图所示的提示。

![debug_log_tip](./assets/debug_log_tip.png)

此时，该节点开始打印 debug 日志，用户可选择在十分钟后下载日志，查看对应节点的日志，也可以选择在 /build/logs 下实时查看节点打印的日志。

:::tip
打印节点 debug 日志的同时 neuron 日志也会打印，并在十分钟后自动切回默认的日志等级。
:::
