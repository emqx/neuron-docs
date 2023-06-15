# 常见问题

## 如何写 eKuiper 规则以满足我的需求

请参考 [eKuiper Docs](https://ekuiper.org/docs/en/latest)

## *data-stream-processing* 北向节点处于未连接状态，而 eKuiper 运行正常

确保您创建了使用 eKuiper Neuron 源的规则，并且 eKuiper 会延迟连接直到规则被启动。

## 如何查看 eKuiper 是否成功从 Neuron 采集到数据

1. 检查 **data-stream-processing** 节点处于连接状态，并且订阅了南向节点。
2. 通过仪表板的性能监控面板，检查 **data-stream-processing** 节点确实采集到了设备数据。
   ![check data-stream-processing metrics](./assets/ekuiper_metrics.gif)
