# SparkPlugB

Sparkplug B is an industrial IoT data transfer specification built on MQTT 3.1.1. Sparkplug B provides a unified way for device manufacturers and software providers to share data by making MQTT networks state-aware and interoperable while ensuring flexibility and efficiency.

Data collected by Neuron from devices can be transferred from the edge to the Sparkplug B application via the Sparkplug B protocol, and users can send data modification commands to Neuron from the application. 

## Add Application

Navigate to **Configuration -> North Apps** and click **Add Application** to add a Sparkplug B client node.

## Configure Application

Sparkplug B is an application-based protocol running on top of MQTT, so the setup in Neuron is similar to the MQTT driver.

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

## Add Subscription

After plugin configuration, data forwarding can be enabled via southbound device subscriptions.

Click the device card or row on the **North Apps** page, then **Add Subscription** on the **Group List** page. And set the following:

- **South device**: Select the southbound device you want to subscribe to, for example, 'modbus-tcp-1'.
- **Group**: Select a group from the southbound device, for example, 'group-1'.

## Use Case

- You can use the Neuron Sparkplug B plugin to report data to EMQX, and decode the complete and accurate data results through the EMQX's encoding and decoding functions. For specific results, see [Integration with EMQX](sparkplug.md).
- You can connect to the Ignition platform through the Neuron SparkPlugB plugin. For specific steps, refer to [Ignition](ignition.md).
- You can also connect to Cogent DataHub through the Neuron SparkPlugB plugin. For specific steps, refer to [Cogent](cogent.md).

## Operation and Maintenance

On the device card or device row, you can click on the **Data Statistics** icon to review the application's operation status and track the data received and sent. For explanations on statistical fields, refer to the [Create a Northbound Application](../north-apps.md) section.

If there are any issues with device operation, you can click on the DEBUG log chart. The system will automatically print DEBUG level logs for that node and switch back to the system default log level after ten minutes. Later, you can click on **System Information** -> **Logs** at the top of the page to view logs and perform troubleshooting. For a detailed interpretation of system logs, see [Managing Logs](../../../usage/admin/log-management.md).
