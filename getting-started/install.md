# 安装 {#endpoint-download}

下文介绍了如何在 x86 或 ARM Linux 设备上安装 Neuron 软件包。

## 下载

Neuron 软件包可从 EMQ 网站 [https://www.emqx.io](https://www.emqx.io/) 下载. docker 镜像请从 docker hub 网站下载 [https://hub.docker.com/r/emq/neuron](https://hub.docker.com/r/emq/neuron).

Neuron 支持以下 Linux 系统：

对于 x86 64 位系统,<br>下载文件： _neuron-0.5-x86_64.tar.gz_

对于支持硬浮点的 ARM 系统,<br>下载文件： _neuron-0.5-armhf.tar.gz_

对于 ARM 64 位系统,<br>下载文件： _neuron-0.5-arm64.tar.gz_

0.5 这个数字，0 是主要版本号，可能会因为整个系统结构的增强而改变，5 是次要版本号，可能会因为 Neuron 软件有一些额外的功能或一些错误修复补丁而改变。

下一个标记指定了安装的平台。例如，x86_64 表示 x86 64 位平台，arm64 表示 ARM 64 位平台等。

## 前提条件 {#endpoint-pre-requisites}

已为 Neuron 测试了以下 Linux 发行版或设备。

| Linux 发行版或设备                                                        | 所需的 Neuron 包         |
| ------------------------------------------------------------------------- | ------------------------ |
| Debian package system for x86<br>Debian 9.x<br>Ubuntu 16.xx Desktop       | neuron-1.4-x86_64.tar.gz |
| Ubuntu 18.xx Desktop<br>Linuxmint 18                                      | neuron-1.4-x86_64.tar.gz |
| Redhat package system for x86<br>Fedora 30 Workstation<br>Centos 7.x-1810 | neuron-1.4-x86_64.tar.gz |
| Raspberry Pi 2                                                            | neuron-1.4-armhf.tar.gz  |
| Raspberry Pi 3                                                            | neuron-1.4-arm64.tar.gz  |
| Raspberry Pi 4                                                            | Neuron-1.4-arm64.tar.gz  |

### 安装 {#endpoint-new-installation}

本节介绍了如何在 Linux 系统上首次安装 Neuron 软件。新的 Neuron 软件必须安装在任何用户账户的主目录下。我们推荐使用 "neuron" 账户进行安装。

注意：在进行新的安装时，可能需要系统用户密码来创建用户帐号。

1. 在你的 Linux 发行版 中创建一个新的 Linux 账户 "neuron"，它将用于安装 Neuron 软件包。或者运行以下命令来创建一个用户账户。

   ```bash
   ~\$ sudo useradd neuron -m -s /bin/bash
   ```

2. 退出并以 "neuron" 用户身份登录到 Linux 提示符 ~\$。

3. 从 EMQ 网站下载 Neuron 软件包。

4. 解压软件包到 \$HOME 目录下，(即 /home/neuron)，输入命令：

   ```bash
   ~\$ tar -zxvf neuron-0.5-x86_64.tar.gz
   ```

5. 第一次运行 Neuron 建立数据目录 ~/dat. 输入命令：

   ```bash
   ~\$ neuronsrt
   ```

6. 停止 Neuron 运行，输入命令：

   ```bash
   ~\$ neuronsrt -s
   ```

### 设置 Shell 路径 {#endpoint-setting}

本节介绍如何为 Neuron 软件设置 shell 执行路径。不同的 Linux 发行版有自己的方法。请参考您的 Linux 手册。对于 Ubuntu，.bash_profile 将被修改如下:

```bash
# Neuron System environment

PATH=$PATH:$HOME/bin:.

NEURONPATH=\$HOME

export NEURONPATH

NEURONDATPATH=\$NEURONPATH/dat

export NEURONDATPATH
```

注意：$NEURONPATH 和 $NEURONDATPATH 都是在 shell 中运行 Neuron 的重要变量。

### 启动系统 {#endpoint-starting}

本节介绍了如何启动 Neuron。

1. 以 "neuron"身份登录

2. Neuron 可以通过以下方式启动

```bash
~\$ neuronsrt
```

### 停止系统 {#endpoint-stopping}

本节介绍如何停止 Neuron。

1. 以 "neuron"身份登录

2. 输入命令以下命令，Neuron 将停止运行

```bash
~\$ neuronsrt -s
```

### 命令开关 {#endpoint-command}

本节介绍了 "neuronsrt" 命令的可用参数。

| 参数 | 描述                |
| ---- | ------------------- |
| -h   | 显示帮助            |
| -p   | 显示运行状态        |
| -r   | 重启                |
| -n   | 用新配置重新启动    |
| -s   | 停止运行            |
| -f   | 修复（dat）数据目录 |
