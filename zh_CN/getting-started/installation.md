# 安装

为满足客户需求，Neuron 分成两种，一种是集成 eKuiper，携带数据流处理引擎界面的，名称为 NeuronEX，另一种是不集成 eKuiper 的，名称为 Neuron。用户可以根据自身需求选择。

## 下载

Neuron 软件包可从 Neuron 官网 [https://neugates.io/zh/downloads](https://neugates.io/zh/downloads) 上下载。官网下载的安装包适配的系统较新，更多系统版本包及适配老系统的版本包请到 [Github 仓库](https://github.com/emqx/neuron/releases) 下载。

| 下载文件                           | 架构    |
| --------------------------------- | ------ |
| neuron-x.y.z-linux-amd64.deb      | X86_64 |
| neuron-x.y.z-linux-armhf.deb      | ARM_32 |
| neuron-x.y.z-linux-arm64.deb      | ARM_64 |

版本号 x.y.z 说明：

* x 为主要版本号，如果整个系统结构得到增强，则可能会更改。
* y 是次要版本号，如果存在某些附加功能，则可能会更改。
* z 是Neuron软件中错误修复的补丁号。

## 安装条件

| Linux 发行版或设备                                                   | 所需包          |
| :----------------------------------------------------------------- | :--------- |
| **Debian package system**</br>Ubuntu 20 </br>Ubuntu 18             | deb/tar.gz |
| **Redhat package system**</br>Contos stream 8</br>Centos stream 9  | rpm/tar.gz |

:::tip
rpm/deb package 中使用了 systemd 管理 neuron 进程，建议优先使用 rpm/deb package。
:::

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
$ sudo tar -zxvf neuron-2.3.0-linux-armhf.tar.gz
$ cd neuron-2.3.0-linux-armhf
```

#### 启动

执行如下命令启动 Neuron：

```bash
$ ./neuron
```

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
$ docker run -d --name neuron -p 7000:7000 --privileged=true --restart=always emqx/neuron:latest
```

启动 NeuronEX:

```bash
## run NeuronEX
$ docker run -d --name neuronex -p 7000:7000 --privileged=true --restart=always emqx/neuronex:latest
```

* tcp 7000: 用于访问 web 和 http api 端口。
* --restart=always: docker 进程重启时，自动重启 neuron 容器。
* --privileged=true: 可选参数，便于排查问题。
* --env DISABLE_AUTH=true: 可选参数，用于关闭鉴权。
* -v /host/dir:/opt/neuron/persistence: 用于将 docker 中 Neuron 配置信息存放在本地目录（例如，/host/dir）。
* --device /dev/ttyUSB0:/dev/ttyS0: 用于映射串口到 docker。

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
