# 连接设备

## 西门子 S7-1200

### 用户名/密码登录

1. 在 TIA V16 编程软件中选择目标 PLC，右键打开“属性”，在“常规”卡片下打开“OPC UA”选项组；

2. 打开“激活 OPC UA 服务器”选项；

3. 在“服务器上可用的安全策略”列表中勾选需要的安全策略，如果安全需求不是特别高，可以只勾选“无安全设置”，这样读写请求的速度会快一些；

4. 在“可信客户端”部分勾选“运行过程中自动接受客户端证书”；

5. 在“访客认证”部分关闭“启用访客认证”；

6. 在“用户名和密码认证”部分勾选“启用用户名和密码认证”；

7. 在“用户管理”列表中添加用户名和密码；

8. 下载程序到 PLC；

9. Neuron 新增南向 OPC UA 设备，打开“设备配置”，填写目标 PLC 的“端点 URL”，用户名/密码，无需添加证书/密钥。

## KEPServerEX

### 用户名/密码登录

1. 右键点击系统托盘中的 KEPServerEX 图标，在菜单中选择“设置”，打开“KEPServerEX 设置”，切换到“用户管理器”卡片，在 Administrators 组下新建用户，设置用户名/密码;

2. 双击系统托盘中的 KEPServerEX 图标，在主界面中打开“项目”的“属性编辑器”，将 OPC UA - “允许匿名登录”设置为“否”;

3. 右键点击系统托盘中的 KEPServerEX 图标，在菜单中选择“OPC UA 配置”，切换到“服务器端点”，双击端点条目，勾选所有安全策略。

4. 右键点击系统托盘中的 KEPServerEX 图标，在菜单中选择“重新初始化”；

5. Neuron 新增南向 OPC UA 设备，打开“设备配置”，填写目标 Server 的“端点 URL”，填写用户名/密码，无需添加证书/密钥，启动设备连接；

6. 右键点击系统托盘中的 KEPServerEX 图标，在菜单中选择“OPC UA 配置”，切换到“受信任的客户端”，将 NeuronClient 证书设置为信任。

7. 右键点击系统托盘中的 KEPServerEX 图标，在菜单中选择“重新初始化”；

### 证书/密钥 + 用户名/密码登录

1. 按照上文设置用户名/密码；

2. 参考[参数示例](./example.md)生成或转换证书/密钥；

3. 右键点击系统托盘中的 KEPServerEX 图标，在菜单中选择“OPC UA 配置”，切换到“受信任的客户端”，将 DER 格式的客户端证书导入列表；

4. 右键点击系统托盘中的 KEPServerEX 图标，在菜单中选择“重新初始化”；

5. Neuron 新增南向 OPC UA 设备，打开“设备配置”，填写目标 Server 的“端点 URL”，填写用户名/密码，添加证书/密钥，启动设备连接；

## Industrial Gateway OPC Server

### 匿名登录

1. 双击系统托盘中的 Industrial Gateway OPC Server 图标，在主界面中打开“项目”的“属性编辑器”，将 OPC UA - “允许匿名登录”设置为“是”;

2. 右键点击系统托盘中的 Industrial Gateway OPC Server 图标，在菜单中选择“OPC UA 配置”，切换到“服务器端点”，双击端点条目，勾选所有安全策略。

3. 右键点击系统托盘中的 KEPServerEX 图标，在菜单中选择“重新初始化”；

4. Neuron 新增南向 OPC UA 设备，打开“设备配置”，填写目标 Server 的“端点 URL”，无需填写用户名/密码，无需添加证书/密钥，启动设备连接；

### 证书/密钥 + 匿名登录

1. 按照上文设置匿名登录；

2. 参考[参数示例](./example.md)生成或转换证书/密钥；

3. 右键点击系统托盘中的 KEPServerEX 图标，在菜单中选择“OPC UA 配置”，切换到“受信任的客户端”，将 DER 格式的客户端证书导入列表；

4. 右键点击系统托盘中的 KEPServerEX 图标，在菜单中选择“重新初始化”；

