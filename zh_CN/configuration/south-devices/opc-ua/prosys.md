# Prosys Simulation Server 连接示例

Prosys Simulation Server 是由 Prosys 公司开发的 OPC UA 服务器，用于模拟 OPC UA 设备和系统的行为，主要用于开发和测试 OPC UA 客户端应用程序。

需要先将 Prosys Simulation Server 切换到 **Expert Mode**，点击菜单 **Options** -> **Switch to Expert Mode**。

## 连接 OPC UA Server（匿名登录）

1. Prosys OPC UA Simulation Server 界面中切换到 **Endpoints** -> **Security Modes** 取消选择 **Sign** 和 **Sign&Encrypt**，选择 **None**。
    ![prosys-1](./assets/prosys-1.jpg)
2. Prosys OPC UA Simulation Server 界面中切换到 **Users** -> **User Authentication Methods** 取消选择 **Username&Password**、**Certificate** 和 **IssuedToken/External System**，选择 **Anonymous**。
    ![prosys-2](./assets/prosys-2.jpg)
3. 保存设置并重新启动 Prosys OPC UA Simulation Server。

## 配置 Neuron

1. 通过 UaExpert 软件查看 Ignition 测点信息， 参考 [配置 UaExpert](./uaexpert.md)。
   ![prosys-5](./assets/prosys-5.jpg)

2. Neuron 新增南向 OPC UA 设备，打开 **设备配置**并进行如下设置后，启动设备连接。

   - **端点 URL**：填写目标 Server 的 URL

   - **用户名/密码**：无需填写

   - **证书/密钥**：无需添加

3. 根据测点信息添加 **Groups** 和 **Tags**。

## 连接 OPC UA Server（证书/密钥 + 匿名登录）

1. 参考[连接策略](./policy.md)生成或转换证书/密钥；

2. Prosys OPC UA Simulation Server 界面中切换到 **Endpoints** -> **Security Modes** 取消选择 **None**，选择 **Sign** 和 **Sign&Encrypt**；

3. Prosys OPC UA Simulation Server 界面中切换到 **Users** -> **User Authentication Methods** 取消选择 **Username&Password**、**Certificate** 和 **IssuedToken/External System**，选择 **Anonymous**；

4. 保存设置并重新启动 Prosys OPC UA Simulation Server。

## 配置 Neuron

1. 通过 UaExpert 软件查看 Ignition 测点信息， 参考 [配置 UaExpert](./uaexpert.md)。
   ![prosys-5](./assets/prosys-5.jpg)
2. Neuron 新增南向 OPC UA 设备，打开 **设备配置**，并进行如下设置后，启动设备连接。
   - **端点 URL**：填写目标 Server 的 URL
   - **用户名/密码**：无需填写
   - **证书/密钥**：添加证书和密钥
3. Prosys OPC UA Simulation Server 界面中切换到 **Certificates**，将列表中的客户端证书设置为信任。
    ![prosys-3](./assets/prosys-3.jpg)

4. 根据测点信息添加 **Groups** 和 **Tags**。

## 连接 OPC UA Server（用户名/密码）

1. Prosys OPC UA Simulation Server 界面中切换到 **Endpoints** -> **Security Modes** 取消选择 **None**，选择 **Sign** 和 **Sign&Encrypt**。
2. Prosys OPC UA Simulation Server 界面中切换到 **Users** -> **User Authentication Methods** 取消选择 **Anonymous**、**Certificate** 和 **IssuedToken/External System**，选择 **Username&Password**，添加自定义用户名/密码。
    ![prosys-4](./assets/prosys-4.jpg)
3. 保存设置并重新启动 Prosys OPC UA Simulation Server。

## 配置 Neuron

1. 通过 UaExpert 软件查看 Ignition 测点信息， 参考 [配置 UaExpert](./uaexpert.md)。
   ![prosys-5](./assets/prosys-5.jpg)

2. Neuron 新增南向 OPC UA 设备，打开 **设备配置**，并进行如下设置后，启动设备连接。

   - **端点 URL**：填写目标 Server 的 URL

   - **用户名/密码**：填写用户名和密码

   - **证书/密钥**：无需添加

   - **更新模式**：可以修改为 Subscribe 或 Read&Subscribe，以 OPC UA 订阅方式获取数据

3. Prosys OPC UA Simulation Server 界面中切换到 **Certificates**，将列表中的客户端证书设置为信任。
4. 根据测点信息添加 **Groups** 和 **Tags**。

## 连接 OPC UA Server（证书/密钥 + 用户名/密码）

用户名/密码以及证书/密钥设置参考 

- [连接 OPC UA Server（证书/密钥 + 匿名登录）](#连接-opc-ua-server-证书-密钥-匿名登录)
- [连接 OPC UA Server（用户名/密码登录）](#连接-opc-ua-server-用户名-密码)

## 配置 Neuron

1. 通过 UaExpert 软件查看 Ignition 测点信息， 参考 [配置 UaExpert](./uaexpert.md)。
   ![prosys-5](./assets/prosys-5.jpg)

2. Neuron 新增南向 OPC UA 设备，打开 **设备配置**，并进行如下设置后，启动设备连接。

   - **端点 URL**：填写目标 Server 的 URL

   - **用户名/密码**：填写用户名和密码

   - **证书/密钥**：添加证书和密钥

   - **更新模式**：可以修改为 Subscribe 或 Read&Subscribe，以 OPC UA 订阅方式获取数据

3. Prosys OPC UA Simulation Server 界面中切换到 **Certificates**，将列表中的客户端证书设置为信任。

4. 根据测点信息添加 **Groups** 和 **Tags**。
   

## 测试点位

| 名称     | 地址   | 属性 | 类型   |
| -------- | ------ | ---- | ------ |
| Counter  | 3!1001 | Read | INT32  |
| Random   | 3!1002 | Read | DOUBLE |
| Sawtooth | 3!1003 | Read | DOUBLE |
| Sinusoid | 3!1004 | Read | DOUBLE |
| Square   | 3!1005 | Read | DOUBLE |
| Triangle | 3!1006 | Read | DOUBLE |

