# Omron FINS TCP 使用常见问题

## FINS TCP 连接断开，错误码 10500

* 检查连接的 PLC 是否支持 FINS TCP 协议，欧姆龙只有部分 PLC 支持 FINS TCP协议。

## 插件连接断开，错误码 3002

* 检查 PLC 的 IP 地址是否正确，可以使用 `ping` 或者是 `telnet` 指令检查网络问题。