5. Neuron 新增南向 OPC UA 设备，打开“设备配置”，填写目标 Server 的“端点 URL”，无需填写用户名/密码，添加证书/密钥，启动设备连接；

## Ignition 

### 用户名/密码登录

1. 打开 Ignition 的管理界面 Config 页面，选择 OPC UA/Server Setting，添加可被其他主机访问的 IP 地址到 Bind Addresses，保存配置；

2. Neuron 新增南向 OPC UA 设备，打开“设备配置”，填写目标 Ignition 的“端点 URL”——opc.tcp://IP:62541/discovery，用户名——opcuauser（Ignition 默认），密码——password（Igniton 默认），无需添加证书/密钥, 启动设备连接。

3. 打开 Ignition 的管理界面 Config 页面，选择 OPC UA/Security，切换到 Server 选项卡，将 Quarantined Certificates 列表中的 NeuronClient 证书设置为信任；

### 证书/密钥 + 用户名/密码登录

1. 参考[参数示例](./example.md)生成或转换证书/密钥；

2. 打开 Ignition 的管理界面 Config 页面，选择 OPC UA/Security，切换到 Server 选项卡，上传客户端证书并设置为信任；

3. Neuron 新增南向 OPC UA 设备，打开“设备配置”，填写目标 Ignition 的“端点 URL”——opc.tcp://IP:62541/discovery，用户名——opcuauser（Ignition 默认），密码——password（Igniton 默认），添加证书/密钥, 启动设备连接。

## Prosys Simulation Server

### 匿名登录

1. Prosys OPC UA Simulation Server 界面中切换到 Endpoints 选项卡，Security Modes 取消选择 Sign 和 Sign&Encrypt，选择 None；

2. Prosys OPC UA Simulation Server 界面中切换到 Users 选项卡，User Authentication Methods 取消选择 Username&Password、Certificate 和 IssuedToken/External System，选择 Anonymous；

3. Neuron 新增南向 OPC UA 设备，打开“设备配置”，填写目标 Server 的“端点 URL”，无需填写用户名/密码，无需添加证书/密钥，启动设备连接；

### 证书/密钥 + 匿名登录

1. 参考[参数示例](./example.md)生成或转换证书/密钥；

2. Prosys OPC UA Simulation Server 界面中切换到 Endpoints 选项卡，Security Modes 取消选择 None，选择 Sign 和 Sign&Encrypt；

3. Prosys OPC UA Simulation Server 界面中切换到 Users 选项卡，User Authentication Methods 取消选择 Username&Password、Certificate 和 IssuedToken/External System，选择 Anonymous；

4. Neuron 新增南向 OPC UA 设备，打开“设备配置”，填写目标 Server 的“端点 URL”，无需填写用户名/密码，添加证书/密钥，启动设备连接；

5. Prosys OPC UA Simulation Server 界面中切换到 Certificates 选项卡，将列表中的客户端证书设置为信任；

### 用户名/密码登录

1. Prosys OPC UA Simulation Server 界面中切换到 Endpoints 选项卡，Security Modes 取消选择 None，选择 Sign 和 Sign&Encrypt；

2. Prosys OPC UA Simulation Server 界面中切换到 Users 选项卡，User Authentication Methods 取消选择 Anonymous、Certificate 和 IssuedToken/External System，选择 Username&Password，添加自定义用户名/密码；

3. Neuron 新增南向 OPC UA 设备，打开“设备配置”，填写目标 Server 的“端点 URL”，填写用户名/密码，无需添加证书/密钥，启动设备连接；

4. Prosys OPC UA Simulation Server 界面中切换到 Certificates 选项卡，将列表中的客户端证书设置为信任；

### 证书/密钥 + 用户名/密码登录

1. 用户名/密码设置同上；

2. Neuron 新增南向 OPC UA 设备，打开“设备配置”，填写目标 Server 的“端点 URL”，填写用户名/密码，添加证书/密钥，启动设备连接；

3. Prosys OPC UA Simulation Server 界面中切换到 Certificates 选项卡，将列表中的客户端证书设置为信任；

 