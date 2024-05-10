# CODESYS V3 TCP

Neuron CODESYS V3 TCP 插件通过 TCP 协议访问基于 CODESYS V3 平台打造的 PLC 和 运动控制系统。

## 设备设置

| 字段     | 说明                                 |
| -------- | ------------------------------------ |
| host     | 设备 IP 地址                         |
| port     | 设备端口, 默认 11740                 |
| timeout  | 请求发送接收超时时间, 默认 3000 毫秒 |
| username | 设备用户名                           |
| password | 设备密码                             |


## 支持的数据类型

* uint8
* int8
* uint16
* int16
* uint32
* int32
* float
* bool
* string

类型对应表

| CODESYS V3 | Neuron |
| ---------- | ------ |
| Bool       | bool   |
| Byte       | uint8  |
| SInt       | int8   |
| USInt      | uint8  |
| Word       | uint16 |
| Int        | int16  |
| UInt       | uint16 |
| DWord      | uint32 |
| DInt       | int32  |
| Real       | float  |
| UDInt      | uint32 |
| String     | string |


## ADDRESS
> TAG NAME

CODESYS V3 平台导出的符号配置，即为 Nueron 的点位地址。


## 地址示例

| 地址                               | 数据类型 | 说明                                           |
| ---------------------------------- | -------- | ---------------------------------------------- |
| Application.PLC_PRG.ok             | bool     | bool 标志位                                    |
| Application.PLC_PRG.d1arr[1]       | int16    | 一维数组下标 1 的值                            |
| Application.PLC_PRG.d2arr[1,1]     | int32    | 二维数组下标 1,1 的值                          |
| Application.PLC_PRG.d3arr[1,1,1]   | int16    | 三维数组下标 1,1,1 的值                        |
| Application.PLC_PRG.point.Y        | float    | 结构体 Point 的 Y 变量值                       |
| Application.PLC_PRG.points[1].Name | string   | 结构体 Point 的数组下标 1 的对象的 Name 变量值 |

