# 统计信息

这个 API 由 [Monitor 插件]实现，提供兼容 [Prometheus] 的统计数据。

[Prometheus]: https://prometheus.io/
[Monitor 插件]: ../configuration/north-apps/monitor/overview.md

## 获取统计信息

*GET*  /api/v2/metrics

### 请求头部

**Authorization** Bearer \<token\>

### 请求参数

**category**  可选, 取值为 `global`, `driver` 或 `app` 之一

**node**      可选, 用节点名过滤, 且必须指定 `category=driver` 或 `category=app`

### 响应状态

* 200 OK
* 400 请求错误
* 500 服务器内部错误

### 响应

```text
# HELP core_dumped Whether there is any core dump
# TYPE core_dumped gauge
core_dumped 0
# HELP uptime_seconds Uptime in seconds
# TYPE uptime_seconds counter
uptime_seconds 314
# HELP north_nodes_total Number of north nodes
# TYPE north_nodes_total gauge
north_nodes_total 1
# HELP north_running_nodes_total Number of north nodes in running state
# TYPE north_running_nodes_total gauge
north_running_nodes_total 1
# HELP north_disconnected_nodes_total Number of north nodes disconnected
# TYPE north_disconnected_nodes_total gauge
north_disconnected_nodes_total 1
# HELP south_nodes_total Number of south nodes
# TYPE south_nodes_total gauge
south_nodes_total 1
# HELP south_running_nodes_total Number of south nodes in running state
# TYPE south_running_nodes_total gauge
south_running_nodes_total 0
# HELP south_disconnected_nodes_total Number of south nodes disconnected
# TYPE south_disconnected_nodes_total gauge
south_disconnected_nodes_total 1
# HELP send_msgs_total Total number of messages sent
# TYPE send_msgs_total counter
send_msgs_total{node="data-stream-processing"} 0
# HELP send_msg_errors_total Total number of errors sending messages
# TYPE send_msg_errors_total counter
send_msg_errors_total{node="data-stream-processing"} 0
# HELP recv_msgs_total Total number of messages received
# TYPE recv_msgs_total counter
recv_msgs_total{node="data-stream-processing"} 0
# HELP last_rtt_ms Last request round trip time in milliseconds
# TYPE last_rtt_ms gauge
last_rtt_ms{node="modbus"} 9999
# HELP send_bytes Total number of bytes sent
# TYPE send_bytes gauge
send_bytes{node="modbus"} 0
# HELP recv_bytes Total number of bytes received
# TYPE recv_bytes gauge
recv_bytes{node="modbus"} 0
# HELP tag_reads_total Total number of tag reads including errors
# TYPE tag_reads_total counter
tag_reads_total{node="modbus"} 0
# HELP tag_read_errors_total Total number of tag read errors
# TYPE tag_read_errors_total counter
tag_read_errors_total{node="modbus"} 0
# HELP group_tags_total Total number of tags in the group
# TYPE group_tags_total gauge
group_tags_total{node="modbus",group="grp"} 1
# HELP group_last_send_msgs Number of messages sent on last group timer invocation
# TYPE group_last_send_msgs gauge
group_last_send_msgs{node="modbus",group="grp"} 0
# HELP group_last_timer_ms Time in milliseconds consumed on last group timer invocation
# TYPE group_last_timer_ms gauge
group_last_timer_ms{node="modbus",group="grp"} 0
```
