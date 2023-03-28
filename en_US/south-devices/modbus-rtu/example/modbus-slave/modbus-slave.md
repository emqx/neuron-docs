# 下载安装 Modbus Slave 模拟器
Modbus Slave 是一款 Modbus 从机模拟器，主要用于 Modbus 主设备开发者在获得物理设备之前，加快 PLC 程序开发与测试。

Modbus Slave 支持以下方式读写设备数据：
* 在 RS232 或者 RS485 串口网络上使用 Modbus RTU, ASCII 通讯。（USB/RS232/485 转换器）
* Modbus TCP/IP
* Modbus Over TCP/IP。（Modbus RTU/ASCII 封装于 TCP 报文）
* Modbus UDP/IP
* Modbus Over UDP/IP。（Modbus RTU/ASCII 封装于 UDP 报文）

安装 Modbus Slave 软件，安装包可从 [modbus tool download](https://www.modbustools.com/download.html) 页面，根据运行环境选择对应的安装包下载。软件提供30天的免费使用时长。免费时长阶段，连接10分钟会断开一次，断开之后需要重启软件。

* 安装完成后，运行 Modbus Slave。
* 按下 F3 或者进入菜单 **Connection -> Connect**，根据实际情况选择连接方式，设置连接参数，然后点击 **OK** 完成配置。
* 按下 F8 ，进入菜单 **Setup -> Slave Definition**，或者点击工具栏 ![Slave Definition](assets/mbpoll-definition-button.png) 配置从机地址信息。根据地址需求设置地址参数信息，点击 **OK** 完成配置。
* 主界面中独立文档窗口就可以看到地址配置相关的数据信息显示。如果想要配置多个从机地址定义，点击 **File -> New** 新建文档窗口，重复上一步从机地址配置即可。在独立文档窗口双击表头为地址的表格项目可以对数据进行修改。
* 如果需要同时模拟多个从设备，运行 Modbus Slave 多个实例，重复上述步骤即可。