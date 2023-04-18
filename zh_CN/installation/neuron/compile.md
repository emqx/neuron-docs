# 源码构建

## 安装依赖

请参考 [Install-dependencies](https://github.com/emqx/neuron/blob/main/Install-dependencies.md)。

## 编译

```
$ git clone https://github.com/emqx/neuron
$ cd neuron
$ mkdir build && cd build
$ cmake .. && make
```

:::tip
CMakeLists 中有三个可选参数：
* CMAKE_BUILD_TYPE "Debug"，默认编译 debug 版本。
* DISABLE_WERROR，将所有的警告当作错误进行处理。</br>使用示例：```cmake -DISABLE_WERROR=1 ..```
* DISABLE_ASAN，选择是否开启 libasan 内存检测。
:::

### 安装 Dashboard

在 [neuron-dashboard](https://github.com/emqx/neuron-dashboard/releases) 页面下载最新的 `neuron-dashboard.zip`，解压后放到 Neuron 可执行目录下的 dist 目录中。

### 运行

```
$ cd build
$ ./neuron
```