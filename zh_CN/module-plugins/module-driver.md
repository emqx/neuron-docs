# 模块配置

本节主要介绍了北向应用和南向设备的参数配置，南向设备的点位信息配置规范。

::: tip
uint16 对应 word 类型。uint32 对应 dword 类型。
:::

## Monitor

Neuron内置监控插件。

### Parameter Setting

| Parameter              | Description                                                  |
| ---------------------- | ------------------------------------------------------------ |
| **client-id**          | MQTT通信的客户端id，必填。（默认为节点名）                   |
| **heartbeat-interval** | 心态报文上报周期（每秒），设为零则禁用心跳上报。             |
| **heartbeat-topic**    | 心跳报文上报的主题, 必填。                                   |
| **host**               | MQTT Broker 主机，必填。                                     |
| **port**               | MQTT Broker 端口号，必填。                                   |
| **username**           | 连接到 Broker 时使用的用户名，选填。                         |
| **password**           | 连接到 Broker 时使用的密码，选填。                           |
| **ssl**                | 是否启用 mqtt ssl，选填，默认 false                          |
| **ca**                 | ca文件，只在ssl值为true时启用，这种情况下为必填。            |
| **cert**               | cert文件，只在ssl值为true时启用，选填。                      |
| **key**                | key文件，只在ssl值为true时启用，选填。                       |
| **keypass**            | key文件密码，只有在ssl值为true时启用，选填。                 |

### 心跳报文

心跳报文会发布到设定的主题**heartbeat-topic**，间隔每**heartbeat-interval**秒。

心跳报文格式如下：

```json
{
  "version": "2.1.0",
  "timestamp": 1658134132237,
  "states": [
    {
      "node": "mqtt-client",
      "link": 2,
      "running": 3
    },
    {
      "node": "fx5u-client",
      "link": 2,
      "running": 3
    }
  ]
}
```

## MQTT

Neuron 从设备采集到的数据可以通过 MQTT 应用程序传输到 MQTT Broker 中，用户也可以通过 MQTT 应用程序向 Neuron 发送指令。

### 应用配置

| 字段                | 说明                                                         |
| ------------------- | ------------------------------------------------------------ |
| **client-id**       | MQTT通信的客户端id，必填。（默认为节点名）                   |
| **upload-topic**    | 订阅数据上报的主题，必填。                                   |
| **format**          | 上报数据的json格式选择，选填，有values模式和tags模式，默认为values模式 |
| **cache-mem-size**  | 通信失败时内存消息缓存大小(MB)限制，必填。范围在[0, 1024], 默认 0。 须不大于*cache-disk-size*。|
| **cache-disk-size** | 通信失败时磁盘消息缓存大小(MB)限制，必填。范围在[0, 10240], 默认 0。设为非零值时, *cache-mem-size*也须为非零值。|
| **host**            | MQTT Broker 主机，必填。                                     |
| **port**            | MQTT Broker 端口号，必填。                                   |
| **username**        | 连接到 Broker 时使用的用户名，选填。                         |
| **password**        | 连接到 Broker 时使用的密码，选填。                           |
| **ssl**             | 是否启用 mqtt ssl，选填，默认 false                          |
| **ca**              | ca文件，只在ssl值为true时启用，这种情况下为必填。            |
| **cert**            | cert文件，只在ssl值为true时启用，选填。                      |
| **key**             | key文件，只在ssl值为true时启用，选填。                       |
| **keypass**         | key文件密码，只有在ssl值为true时启用，选填。                 |

## Modbus

Modbus 协议包括三种协议：Modbus TCP、Modbus RTU 和 Modbus RTU over TCP。三种协议除了设备配置方式不一致外，支持的数据类型及地址格式都一致。

### Modbus TCP / Modbus RTU over TCP 设备配置

| 字段                  | 说明                                                    |
| -------------------- | ------------------------------------------------------- |
| **connection mode** | 驱动程序连接到设备的方式，默认为 client，即把 Neuron 作为客户端使用 |
| **host**            | 当 Neuron 作为客户端使用时，host 指远程设备的 IP。当 Neuron 作为服务端使用时，host 指 Neuron 在本地使用的 IP，默认可填写 0.0.0.0  |
| **port**            | 当 Neuron 作为客户端使用时，post 指远程设备的 TCP 端口。当 Neuron 作为服务端使用时，host 指 Neuron 在本地使用的 TCP 端口，默认为 502  |
| **timeout**         | 向设备发送请求超时时间                                   |

### Modbus RTU 设备配置

| 字段        | 说明                               |
| ----------- | -------------------------------- |
| **device**  | 使用串口设备，例如“/dev/ttyUSB0”    |
| **stop**    | 停止位，默认值是 1                  |
| **parity**  | 校验位，默认值是 2，代表偶校验        |
| **baud**    | 波特率，默认值是 9600               |
| **data**    | 数据位，默认值是 8                  |
| **timeout** | 向设备发送请求超时时间               |

### 支持的数据类型

* INT16
* INT32
* UINT16
* UINT32
* FLOAT
* BIT
* STRING

### 地址格式

