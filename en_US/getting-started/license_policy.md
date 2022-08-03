# License Policy

Neuron is an open source project. We encourage our community to develop their own pluggable modules.

Core framework, dashboard and a few plugin modules such as modbus, mqtt and eKuiper are open source under LGPLv3 license. Neuron may run with these open source modules without EMQ license. But all other commercial plugin modules require an official EMQ license to run without limitation.

A trial EMQ license can be download from our official website [https://www.emqx.com/en/apply-licenses/neuron](https://www.emqx.com/en/apply-licenses/neuron). All available modules could be used with limitation on 100 connections and 1000 data tags for 15 days trial. If trial EMQ license is expired, you can apply the trial EMQ license via our official website again. However, a mailbox can only apply for a trial license up to two times.

The below diagram are license details:

![license](../getting-started/assets/license.png)

Maximum number of nodes means the large number of connection nodes you can create in the Neuron. Each node is either a southbound connection to external device or a northbound link to application.

Maximum number of tags are the total number of data tags created in the Neuron. Neuron pricing scheme is based on this maximum number of data tags.

Each commercial plugin module can be authorized independently in EMQ license. Enabled plugins is a list of authorized modules in Neuron.
