# 安装

下文介绍了如何在 X86 / ARM Linux 设备上安装 Neuron 软件包。

## 下载

Neuron 软件包可从 Neuron 网站[https://neugates.io/zh/downloads](https://neugates.io/zh/downloads)上根据实际系统对应下载。

| 下载文件                 | 架构    |
| ----------------------- | ------ |
| neuron-amd.zip          | X86_64 |
| neuron-armhf.zip        | ARM_32 |
| neuron-arm64.zip        | ARM_64 |

## 安装条件

| 系统要求      | 包名称             |
| ------------ | ---------------- |
| ubuntu 18.xx | deb包, tar.gz包   |
| ubuntu 20.xx | deb包, tar.gz包   |
| centos 8     | rpm包, tar.gz包   |
| centos 9     | rpm包, tar.gz包   |

## 安装步骤

本节介绍了如何在 Linux 系统上首次安装 Neuron 软件。

### 方法一：使用 .deb 安装

输入命令：

```bash
sudo dpkg -i xxx.deb
```

根据不同版本安装，例如 neuron-2.0.0-beta.1-armhf.deb

**注意：** 成功安装 deb 包后，自启动 Neuron

#### 卸载 deb 的指令

```bash
sudo dpkg -r neuron
```

### 方法二：使用 .rmp 安装

输入命令：

```bash
sudo rpm -i xxx.rpm --nodeps --force
```

根据不同版本安装，例如 neuron-2.0.0-beta.1-armhf.rpm

**注意：** 成功安装 rmp 包后，自启动 Neuron

#### 卸载 rmp 指令

```bash
sudo rpm -e neuron
```

### 方法三：使用 .tar.gz 安装

输入命令：

```bash
sudo tar -zxvf xxx.tar.gz
cd xxx
```

根据不同版本安装，例如 neuron-2.0.0-beta.1-armhf.tar.gz

#### 启动 Neuron

```bash
./neuron
```

### Neuron 操作

用 rpm 和 deb 方式安装的都可以通过以下指令查看/起停 Neuron：

#### 查看 Neuron 状态

```bash
sudo systemctl status neuron
```

#### 停止 Neuron

```bash
sudo systemctl stop neuron
```

#### 重启 Neuron

```bash
sudo systemctl restart neuron
```
