# 概览

Neuron 可通过外部辅助程序 neuopc.exe 间接访问运行于 Windows 操作系统的 OPC DA 服务器。NeuOPC 通过将 DA 协议转换为 UA 协议，再通过 Neuron已有的 OPC UA 插件进行数据获取，DA 的所有可访问点位都被映射至 UA 的"命名空间2"当中，点位的 ID 则与 DA 保持一致。

NeuOPC 的组件包可以前往 NeuOPC 的[项目页面](https://github.com/neugates/neuopc)下载（NeuOPC 是GPL协议下的开源项目）。安装以及远程连接的系统配置参考 [NeuOPC 安装](./install.md)和 [NeuOPC 远程访问](./remote.md)。

## 参数 

### NeuOPC 参数

|  参数       | 说明                                                         |
| ----------- | ------------------------------------------------------------ |
| DA Host     | 需要连接目标主机标识，可以是目标 IP 或者 Hostname，本机可以不设置 |
| DA Server   | DA 服务器的名称，如"Matrikon.OPC.Simulation.1"，填写 DA Host 之后可以点击下拉按钮尝试获取 Server 列表 |
| UA Port     | UA 服务器的监听端口设置，默认 `48401`                        |
| UA User     | UA 服务器的授权访问用户名，默认 `admin`                      |
| UA Password | UA 服务器的访问密码，默认 `123456`                           |

### Neuron opcua 参数

|  参数        | 说明                                                  |
| ------------ | ----------------------------------------------------- |
| 端点 URL     | NeuOPC 的访问地址，默认是`opc.tcp://127.0.0.1:48401/` |
| 用户名       | NeuOPC 的授权用户名                                   |
| 密码         | NeuOPC 的访问密码                                     |

## 数据类型

* INT8（用于表示 SBYTE 类型）
* INT16
* INT32
* INT64
* UINT8（用于表示 BYTE 类型）
* UINT16
* UINT32（同时用于表示 DATETIME 类型）
* UINT64
* FLOAT
* DOUBLE
* BOOL
* STRING

## 地址格式

> IX!NODEID</span>

**IX** 名字空间索引，访问 NeuOPC 时，IX 只能为2。

**NODEID** 节点 ID，与 DA 服务器中的字符串一致。

## 地址示例

| 地址                   | 数据类型 | 说明                                                         |
| ---------------------- | -------- | ------------------------------------------------------------ |
| 2!Bucket Brigade.UInt2 | UINT16   | 获取类型为 UINT16 的数据点；NS 为2，NODEID 为 Bucket Brigade.UInt2 |