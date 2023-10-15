# 配置管理

Neuron 支持通过`命令行`、`环境变量`、`配置文件`的方式，对Neuron的配置参数进行修改，可以提供更加灵活的启动和运行方式。
如果同时配置了`命令行`、`环境变量`、`配置文件`，三者的优先级关系为：命令行>环境变量>配置文件

## 命令行

![cli_info](./assets/cli_info.png)

## 环境变量

Neuron 支持在启动过程中读取环境变量来配置启动参数，目前支持的环境变量如下:

| 配置名                  | 配置作用                                                                      |
| ---------------------- | --------------------------------------------------------------------------- |
| NEURON_DAEMON          | 设置为1，Neuron 守护进程运行；设置为0，Neuron 正常运行                             |
| NEURON_LOG             | 设置为1，Neuron Log输出到标准输出stdout；设置为0，Neuron Log不输出到标准输出stdout； |
| NEURON_LOG_LEVEL       | Neuron日志输出等级，可设置为DEBUG或NOTICE                                        |
| NEURON_RESTART         | Neuron重启设置，可设置为never，always，on-failure或者NUMBER（1,2,3,4）            |
| NEURON_DISABLE_AUTH    | 设置为1，Neuron 关闭Token鉴权认证；设置为0，Neuron 开启Token鉴权认证                |
| NNEURON_CONFIG_DIR     | Neuron配置文件目录                                                             |
| NEURON_PLUGIN_DIR      | Neuron插件文件目录                                                             |


## 配置文件

Neuron提供 json 格式配置文件配置Neuron相关个性化参数，目前支持 ip，port 和 disable_auth 三个配置项目，配置文件路径为neuron安装目录config/neuron.json。默认配置内容如下:
```json
{
    "ip": "0.0.0.0",
    "port": 7000,
    "disable_auth": 0
}
```
