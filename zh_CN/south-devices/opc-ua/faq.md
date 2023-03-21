# 常见问题

1. PLC 设备开启 OPC UA Server 时需要打开“接受客户端证书”选项。

2. KepServer 或 Industrial Gateway OPC Server 在不使用匿名登录的情况下需要将“受信任的客户端”列表中的 NeuronClient 设置为信任。

3. 只有 PEM 的证书/密钥时需要参照[参数示例](./example.md)进行转换。

4. Neuron 连接不上时，可以使用其他 OPC UA 测试软件测试一下是不是 OPC UA 服务器无法连接。