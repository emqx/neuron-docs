# Overview

Sparkplug B is an industrial IoT data transfer specification built on MQTT 3.1.1. Sparkplug B provides a unified way for device manufacturers and software providers to share data by making MQTT networks state-aware and interoperable while ensuring flexibility and efficiency.

Data collected by Neuron from devices can be transferred from the edge to the Sparkplug B application via the Sparkplug B protocol, and users can send data modification commands to Neuron from the application. sparkplug B is an application-based protocol running on top of MQTT, so the setup in Neuron is similar to the MQTT driver.

## Parameters

|  Parameter         |  Description                                                        |
| ------------- | ------------------------------------------------------------ |
| **Client ID** |  MQTT client ID, a unique identifier for the connection                          |
| **Group ID**  | The top-level logical grouping in the Sparkplug B protocol, which can represent entities such as factories or workshops     |
| **Node ID**   | Unique Identification of Edge Nodes in Sparkplug B Protocol                           |
| **SSL**       | Whether to enable mqtt ssl, default false                                 |
| **Broker Host**      | MQTT Broker Host                                            |
| **Broker Port**      | MQTT Broker Port                                           |
| **Username**  |  Username to use when connecting to Broker                                 |
| **Password**  |  Password to use when connecting to Broker                                   |
| **CA**        |  Ca file, enabled only if the ssl value is true                             |
| **Client Cert**      | Cert file, enabled only if the ssl value is true                           |
| **Client Key**       | Key file, enabled only if the ssl value is true                           |
| **Keypass**   |  Key file password, only enabled if ssl value is true                     |

:::tip
Only the `Group ID` and `Node ID` are from the Sparkplug B specification, the rest are connection parameters of the MQTT Broker, see [MQTT Overview](../mqtt/overview.md).
:::
