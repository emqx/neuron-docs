# Build from source

## Installation dependencies

Please refer to [Install dependencies](https://github.com/emqx/neuron/blob/main/Install-dependencies.md).

## Compilation

```
$ git clone https://github.com/emqx/neuron
$ cd neuron
$ mkdir build && cd build
$ cmake .. && make
```

:::tip
There are three optional parameters in CMakeLists:
* CMAKE_ BUILD_ Type "Debug", which compiles the debug version by default.
* DISABLE_WERROR, which treats all warnings as errors.<br />Usage example:```cmake -DISABLE_WERROR=1 ..```
* DISABLE_ ASAN, select whether to enable libasan memory detection.
:::

## Install Dashboard

On the [neuron dashboard](https://github.com/emqx/neuron-dashboard/releases) download the latest `neuron-dashboard.zip` from the page, extract it, and place it in the dist directory under the Neuron executable directory.

## Operation

```
$ cd build
$ ./ neuron
```