> SLAVE!ADDRESS\[.BIT][#ENDIAN]\[.LEN\[H]\[L]\[D]\[E]]</span>

#### **SLAVE**

必填，指从机地址或者是站点号。

#### **ADDRESS**

必填，指寄存器地址。Modbus 协议有四个区域，每个区域最大有 65536 个寄存器，每个区域的地址范围如下表所示。需要注意的是实际应用中一般不需要 65536 这么大的存储区，一般 PLC 厂家普遍采用 10000 以内的地址范围，请注意根据设备的区域及功能码，正确填写点位地址。

| 区域                       | 地址范围          | 属性        | 寄存器大小     | 功能码        | 数据类型 |
| ------------------------- | ---------------- | ---------- | ------------- | ------------ | ------- |
| coil（线圈）                | 000001 ~ 065536 | 读/写       | 1bit          | 0x01,0x05,0x0f | bit     |
| input（离散量输入）          | 100001 ~ 165536 | 读          | 1bit          | 0x02          | bit     |
| input register（输入寄存器） | 300001 ~ 365536 | 读          | 16bit         | 0x04          | bit,int16,uint16,int32,uint32,float,string |
| hold register（保持寄存器）  | 400001 ~ 465536 | 读/写       | 16bit         | 0x03,0x06,0x10 | bit,int16,uint16,int32,uint32,float,string |

::: tip
一些设备文件会使用功能码和寄存器地址来描述指令，因为寄存器地址编号是从 0 开始的，所以每个区域的寄存器地址范围为 0 ～ 65535。首先，根据功能码确定地址的最高位数，并在寄存器地址上加1，作为 Neuron 的使用地址。
:::

例如，功能码是 0x03，寄存器地址是 0，Neuron 使用的地址是 400001。功能码是 0x02，寄存器地址是 5，Neuron 使用的地址是 100006。

#### **.BIT**

选填，一个寄存器地址的某一位，例如：
| 地址         | 数据类型 | 说明                                                |
| ----------- | ------- | --------------------------------------------------- |
| 1!300004.0  | bit     | 指站号为1，离散量输入区域，地址为 300004，第 0 位    |
| 1!400010.4  | bit     | 指站号为1，保持寄存器区域，地址为 400010，第 4 位    |
| 2!400001.15 | bit     | 指站号为2，保持寄存器区域，地址为 400001，第 15 位   |

#### **#ENDIAN**

选填，字节顺序，适用于 int16/uint16/int32/uint32/float 数据类型，详细说明见下表。
| 符号 | 字节顺序 | 支持的数据类型        | 备注 |
| --- | ------- | ------------------ | ----- |
| #B  | 2,1     | int16/uint16       |       |
| #L  | 1,2     | int16/uint16       | 不填，默认字节顺序 |
| #LL | 1,2,3,4 | int32/uint32/float | 不填，默认字节顺序 |
| #LB | 2,1,4,3 | int32/uint32/float | |
| #BB | 3,4,1,2 | int32/uint32/float | |
| #BL | 4,3,2,1 | int32/uint32/float | |

*例子：*

| 地址         | 数据类型  | 说明       |
| ----------- | -------- | --------- |
| 1!300004    | int16    | 指站号为 1，离散量输入区域，地址为 300004，字节顺序为 #L |
| 1!300004#B  | int16    | 指站号为 1，离散量输入区域，地址为 300004，字节顺序为 #B |
| 1!300004#L  | uint16   | 指站号为 1，离散量输入区域，地址为 300004，字节顺序为 #L |
| 1!400004    | int16    | 指站号为 1，保持寄存器区域，地址为 400004，字节顺序为 #L |
| 1!400004#L  | int16    | 指站号为 1，保持寄存器区域，地址为 400004，字节顺序为 #L |
| 1!400004#B  | uint16   | 指站号为 1，保持寄存器区域，地址为 400004，字节顺序为 #B |
| 1!300004    | int32    | 指站号为 1，离散量输入区域，地址为 300004，字节顺序为 #LL |
| 1!300004#BB | uint32   | 指站号为 1，离散量输入区域，地址为 300004，字节顺序为 #BB |
| 1!300004#LB | uint32   | 指站号为 1，离散量输入区域，地址为 300004，字节顺序为 #LB |
| 1!300004#BL | float    | 指站号为 1，离散量输入区域，地址为 300004，字节顺序为 #BL |
| 1!300004#LL | int32    | 指站号为 1，离散量输入区域，地址为 300004，字节顺序为 #LL |
| 1!400004    | int32    | 指站号为 1，保持寄存器区域，地址为 400004，字节顺序为 #LL |
| 1!400004#LB | uint32   | 指站号为 1，保持寄存器区域，地址为 400004，字节顺序为 #LB |
| 1!400004#BB | uint32   | 指站号为 1，保持寄存器区域，地址为 400004，字节顺序为 #BB |
| 1!400004#LL | int32    | 指站号为 1，保持寄存器区域，地址为 400004，字节顺序为 #LL |
| 1!400004#BL | float    | 指站号为 1，保持寄存器区域，地址为 400004，字节顺序为 #BL |

#### .LEN\[H]\[L]\[D]\[E]

当数据类型为 string 类型时，**.LEN** 是必填项，表示字符串需要占用的字节长度，每个寄存器中包含**H**，**L**，**D** 和**E** 四种存储方式，如下列表格所示。
| 符号 | 说明                                  |
| --- | ------------------------------------- |
| H   | 一个寄存器存储两个字节，高字节在前低字节在后 |
| L   | 一个寄存器存储两个字节，低字节在前高字节在后 |
| D   | 一个寄存器存储一个字节，且存储在低字节      |
| E   | 一个寄存器存储一个字节，且存储在高字节      |

*例子：*

| 地址         | 数据类型 | 说明 |
| ----------- | ------- | --------- |
| 1!300001.10  | String  | 指站号为1，离散量输入区域，地址为 300001，字符长度为 10，字节顺序为 L，即占用的地址为 300001 ～ 300005 |
| 1!300001.10H | String  | 指站号为1，离散量输入区域，地址为 300001，字符长度为 10，字节顺序为 H，即占用的地址为 300001 ～ 300005 |
| 1!300001.10L | String  | 指站号为1，离散量输入区域，地址为 300001，字符长度为 10，字节顺序为 L，即占用的地址为 300001 ～ 300005 |
| 1!400001.10  | String  | 指站号为1，保持寄存器区域，地址为 400001，字符长度为 10，字节顺序为 L，即占用的地址为 400001 ～ 400005 |
| 1!400001.10H | String  | 指站号为1，保持寄存器区域，地址为 400001，字符长度为 10，字节顺序为 H，即占用的地址为 400001 ～ 400005 |
| 1!400001.10L | String  | 指站号为1，保持寄存器区域，地址为 400001，字符长度为 10，字节顺序为 L，即占用的地址为 400001 ～ 400005 |
| 1!400001.10D | String  | 指站号为1，保持寄存器区域，地址为 400001，字符长度为 10，字节顺序为 D，即占用的地址为 400001 ～ 400010 |
| 1!400001.10E | String  | 指站号为1，保持寄存器区域，地址为 400001，字符长度为 10，字节顺序为 E，即占用的地址为 400001 ～ 400010 |

## File

File 插件用于读写文件。

### 设备配置

| 字段         | 说明                  |
| ----------- | --------------------- |
| file_length | 设置读写文件内容的字符长度 |

### 支持的数据类型

* STRING

### 地址格式

> FILE PATH</span>

*例子:*

| 地址                      | 数据类型 | 说明                     |
| ------------------------ | ------ | ------------------------ |
| /home/root/test/test.txt | string | 读写 test.txt 文件中的内容 |

:::tip
地址需填写文件的绝对路径。

写操作时，写入的内容将会覆盖之前的文件内容。
:::

## OPC UA

### 设备配置

| 字段               | 说明                      |
| ----------------- | ------------------------- |
| **endpoint url**  | 远程访问 PLC 的地址，默认值是`opc.tcp://127.0.0.1:4840/` |
| **username**      | 连接到 PLC 时，使用的用户名 |
| **password**      | 连接到 PLC 时，使用的密码 |
| **cert**     | 提供登录用户认证的证书 |
| **key**      | 私钥文件，用于提供签名和加密传输 |

认证方式：

* anonymos，需要 OPCUA 服务端开启匿名登录；
* username-password，需要 OPCUA 服务端已经创建好具备访问权限的 username，Neuron 自动会匹配 OPCUA 服务端的安全设置并尝试登录；
* cert-key + anonymos，需要 OPCUA 服务端开启合适的安全设置并设置证书，并且**开启匿名登录**；
* cert-key + username-password，需要 OPCUA 服务端已经创建好具备访问权限的username，并开启合适的安全设置并设置证书；

### 证书设置

OPCUA可通过用户自签名证书登录到 OPC-UA 服务器，certificate 和 key 必须满足以下条件：

* CERTIFICATE 和 KEYFILE 必须同时设置
* Certificate 必须以X.509v3标准生成
* Certficate 的SAN字段必须包含`URI:urn:xxx.xxx.xxx`,“xxx”部分为自定义部分
* Certificate 文件和 Key 文件必须使用DER格式编码

证书文件可以提前导入到目标服务器中并设置为信任，也可以由 neuron 设置后自动提交再由服务端设置为信任。注：老版本的 kepware 或者 IGS 可能需要手动导入证书。

证书生成步骤（Windows/Linux/Mac）：

```sh
openssl req -config localhost.cnf -new -nodes -x509 -sha256 -newkey rsa:2048 -keyout localhost.key -days 365 -subj "/C=DE/O=neuron/CN=NeuronClient@localhost" -out localhost.crt
openssl x509 -in localhost.crt -outform der -out client_cert.der
openssl rsa -inform PEM -in localhost.key -outform DER -out client_key.der
rm localhost.crt
rm localhost.key
```

`-config`指定的 *.cnf 文件可以使用 [openssl 的模版文件](https://github.com/openssl/openssl/blob/master/apps/openssl.cnf) 进行修改，需包含如下配置节：

```sh
[ v3_req ]

# Extensions to add to a certificate request

basicConstraints = CA:FALSE
keyUsage = nonRepudiation, digitalSignature, keyEncipherment
subjectAltName = @alt_names

[ alt_names ]
URI.1 = urn:xxx.xxx.xxx
DNS.1 = localhost
#DNS.2 = localhost
IP.1 = 127.0.0.1
#IP.2 = 0.0.0.0
```

`-days`可以根据需要设置数值。

### 证书转换

可以通过以下步骤和命令将 PEM 证书以及私钥转换为 DER 格式

1. 将包括"-----BEGIN CERTIFICATE-----"和"-----END CERTIFICATE-----"的所有内容保存为1.crt;
2. 将包括"-----BEGIN PRIVATE KEY-----"和"-----END PRIVATE KEY-----"的所有内容保存为1.key;
3. 执行如下命令:

```sh
openssl x509 -in 1.crt -outform der -out cert.der   
openssl rsa -inform PEM -in 1.key -outform DER -out key.der
```

### 支持的数据类型

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

### 地址格式

> IX!NODEID</span>

**IX** 名字空间索引。

**NODEID** 节点 ID，可以设置为数字形式或者字符串形式。

*例子：*

| 地址                   | 数据类型 | 说明                                                         |
| ---------------------- | -------- | ------------------------------------------------------------ |
| 0!2258                 | UINT32   | 使用数字类型的 NODEID，获取 OPCUA 服务器的时间戳；NS 为0，NODEID 为2258 |
| 2!Device1.Module1.Tag1 | INT8     | 使用字符串类型的 NODEID，获取类型为 SBYTE 的数据点；NS 为2，NODEID 为 Device1.Module1.Tag1 |

可以使用 UaExpert 软件协助查看所需点位的名字空间和节点 ID 信息。

::: tip
关于命名空间索引和节点 ID 的解释，请参考 OPC UA 标准。

Neuron 设置的数据类型必须与 OPCUA 数据类型相匹配。

:::

## Siemens S7 ISOTCP

s7comm 插件用于带有网络端口的西门子PLC，如，s7-200/300/400/1200/1500。

### 设备配置

| 字段      | 说明                     |
| -------- | ------------------------ |
| **host** | 远程 PLC 的 IP            |
| **port** | 远程 PLC 的端口，默认为 102 |
| **rack** | PLC 机架号，默认为 0       |
| **slot** | PLC 插槽号，默认为 1       |

::: tip
当使用S7COMM插件访问S7 1200/1500 PLC时，你需要使用西门子软件（TIA16）对PLC进行一些设置。( 详细设置请参考 [PLC 设置](./plc-settings/siemens-s7-1200-1500.md) )
:::

* 优化块访问必须被关闭。
* 访问级别必须是**完全**，**连接机制**必须允许 GET/PUT。

### 支持的数据类型

* INT16
* UINT16
* INT32
* UINT32
* FLOAT
* DOUBLE
* BIT
* STRING

### 地址格式

> AREA ADDRESS\[.BIT][.LEN]</span>

#### AREA ADDRESS

| 区域  | 数据类型                                           | 属性   | 备注         | S7-200 smart |
| ---- | ------------------------------------------------- | ----- | ------------ | ---- |
| I    | int16/uint16/bit                                  | 读    | 输入          | 输入I、E |
| O    | int16/uint16/bit                                  | 读/写 | 输出          | 输出Q、A |
| F    | int16/uint16/bit                                  | 读/写 | 标志          | 标志内存M |
| T    | int16/uint16                                      | 读/写 | 计时器        | 计时器T |
| C    | int16/uint16                                      | 读/写 | 计数器        | 计数器C |
| DB   | int16/uint16/bit/int32/uint32/float/double/string | 读/写 | 全局数据块     | 变量内存V，全局数据块1 |

*例子：*

| 地址 | 数据类型 | 说明 |
| ------ | ------- | -------- |
| I0         | int16   | I 区域，地址为 0 |
| I1         | uint16  | I 区域，地址为 1 |
| O2         | int16   | O 区域，地址为 2 |
| O3         | uint16  | O 区域，地址为 3 |
| F4         | int16   | F 区域，地址为 4 |
| F5         | int16   | F 区域，地址为 5 |
| T6         | int16   | T 区域，地址为 6 |
| T7         | int16   | T 区域，地址为 7 |
| C8         | uint16  | C 区域，地址为 8 |
| C9         | uint16  | C 区域，地址为 9 |
| DB10.DBW10 | int16   | 10 数据块中，起始数据字为 10 |
| DB12.DBW10 | uint16  | 12 数据块中，起始数据字为 10 |
| DB10.DBW10 | float   | 10 数据块中，起始数据字为 10 |
| DB11.DBW10 | double  | 11 数据块中，起始数据字为 10 |

#### .BIT

选填，指某一地址的某一位。

*例子：*

| 地址         | 数据类型 | 说明                    |
| ----------- | ------- | ---------------------- |
| I0.0        | bit     | I 区域，地址为0，第 0 位  |
| I0.1        | bit     | I 区域，地址为0，第 1 位  |
| O1.0        | bit     | O 区域，地址为1，第 0 位  |
| O1.2        | bit     | O 区域，地址为1，第 2 位  |
| F2.1        | bit     | F 区域，地址为2，第 1 位  |
| F2.2        | bit     | F 区域，地址为2，第 2 位  |
| T3.3        | bit     | T 区域，地址为3，第 3 位  |
| T3.4        | bit     | T 区域，地址为3，第 4 位  |
| C4.5        | bit     | C 区域，地址为4，第 5 位  |
| C4.6        | bit     | C 区域，地址为4，第 6 位  |
| DB1.DBW10.1 | bit     | 1 数据块中，起始数据字为 10，第 0 位  |
| DB2.DBW1.15 | bit     | 2 数据块中，起始数据字为 1，第 15 位  |

#### .LEN

当数据类型为 string 类型时，是必填项，表示字符串长度。

*例子：*

| 地址          | 数据类型 | 说明                                    |
| -------------| ------- | -------------------------------------- |
| DB1.DBW12.20 | string  | 1 数据块中，起始数据字为 12，字符串长度为 20 |

## OMRON FINS on TCP

fins插件用于带有网口的欧姆龙 PLC，如 CP2E。

### 设备配置

| 字段 | 说明 |
| -------- | ------------- |
| **host** | 远程 PLC 的 ID |
| **port** | 远程 PLC 的端口，默认为 9600 ｜

### 支持的数据类型

* UINT8
* INT8
* INT16
* UINT16
* INT32
* UINT32
* FLOAT
* DOUBLE
* BIT
* STRING

### 地址格式

> AREA ADDRESS\[.BIT]\[.LEN\[H]\[L]]</span>

#### AREA ADDRESS

| 区域 | 数据类型                                      | 属性     | 备注        |
| ---- | ------------------------------------------- | ------- | ---------- |
| CIO  | 除 uint8/int8 外的所有类型                    | 读/写    | CIO 区     |
| A    | 除 uint8/int8 外的所有类型                    | 读       | 辅助区     |
| W    | 除 uint8/int8 外的所有类型                    | 读/写    | 工作区     |
| H    | 除 uint8/int8 外的所有类型                    | 读/写    | 保持区     |
| D    | 除 uint8/int8 外的所有类型                    | 读/写    | 数据存储区  |
| P    | 除 uint8/int8 外的所有类型，但 bit 只支持读     | 读/写    | PVs        |
| F    | int8/uint8                                  | 读      | 标志区域     |
| EM   | 除 uint8/int8 外的所有类型                    | 读/写    | 扩展内存    |

*例子：*

| 地址         | 数据类型 | 说明                   |
| ----------- | ------- | --------------------- |
| F0          | uint8   | F 区域，地址为 0        |
| F1          | int8    | F 区域，地址为 1        |
| CIO1        | int16   | CIO 区域，地址为 1      |
| CIO2        | uint16  | CIO 区域，地址为 2      |
| A2          | int32   | A 区域，地址为 2        |
| A4          | uint32  | A 区域，地址为 4        |
| W5          | float   | W 区域，地址为 5        |
| W10         | float   | W 区域，地址为 10       |
| H20         | double  | H 区域，地址为 20       |
| H30         | uint32  | H 区域，地址为 30       |
| D10         | int32   | D 区域，地址为 10       |
| D20         | float   | D 区域，地址为 20       |
| EM10W100    | float   | EM10 区域，地址为 100   |

#### .BIT

选填，指某一地址的某一位。

*例子：*

| 地址          | 数据类型 | 说明                         |
| ------------ | ------- | ---------------------------- |
| CIO0.0       | bit     | CIO 区域，地址为 0，第 0 位     |
| CIO1.2       | bit     | CIO 区域，地址为 1，第 2 位     |
| A2.1         | bit     | A 区域，地址为 2，第 1 位       |
| A2.3         | bit     | A 区域，地址为 2，第 3 位       |
| W3.4         | bit     | W 区域，地址为 3，第 4 位       |
| W3.0         | bit     | W 区域，地址为 3，第 0 位       |
| H4.15        | bit     | H 区域，地址为 4，第 15 位      |
| H4.10        | bit     | H 区域，地址为 4，第 10 位      |
| D5.2         | bit     | D 区域，地址为 5，第 2 位       |
| D5.3         | bit     | D 区域，地址为 5，第 3 位       |
| EM10W100.0   | bit     | EM10 区域，地址为 100，第 0 位  |

#### .LEN\[H]\[L]

当数据类型是 string 类型时，是必填项，**.LEN** 表示字符串长度，包含 **H** 和 **L** 两种字节顺序，不填默认是 **H** 字节顺序。

*例子：*

| 地址       | 数据类型  | 说明 |
| --------- | -------- | -------- |
| CIO0.20   | string | CIO 区域，地址为 0，字符串长度 20 个字节，字节顺序为 L  |
| CIO1.20H  | string | CIO 区域，地址为 1，字符串长度 20 个字节，字节顺序为 H  |
| A2.10L    | string | A 区域，地址为 2，字符串长度 10 个字节，字节顺序为 L  |
| A2.30     | string | A 区域，地址为 2，字符串长度 30 个字节，字节顺序为 L  |
| W3.40H    | string | W 区域，地址为 3，字符串长度 40 个字节，字节顺序为 H  |
| W3.10     | string | W 区域，地址为 3，字符串长度 10 个字节，字节顺序为 L  |
| H4.15L    | string | H 区域，地址为 4，字符串长度 15 个字节，字节顺序为 L  |
| H4.10     | string | H 区域，地址为 4，字符串长度 10 个字节，字节顺序为 L  |
| D5.20H    | string | D 区域，地址为 5，字符串长度 20 个字节，字节顺序为 H  |
| D5.30     | string | D 区域，地址为 5，字符串长度 30 个字节，字节顺序为 L  |
| EM10.10   | string | EM 区域，地址为 10，字符串长度 10 个字节，字节顺序为 L  |

## Mitsubishi MELSEC-Q E71

qna3e 插件用于通过以太网访问三菱的QnA兼容PLC，包括Q系列（MC）、iQ-F系列（SLMP）和iQ-L系列。

### 设备配置

| 字段 | 说明 |
| -------- | -------------------------- |
| **host** | 远程 PLC 的 IP 地址        |
| **port** | 远程 PLC 的端口号，默认为 2000 |

### 支持的数据类型

* INT16
* UINT16
* INT32
* UINT32
* FLOAT
* DOUBLE
* BIT
* STRING

### 地址格式

> AREA ADDRESS\[.BIT]\[.LEN\[H]\[L]]</span>

#### AREA ADDRESS

| 区域 |数据类型 | 属性  | 备注                           |
| ---- | --------- | ---------- | -------------------------------- |
| X    | bit       | 读/写 | 输入继电器  (Q/iQ-F)             |
| DX   | bit       | 读/写 | (Q/iQ-F)                         |
| Y    | bit       | 读/写 | 输出继电器 (Q/iQ-F)            |
| DY   | bit       | 读/写 | (Q/iQ-F)                         |
| B    | bit       | 读/写 | 链接继电器 (Q/iQ-F)              |
| SB   | bit       | 读/写 | 链接专用继电器               |
| M    | bit       | 读/写 | 内部继电器 (Q/iQ-F)          |
| SM   | bit       | 读/写 | 特殊寄存器 (Q/iQ-F)           |
| L    | bit       | 读/写 | 锁存器 (Q/iQ-F)             |
| F    | bit       | 读/写 | 信号器 (Q/iQ-F)             |
| V    | bit       | 读/写 | 边缘继电器 (Q/iQ-F)              |
| S    | bit       | 读/写 | (Q/iQ-F)                         |
| TS   | bit       | 读/写 | 定时器触点 (Q/iQ-F)           |
| TC   | bit       | 读/写 | 定时器线圈 (Q/iQ-F)              |
| SS   | bit       | 读/写 | (Q/iQ-F)                         |
| STS  | bit       | 读/写 | 保持定时器触点 (Q/iQ-F)    |
| SC   | bit       | 读/写 | (Q/iQ-F)                         |
| CS   | bit       | 读/写 | 计数器触点 (Q/iQ-F)         |
| CC   | bit       | 读/写 | 计数器线圈 (Q/iQ-F)            |
| TN   | 所有类型   | 读/写 | 定时器当前值 (Q/iQ-F)     |
| STN  | 所有类型   | 读/写 | 保持定时器 (Q/iQ-F)         |
| SN   | 所有类型   | 读/写 | (Q/iQ-F)                         |
| CN   | 所有类型   | 读/写 | 计数器当前值  (Q/iQ-F)  |
| D    | 所有类型   | 读/写 | 数据寄存器 (Q/iQ-F)           |
| DSH  | -- |       |                                  |
| DSL  | -- |      |                                  |
| SD   | 所有类型   | 读/写 | 专用寄存器Specical register (Q/iQ-F)       |
| W    | 所有类型   | 读/写 | 链接寄存器 (Q/iQ-F)           |
| WSH  | -- |      |                                  |
| WSL  | -- |      |                                  |
| SW   | 所有类型   | 读/写 | 链接专用寄存器 (Q/iQ-F)   |
| R    | 所有类型   | 读/写 | 文件寄存器 (Q/iQ-F)           |
| ZR   | 所有类型   | 读/写 | 文件寄存器 File register (Q/iQ-F)           |
| RSH  | -- |  |                                  |
| ZRSH | -- |  |                                  |
| RSL  | -- |  |                                  |
| ZRSL | -- |  |                                  |
| Z    | 所有类型  | 读/写  | 索引寄存器 Index register (Q/iQ-F)          |

*例子：*

| 地址   | 数据类型 | 说明 |
| ----- | ------- | ----- |
| X0    | bit     | X 区域，地址为 0    |
| X1    | bit     | X 区域，地址为 1    |
| Y0    | bit     | Y 区域，地址为 0    |
| Y1    | bit     | Y 区域，地址为 1    |
| D100  | int16   | D 区域，地址为 100  |
| D1000 | uint16  | D 区域，地址为 1000 |
| D200  | uint32  | D 区域，地址为 200  |
| D10   | float   | D 区域，地址为 10   |
| D20   | double  | D 区域，地址为 20   |

#### .BIT

只可用于**非bit类型区域**，表示读取指定地址的指定二进制位，二进制位索引区间为[0, 15]。

| 地址  | 数据类型 | 说明  |
| ------- | --------- | --------- |
| D20.0 | bit | D 区域，地址为 20，第 0 位|
| D20.2 | bit | D 区域，地址为 20，第 2 位|

#### .LEN\[H]\[L]

当数据类型是 string 类型时，**.LEN** 表示的是字符串长度；可以选填 **H**和 **L** 表示两种字节顺序，默认的是 **H** 的字节顺序。

*例子：*

| 地址       | 数据类型 | 说明 |
| --------- | ------- | ----- |
| D1002.16L | string  | D 区域，地址为 1002，字符串长度为 16，字节顺序为 L |
| D1003.16 | string  | D 区域，地址为 1003，字符串长度为 16，字节顺序为 H |

## IEC 60870-5-104

### 设备配置

| 字段 | 说明 |
| ------- | ------------- |
| **host** | 设备 IP |
| **port** | 设备端口号，默认为 2404 |
| **ca** |  公共地址 |
| **interval** | 站点问询时间间隔 |

### 支持的数据类型

* UINT16
* INT16
* FLOAT
* BIT
* UINT8
* INT8

### 地址格式

> IOA</span>

| IEC 60870-5-104  类型 ID         | 数据类型  |
| :------------------------------ | :------------ |
| M_ME_NB_1、M_ME_TE_1            | uint16/int16 |
| M_ME_NC_1、M_ME_TF_1            | float        |
| M_SP_NA_1、M_SP_TB_1            | bit          |
| M_ME_NA_1、M_ME_TD_1、M_ME_ND_1 | uint16/int16 |

## KNXnet/IP

### 设备配置

| Parameter | Description                               |
| --------- | ----------------------------------------- |
| **host**  | KNXnet/IP设备ip, 默认224.0.23.12          |
| **port**  | KNXnet/IP设备端口, 默认3671               |

注意如果使用多拨地址*224.0.23.12*进行配置，通常要求设备与Neuron部署在同一网段中。

由于KNXnet/IP协议的工作原理，如果使用虚拟化技术如虚拟机或docker部署Neuron，KNX插件可能
无法正常工作。如果是在Linux主机中使用docker镜像部署Neuron，那么需要使用docker选项`--net=host`。
在其他情况下，推荐您使用二进制安装包部署Neuron。

### 支持的数据类型

* BIT
* BOOL
* INT8
* UINT8
* INT16
* UINT16
* FLOAT

### 地址格式

代表 KNX 组地址，只能在 Neuron 中写入，属于该组的 KNX 设备将对发送到该组的消息做出响应。

*例子：*

`0/0/1` 是一个 KNX 组地址，只在 Neuron 中写入，属于 `0/0/1` 组的 KNX 设备将对发送到 `0/0/1` 组的消息做出响应。

* > GROUP_ADDRESS,INDIVIDUAL_ADDRESS</span>

表示一个KNX设备地址及其所属的组地址。进行读操作时，KNX插件发送`GroupValueRead`
隧道请求，在收到匹配设备地址的`GroupValueResp`报文时更新点位数据。
进行写操作时， KNX插件发送一个`GroupValueWrite`隧道请求报文。

*例子：*

`0/0/1,1.1.1` 代表 KNX 组地址 `0/0/1`下的设备地址 `1.1.1`。

* > GROUP_ADDRESS,INDIVIDUAL_ADDRESS,BIT</span>

与上相同，但为读取比特位数少于8的`uint8`类型数据时使用，如KNX data point类型`B2`和`B1U3`等。
其中*BIT*表示数据比特位数。

*例子：*

`0/0/1,1.1.1,2` 代表 KNX 组地址 `0/0/1`下的设备地址 `1.1.1`，数据为两个比特。

## BACnet/IP

### 设备配置

| 字段      | 说明                            |
|--------- | ------------------------------ |
| **host** | BACnet 设备的 IP                |
| **port** | BACnet 设备的端口号，默认为 47808 |

### 支持的数据类型

* FLOAT
* BIT

### 地址格式

> AREA ADDRESS</span>

| 区域  | 地址范围      | 属性    | 数据类型 |  备注        |
| ---- | ------------ | ------ | ------- | ----------- |
| AI   | 0 - 0x3fffff | 读     | float   | 模拟输入      |
| AO   | 0 - 0x3fffff | 读/写  | float   | 模拟输出      |
| AV   | 0 - 0x3fffff | 读/写  | float   | 模拟量        |
| BI   | 0 - 0x3fffff | 读     | bit     | 二进制输入     |
| BO   | 0 - 0x3fffff | 读/写  | bit      | 二进制输出    |
| BV   | 0 - 0x3fffff | 读/写  | bit      | 二进制值      |
| MSI  | 0 - 0x3fffff | 读     | bit      | 多状态输入    |
| MSO  | 0 - 0x3fffff | 读/写  | bit      | 多状态输出    |
| MSV  | 0 - 0x3fffff | 读/写  | bit      | 多状态值     |

*例子：*

| 地址    | 数据属性 | 说明              |
| ------ | ------- | ---------------- |
| AI0    | float   | AI 区域，地址为 0  |
| AI1    | float   | AI 区域，地址为 1  |
| BO10   | float   | BO 区域，地址为 10 |
| BO20   | float   | BO 区域，地址为 20 |
| AV30   | float   | AV 区域，地址为 30 |
| BI0    | bit     | BI 区域，地址为 0  |
| BI1    | bit     | BI 区域，地址为 1  |
| BV3    | bit     | BV 区域，地址为 3  |
| MSI10  | bit     | MAI 区域，地址为 10 |
| MSI20  | bit     | MSI 区域，地址为 20 |
| MSI30  | bit     | MSI 区域，地址为 30 |

## DL/T645-2007

dlt645 驱动支持串口和 TCP 连接。

### 设备配置

#### serival

| 字段               | 说明                               |
| ----------------- | -------------------------------- |
| **timeout**       | 向设备发送请求超时时间               |
| **interval**      | 读指令时间间隔，单位为 ms            |
| **device**        | 使用串口设备，例如，/dev/ttyUSB0    |
| **stop**          | 停止位，默认值是 1                  |
| **parity**        | 校验位，默认值是 2，代表偶校验        |
| **baud**          | 波特率，默认值是 9600               |
| **data**          | 数据位，默认值是 8                  |

#### TCP

| 字段                 | 说明                                                    |
| ------------------- | ------------------------------------------------------- |
| **timeout**         | 向设备发送请求超时时间               |
| **interval**        | 读指令时间间隔                      |
| **host**            | 当 Neuron 作为客户端使用时，host 指远程设备的 IP。当 Neuron 作为服务端使用时，host 指 Neuron 在本地使用的 IP，默认可填写 0.0.0.0  |
| **port**            | 当 Neuron 作为客户端使用时，post 指远程设备的 TCP 端口。当 Neuron 作为服务端使用时，host 指 Neuron 在本地使用的 TCP 端口  |
| **connection mode** | 驱动程序连接到设备的方式，默认为 client，即把 Neuron 作为客户端使用 |

### 支持的数据类型

* UIN8
* UINT16
* UINT32
* UIN64

### 地址格式

> mail_address#DI<sub>3</sub>-DI<sub>2</sub>-DI<sub>1</sub>-DI<sub>0</sub> </span>

* mail_address 代表电表的通信地址。
* DI<sub>3</sub>-DI<sub>2</sub>-DI<sub>1</sub>-DI<sub>0</sub> 代表的是数据标识，所有点位只支持读属性，且用十六进制表示。

例如，123456789012#02-01-01-00，代表通信地址为 123456789012 的电表设备的 A 相电压的值。

:::tip
支持一个节点配置多个通信地址的点位，即单串口的多设备连接。

具体的数据标识对应的数据项名称请参考 DL/T645-2007 行业标准的数据编码表格。

* 数据长度为 1，数据类型选择 UINT8；
* 数据长度为 2，数据类型选择 UINT16；
* 数据长度为 3 或 4，数据类型选择 UINT32；
* 数据长度为 5 或 6 或 7 或 8，数据类型选择 UINT64；
* 根据数据格式设置 Decimal 的值，例如数据格式为 XXX.X，则 Decimal 设置为 0.1；
:::

| DI<sub>3</sub> | DI<sub>2</sub>    | DI<sub>1</sub>   | DI<sub>0</sub>   | 说明                             | 数据类型 | Decimal 值 | 举例                                                         |
| -------------- | ----------------- | ---------------- | --------------- | -------------------------------- | ------- | --------- | ------------------------------------------------------------ |
| 00    | 00 ~ 0A  | 00 ~ 3F | 00 ~ 0C      | DI<sub>3</sub>= 00，代表电能量</br>DI<sub>0</sub>，代表结算日               | UINT64  | 0.01 | 00-00-00-00 代表（当前）组合有功总电能</br>00-00-00-01 代表（上 1 结算日）组合有功总电能 |
| 00    | 80~86</br>15~1E</br>94~9A</br>29~32</br>A8~AE</br>3D~46</br>BC~C2 | 00      | 00 ~ 0C   | DI<sub>3</sub> = 00，代表电能量</br>DI<sub>0</sub>，代表结算日                 | UINT64  | 0.01  | 00-80-00-00 代表（当前）关联总电能</br>00-80-00-01 代表（上 1 结算日）关联总电能</br>00-15-00-01 代表（上 1 结算日）A 相正向有功电能</br>00-15-00-01 代表（上 2 结算日）A 相正向有功电能</br> 00-29-00-02 代表（上 2 结算日）B 相正向有功电能 |
| 02    | 01 ~ 09   | 01 ~ 03  | 00                   | DI<sub>3</sub>= 02，代表变量                                 | UINT16</br>UINT32 | 0.1</br>0.01</br>0.001</br>0.0001 | 02-01-01-00 代表 A 相电压</br>02-02-01-00 代表 A 相电流|
| 02    | 0A ~ 0B   | 01 ~ 03  | 01 ~15               | DI<sub>2</sub>= 0A，代表电压谐波含量</br>DI<sub>2</sub> = 0B，代表电流谐波含量</br>DI<sub>1</sub> ，代表A，B，C 相</br> DI~0~，代表第几次谐波含量 | UINT16 |  0.01   | 02-0A-01-01 代表 A 相电压 1 次谐波含量</br>02-0A-02-02 代表 B 相电压 2 次谐波含量</br>02-0B-01-01 代表 A 相电流 1 次谐波含量</br>02-0B-02-02 代表 B 相电流 2 次谐波含量 |
| 02    | 80        | 00       | 01 ~ 0A              | DI<sub>3</sub>= 02，代表变量     | UINT16    | 0.01 | 02-80-00-01 代表零线电流 </br>02-80-00-02 代表电网频率     |
| 04    | 00        | 01 ~ 0E  | 01 ~ 0C              | DI<sub>3</sub>= 04，代表参变量   | UINT8</br>UINT16</br>UINT32</br>UINT64  | 0</br>0.1</br>0.001</br>0.0001 | 04-00-01-01 代表日期及时间</br>04-00-01-03 代表最大需量周期</br>04-00-04-01 代表通信地址</br>04-00-05-01 代表电表运行状态字 1 |
| 06    | 00 ~ 06   | 00       | 00 ~ 02              | DI<sub>3</sub>= 06，代表负荷记录  | UINT8</br>UINT64  | 0    | 06-00-00-00 代表最早记录块</br>06-06-00-00 代表第 6 类负荷最早记录块 |

## Sparkplug_B

Neuron 从设备采集到的数据可以通过Sparkplug_B协议从边缘端传输到Sparkplug_B应用中，用户也可以从应用程序向 Neuron 发送数据修改指令。Sparkplug_B是运行再MQTT之上的应用型协议，所以在Neuron中的设置与MQTT驱动相似。

### 应用配置

| 字段          | 说明                                                         |
| ------------- | ------------------------------------------------------------ |
| **client-id** | MQTT 客户端 ID，连接的唯一标识，必填                         |
| **group-id**  | Sparkplug_B 协议中的最顶层逻辑分组，可以代表工厂或车间等实体，必填 |
| **node-id**   | Sparkplug_B 协议中的边缘节点唯一标识，必填                   |
| **ssl**       | 是否启用 mqtt ssl，默认 false                                |
| **host**      | MQTT Broker 主机，必填                                       |
| **port**      | MQTT Broker 端口号，必填                                     |
| **username**  | 连接到 Broker 时使用的用户名，可选填                         |
| **password**  | 连接到 Broker 时使用的密码，可选填                           |
| **ca**        | ca 文件，只在 ssl 值为 true 时启用，这种情况下为必填         |
| **cert**      | cert 文件，只在 ssl 值为 true 时启用，可选填                 |
| **key**       | key 文件，只在 ssl 值为 true 时启用，可选填                  |
| **keypass**   | key 文件密码，只有在 ssl 值为 true 时启用，可选填            |

## 非 A11

### 设备设置

| 字段            | 说明                                                         |
| --------------- | ------------------------------------------------------------ |
| connection mode | 驱动程序连接到设备的方式，默认为 client，即把 Neuron 作为客户端使用 |
| host            | 当 Neuron 作为客户端使用时，host 指远程设备的 IP。当 Neuron 作为服务端使用时，host 指 Neuron 在本地使用的 IP，默认可填写 0.0.0.0 |
| port            | 当 Neuron 作为客户端使用时，post 指远程设备的 TCP 端口。当 Neuron 作为服务端使用时，host 指 Neuron 在本地使用的 TCP 端口。 |
| site            | 非A11设备站点号。                                            |

### 支持的数据类型

* INT16
* UINT16
* INT32
* UINT32
* FLOAT
* STRING

### 地址格式

> COMMAND ! OFFSET[.LEN]</span>

*Example:*

| 地址    | 数据类型           | 说明                        |
| ------- | ------------------ | --------------------------- |
| 1!10.20 | string             | 指令1，偏移10，字符串长度20 |
| 12!1    | uint16/int16       | 指令12，偏移1               |
| 20!32   | uint32/int32/float | 指令20，偏移32              |

## ADS

通过ads插件可以连接Beckhoff ADS/AMS设备.

### 设备设置

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

### 支持的数据类型

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

### 地址格式

> INDEX_GROUP,INDEX_OFFSET</span>

`INDEX_GROUP`和`INDEX_OFFSET`可以分别独立使用十进制或十六进制指定.

*示例:*

| 地址            | 数据类型           | 说明                        |
| --------------- | ------------------ | --------------------------------------------------------- |
| 0x4040,0x7d01c  | bool               | index_group 0x4040, index_offset 0x7d01c                  |
| 16448,51029     | uint8              | index_group 0x4040, index_offset 0x7d01d                  |
| 0x4040,512896.5 | string             | index_group 0x4040, index_offset 0x7d380, 字符串长度为5   |

## OPC DA

Neuron 可通过外部辅助程序 neuopc.exe 间接访问运行于 Windows 操作系统的 OPCDA 服务器。neuopc 通过将 DA 协议转换为 UA 协议，再通过 Neuron已有的 opcua driver 进行数据获取，DA 的所有可访问点位都被映射至 UA 的"命名空间2"当中，点位的 ID 则与 DA 保持一致。

### 设备配置

neuopc 的组件包可以前往 neuopc 的[项目页面](https://github.com/neugates/neuopc)下载（neuopc是GPL协议下的开源项目）。安装以及远程连接的系统配置参考 [neuopc 运行环境设置](plc-settings/opcda.md)。

![](./plc-settings/assets-opcda/neuopc-setting.png)
#### neuopc配置

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

#### Neuron opcua 连接配置

| 字段         | 说明                                                  |
| ------------ | ----------------------------------------------------- |
| endpoint url | neuopc 的访问地址，默认是`opc.tcp://127.0.0.1:48401/` |
| username     | neuopc 的授权用户名                                   |
| password     | neuopc 的访问密码                                     |

步骤：

1. 在 neuron 南向设备管理中添加一个 opcua 设备；
2. 在设备配置中修改 endpoint url 为 neuopc 的 UA Server 地址；
3. 在设备配置中填写 Username，与 neuopc 中设置的一致；
4. 在设备配置中填写 Password，与neuopc 中设置的一直；
5. 无需填写 Cert 和 Key，直接提交设置表单。

### 支持的数据类型

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

### 地址格式

> IX!NODEID</span>

**IX** 名字空间索引，访问 neuopc 时，IX只能为2。

**NODEID** 节点 ID，与 DA 服务器中的字符串一致。

*例子：*

| 地址                   | 数据类型 | 说明                                                         |
| ---------------------- | -------- | ------------------------------------------------------------ |
| 2!Bucket Brigade.UInt2 | UINT16   | 获取类型为 UINT16 的数据点；NS 为2，NODEID 为 Bucket Brigade.UInt2 |

## CNC FANUC FOCAS

**支持架构**: amd64, arm/v7

### 设备设置

| 字段    | 说明         |
| ------- | ------------ |
| host    | 设备IP地址   |
| port    | 设备端口号   |
| timeout | 连接超时时间 |

### 支持的数据类型

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
* bit
* string

### CNC 数据

| tag标识（地址） | 说明                                         | 数据类型     | 参数               |
| --------------- | -------------------------------------------- | ------------ | ------------------ |
| actf            | actual feed rate                             | int64/uint64 | -                  |
| absolute        | absolute position data of axis               | int64/uint64 | axis number(.n)    |
| machine         | machine position data of axis                | int64/uint64 | axis number(.n)    |
| relative        | relative position data of axis               | int64/uint64 | axis number(.n)    |
| distance        | distance to go of axis                       | int64/uint64 | axis number(.n)    |
| acts            | actual rotational speed of the spindle       | int64/uint64 | -                  |
| skip            | skipped position of axis                     | int64/uint64 | axis number(.n)    |
| srvdelay        | servo delay amount of axis                   | int64/uint64 | axis number(.n)    |
| accdecdly       | acceleration/deceration delay amount of axis | int64/uint64 | axis number(.n)    |
| spcss_srpm      | converted spindle speed                      | int64/uint64 | -                  |
| spcss_sspm      | specified surface speed                      | int64/uint64 | -                  |
| spcss_smax      | clamp of maxmum spindle speed                | int64/uint64 | -                  |
| movrlap_input   | input overlapped motion value                | int64/uint64 | axis number(.n)    |
| movrlap_output  | output overlapped motion value               | int64/uint64 | axis number(.n)    |
| spload          | load information of the serial spindle       | int32/uint32 | spindle number(.n) |
| spmaxrpm        | maximum r.p.m ratio of serial spindle        | int32/uint32 | spindle number(.n) |
| spgear          | gear ratio of the serial spindle             | int32/uint32 | spindle number(.n) |

*CNC地址示例*

| 地址       | 说明                                  |
| ---------- | ------------------------------------- |
| actf       | 读取 actual feed rate                 |
| absolute.1 | 读取第1个axis的absolute position      |
| machine.3  | 读取第3个axis的machine position       |
| spload.1   | 读取第1个spindle的load information    |
| spmaxrpm.3 | 读取第3个spindle的maximum r.p.m ratio |

### PMC数据

| 标识 | 说明                            | 类型 | 权限 |
| ---- | ------------------------------- | ---- | ---- |
| A    | message demand                  | all  | 读写 |
| C    | counter                         | all  | 读写 |
| D    | data table                      | all  | 读写 |
| E    | extended relay                  | all  | 读写 |
| F    | signal to CNC -> PMC            | all  | 只读 |
| G    | signal to PMC -> CNC            | all  | 读写 |
| K    | keep relay                      | all  | 读写 |
| M    | input signal from other device  | all  | 读写 |
| N    | output signal from other device | all  | 读写 |
| R    | internal relay                  | all  | 读写 |
| T    | changeable timer                | all  | 读写 |
| X    | signal to machine -> PMC        | all  | 只读 |
| Y    | signal to PMC -> machine        | all  | 读写 |

*PMC点位示例*

| 地址 | 类型                                                         | 说明                                                    |
| ---- | ------------------------------------------------------------ | ------------------------------------------------------- |
| A0   | uint8/int8/uint16/int16/uint32/int32/int64/uint64/float/double | PMC **message demand** 区域，地址0的数据                |
| A0.1 | bit                                                          | PMC **message demand** 区域，地址0的的字节，第1个bit位  |
| A0.0 | bit                                                          | PMC **message demand** 区域，地址0的字节，第0个bit位    |
| A0.2 | string                                                       | PMC **message demand** 区域，地址0开始，长度为2的字符串 |
| D0.2 | string                                                       | PMC **data table** 区域，地址0开始，长度为2的字符串     |
| D0.7 | bit                                                          | PMC **data table** 区域，地址0的字节，第7个bit位        |
## Mitsubishi MELSEC-Q A1E

a1e 插件用于通过以太网访问三菱的 A 系列、FX3U、FX3G、iQ-F 系列 PLC（iQ-F 需要特定固件版本支持）。

### 设备配置

| 字段     | 说明                           |
| -------- | ------------------------------ |
| **host** | 远程 PLC 的 IP 地址            |
| **port** | 远程 PLC 的端口号，默认为 2000 |

### 支持的数据类型

* INT16
* UINT16
* INT32
* UINT32
* FLOAT
* DOUBLE
* BIT
* STRING

### 地址格式

> AREA ADDRESS\[.BIT]\[.LEN\[H]\[L]]</span>

#### AREA ADDRESS

| 区域 | 数据类型 | 属性  | 备注                                   |
| ---- | -------- | ----- | -------------------------------------- |
| X    | bit      | 读/写 | 输入继电器  (FX3/iQ-F)                 |
| Y    | bit      | 读/写 | 输出继电器 (FX3/iQ-F)                  |
| M    | bit      | 读/写 | 内部继电器 (FX3/iQ-F)                  |
| L    | bit      | 读/写 | 锁存器 (FX3)                           |
| F    | bit      | 读/写 | 信号器 (FX3)                           |
| B    | bit      | 读/写 | 链接继电器 (FX3)                       |
| SB   | bit      | 读/写 | 链接专用继电器(FX3/iQ-F)               |
| S    | bit      | 读/写 | 步继电器(FX3/iQ-F)                     |
| D    | 所有类型 | 读/写 | 数据寄存器 (FX3/iQ-F)                  |
| W    | 所有类型 | 读/写 | 链接寄存器 (FX3)                       |
| TS   | bit      | 读/写 | 定时器触点 (FX3/iQ-F)                  |
| TC   | bit      | 读/写 | 定时器线圈 (FX3)                       |
| TN   | 所有类型 | 读/写 | 定时器当前值 (FX3/iQ-F)                |
| STS  | bit      | 读/写 | 保持定时器触点 (FX3)                   |
| STC  | bit      | 读/写 | 保持定时器线圈(FX3)                    |
| STN  | 所有类型 | 读/写 | 保持定时器 (FX3)                       |
| CS   | bit      | 读/写 | 计数器触点 (FX3/iQ-F)                  |
| CC   | bit      | 读/写 | 计数器线圈 (FX3)                       |
| CN   | 所有类型 | 读/写 | 计数器当前值  (FX3/iQ-F)               |
| LCS  | bit      | 读/写 | 长计数器触点（FX3/iQ-F）               |
| LCC  | bit      | 读/写 | 长计数器线圈（FX3）                    |
| LCN  | 所有类型 | 读/写 | 长计数器当前值（FX3/iQ-F）             |
| SB   | bit      | 读/写 | 链接特殊继电器（FX3）                  |
| SW   | 所有类型 | 读/写 | 链接专用寄存器 (FX3)                   |
| SM   | bit      | 读/写 | 特殊寄存器 (FX3/iQ-F)                  |
| SD   | 所有类型 | 读/写 | 专用寄存器Specical register (FX3/iQ-F) |
| Z    | 所有类型 | 读/写 | 索引寄存器 Index register (FX3)        |
| LZ   | 所有类型 | 读/写 | 长变址寄存器 (FX3)                     |
| DX   | bit      | 读/写 | 链接直接软元件 链接输入(FX3)           |
| DY   | bit      | 读/写 | 链接直接软元件 链接输出(FX3)           |
| R    | 所有类型 | 读/写 | 文件寄存器 (FX3/iQ-F)                  |

*例子：*

| 地址  | 数据类型 | 说明                |
| ----- | -------- | ------------------- |
| X0    | bit      | X 区域，地址为 0    |
| X1    | bit      | X 区域，地址为 1    |
| Y0    | bit      | Y 区域，地址为 0    |
| Y1    | bit      | Y 区域，地址为 1    |
| D100  | int16    | D 区域，地址为 100  |
| D1000 | uint16   | D 区域，地址为 1000 |
| D200  | uint32   | D 区域，地址为 200  |
| D10   | float    | D 区域，地址为 10   |
| D20   | double   | D 区域，地址为 20   |

#### .BIT

只可用于**非bit类型区域**，表示读取指定地址的指定二进制位，二进制位索引区间为[0, 15]。

| 地址  | 数据类型 | 说明                       |
| ----- | -------- | -------------------------- |
| D20.0 | bit      | D 区域，地址为 20，第 0 位 |
| D20.2 | bit      | D 区域，地址为 20，第 2 位 |

#### .LEN\[H]\[L]

当数据类型是 string 类型时，**.LEN** 表示的是字符串长度；可以选填 **H**和 **L** 表示两种字节顺序，默认的是 **H** 的字节顺序。

*例子：*

| 地址      | 数据类型 | 说明                                               |
| --------- | -------- | -------------------------------------------------- |
| D1002.16L | string   | D 区域，地址为 1002，字符串长度为 16，字节顺序为 L |
| D1003.16  | string   | D 区域，地址为 1003，字符串长度为 16，字节顺序为 H |

## EtherNet/IP(CIP)

此驱动主要用于支持EtherNet/IP协议的设备。

### 设备配置

| 字段 | 说明                  |
| ---- | --------------------- |
| host | 设备IP地址            |
| port | 设备端口，默认为44818 |
| slot | CPU槽号，默认为0      |

### 支持的数据类型

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
* BOOL
* BIT
* STRING
* WORD
* DWORD
* LWORD

### PLC数据地址

>  TAG NAME </span>

## Siemens FetchWrite

s5fetch-write 插件用于带有网络扩展模块CP443的西门子PLC的访问，如，s7-300/400。

### 设备配置

| 字段     | 说明                        |
| -------- | --------------------------- |
| **host** | 远程 PLC 的 IP              |
| **port** | 远程 PLC 的端口，默认为 102 |

### 支持的数据类型

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
* BIT
* STRING

### 地址格式

> AREA ADDRESS\[.BIT][.LEN]</span>

#### AREA ADDRESS

| 区域 | 数据类型                                                     | 属性  | 备注                    |
| ---- | ------------------------------------------------------------ | ----- | ----------------------- |
| DB   | int16/uint16/bit/int32/uint32/int64/uint64/float/double/string | 读    | 主存数据块，以words读写 |
| M    | int8/uint8/int16/uint16/bit/int32/uint32/int64/uint64/float/double/string | 读/写 | 标志内存M，以bytes读写  |
| I    | int8/uint8/int16/uint16/bit/int32/uint32/int64/uint64/float/double/string | 读/写 | 输入，以bytes读写       |
| Q    | int8/uint8/int16/uint16/bit/int32/uint32/int64/uint64/float/double/string | 读/写 | 输出，以bytes读写       |
| PEPA | int8/uint8/int16/uint16/bit/int32/uint32/int64/uint64/float/double/string | 读/写 | IO modules，以bytes读写 |
| Z    | int16/uint16/bit/int32/uint32/int64/uint64/float/double/string | 读/写 | 计数器，以words读写     |
| T    | int16/uint16/bit/int32/uint32/int64/uint64/float/double/string | 读/写 | 计时器，以words读写     |

*例子：*

| 地址       | 数据类型 | 说明                         |
| ---------- | -------- | ---------------------------- |
| I0         | int16    | I 区域，地址为 0             |
| I1         | uint16   | I 区域，地址为 1             |
| Q2         | int16    | Q 区域，地址为 2             |
| Q3         | uint16   | Q 区域，地址为 3             |
| PEPA4      | int16    | PEPA 区域，地址为 4          |
| PEPA5      | int16    | PEPA 区域，地址为 5          |
| T6         | int16    | T 区域，地址为 6             |
| T7         | int16    | T 区域，地址为 7             |
| Z8         | uint16   | Z 区域，地址为 8             |
| Z9         | uint16   | Z 区域，地址为 9             |
| DB10.DBW10 | int16    | 10 数据块中，起始数据字为 10 |
| DB12.DBW10 | uint16   | 12 数据块中，起始数据字为 10 |
| DB10.DBW10 | float    | 10 数据块中，起始数据字为 10 |
| DB11.DBW10 | double   | 11 数据块中，起始数据字为 10 |

#### .BIT

选填，指某一地址的某一位。

*例子：*

| 地址        | 数据类型 | 说明                                 |
| ----------- | -------- | ------------------------------------ |
| I0.0        | bit      | I 区域，地址为0，第 0 位             |
| I0.1        | bit      | I 区域，地址为0，第 1 位             |
| Q1.0        | bit      | Q 区域，地址为1，第 0 位             |
| Q1.2        | bit      | Q 区域，地址为1，第 2 位             |
| PEPA2.1     | bit      | PEPA 区域，地址为2，第 1 位          |
| PEPA2.2     | bit      | PEPA 区域，地址为2，第 2 位          |
| T3.3        | bit      | T 区域，地址为3，第 3 位             |
| T3.4        | bit      | T 区域，地址为3，第 4 位             |
| Z4.5        | bit      | Z 区域，地址为4，第 5 位             |
| Z4.6        | bit      | Z 区域，地址为4，第 6 位             |
| DB1.DBW10.1 | bit      | 1 数据块中，起始数据字为 10，第 0 位 |
| DB2.DBW1.15 | bit      | 2 数据块中，起始数据字为 1，第 15 位 |

#### .LEN

当数据类型为 string 类型时，是必填项，表示字符串长度。

*例子：*

| 地址         | 数据类型 | 说明                                         |
| ------------ | -------- | -------------------------------------------- |
| DB1.DBW12.20 | string   | 1 数据块中，起始数据字为 12，字符串长度为 20 |



## HJ212-2017

HJ212-2017主要用于采集支持环保HJ212-2017标准的设备数据，此驱动目前只支持设备主动上传数据。

### 以太网连接配置

| 字段        | 说明                                                         |
| ----------- | ------------------------------------------------------------ |
| **timeout** | 向设备发送请求超时时间                                       |
| **host**    | 当 Neuron 作为客户端使用时，host 指远程设备的 IP。当 Neuron 作为服务端使用时，host 指 Neuron 在本地使用的 IP，默认可填写 0.0.0.0 |
| **port**    | 当 Neuron 作为客户端使用时，post 指远程设备的 TCP 端口。当 Neuron 作为服务端使用时，host 指 Neuron 在本地使用的 TCP 端口，默认为 502 |

### 串口连接配置

| 字段        | 说明                             |
| ----------- | -------------------------------- |
| **device**  | 使用串口设备，例如“/dev/ttyUSB0” |
| **stop**    | 停止位，默认值是 1               |
| **parity**  | 校验位，默认值是 2，代表偶校验   |
| **baud**    | 波特率，默认值是 9600            |
| **data**    | 数据位，默认值是 8               |
| **timeout** | 向设备发送请求超时时间           |

### 支持的数据类型

* STRING
* DOUBLE
* UINT8
* INT8



### 地址格式

#### 污染物实时数据

> RT!xxxx-[Rtd\][Flag\][SampleTime\][EFlag]</span>

| 地址                 | 类型   | 说明                         |
| -------------------- | ------ | ---------------------------- |
| RT!w01018-Rtd        | double | 污染物 w01018实时数据        |
| RT!w01018-Flag       | string | 污染物w01018实时数据标志     |
| RT!w01018-SampleTime | string | 污染物w01018实时数据采样时间 |
| RT!w01018-EFlag      | string | 污染物w01018设备标志         |
| RT!w01018-ZsRtd      | double | 污染物w01018实时采样折算数据 |

#### 污染物分钟数据

> MIN!xxxx-[Cou\][Min\][Avg\][Max\][Flag]

| 地址             | 类型   | 说明                       |
| ---------------- | ------ | -------------------------- |
| MIN!w01018-Cou   | double | 污染物w01018分钟累计值     |
| MIN!w01018-Min   | double | 污染物w01018分钟最小值     |
| MIN!w01018-Avg   | double | 污染物w01018分钟平均值     |
| MIN!w01018-Max   | double | 污染物w01018分钟最大值     |
| MIN!w01018-Flag  | string | 污染物w01018分钟数据标志   |
| MIN!w01018-ZsMin | double | 污染物w01018分钟折算最小值 |
| MIN!w01018-ZsAvg | double | 污染物w01018分钟折算平均值 |
| MIN!w01018-ZsMax | double | 污染物w01018分钟折算最大值 |

#### 污染物小时数据

> HOUR!xxxx-[Cou\][Min\][Avg\][Max\][Flag]

| 地址              | 类型   | 说明                       |
| ----------------- | ------ | -------------------------- |
| HOUR!w01018-Cou   | double | 污染物w01018小时累计值     |
| HOUR!w01018-Min   | double | 污染物w01018小时最小值     |
| HOUR!w01018-Avg   | double | 污染物w01018小时平均值     |
| HOUR!w01018-Max   | double | 污染物w01018小时最大值     |
| HOUR!w01018-Flag  | string | 污染物w01018小时数据标志   |
| HOUR!w01018-ZsMin | double | 污染物w01018小时折算最小值 |
| HOUR!w01018-ZsAvg | double | 污染物w01018小时折算平均值 |
| HOUR!w01018-ZsMax | double | 污染物w01018小时折算最大值 |

#### 污染物日数据

> DAY!xxxx-[Cou\][Min\][Avg\][Max\][Flag]

| 地址             | 类型   | 说明                     |
| ---------------- | ------ | ------------------------ |
| DAY!w01018-Cou   | double | 污染物w01018日累计值     |
| DAY!w01018-Min   | double | 污染物w01018日最小值     |
| DAY!w01018-Avg   | double | 污染物w01018日平均值     |
| DAY!w01018-Max   | double | 污染物w01018日最大值     |
| DAY!w01018-Flag  | string | 污染物w01018日数据标志   |
| DAY!w01018-ZsMin | double | 污染物w01018日折算最小值 |
| DAY!w01018-ZsAvg | double | 污染物w01018日折算平均值 |
| DAY!w01018-ZsMax | double | 污染物w01018日折算最大值 |

