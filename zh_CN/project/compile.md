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

## 步骤调试

1. 使用日志，打印相关调试信息
2. 因 Neuron 是多线程异步并发的程序，不推荐使用 GDB 进行断点调试等。
3. 结合 libasan 运行时内存分析，可调式大部分内存问题。

:::tip
libasan 是指 AddressSanitizer（ASan）库，是一种内存错误检测工具，用于帮助发现程序运行时的内存错误，如缓冲区溢出、使用已释放的内存、使用未初始化的内存等。
ASan 在程序运行时，通过注入额外的代码来检测内存错误。它使用了一种红黑树数据结构来跟踪内存块的分配情况，并使用影子内存来检测对未分配内存的读写访问。当检测到内存错误时，ASan 会打印相关信息，例如出错位置、错误类型等。
libasan 是 ASan 的运行时库，可与编译器配合使用，如 Clang、GCC 等。它提供了必要的函数和数据结构，以便在程序执行期间进行内存错误检测和报告。
:::