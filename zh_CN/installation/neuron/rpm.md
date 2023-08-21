# 使用 rpm 包安装

## 下载

根据不同版本及架构下载安装包，例如：

```bash
$ wget https://www.emqx.com/en/downloads/neuron/2.5.3/neuron-2.5.3-linux-amd64.rpm
```

## 安装

根据不同版本及架构安装，例如：

```bash
$ sudo rpm -i neuron-2.5.3-linux-amd64.rpm
```

::: tip
成功安装 rpm 包后，自启动 Neuron。
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
$ sudo rpm -e neuron
```