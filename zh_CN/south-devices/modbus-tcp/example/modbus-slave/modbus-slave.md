# Modbus Slave 连接示例

## 下载安装 Modbus Slave 模拟器
Modbus Slave 是一款 Modbus 从机模拟器，主要用于 Modbus 主设备开发者在获得物理设备之前，加快 PLC 程序开发与测试。

Modbus Slave 支持以下方式读写设备数据：
* 在 RS232 或者 RS485 串口网络上使用 Modbus RTU, ASCII 通讯。（USB/RS232/485 转换器）
* Modbus TCP/IP
* Modbus Over TCP/IP。（Modbus RTU/ASCII 封装于 TCP 报文）
* Modbus UDP/IP
* Modbus Over UDP/IP。（Modbus RTU/ASCII 封装于 UDP 报文）

安装 Modbus Slave 软件，安装包可从 [modbus tool 下载](https://www.modbustools.com/download.html) 页面，根据运行环境选择对应的安装包下载。软件提供30天的免费使用时长。免费时长阶段，连接10分钟会断开一次，断开之后需要重启软件。

## 如何连接作为 Client 的 Neuron？

本节主要介绍 Neuron 作为 Client，Modbus Slave 作为 Server 时，Neuron 与 Modbus Slave 的相关配置。

Neuron 作为 Client，主动向 Modbus Slave 发起连接请求，用户需要保证 Neuron -> Modbus Slave 的网络连通性。

### 配置 Modbus Slave

* 安装完成后，运行 Modbus Slave。
* 按下 F3 或者进入菜单 **Connection -> Connect**，根据实际情况选择连接方式（本示例为Modbus TCP/IP），设置连接参数（监听 Port），然后点击 **OK** 完成配置，如下图所示。
![modbus-slave-connection-setup](../assets/modbus-slave-connection-setup.png)
* 按下 F8 ，进入菜单 **Setup -> Slave Definition**，或者点击工具栏 ![Slave Definition](../assets/mbpoll-definition-button.png) 配置从机地址信息。根据地址需求设置地址参数信息，点击 **OK** 完成配置。
* 主界面中独立文档窗口就可以看到地址配置相关的数据信息显示。如果想要配置多个从机地址定义，点击 **File -> New** 新建文档窗口，重复上一步从机地址配置即可。在独立文档窗口双击表头为地址的表格项目可以对数据进行修改。
* 如果需要同时模拟多个从设备，运行 Modbus Slave 多个实例，重复上述步骤即可。


### 配置 Neuron 南向驱动 Client

在南向驱动管理中建立插件为 modbus-tcp-client 的节点，并进行驱动配置，如下图所示。
![neuron-client-config](../assets/neuron-client-config.png)

* 连接模式选择 client；
* Host 填写 Modbus Slave 的 IP 地址；
* Port 填写 Modbus Slave 配置的端口；