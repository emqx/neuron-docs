# 学会编译

## 从源码构建

### 安装依赖

请参考 [Install-dependencies](https://github.com/emqx/neuron/blob/main/Install-dependencies.md)

### 编译

```
$ git clone https://github.com/emqx/neuron
$ cd neuron
$ mkdir build && cd build
$ cmake .. && make
```

### 安装 Dashboard

在 [neuron-dashboard](https://github.com/emqx/neuron-dashboard/releases) 页面下载最新的 `neuron-dashboard.zip`，解压后放到 Neuron 可执行目录下的 dist 目录中。

### 运行

```
$ cd build
$ ./neuron
```