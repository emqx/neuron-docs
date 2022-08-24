# License Policy

Neuron is an open source project. We encourage our community to develop their own pluggable modules.

Core framework, dashboard and a few plugin modules such as modbus, mqtt and eKuiper are open source under LGPLv3 license. Neuron may run with these open source modules without an EMQ license. But all other commercial plugin modules require an official EMQ license to run without limitation.

A trial EMQ license can be download from our official website [https://www.emqx.com/en/apply-licenses/neuron](https://www.emqx.com/en/apply-licenses/neuron). All available modules could be used with limitation on 100 connections and 1000 data tags for 15 days. If trial EMQ license is expired, you can apply the trial EMQ license via our official website again. However, a mailbox can only apply for a trial license up to two times.

Of course, you can also directly [contact us](https://www.emqx.com/en/contact?product=neuron) to obtain the official license.

The below diagram are license details:

![license](../getting-started/assets/license.png)

* Maximum number of nodes means the maximum number of connection nodes you can create in the Neuron, including southbound northbound connection nodes.

* Maximum number of tags are the maximum total number of data tags created in the Neuron. Neuron pricing scheme for commercial modules is based on this maximum number of data tags.

* Each commercial plugin module can be authorized independently in EMQ license. "Enabled plugins" will list out all the authorized pluggable modules.

:::tip
For detailed steps of license installation, please refer to [Install License](../console-management/license-installation.md)。
:::
