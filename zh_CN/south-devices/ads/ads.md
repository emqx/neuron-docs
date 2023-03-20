# Beckhoff ADS 介绍与使用

## 模块描述

通过ads插件可以连接Beckhoff ADS/AMS设备.

## 参数设置

| 字段            | 说明                                                         |
| --------------- | ------------------------------------------------------------ |
| host            | 远程设备IP.                                                  |
| port            | 远程设备TCP端口（默认48898）.                                |
| src-ams-net-id  | 运行neuron的设备的AMSNetId.                                  |
| src-ads-port    | 运行neuron的设备的AMSPort.                                   |
| dst-ams-net-id  | 目标PLC的AMSNetId.                                           |
| dst-ads-port    | 目标PLC的AMSPort.                                            |

请注意，为了让neuron能与PLC正常通信，需要在目标TC runtime (PLC) 中添加和设置对应的
ADS路由.

## 支持的数据类型

* BOOL
* INT8
* UINT8
* INT16
* UINT16
* INT32
* UINT32
* INT64
* UINT64
* FLOAT
* DOUBLE
* STRING

## 地址格式用法

### 地址格式

> INDEX_GROUP,INDEX_OFFSET</span>

`INDEX_GROUP`和`INDEX_OFFSET`可以分别独立使用十进制或十六进制指定.

### 地址示例

| 地址            | 数据类型           | 说明                        |
| --------------- | ------------------ | --------------------------------------------------------- |
| 0x4040,0x7d01c  | bool               | index_group 0x4040, index_offset 0x7d01c                  |
| 16448,51029     | uint8              | index_group 0x4040, index_offset 0x7d01d                  |
| 0x4040,512896.5 | string             | index_group 0x4040, index_offset 0x7d380, 字符串长度为5   |
