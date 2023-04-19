# 使用 deb 包安装

## 下载

根据不同版本及架构下载安装包，例如：

```bash
$ wget https://www.emqx.com/en/downloads/neuron/2.4.0/neuron-2.4.0-linux-amd64.deb
```

## 安装

根据不同版本及架构安装，例如：

```bash
$ sudo dpkg -i neuron-2.4.0-linux-amd64.deb
```

为避免 ubuntu 系统自动更新时替换 neuron 包，还需要执行以下命令使 neuron 软件包在 apt 升级中保留。

```bash
$ sudo apt-mark hold neuron
```

::: tip
成功安装 deb 包后，自启动 Neuron。
:::

## 状态

```bash
$ sudo systemctl status neuron
```

## 停止

```bash
$ sudo systemctl stop neuron
```

## 重启

```bash
$ sudo systemctl restart neuron
```

## 卸载

```bash
$ sudo dpkg -r neuron
```