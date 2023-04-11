# SDK-based Driver Development

This article mainly introduces how to develop a new driver plugin based on the SDK package and apply it to Neuron.

## Step 1 Download and install the SDK

Download link: [https://github.com/emqx/neuron/releases](https://github.com/emqx/neuron/releases)

According to different development systems, download the corresponding sdk tar.gz package, e.g. neuron-sdk-2.1.3-linux-amd64.tar.gz to the corresponding development system and decompress it to obtain neuron-sdk-x.x.x, where x.x.x represents the version number, execute the following command.

```bash
# take version 2.3.0 as an example
$ cd neuron-sdk-2.3.0
# install sdk
$ sudo ./sdk-install.sh
```

After the script is executed, you need to pay attention to the usage of the following paths.

| Path                      | Description                            |
| --------------------------| ------------------------------------------------------------------------------------------------------------------- |
| /usr/local/include/neuron | Stores Neuron header files and apply to include_directories in the CMakeLists.txt compilation file                   |
| /usr/local/lib/neuron     | Stores Neuron dependent library files, which are applied to link_directories in the CMakeLists.txt compilation file |
| /usr/local/bin/neuron     | Holds files needed to run Neuron             |

## Step 2 Driver development

Create a new directory file in the development environment to store the files required for the development driver, create a compilation configuration file CMakeLists.txt under the directory file, a build directory file to store the compiled files and a plugins directory file for To store all the driver files that need to be developed, each driver needs to have an independent directory to store the required files for driver development. Taking the development of modbus-tcp driver plug-in as an example, the directory level is shown in the figure below.

![driver-tree](./assets/driver-tree.png)

### CMakeLists.txt example

The main thing is that include_directories, link_directories and add_subdirectory should be configured correctly.

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

The driver development file mainly includes the compilation configuration file CMakeLists.txt, the driver configuration json file and the driver code file.

#### CMakeLists.txt example

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

The interface file of the driver plugin, for the specific driver development example, please refer to [modbus plugin development example](./sdk-example/modbus-example.md).

static const neu_plugin_intf_funs_t plugin_intf_funs structure description.

| Parameters           | Description                       |
| -------------------- | --------------------------------- |
| .open                | The first function called by neuron when creating a node based on the plugin, create a struct neu_plugin defined by the plugin itself |
| .close               | The last function called by neuron when a node is removed to release the neu_plugin_t created by open |
| .init                | When creating a node, after neuron calls open, the function called immediately after that. This function is mainly used for some resources that need to be initialized in the plugin |
| .uninit              | The function that neuron calls first when deleting a node. This function mainly releases some resources applied and initialized in init |
| .start               | On the node page, set the job status to start, neuron will call this function to notify the plugin to start running, and start connecting to the device |
| .stop                | On the node page, set the working status to stop, neuron will call this function to notify the plugin to stop running, close the connection with the device, and driver.group_timer will no longer trigger |
| .setting             | On the node page, when the plugin is set, the parameters will be set in json format, and neuron will notify the plugin to set through this function |
| .request             | This function has not been used in the development of southbound driver |
| .driver.validate_tag | When a node adds or updates a tag, neuron will use this function to notify the plug-in of the relevant parameters of the tag. The plug-in checks whether the tag meets the requirements of the plug-in according to its own implementation. The function returns 0, which means success |
| .driver.group_timer  | When a group is added to a node and the node status is running, this function will be called periodically to read device data with the interval parameter of the group |
| .driver.write_tag    | When using the write API, neuron calls this function to notify the plugin to write a specific value to the point tag |

Dynamic library export data structure definition const neu_plugin_module_t neu_plugin_module Description.

| Parameters        | Description                 |
| ----------------- | --------------------------- |
| version           | Plugin version number       |
| module_name       | module name                 |
| module_descr      | Module description          |
| intf_funs         | Plugin interface function   |
| kind              | Plugin type                 |
| type              | The type of node when the plugin is instantiated as node |

The struct neu_plugin structure is the pre-name of the plugin. Each plugin needs to provide the specific definition of the structure, and the first member must be common, and other members are added according to the driver's configuration.

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

The driver configuration file.

| Field         | Description |
| ------------- | ----------------------------------------------------- |
| tag_regex     | Regex for address configuration for drivers that support different data types |
| description   | A detailed description of the field                |
| attribute     | The attribute of the field, there are only two optional and required options, namely required and optional |
| type          | The type of the field, currently int and string are commonly used  |
| default       | The default value to fill in      |
| valid         | The range that this field can be filled in  |

:::tip
The name of the json file should be the same as the module name module_name.
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

After the driver development code is completed, execute compilation in this directory.

```bash
$ cmake ..
$ make
```

## Step 3 The plugin is applied to Neuron

### Copy the driver .so file

After compiling, go to modbus/build/plugins and copy the generated driver .so file (for example, libplugin-modbus-tcp.so ) to the /usr/local/bin/neuron/plugins directory.

### Copy the driver configuration .json file

Copy the modbus/modbus-tcp.json file to the /usr/local/bin/neuron/plugins/schema directory.

### Modify plugins.json file

Open the plugins.json file in the /usr/local/bin/neuron/persistence directory and add the name of the newly added driver .so file to it.

### Start Neuron verification driver

Go back to the /usr/local/bin/neuron directory and execute the following command to run Neuron.

```bash
$ sudo ./neuron --log
```

Open Neuron on the web page to view the added plugins and their usage.
