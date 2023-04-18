# 基于 SDK 的驱动开发

本文主要介绍如何基于 SDK 包开发一个新的驱动插件并应用到 Neuron 中。

## 第一步，下载安装 SDK

下载链接：[https://github.com/emqx/neuron/releases](https://github.com/emqx/neuron/releases)

根据不同的开发系统，下载对应的 sdk tar.gz 包（ 例如，neuron-sdk-2.1.3-linux-amd64.tar.gz ）到相应的开发系统中并解压得到 neuron-sdk-x.x.x，其中 x.x.x 代表的是版本号，执行以下指令。

```bash
# take version 2.3.0 as an example
$ cd neuron-sdk-2.3.0
# install sdk
$ sudo ./sdk-install.sh
```

脚本执行完成后，需要注意以下路径的用法。

| 路径                         | 说明            |
| --------------------------- | ------------------------------------------------------------------------- |
| /usr/local/include/neuron   | 存放 Neuron 的头文件，应用于 CMakeLists.txt 编译文件中的 include_directories    |
| /usr/local/lib/neuron       | 存放 Neuron 依赖库文件，应用于 CMakeLists.txt 编译文件中的 link_directories     |
| /usr/local/bin/neuron       | 存放运行 Neuron 所需的文件                                                   |

## 第二步，驱动开发

在开发环境中新建一个目录文件用于存放开发驱动所需要的文件，在该目录文件下新建一个编译配置文件 CMakeLists.txt，一个 build 目录文件用于存放编译后的文件和一个 plugins 目录文件用于存放所有需要开发的驱动文件，每一个驱动都需要有一个独立的目录来存放驱动开发的所需的文件，以开发 modbus-tcp 驱动插件为例，目录层级如下图所示。

![driver-tree](./assets/driver-tree.png)

### CMakeLists.txt 范例

最主要的是 include_directories，link_directories 和 add_subdirectory 要配置正确。

```shell
cmake_minimum_required(VERSION 3.12)
project(modbus_tcp)
enable_language(C)
set(CMAKE_C_STANDARD 99)

find_package(Threads)

# add the path to the neuron header
include_directories(/usr/local/include /usr/local/include/neuron)
# add the path to the neuron library
link_directories(/usr/local/lib /usr/local/lib/neuron)

# add driver submodule
add_subdirectory(plugins/modbus-tcp)
```

### plugins/modbus

驱动开发文件中主要包含编译配置文件 CMakeLists.txt 和 驱动配置的 json 文件和驱动代码文件。

#### CMakeLists.txt 示例

```shell
set(LIBRARY_OUTPUT_PATH "${CMAKE_BINARY_DIR}/plugins")

set(CMAKE_BUILD_RPATH ./)
# set plugin name
set(MODBUS_TCP_PLUGIN plugin-modbus-tcp)
# set the driver development code file
set(MODBUS_TCP_PLUGIN_SOURCES  modbus_tcp.c)
add_library(${MODBUS_TCP_PLUGIN} SHARED)
target_sources(${MODBUS_TCP_PLUGIN} PRIVATE ${MODBUS_TCP_PLUGIN_SOURCES})
target_link_libraries(${MODBUS_TCP_PLUGIN} neuron-base)
```

#### modbus_tcp.c

驱动插件的接口文件，具体的驱动开发示例，请参考 [modbus 插件开发示例](../sdk-tutorial/sdk-example/modbus-example.md)。

static const neu_plugin_intf_funs_t plugin_intf_funs 结构体说明。

| 参数                    | 说明 |
| ---------------------- | ----------- |
| .open                  | 基于 plugin 创建 node 时 neuron 第一个调用的函数，创建插件自己定义的 struct neu_plugin    |
| .close                 | 删除 node 时，neuron 调用的最后一个函数，用于释放由 open 创建的 neu_plugin_t             |
| .init                  | 创建 node 时，neuron 调用完 open 后，紧接着调用的函数，此函数主要做插件内需要初始化的一些资源 |
| .uninit                | 删除 node 时，neuron 首先调用的函数，此函数主要释放一些在 init 中申请以及初始化的资源       |
| .start                 | 在 node 页面，将工作状态置为开始，neuron 会调用此函数，通知插件开始运行，以及开始连接设备      |
| .stop                  | 在 node 页面，将工作状态置为停止，neuron 会调用此函数，通知插件停止运行，关闭与设备的连接，driver.group_timer 不再触发 |
| .setting               | 在 node 页面，进行插件设置时，将通过 json 格式设置参数，neuron 通过此函数通知插件进行设置   |
| .request               | 此函数在南向 driver 开发中暂未使用       |
| .driver.validate_tag   | node 添加或者更新 tag 时，neuron 会把 tag 相关参数使用此函数通知到插件，插件根据各自实现检查此 tag 是有符合插件要求，该函数返回 0，代表成功 |
| .driver.group_timer    | 在 node 中添加 group 并且 node 状态为 running 时，此函数将以 group 的 interval 参数定时调用读取设备数据 |
| .driver.write_tag      | 当使用 write API 时，neuron 调用此函数，通知插件，向点位 tag 写入特定的值      |

动态库导出数据结构定义 const neu_plugin_module_t neu_plugin_module 说明。

| 参数               | 说明               |
| ----------------- | ------------------ |
| version           | 插件版本号           |
| module_name       | 模块名称             |
| module_descr      | 模块描述             |
| intf_funs         | 插件接口函数          |
| kind              | 插件类型             |
| type              | 插件实例化为 node 时，node 的类型   |

struct neu_plugin 结构体为插件的前置声名，每个插件需要提供该结构体的具体定义，且首成员必须是 common，其它成员根据驱动的配置添加。

```c
#include <stdlib.h>

#include <neuron.h>

static neu_plugin_t *driver_open(void);

static int driver_close(neu_plugin_t *plugin);
static int driver_init(neu_plugin_t *plugin);
static int driver_uninit(neu_plugin_t *plugin);
static int driver_start(neu_plugin_t *plugin);
static int driver_stop(neu_plugin_t *plugin);
static int driver_config(neu_plugin_t *plugin, const char *config);
static int driver_request(neu_plugin_t *plugin, neu_reqresp_head_t *head,
                          void *data);

static int driver_validate_tag(neu_plugin_t *plugin, neu_datatag_t *tag);
static int driver_group_timer(neu_plugin_t *plugin, neu_plugin_group_t *group);
static int driver_write(neu_plugin_t *plugin, void *req, neu_datatag_t *tag,
                        neu_value_u value);

static const neu_plugin_intf_funs_t plugin_intf_funs = {
    .open    = driver_open,
    .close   = driver_close,
    .init    = driver_init,
    .uninit  = driver_uninit,
    .start   = driver_start,
    .stop    = driver_stop,
    .setting = driver_config,
    .request = driver_request,

    .driver.validate_tag = driver_validate_tag,
    .driver.group_timer  = driver_group_timer,
    .driver.write_tag    = driver_write,
};

const neu_plugin_module_t neu_plugin_module = {
    .version      = NEURON_PLUGIN_VER_1_0,
    .module_name  = "modbus-tcp",
    .module_descr = "modbus tcp",
    .intf_funs    = &plugin_intf_funs,
    .kind         = NEU_PLUGIN_KIND_SYSTEM,
    .type         = NEU_NA_TYPE_DRIVER,
};

struct neu_plugin {
        neu_plugin_common_t common;
};

static neu_plugin_t *driver_open(void)
{
    neu_plugin_t *plugin = calloc(1, sizeof(neu_plugin_t));

    neu_plugin_common_init(&plugin->common);

    return plugin;
}

static int driver_close(neu_plugin_t *plugin)
{
    free(plugin);

    return 0;
}

static int driver_init(neu_plugin_t *plugin)
{
    plog_info(plugin, "node: modbus init");

    return 0;
}

static int driver_uninit(neu_plugin_t *plugin)
{

    plog_info(plugin, "node: modbus uninit");

    return 0;
}

static int driver_start(neu_plugin_t *plugin)
{
    plog_info(plugin, "node: modbus start");

    return 0;
}

static int driver_stop(neu_plugin_t *plugin)
{
    plog_info(plugin, "node: modbus stop");
    return 0;
}

static int driver_config(neu_plugin_t *plugin, const char *config)
{
    plog_info(plugin, "config: %s", config);

    return 0;
}

static int driver_request(neu_plugin_t *plugin, neu_reqresp_head_t *head,
                          void *data)
{
    (void) data;
    (void) plugin;
    (void) head;

    return 0;
}

static int driver_validate_tag(neu_plugin_t *plugin, neu_datatag_t *tag)
{
    plog_info(plugin, "validate tag: %s", tag->name);

    return 0;
}

static int driver_group_timer(neu_plugin_t *plugin, neu_plugin_group_t *group)
{
    (void) plugin;
    (void) group;

    plog_info(plugin, "timer....");

    return 0;
}

static int driver_write(neu_plugin_t *plugin, void *req, neu_datatag_t *tag,
                        neu_value_u value)
{
    (void) plugin;
    (void) req;
    (void) tag;
    (void) value;

    return 0;
}
```

#### modbus-tcp.json

驱动配置文件。

| 字段           | 说明                                                  |
| ------------- | ----------------------------------------------------- |
| tag_regex     | 针对驱动支持不同的数据类型，对地址配置的正则                 |
| description   | 该字段的详细说明                                        |
| attribute     | 该字段的属性，只有两种可选和必选，即 required 和 optional   |
| type          | 该字段的类型，目前常用的是 int 和 string 两种类型           |
| default       | 填写的默认值                                            |
| valid         | 该字段可填写的范围                                       |

:::tip
json 文件的名称应与模块名称 module_name 保持一致。
:::

```json
{
    "tag_regex": [
        {
            "type": 3,
            "regex": "[1-9]+![3-4][0-9]+(#B|#L|)$"
        },
        {
            "type": 4,
            "regex": "[1-9]+![3-4][0-9]+(#B|#L|)$"
        },
        {
            "type": 5,
            "regex": "[1-9]+![3-4][0-9]+(#BB|#BL|#LL|#LB|)$"
        },
        {
            "type": 6,
            "regex": "[1-9]+![3-4][0-9]+(#BB|#BL|#LL|#LB|)$"
            },
        {
            "type": 9,
            "regex": "[1-9]+![3-4][0-9]+(#BB|#BL|#LL|#LB|)$"
        },
        {
            "type": 11,
            "regex": "[1-9]+!([0-1][0-9]+|[3-4][0-9]+.([0-9]|[0-1][0-5]))$"
        }
    ],
    "host": {
        "name": "host",
        "description": "local ip in server mode, remote device ip in client mode",
        "attribute": "required",
        "type": "string",
        "valid": {
            "regex": "/^((2[0-4]\\d|25[0-5]|[01]?\\d\\d?)\\.){3}(2[0-4]\\d|25[0-5]|[01]?\\d\\d?)$/",
            "length": 30
        }
    },
    "port": {
        "name": "port",
        "description": "local port in server mode, remote device port in client mode",
        "attribute": "required",
        "type": "int",
        "default": 502,
        "valid": {
        "min": 1,
        "max": 65535
        }
    },
    "timeout": {
        "name": "timeout",
        "description": "recv msg timeout(ms)",
        "attribute": "required",
        "type": "int",
        "default": 3000,
        "valid": {
            "min": 1000,
            "max": 65535
        }
    }
}
```

### build

驱动开发代码完成之后，在该目录下执行编译。

```bash
cmake ..
make
```

## 第三步，插件应用于 Neuron

### 拷贝驱动 .so 文件

编译完成后，进入 modbus/build/plugins 中将生成的驱动 .so 文件（例如，libplugin-modbus-tcp.so ） 拷贝到 /usr/local/bin/neuron/plugins 目录下。

### 拷贝驱动配置 .json 文件

将 modbus/modbus-tcp.json 文件拷贝到 /usr/local/bin/neuron/plugins/schema 目录下。

### 修改 plugins.json 文件

打开 /usr/local/bin/neuron/persistence 目录下的 plugins.json 文件，将新添加的驱动 .so 文件名称添加进去。

### 启动 Neuron 验证驱动

回到 /usr/local/bin/neuron 目录下，执行以下指令，运行 Neuron。

```bash
sudo ./neuron --log
```

在网页打开 Neuron 查看添加的插件及其使用。
