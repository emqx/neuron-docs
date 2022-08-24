# 许可证政策

Neuron 是一个开源项目。我们鼓励我们的社区开发自己的插件模块。

核心架构，仪表板和一些驱动模块（例如 modbus，mqtt 和 eKuiper 等）是在 LGPLv3 许可下开源的。Neuron 可以在没有 EMQ 许可证的情况下运行这些开源模块。但是，所有商业模块都需要 EMQ 官方许可证才能不受限制地运行。

试用的 EMQ 许可证可从官方网站上下载 [https://www.emqx.com/zh/apply-licenses/neuron](https://www.emqx.com/zh/apply-licenses/neuron)。所有可用的模块都可以在 100 个连接和 1000 个数据标签的限制下试用 15 天。 如果试用 EMQ 许可证过期，您可以通过我们的官网重新申请试用 EMQ 许可证。 但是，一个邮箱最多只能申请两次试用许可证。

当然，您也可以直接 [联系我们](https://www.emqx.com/zh/contact?product=neuron)获取正式的 License。

下图是许可证的详细信息：

![license](../getting-started/assets/license.png)

* 节点数限制指的是用户可以在 Neuron 中创建的最大节点数量。每个节点就是一个连接到外部设备的南向连接或者是连接到应用程序的北向连接。

* 节点下 Tag 数目限制指的是用户可在 Neuron 中创建的所有 tag 总和的最大值。Neuron 的定价方案是基于此最大数据标签数。

* 每个商业插件模块都可以在 EMQ 许可证中独立授权。可用的 Plugin 指的是在 Neuron 中已授权模块的列表。

:::tip
License 安装的详细步骤请参考 [安装 License](../console-management/license-installation.md)。
:::
