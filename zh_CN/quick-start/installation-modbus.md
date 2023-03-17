# 下载安装 Modbus 模拟器

安装 PeakHMI Slave Simulators 软件，安装包可在 [PeakHMI 官网](https://hmisys.com) 中下载。在官网中进入 **Download -> PeakHMI Slave Simulators** 页面，点击 **Slave Simulator Installer** 进行下载。

* 安装后，运行 Modbus TCP slave EX。
* 进入 **Windows -> Register data**，首先选择站点号，例如，1。点击 **OK** 后选择寄存器，例如，40001。则对应地址为1!40001，可以在其中输入点位数值。

:::tip
须保证安装 Neuron 的设备与安装模拟器的设备之间的网络能通。

因模拟器默认使用 502（低于 1024 的为特权端口）端口，Windows 防火墙会阻止 502 端口数据，可选择关闭 Windows 防火墙，或在模拟器设置中修改模拟器端口为大于 1024 的端口，并重启模拟器。
:::