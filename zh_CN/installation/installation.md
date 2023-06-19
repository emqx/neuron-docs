# 安装

Neuron 在基于 Linux 的操作系统上支持 32位/64位 ARM 和 64位 X86 架构，并提供以下安装包格式：

* Debian 软件包（.deb）格式，用于基于 Debian、Ubuntu Linux 的操作系统；

* Radhat 包管理器（.rpm）格式，适用于基于 Red Hat、CentOS Linux 的操作系统。

## Linux 发行版的安装包

| Linux 发行版                                    | 所需包        |
| ------------------------------------------------------------ | ------------------ |
| Ubuntu 20.04 </br>Ubuntu 18.04 </br>Ubuntu16.04</br>Debian 11</br>Debian 10</br>Debian 9</br>Debian 8               | **Debian Software Package** (.deb)         |
| CentOS Stream 9</br>CentOS Stream 8</br>CentOS 7    | **Redhat Package Manager** (.rpm)         |
| Other Linux | **Tape Archiver** (tar.gz) |

:::tip
建议安装 rpm/deb 包来设置系统服务管理器（systemd）以监视 Neuron 运行实例。
:::

## 硬件要求

Neuron 完全使用 C 语言开发，支持运行在 X86，ARM，MIPS，RISC-V 等硬件架构的设备上以及支持容器化的部署，如 K8s、KubeEdge 等。在有限硬件资源的设备上也能达到 100 毫秒，甚至 10 毫秒级别的数据采集，在硬件资源充足的服务器上，Neuron 也能充分利用多核 CPU，能够同时对几十万的点位进行 100 毫秒频率的数据采集以及点位写入控制。

下表列出了 Neuron 在不同点位数量下的最低硬件要求。

| 点位数                 | 建议最小内存   | 硬件架构                              | 备注          |
| :-------------------- | :----------- | :---------------------------------- | :----------------------------------- |
| 100 tags               | 128M memory | 32-bit/64-bit ARM 和 64-bit x86 架构 | Raspberry Pi 3 |
| 1,000 tags             | 256M memory | 32-bit/64-bit ARM 和 64-bit x86 架构  | Raspberry Pi 4 |
| 10,000 tags            | 512M memory | 64-bit ARM 和 64-bit x86 架构         | Industrial PC 等 |
| More than 10,000 tags  | 1G memory   | 64-bit x86 架构                       | Powerful Industrial PC, Server 等 |

:::tip
Neuron 没有点位数量上限。取决于分配的 CPU 和内存资源。Neuron 非常容易移植，可以运行在类似单板机等有限的资源的硬件上，也可以运行在功能强大的服务器上。以下提供一些 Neuron 的性能测试结果供用户参考，这些测试数据仍然不是上限。更强大的服务器支持配置更多的数据点位。

Platform                         : Intel(R) Xeon(R) Gold 6266C@3.00GHz</br>
Memory                           : 4G</br>
Architecture                     : x86</br>
OS Support                       : Ubuntu 20.04</br>
No. of connections               : 1000 connections</br>
No. of tags for each connection  : 300 tags</br>
Total tags                       : 300,000 tags</br>
Memory Usage                     : 300M</br>
CPU Usage                        : 90%</br>

:::

## 下载

Neuron 软件包可由 Neuron 官网 [https://neugates.io/downloads](https://neugates.io/downloads)下载。也可以到 [Github](https://github.com/emqx/neuron/releases) 仓库下载。

## Debian 软件包

| 下载文件                     | 架构   |
| ---------------------------- | ------ |
| neuron-x.y.z-linux-amd64.deb | X86_64 |
| neuron-x.y.z-linux-armhf.deb | ARM_32 |
| neuron-x.y.z-linux-arm64.deb | ARM_64 |


## Redhat 软件包管理工具

| 下载文件                     | 架构   |
| ---------------------------- | ------ |
| neuron-x.y.z-linux-amd64.rpm | X86_64 |
| neuron-x.y.z-linux-armhf.rpm | ARM_32 |
| neuron-x.y.z-linux-arm64.rpm | ARM_64 |


## Tape Archive（tar）

| 下载文件                        | 架构   |
| ------------------------------- | ------ |
| neuron-x.y.z-linux-amd64.tar.gz | X86_64 |
| neuron-x.y.z-linux-armhf.tar.gz | ARM_32 |
| neuron-x.y.z-linux-arm64.tar.gz | ARM_64 |


## Docker 镜像

| 下载文件            | 架构   |
| ------------------- | ------ |
| neuron-x.y.z-alpine | Docker |


## 源码构建

| 下载文件                      | 备注          |
| ----------------------------- | ------------- |
| http://github.com/emqx/neuron | Github Source |

版本号 x.y.z 说明：

* x 为主要版本号：一般情况下，该版本会引入一些重大功能，如引入架构性的更改，主版本升级不保证与老版本之间的兼容性；
* y 是次要版本号：一般情况下，该类型版本会引入一些新功能，但是会保证在该主要版本号下的兼容性；
* z 是维护版本号：一般情况下，该版本只包含软件中错误修复的补丁等。


## License

目前 Neuron 已开源 MQTT、RESTful API 和 Modbus TCP，用户可以直接使用开源的驱动协议。但是，通过上传有效的许可证，用户可以使用更多的驱动协议，如 OPC UA，Modbus RTU，三菱 PLC 和欧姆龙 PLC。


请参考[模块列表](../introduction/plugin-list/plugin-list.md)获取更多的 Neuron 支持的驱动模块。

