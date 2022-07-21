# Neuron Policy

Neuron is an open source project. We encourage our community to develop their own plugin modules.

Core framework, and a few plugin modules such as modbus, mqtt and eKuiper are open source under LGPLv3 license. Neuron may run with these open source modules without EMQ license. But all other commercial plugin modules require an official EMQ license to run without any limitation.

A trial EMQ license can be download from website [https://www.emqx.com/zh/apply-licenses/neuron](https://www.emqx.com/zh/apply-licenses/neuron). All available modules could be used for 15 days without limitation. A mailbox can only apply for a trial license up to two times.

The below diagram are license details:

![license](../getting-started/assets/license.png)

Maximum number of nodes means the large number of nodes you can create in the Neuron. Each node is either a southbound connection to external device or a northbound link to application.

Maximum number of tags are the total number of data tags created in the Neuron. Neuron pricing scheme is based on this maximum number of data tags.

Each commercial plugin module can be authorized independently in EMQ license. Enabled plugins is a list of authorized modules in Neuron.
