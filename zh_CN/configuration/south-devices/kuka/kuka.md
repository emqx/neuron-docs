# 概览

Neuron KUKA Ethernet KRL TCP 插件通过 TCP 协议访问安装有 KUKA Ethernet KRL 模块的 KUKA 机器人设备，目前支持机器人设备 Server 模式，Neuron KUKA 插件作为 Client 主动连接。

## 设备设置

| 字段 | 说明                  |
| ---- | --------------------- |
| host | 设备 IP 地址          |
| port | 设备端口号, 默认 5000 |

## 支持的数据类型

* uint8
* int8
* uint16
* int16
* uint32
* int32
* uint64
* int64
* float
* double
* bool
* string

## KUKA Ethernet KRL 脚本设置
现场机器人设备需要提前安装好 KUKA Ethernet KRL 模块，Neuron 提供机器人设备端 TCP Server 脚本编写示例。获取脚本和配置文档，可直接 [联系我们](https://www.emqx.com/zh/contact?product=neuron)。

## ADDRESS
插件地址为 XML XPATH 形式.

## 地址示例

| 地址                    | 数据类型 | 说明          |
| ----------------------- | -------- | ------------- |
| /RobotState/Current/@A1 | float    | A1 轴实时电流 |
| /RobotState/Current/@A2 | float    | A2 轴实时电流 |
| /RobotState/Torque/@A1  | float    | A1 轴实时扭矩 |
| /RobotState/Torque/@A2  | float    | A2 轴实时扭矩 |
| /RobotState/Err/@number | int32    | 错误编号      |

