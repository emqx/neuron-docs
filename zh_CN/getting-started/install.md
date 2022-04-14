# 安装

下文介绍了如何在 X86 / ARM Linux 设备上安装 Neuron 软件包。

## 下载

Neuron 软件包可从 Neuron 网站[https://neugates.io/zh/downloads](https://neugates.io/zh/downloads)上根据实际系统对应下载。

| 下载文件                                | 架构    |
| -------------------------------------- | ------ |
| neuron-x.y.z-linux-amd64.deb | X86_64 |
| neuron-x.y.z-linux-armhf.deb | ARM_32 |
| neuron-x.y.z-linux-arm64.deb | ARM_64 |

版本号x.y.z，x为主要版本号，如果整个系统结构得到增强，则可能会更改； y是次要版本号，如果存在某些附加功能，则可能会更改。 z是Neuron软件中错误修复的补丁号。

## 安装条件

rpm/deb package中使用了systemd管理neuron进程，建议优先使用rpm/deb package。

| Linux 发行版或设备 | 所需包          |
| ------------ | ---------------- |
| **Debian package system**</br>Ubuntu 20.xx </br>Ubuntu 18.xx | deb/tar.gz |
| **Redhat package system**</br>Contos 8</br>Centos 9 | rpm/tar.gz |

## 安装步骤

本节介绍了如何在 Linux 系统上首次安装 Neuron 软件。

### 使用 deb package

#### 安装

```bash
$ sudo dpkg -i xxx.deb
```

根据不同版本安装，例如 neuron-2.0.0-beta.2-linux-armhf.deb

**注意：** 成功安装 deb 包后，自动启动 Neuron

#### 卸载

```bash
$ sudo dpkg -r neuron
```

### 使用 rpm package

#### 安装

```bash
$ sudo rpm -i xxx.rpm --nodeps --force
```

根据不同版本安装，例如 neuron-2.0.0-beta.2-linux-armhf.rpm

**注意：** 成功安装 rpm 包后，自启动 Neuron

#### 卸载 

```bash
$ sudo rpm -e neuron
```

### 使用 .tar.gz package

#### 解压

```bash
$ sudo tar -zxvf xxx.tar.gz
$ cd xxx
```

根据不同版本安装，例如 neuron-2.0.0-beta.2-linux-armhf.tar.gz

#### 启动

执行如下命令可在当前终端启动：

```bash
$ ./neuron
```

若想以守护进程方式运行，则可执行如下命令：

```bash
$ ./neuron -d
```

执行如下命令可查看所有命令行可用参数：

```bash
$ ./neuron -h
```

### 使用Docker运行

#### 获取镜像

docker镜像请从docker hub网站下载 https://hub.docker.com

```bash
$ docker pull neugates/neuron:2.0.0-rc1
```

#### 启动

```bash
$ docker run -d --name neuron -p 7000:7000 -p 7001:7001 --privileged=true --restart=always neugates/neuron:2.0.0-rc1
```

tcp 7000: 用于访问web。

tcp 7001: http api端口。

--restart=always: docker进程重启时，自动重启neuron容器。

--privileged=true：便于排查问题。

--device /dev/ttyUSB0:/dev/ttyS0: 用于映射串口到docker。

### Neuron 操作

用 rpm 和 deb 方式安装的都可以通过以下指令查看/起停 Neuron：

#### 查看 Neuron 状态

```bash
$ sudo systemctl status neuron
```

#### 停止 Neuron

```bash
$ sudo systemctl stop neuron
```

#### 重启 Neuron

```bash
$ sudo systemctl restart neuron
```
