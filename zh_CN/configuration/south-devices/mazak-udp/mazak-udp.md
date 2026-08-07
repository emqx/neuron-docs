# Mazak CNC

Mazak CNC 插件通过被动 UDP 监听方式采集 Mazak CNC 的实时运行数据。Mazak CNC 通过 UDP 发送状态数据包，插件将数据包中的各个字段解析为独立的数据点位。该驱动不会向 CNC 发送任何请求，仅监听传入的 UDP 数据。

::: tip
Mazak CNC 插件为只读插件，仅支持数据采集（读取），不支持反向控制（写入）。
:::

## 添加插件

在 **配置 -> 南向设备**，点击**添加设备**来创建设备节点，输入插件名称，插件类型选择 **Mazak CNC** 启用插件。

## 设备配置

点击插件卡片或插件列，进入**设备配置**页。配置 Neuron 与设备建立连接所需的参数，下表为插件相关配置项。

| <div style="width:100pt">参数</div> | 说明                                                                |
| ----------------------------------- | ------------------------------------------------------------------- |
| **Bind IP**                         | 绑定 UDP 监听的本地 IP 地址。默认为 `0.0.0.0`（监听所有网络接口）。 |
| **Port**                            | 监听的 UDP 端口号，取值 1~65535。默认为 `51001`。                   |
| **连接超时时间 (ms)**               | UDP 接收超时时间，取值 1~60000。默认为 `3000`。                     |

## 设置组和点位

完成插件的添加和配置后，要建立设备与 Neuron 之间的通信，首先为南向驱动程序添加组和点位。

完成设备配置后，在**南向设备**页，点击设备卡片/设备列进入**组列表**页。点击**创建**来创建组，设定组名称以及采集间隔。完成组的创建后，点击组名称进入**点位列表**页，添加需要采集的设备点位，包括点位地址，点位属性，数据类型等。

公共配置项部分可参考[连接南向设备](../south-devices.md)，本页将介绍支持的数据类型和地址格式部分。

::: tip
Mazak CNC 插件仅支持点位属性为**只读**。所有点位地址均为扁平字符串名称，不区分数据区域或索引。
:::

### 数据类型

* STRING
* INT32

### 地址格式

Mazak CNC 插件定义了固定的点位地址集合，每个地址对应从 UDP 数据包中解析出的特定字段。

| 地址              | 数据类型 | 属性 | 说明                                                   |
| ----------------- | -------- | ---- | ------------------------------------------------------ |
| machine_name      | STRING   | 只读 | 机床名称                                               |
| machine_ip        | STRING   | 只读 | 机床 IP 地址                                           |
| status            | STRING   | 只读 | 机床状态（STOPPED, ACTIVE, FEED_HOLD）                 |
| mode              | STRING   | 只读 | 操作模式（AUTOMATIC, MANUAL_DATA_INPUT, MANUAL, EDIT） |
| program_number    | STRING   | 只读 | 当前程序号                                             |
| program_name      | STRING   | 只读 | 当前程序名称                                           |
| subprogram_number | STRING   | 只读 | 当前子程序号                                           |
| subprogram_name   | STRING   | 只读 | 当前子程序名称                                         |
| alarm_number      | STRING   | 只读 | 报警编号                                               |
| alarm_message     | STRING   | 只读 | 报警信息文本                                           |
| alarm_fore_color  | STRING   | 只读 | 报警前景色                                             |
| alarm_back_color  | STRING   | 只读 | 报警背景色                                             |
| part_count        | INT32    | 只读 | 加工计件数                                             |
| tool              | STRING   | 只读 | 当前刀具标识                                           |
| rapid_rate        | INT32    | 只读 | 快移倍率                                               |
| feed_sp_rate      | INT32    | 只读 | 进给/主轴倍率                                          |
| feed_rate          | INT32    | 只读 | 进给速率                                           |

#### 状态值

`status` 地址返回以下字符串值之一：

| 值        | 含义         |
| --------- | ------------ |
| STOPPED   | 机床已停止   |
| ACTIVE    | 机床正在运行 |
| FEED_HOLD | 进给保持     |
| UNKNOWN   | 未知状态     |

#### 模式值

`mode` 地址返回以下字符串值之一：

| 值                | 含义                    |
| ----------------- | ----------------------- |
| AUTOMATIC         | 自动操作模式            |
| MANUAL_DATA_INPUT | MDI（手动数据输入）模式 |
| MANUAL            | 手动操作模式            |
| EDIT              | 程序编辑模式            |
| UNKNOWN           | 未知操作模式            |

### 地址示例

| 地址           | 数据类型 | 说明         |
| -------------- | -------- | ------------ |
| machine_name   | STRING   | 机床名称     |
| status         | STRING   | 机床状态     |
| mode           | STRING   | 操作模式     |
| program_number | STRING   | 当前程序号   |
| alarm_number   | STRING   | 报警编号     |
| alarm_message  | STRING   | 报警信息文本 |
| part_count     | INT32    | 加工计件数   |
| tool           | STRING   | 当前刀具标识 |
| rapid_rate     | INT32    | 快移倍率     |
| feed_rate      | INT32    | 进给速率     |

## 数据监控

完成点位的配置后，您可点击 **监控** -> **数据监控**查看设备信息，具体可参考[数据监控](../../../admin/monitoring.md)。
