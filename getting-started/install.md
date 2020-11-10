# 安装 {#endpoint-download}

下文介绍了如何在 x86 或 ARM Linux 设备上安装 Neuron 软件包。

## 下载

Neuron 软件包可从 EMQ 网站 [https://www.emqx.io](https://www.emqx.io/) 下载. 

| 下载文件                                         | 架構   |
| ------------------------------------------------ | --------------------- |
| _neuron-x.y.z-linux-x86_64.tar.gz_               | x86 64-bit            |
| _neuron-x.y.z-linix-armv7l.tar.gz_               | ARM hardware floating |
| _neuron-x.y.z-linix-aarch64.tar.gz_              | ARM 64-bit            |

对于版本号x.y.z，x是主要版本号，如果整个系统结构得到增强，则可能会更改； y是次要版本号，如果存在某些附加功能，则可能会更改。 z是Neuron软件中错误修复的补丁号。

## 安装条件 {#endpoint-pre-requisites}

已为 Neuron 测试了以下 Linux 发行版或设备。

| Linux 发行版或设备                                                                   | 所需的 Neuron 包                  |
| ------------------------------------------------------------------------------------ | --------------------------------- |
| **Debian package system for x86_64** <br>Ubuntu 20.xx<br>Ubuntu 18.xx Desktop<br>Ubuntu 16.xx Desktop (install openssl1.1)<br>Ubuntu 14.xx Desktop (install openssl1.1)  | neuron-x.y.z-linux-x86_64.tar.gz |
| **Redhat package system for x86_64** <br>Centos 8<br>Centos 7.x (install openssl1.1) | neuron-x.y.z-linux-x86_64.tar.gz  |
| **Raspberry Pi 2** <br>Pi 4b+<br>Pi 3b+<br>Pi 2b+ (install openssl1.1)               | neuron-x.y.z-linux-armv7l.tar.gz  |
| armv7l Ubuntu Linux System                                                           | neuron-x.y.z-linux-armv7l.tar.gz  |
| aarch64 Ubuntu Linux System                                                          | neuron-x.y.z-linux-aarch64.tar.gz |

注意: 一些Linux发行版要求安装 **openssl1.1**.
Debian 包, wget [http://archive.ubuntu.com/ubuntu/pool/main/o/openssl/libssl1.1_1.1.0g-2ubuntu4_amd64.deb](http://archive.ubuntu.com/ubuntu/pool/main/o/openssl/libssl1.1_1.1.0g-2ubuntu4_amd64.deb)
Redhat 包, [https://linuxscriptshub.com/update-openssl-1-1-0-centos-6-9-7-0](https://linuxscriptshub.com/update-openssl-1-1-0-centos-6-9-7-0/)

### 安装 {#endpoint-new-installation}

本节介绍了如何在 Linux 系统上首次安装 Neuron 软件。新的 Neuron 软件必须安装在任何用户账户的主目录下。我们推荐使用 "neuron" 账户进行安装。

1. 解压软件包到任何目录下，(例 /home/neuron)，输入命令：

   ```bash
   ~\$ tar -zxvf neuron-x.y.z-linux-x86_64.tar.gz
   ```

2. 第一次运行 Neuron 建立数据目录 ~/dat. 输入命令：

   ```bash
   ~\$ {PATH}/neuron start
   Directory {PATH}/dat created
   Directory {PATH}/dat/0 created
   Directory {PATH}/dat/0/adm created
   Directory {PATH}/dat/0/adm/usr created
   Directory {PATH}/dat/0/alm created
   Directory {PATH}/dat/0/cfg created
   Directory {PATH}/dat/0/log created
   Directory {PATH}/dat/0/scp created
   Directory {PATH}/dat/0/scp/subr created
   Directory {PATH}/dat/0/obj created
   Directory {PATH}/dat/0/trd created
   Neuron instance 0 is now running with PID:6312 Port:7000
   ```

### 启动系统 {#endpoint-starting}

Neuron 可以通过以下方式启动

```bash
~\$ {PATH}/neuron start
Neuron instance 0 is now running with PID:6037 Port:7000
```

### 停止系统 {#endpoint-stopping}

输入以下命令，Neuron 将停止运行

```bash
~\$ {PATH}/neuron stop
Neuron instance 0 is stopping ...
Stopped !
```

## 启动特定系统 {#endpoint-specific-starting}

特定 Neuron 可以通过以下方式启动

```bash
~\$ {PATH}/neuron start -i7
Neuron instance 7 is now running with PID:8097 Port:7007
```

## 停止特定系统 {#endpoint-specific-stopping}

输入以下命令，特定 Neuron 将停止运行

```bash
~\$ {PATH}/neuron stop -i7
Neuron instance 7 is stopping ...
Stopped !
```

## 启动多个系统 (#endpoint-multi-starting)

多个 Neuron 可以通过以下方式启动

```bash
~\$ {PATH}/neuron start -a5
Neuron instance 0 is now running with PID:6066 Port:7000
Neuron instance 1 is now running with PID:6069 Port:7001
Neuron instance 2 is now running with PID:6076 Port:7002
Neuron instance 3 is now running with PID:6087 Port:7003
Neuron instance 4 is now running with PID:6090 Port:7004
```

## 停止多个系统 {#endpoint-multi-stopping}

输入以下命令，多个 Neuron 将停止运行

```bash
~\$ {PATH}/neuron stop -a5
Neuron instance 0 is stopping ...
Stopped !
Neuron instance 1 is stopping ...
Stopped !
Neuron instance 2 is stopping ...
Stopped !
Neuron instance 3 is stopping ...
Stopped !
Neuron instance 4 is stopping ...
Stopped !
```

### 检查系统 {#endpoint-checking}

输入以下命令，检查Neuron 是否运行

```bash
~\$ {PATH}/neuron status
Neuron instance 0 is running with PID:6118 Port:7000
Neuron instance 1 is running with PID:6121 Port:7001
Neuron instance 2 is running with PID:6132 Port:7002
Neuron instance 3 is running with PID:6139 Port:7003
Neuron instance 4 is running with PID:6144 Port:7004
```

### 命令参数 {#endpoint-command}

本节介绍了 "neuron" 命令的可用参数。

用法: neuron [start|stop|status] [options]
| 参数 							        | 描述                  				  |
| ------------------------------- | ------------------------------------- |
| -a 或 --allinstance `<number>`  | 数量 `<2-10>`
| -i 或 --instance `<instanceno>` | 实例号 `<0-9>`                         |
| -u 或 --uuid `<uuid>`           | 通用唯一ID `<最大36字符>`            |

在两者 `[-a|-i]` 之间，只能选择其中之一

## 在Docker运行 {#endpoint-docker}

docker 镜像请从 docker hub 网站下载 [https://hub.docker.com](https://hub.docker.com).

```bash
~\$ docker pull emqx/neuron:1.0.0
```

启动 docker 容器

```bash
~\$ docker run -d --name neuron -p 7000:7000 emqx/neuron:1.0.0
```

## 申请试用软件授权

Neuron 缺省安装包提供了

