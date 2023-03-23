# 下载安装 Modbus 模拟器

## PeakHMI Slave Simulators
安装 PeakHMI Slave Simulators 软件，安装包可在 [PeakHMI 官网](https://hmisys.com) 中下载。在官网中进入 **Download -> PeakHMI Slave Simulators** 页面，点击 **Slave Simulator Installer** 进行下载。

* 安装后，运行 Modbus TCP slave EX。
* 进入 **Windows -> Register data**，首先选择站点号，例如，1。点击 **OK** 后选择寄存器，例如，40001。则对应地址为1!40001，可以在其中输入点位数值。


## Modbus Poll
Modbus Poll是一款Modbus主机模拟器，主要用于帮助Modbus从设备开发者或其他想要测试和模拟Modbus协议的开发者使用。

Modbus Poll支持以下方式读写设备数据：
* 在RS232或者RS485串口网络上使用Modbus RTU, ASCII通讯。（USB/RS232/485转换器）
* Modbus TCP/IP
* Modbus Over TCP/IP。（Modbus RTU/ASCII封装于TCP报文）
* Modbus UDP/IP
* Modbus Over UDP/IP。（Modbus RTU/ASCII封装于UDP报文）
  
安装 Modbus Poll 软件，安装包可从[modbus tool download](https://www.modbustools.com/download.html)页面，根据运行环境选择对应的安装包下载。

* 安装完成后，运行Modbus Poll。
* 按下F3或者进入菜单 **Connection -> Connect**，根据实际情况选择连接方式，设置连接参数，然后点击 **OK** 完成配置。
* 按下F8，进入菜单 **Setup -> Read/Write Definition**，或者点击工具栏![Read/Write Definition](assets/mbpoll-definition-button.png)配置读写。根据读写需求设置地址参数信息，点击 **OK**完成配置。
* 主界面独立文档窗口就可以看到读写配置数据信息。如果想要配置多个读写定义，点击 **File -> New**新建文档窗口，重复上一步读写配置即可。在独立文档窗口双击表头为地址的表格项目，输入站点号，地址，和值，即可对从机对应数据进行修改。
* 如果需要同时连接多个从设备，运行Modbus Poll多个实例，重复上述步骤即可。

## Modbus Slave
Modbus Slave是一款Modbus从机模拟器，主要用于Modbus主设备开发者加快PLC程序开发与测试，在获得物理设备之前。

Modbus Slave支持以下方式读写设备数据：
* 在RS232或者RS485串口网络上使用Modbus RTU, ASCII通讯。（USB/RS232/485转换器）
* Modbus TCP/IP
* Modbus Over TCP/IP。（Modbus RTU/ASCII封装于TCP报文）
* Modbus UDP/IP
* Modbus Over UDP/IP。（Modbus RTU/ASCII封装于UDP报文）

安装 Mobus Slave 软件，安装包可从[modbus tool download](https://www.modbustools.com/download.html)页面，根据运行环境选择对应的安装包下载。

* 安装完成后，运行Modbus Slave。
* 按下F3或者进入菜单 **Connection -> Connect**，根据实际情况选择连接方式，设置连接参数，然后点击 **OK** 完成配置。
* 按下F8，进入菜单 **Setup -> Slave Definition**，或者点击工具栏![Slave Definition](assets/mbpoll-definition-button.png)配置从机地址信息。根据地址需求设置地址参数信息，点击 **OK**完成配置。
* 主界面中独立文档窗口就可以看到地址配置数据信息。如果想要配置多个从机地址定义，点击 **File -> New**新建文档窗口，重复上一步读写配置即可。在独立文档窗口双击表头为地址的表格项目可以对数据进行修改。
* 如果需要同时模拟多个从设备，运行Modbus Slave多个实例，重复上述步骤即可。



:::tip
须保证安装 Neuron 的设备与安装模拟器的设备之间的网络能通。

因模拟器默认使用 502（低于 1024 的为特权端口）端口，Windows 防火墙会阻止 502 端口数据，可选择关闭 Windows 防火墙，或在模拟器设置中修改模拟器端口为大于 1024 的端口，并重启模拟器。
:::