# 安装

下文介绍了如何在 X86 / ARM Linux 设备上安装 Neuron 软件包。

## 下载

Neuron 软件包可从 Neuron 网站[https://neugates.io/zh/downloads](https://neugates.io/zh/downloads)上下载。

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

解压软件包到任何目录下（例如：/home/Neuron），输入命令:

```bash
~\$ unzip xxx.zip
```

根据系统选择对应的安装包，例如 neuron-armhf.zip

### 方法一：使用 .deb 安装

输入命令：

```bash
~\$ sudo dpkg -i xxx.deb
cd opt/neuron
```

根据不同版本安装，例如 neuron-2.0.0-beta.1-armhf.deb

**注意：** 安装 deb 包成功后，自启动 Neuron

#### 查看 Neuron 状态

```bash
~\$ sudo systemctl status neuron
```

#### 停止 Neuron

```bash
~\$ sudo systemctl stop neuron
```

#### 重启 Neuron

```bash
~\$ sudo systemctl restart neuron
```

#### 卸载 deb

```bash
~\$ sudo dpkg -r neuron
```

### 方法二：使用 .rmp 安装

输入命令：

```bash
~\$ sudo rpm -i xxx.rpm --nodeps --force
cd opt/neuron
```

根据不同版本安装，例如 neuron-2.0.0-beta.1-armhf.rpm

**注意：** 安装 rmp 包成功后，自启动 Neuron

#### 查看 Neuron 状态

```bash
~\$ sudo systemctl status neuron
```

#### 停止 Neuron

```bash
~\$ sudo systemctl stop neuron
```

#### 重启 Neuron

```bash
~\$ sudo systemctl restart neuron
```

#### 卸载 deb

```bash
~\$ sudo rpm -e neuron
```

### 方法三：使用 .tar.gz 安装

输入命令：

```bash
~\$ sudo tar -zxvf xxx.tar.gz
cd xxx
```

根据不同版本安装，例如 neuron-2.0.0-beta.1-armhf.tar.gz

**注意：** 安装deb包成功后，自启动 Neuron

#### 启动 Neuron

```bash
~\$ ./neuron
```
