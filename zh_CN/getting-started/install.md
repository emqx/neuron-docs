# 安装

下文介绍了如何在 X86 / ARM Linux 设备上安装 Neuron 软件包。

## 下载

Neuron 软件包可从 Neuron 网站[https://neugates.io/zh/downloads](https://neugates.io/zh/downloads)上下载。

| 下载文件                 | 架构    |
| ----------------------- | ------ |
| neuron-amd64-2022-03-08.zip | X86_64 |
| neuron-arm-2022-03-08.zip   | ARM_32 |
| neuron-arm64-2022-03-8.zip  | ARM_64 |

## 安装条件

| 系统要求      |
| ------------ |
| ubuntu 18.xx |
| ubuntu 20.xx |
| centos 8     |
| centos 9     |

## 安装步骤

本节介绍了如何在 Linux 系统上首次安装 Neuron 软件。

解压软件包到任何目录下（例如：/home/Neuron），输入命令：

```bash
~\$ unzip neuron-arm-2022-03-08.zip
dpkg neuron-2.main-2022-03-08_arm.deb
cd opt
```

## 运行Neuron

```bash
~\$ cd {PATH}/neuron
cd bin
./neuron
```
