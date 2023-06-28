# 概览

## 参数配置

| Parameter | Description                               |
| --------- | ----------------------------------------- |
| **host**  | KNXnet/IP 设备 ip, 默认224.0.23.12          |
| **port**  | KNXnet/IP 设备端口, 默认3671               |

注意如果使用多拨地址*224.0.23.12*进行配置，通常要求设备与 Neuron 部署在同一网段中。

由于 KNXnet/IP 协议的工作原理，如果使用虚拟化技术如虚拟机或 docker 部署 Neuron，KNX 插件可能
无法正常工作。如果是在 Linux 主机中使用 docker 镜像部署 Neuron，那么需要使用 docker 选项`--net=host`。
在其他情况下，推荐您使用二进制安装包部署 Neuron。

## 支持的数据类型

* BIT
* BOOL
* INT8
* UINT8
* INT16
* UINT16
* FLOAT

## 地址格式用法

### 地址格式

* > GROUP_ADDRESS,INDIVIDUAL_ADDRESS</span>

表示一个 KNX 设备地址及其所属的组地址。进行读操作时，KNX 插件发送`GroupValueRead`
隧道请求，在收到匹配设备地址的`GroupValueResp`报文时更新点位数据。
进行写操作时， KNX 插件发送一个`GroupValueWrite`隧道请求报文。

*例子：*

`0/0/1,1.1.1` 代表 KNX 组地址 `0/0/1`下的设备地址 `1.1.1`。

</br>
</br>
* > GROUP_ADDRESS,INDIVIDUAL_ADDRESS,BIT</span>

与上相同，但为读取比特位数少于8的`uint8`类型数据时使用，如 KNX data point 类型`B2`和`B1U3`等。
其中*BIT*表示数据比特位数。

*例子：*

`0/0/1,1.1.1,2` 代表 KNX 组地址 `0/0/1`下的设备地址 `1.1.1`，数据为两个比特。
