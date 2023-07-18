# 常见问题

## 设备状态长时间为“连接断开” 或 数据监控页面出现错误码——ERROR(3002)：插件未连接

* 通过 Telnet 工具测试 OPC UA 服务器端口是否可用，命令

  ```
   telnet target-ip target-port
  ```

  如果未能连接，需要检查 OPC UA 服务器是否监听了正确的网络，检查网络防火墙设置是否开放了相关端口。

* 可以使用其他 OPC UA 测试软件，如：UaExpert 测试 OPC UA 服务器是否可以连接。

* PLC 设备开启 OPC UA Server 时需要打开“接受客户端证书”选项。

* OPC Server 在不使用匿名登录的情况下需要将“受信任的客户端”列表中的 NeuronClient 设置为信任。

* 检查 Neuron OPC UA 设备配置是否正确。

* 向开发者提供 Neuron 设备日志帮助排查问题。

## 错误码——ERROR(3008)：插件 Tag 值失效

* 读取超时，可以适当调高 Group 的 Interval 值。
