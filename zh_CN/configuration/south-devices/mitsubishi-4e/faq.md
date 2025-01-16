# 常见问题

## 设备能 ping 通，但是 Neuron 显示连接断开
 
* PLC TCP 模式下，每一个网络端口只允许建立一个 TCP 连接，且应保证只有唯一的 Neuron 实例能通过该端口访问 PLC。
  