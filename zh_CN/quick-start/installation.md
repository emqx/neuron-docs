# 下载安装

Neuron 分成两个安装包：
- NeuronEX：集成 eKuiper，携带数据流处理引擎功能，用户可以在采集数据的同时对数据进行处理；
- Neuron：不集成 eKuiper，主要实现工业数据的采集；

用户可以根据自身需求选择。

## 安装条件

| Linux 发行版                                                   | 所需包          |
| :----------------------------------------------------------------- | :--------- |
| **Debian package system**</br>Ubuntu 20.04 </br>Ubuntu 18.04 </br>Ubuntu 16.04 </br>Debian 11</br>Debian 10</br>Debian 9</br>Debian 8             | deb |
| **Redhat package system**</br>CentOS Stream 9</br>CentOS Stream 8</br>CentOS 7  | rpm |

:::tip
rpm/deb package 中使用了 systemd 管理 neuron 进程，建议优先使用 rpm/deb package。
:::

## 硬件要求

|规格|配置推荐|硬件架构|备注|
| :-------------------- | :----------------------------------- | :------------------------------ | :----------------------------------- |
| 100 点位 | 128M 内存 | ARM/X86/MIPS/RISC-V 等 CPU 架构；Linux 系统或 Docker 容器化 | 小型网关设备 |
| 1,000 点位 | 256M 内存 | ARM/X86/MIPS/RISC-V 等 CPU 架构；Linux 系统或 Docker 容器化 | 中型网关设备 |
| 10,000 点位 | 512M 内存 | ARM/X86/MIPS/RISC-V 等 CPU 架构；Linux 系统或 Docker 容器化 | 中型网关、工控机等 |
| 大于 10,000 点位 | 1G 内存 | ARM/X86/MIPS/RISC-V 等 CPU 架构；Linux 系统或 Docker 容器化 | 中大型网关、工控机、服务器等 |

## 下载

Neuron 软件包可由 Neuron 官网 [https://neugates.io/zh/downloads](https://neugates.io/zh/downloads) 下载。也可以到 [Github 仓库](https://github.com/emqx/neuron/releases) 下载。

| 下载文件                           | 架构    |
| --------------------------------- | ------ |
| neuron-x.y.z-linux-amd64.deb      | X86_64 |
| neuron-x.y.z-linux-armhf.deb      | ARM_32 |
| neuron-x.y.z-linux-arm64.deb      | ARM_64 |

版本号 x.y.z 说明：

* x 为主要版本号：一般情况下，该版本会引入一些重大功能，如引入架构性的更改，主版本升级不保证与老版本之间的兼容性；
* y 是次要版本号：一般情况下，该类型版本会引入一些新功能，但是会保证在该主要版本号下的兼容性；
* z 是维护版本号：一般情况下，该版本只包含软件中错误修复的补丁等。

## 使用 Docker 运行

### 获取镜像

neuron docker 镜像请从 [docker hub](https://hub.docker.com/r/emqx/neuron/tags) 网站下载。

```bash
## pull Neuron
$ docker pull emqx/neuron:latest
```

支持更小占用的 alpine 镜像，请从 [docker hub](https://hub.docker.com/r/emqx/neuron/tags) 网站下载。

```bash
## pull Neuron
$ docker pull emqx/neuron:2.3.0-alpine
```

NeuronEX docker 镜像请从 [docker hub](https://hub.docker.com/r/emqx/neuronex/tags) 网站下载。

```bash
## pull NeuronEX
$ docker pull emqx/neuronex:latest
```

### 启动

启动 Neuron:

```bash
## run Neuron
$ docker run -d --name neuron -p 7000:7000 --privileged=true -v /host/dir:/opt/neuron/persistence --device /dev/ttyUSB0:/dev/ttyS0 --restart=always emqx/neuron:latest
```

启动 NeuronEX:

```bash
## run NeuronEX
$ docker run -d --name neuronex -p 7000:7000 --privileged=true -v /host/dir:/opt/neuron/persistence  --device /dev/ttyUSB0:/dev/ttyS0 --restart=always emqx/neuronex:latest
```

* tcp 7000: 用于访问 web 和 http api 端口。
* --restart=always: docker 进程重启时，自动重启 neuron 容器。
* --privileged=true: 可选参数，便于排查问题。
* --env DISABLE_AUTH=1: 可选参数，用于关闭鉴权。
* -v /host/dir:/opt/neuron/persistence: 用于将 docker 中 Neuron 配置信息存放在本地目录（例如，/host/dir 放在 /opt/neuron/persistence）。
* --device /dev/ttyUSB0:/dev/ttyS0: 用于映射串口到 docker。/dev/ttyUSB0 是 Linux 下串口设备；/dev/ttyS0 是 Docker 下串口设备。
* --ulimit nofile=65535 : 默认为 1024，当连接设备较多时增大此字段的值，例如 65535。

## 使用 deb 包安装

### 安装

根据不同版本及架构安装，例如：

```bash
$ sudo dpkg -i neuron-2.3.0-linux-armhf.deb
```

为避免 ubuntu 系统自动更新时替换 neuron 包，还需要执行以下命令使 neuron 软件包在 apt 升级中保留。

```bash
$ sudo apt-mark hold neuron
```

::: tip
成功安装 deb 包后，自动启动 Neuron
:::

### 卸载

```bash
$ sudo dpkg -r neuron
```

## 使用 rpm 安装包

### 安装

根据不同版本及架构安装，例如：

```bash
$ sudo rpm -i neuron-2.3.0-linux-armhf.rpm
```

::: tip
成功安装 rpm 包后，自启动 Neuron。
:::

### 卸载

```bash
$ sudo rpm -e neuron
```

## 使用 .tar.gz 安装包

### 下载安装包

根据不同的版本及架构下载，例如：

```bash
$ wget https://www.emqx.com/en/downloads/neuron/2.3.0/neuron-2.3.0-linux-armhf.tar.gz
```

### 解压

```bash
$ tar -zxvf neuron-2.3.0-linux-armhf.tar.gz
$ cd neuron-2.3.0-linux-armhf
```

#### 启动

执行如下命令启动 Neuron：

```bash
$ ./neuron
```

## Neuron 操作

用 rpm 和 deb 方式安装的都可以通过以下指令查看/起停 Neuron：

### 查看 Neuron 状态

```bash
$ sudo systemctl status neuron
```

### 停止 Neuron

```bash
$ sudo systemctl stop neuron
```

### 重启 Neuron

```bash
$ sudo systemctl restart neuron
```
