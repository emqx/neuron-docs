# Learn to compile

## Build from source

### Installation dependencies

Please refer to [Install dependencies](https://github.com/emqx/neuron/blob/main/Install-dependencies.md)

### Compilation

```
$ git clone https://github.com/emqx/neuron
$ cd neuron
$ mkdir build && cd build
$ cmake .. && make
```

:::tip
There are three optional parameters in CMakeLists:
* CMAKE_ BUILD_ Type "Debug", which compiles the debug version by default.
* DISABLE_WERROR, which treats all warnings as errors.</br>Usage example:```cmake -DISABLE_WERROR=1 ..```
* DISABLE_ ASAN, select whether to enable libasan memory detection.
:::

### Install Dashboard

On the [neuron dashboard](https://github.com/emqx/neuron-dashboard/releases) download the latest 'neuron dashboard. zip' from the page, extract it, and place it in the dist directory under the Neuron executable directory.

### Operation

```
$ cd build
$ ./ neuron
```

## Step debugging

1. Use logs to print relevant debugging information
2. Because Neuron is a multithreaded asynchronous concurrent program, it is not recommended to use GDB for breakpoint debugging, etc.
3. Combining libasan runtime memory analysis, most memory issues can be resolved.

:::tip
Libasan refers to the Address Sanitizer (ASan) library, which is a memory error detection tool used to help detect memory errors during program execution, such as buffer overflows, using freed memory, and using uninitialized memory.</br>
ASan detects memory errors by injecting additional code while the program is running. It uses a red and black tree data structure to track the allocation of memory blocks, and uses shadow memory to detect read and write access to unallocated memory. When a memory error is detected, ASan prints relevant information, such as the location and type of the error.</br>
Libasan is a runtime library for ASan that can be used with compilers, such as Clang, GCC, and so on. It provides the necessary functions and data structures to detect and report memory errors during program execution.
:::