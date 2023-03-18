# OPC DA

Neuron 可通过外部辅助程序 neuopc.exe 间接访问运行于 Windows 操作系统的 OPCDA 服务器。neuopc 通过将 DA 协议转换为 UA 协议，再通过 Neuron已有的 opcua driver 进行数据获取，DA 的所有可访问点位都被映射至 UA 的"命名空间2"当中，点位的 ID 则与 DA 保持一致。

## 设备配置

neuopc 的组件包可以前往 neuopc 的[项目页面](https://github.com/neugates/neuopc)下载（neuopc是GPL协议下的开源项目）。安装以及远程连接的系统配置参考 [neuopc 运行环境设置](./neuopc/neuopc.md)。

![neuopc-setting](./neuopc/assets/neuopc-setting.png)

### neuopc 配置

| 字段        | 说明                                                         |
| ----------- | ------------------------------------------------------------ |
| DA Host     | 需要连接目标主机标识，可以是目标 IP 或者 Hostname，本机可以不设置 |
| DA Server   | DA 服务器的名称，如"Matrikon.OPC.Simulation.1"，填写 DA Host 之后可以点击下拉按钮尝试获取 Server 列表 |
| UA Port     | UA 服务器的监听端口设置，默认 `48401`                        |
| UA User     | UA 服务器的授权访问用户名，默认 `admin`                      |
| UA Password | UA 服务器的访问密码，默认 `123456`                           |

步骤：

1. 填写 DA Host，可以填写 IP 或 Hostname，不填写则默认为本机；
2. 尝试点击 DA Server 的下拉按钮，可以尝试获取目标 Host 的 DA Server 列表，如果下拉为空则说明检测不到任何目标主机上的 DA Server；
3. 点击 Connect 按钮，服务器连接成功后会显示当前 DA Server 的所有可获取的测点信息，状态栏会出现当前服务器的连接信息，如图示8；
4. 设置 UA Port；
5. 设置 UA User；
6. 设置 UA Password；
7. 点击 Run 按钮，UA 服务器启动后，所有列表中的测点都会被映射到 UA Server 的 NeuOPC 目录下，所有测点的 UA namespace 为2，此时 UA 的相关设置项目会变为不可设置状态；
8. 通过鼠标双击 neuopc 测点列表的 Name 列可将对应的测点名称复制到剪贴板中，然后在 neuron 的 tag 表单中粘贴。

### Neuron opcua 连接配置

| 字段         | 说明                                                  |
| ------------ | ----------------------------------------------------- |
| endpoint url | neuopc 的访问地址，默认是`opc.tcp://127.0.0.1:48401/` |
| username     | neuopc 的授权用户名                                   |
| password     | neuopc 的访问密码                                     |

步骤：

1. 在 neuron 南向设备管理中添加一个 opcua 设备；
2. 在设备配置中修改 endpoint url 为 neuopc 的 UA Server 地址；
3. 在设备配置中填写 Username，与 neuopc 中设置的一致；
4. 在设备配置中填写 Password，与 neuopc 中设置的一致；
5. 无需填写 Cert 和 Key，直接提交设置表单。

## 支持的数据类型

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

## 地址格式用法

### 地址格式

> IX!NODEID</span>

**IX** 名字空间索引，访问 neuopc 时，IX只能为2。

**NODEID** 节点 ID，与 DA 服务器中的字符串一致。

### 地址示例

| 地址                   | 数据类型 | 说明                                                         |
| ---------------------- | -------- | ------------------------------------------------------------ |
| 2!Bucket Brigade.UInt2 | UINT16   | 获取类型为 UINT16 的数据点；NS 为2，NODEID 为 Bucket Brigade.UInt2 |