# IEC61850

IEC61850 是一种国际通信标准协议，通过对设备的一系列规范化，达到了全站的通讯统一。 IEC61850 广泛应用于电力行业。

MMS 报文规范运用在 IEC61850 标准站控层和间隔层之间，MMS 通过对实际设备进行面向对象建模方法，实现了网络环境下不同制造设备之间的互操作。

IEC61850 插件用于对 IEC61850 服务器的读/写，目前支持 MMS 协议的访问。

## 添加插件

在 **配置 -> 南向设备**，点击**添加设备**来创建设备节点，输入插件名称，插件类型选择 **IEC61850** 启用插件。

## 设备配置

点击插件卡片或插件列，进入**设备配置**页。配置 IEC61850 驱动与设备建立连接所需的参数，下表为插件相关的配置项。

|  参数    | 说明                       |
| -------- | -------------------------- |
| **设备 IP 地址** | 目标设备 IP              |
| **设备端口** | 目标设备端口号，默认为 102 |
| **总召唤间隔** | 设备发送总召唤的间隔，为 0 时关闭总招，单位秒 |

## 设置组和点位

完成插件的添加和配置后，要建立设备与驱动之间的通信，首先为南向驱动程序添加组和点位。

IEC61850 插件只支持通过导入 SCL 文件自动添加组与点位，SCL 文件中的 Report 块生成可读性数据组，根据引用的 DataSet 生成点位；根据 FC 为 CO、SP、SG 的数据生成可写点位，可写点位单独在一个 Control 组中。

IEC61850 插件根据行业规范，单独定义了数据上报结构，在每个数据点位中，除了点位值外，还包含 timestamp、quality 字段。

```json
{
 "timestamp": 1647497389075,
 "node": "iec61850",
 "group": "grp1",
 "tags": [{
   "name": "tag1",
   "value": 123,
   "q": 3,
   "t": 129401039041
  },
  {
   "name": "tag2",
   "value": 123,
   "q": 3,
   "t": 129401039088
  }
 ]
}
```

::: tip 注意

由于 IEC61850 插件采用特殊数据上报结构，所以在北向插件选择数据格式时，需要对应选择 **Tags-format** 格式。
:::

## 应用场景

您可通过 Neuron IEC61850 插件接入 LibIEC61850 服务器，具体步骤，见 [libiec61850](libiec61850.md)。

## 数据监控

完成点位的配置后，您可点击 **监控** -> **数据监控**查看设备信息以及反控设备，具体可参考[数据监控](../../../admin/monitoring.md)。

## 通过 MQTT 触发总招

topic: action/req

```json
{
  "uuid": "123456",
  "node": "iec61850",
  "action": "GI"
}
```

topic: action/resp

```json
{
  "uuid": "123456",
  "error": 0
}
```

## 通过 MQTT 获取文件列表

topic: flist/req

```json
{
  "uuid": "123456",
  "node": "iec61850",
  "path": "path"
}
```

topic: flist/resp

```json
{
  "uuid": "123456",
  "files": [
    {
      "name": "file1",
      "size": 123,
      "t": 1234567890,
      "type": 1
    },
    {
      "name": "dir1",
      "size": 0,
      "t": 1234567890,
      "type": 2
    }
  ]
}
```

## 通过 MQTT 上传文件

topic: fup/req

```json
{
  "uuid": "123456",
  "node": "iec61850",
  "path": "path"
}
```

topic: fup/resp

```json
{
  "uuid": "123456",
  "error": 0,
  "size": 123
}
```

topic: fupdata/req

```json
{
  "uuid": "123456",
  "node": "iec61850",
  "path": "path"
}
```

topic: fupdata/resp

```json
{
  "uuid": "123456",
  "error": 0,
  "more": true,
  "data": [1,2,3,4]
}
```

## 通过 MQTT 下载文件

topic: fdown/req

```json
{
  "uuid": "123456",
  "node": "iec61850",
  "src path": "src path",
  "dst path": "dst path",
  "size": 123
}
```

topic: fdown/resp

```json
{
  "uuid": "123456",
  "error": 0
}
```

topic: fdowndata/req

```json
{
  "uuid": "123456",
  "node": "iec61850",
  "src path": "src path",
  "more": true,
  "data": [1,2,3,4]
}
```

topic: fdowndata/resp

```json
{
  "uuid": "123456",
  "node": "iec61850",
  "path": "path"
}
```