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

Note: 一些Linux发行版要求安装 **openssl1.1**.
For Debian package, wget [http://archive.ubuntu.com/ubuntu/pool/main/o/openssl/libssl1.1_1.1.0g-2ubuntu4_amd64.deb](http://archive.ubuntu.com/ubuntu/pool/main/o/openssl/libssl1.1_1.1.0g-2ubuntu4_amd64.deb)
For Redhat package, [https://linuxscriptshub.com/update-openssl-1-1-0-centos-6-9-7-0](https://linuxscriptshub.com/update-openssl-1-1-0-centos-6-9-7-0/)

### 安装 {#endpoint-new-installation}

本节介绍了如何在 Linux 系统上首次安装 Neuron 软件。新的 Neuron 软件必须安装在任何用户账户的主目录下。我们推荐使用 "neuron" 账户进行安装。

1. 解压软件包到任何目录下，(例 /home/neuron)，输入命令：

   ```bash
   ~\$ tar -zxvf neuron-x.y.z-linux-x86_64.tar.gz
   ```

2. 第一次运行 Neuron 建立数据目录 ~/dat. 输入命令：

   ```bash
   ~\$ {PATH}/neuron start
   ```

### 启动系统 {#endpoint-starting}

Neuron 可以通过以下方式启动

```bash
~\$ {PATH}/neuron start
```

### 停止系统 {#endpoint-stopping}

输入以下命令，Neuron 将停止运行

```bash
~\$ {PATH}/neuron stop
```

### 检查系统 {#endpoint-checking}

输入以下命令，检查Neuron 是否运行

```bash
~\$ {PATH}/neuron status
```

### 命令参数 {#endpoint-command}

本节介绍了 "neuron" 命令的可用参数。

用法: neuron [start|stop|status] [options]
| 参数 							  | 描述                  				  |
| ------------------------------- | ------------------------------------- |
| -i or --instance `<instanceno>` |实例号 `<0-9>`                         |
| -u or --uuid `<uuid>`           |通用唯一ID `<max 36 chars>`            |

## 在Docker运行 {#endpoint-docker}

docker 镜像请从 docker hub 网站下载 [https://hub.docker.com](https://hub.docker.com).

```bash
~\$ docker pull emqx/neuron:1.0.0
```

启动 docker container

```bash
~\$ docker run -d --name neuron -p 7000:7000 emqx/neuron:1.0.0
```



