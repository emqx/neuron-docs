# WebSocket

[WebSocket] is a network protocol that provides full-duplex communication channels over a single TCP connection. The WebSocket protocol was standardized by the IETF as [RFC 6455] in 2011. The WebSocket protocol specification defines two schemes, **ws** (WebSocket) and **wss** (WebSocket Secure), for unsecured and secure connections respectively. WebSocket has several advantages over traditional polling-based techniques, including lower latency, reduced network traffic, and improved scalability.

The Neuron WebSocket plugin is a commercial northbound plugin, which enables users to push collected data to WebSocket servers.

## Add Application

Navigate to **Configuration -> North Apps** and click **Add Application** to add a WebSocket client node.

## Configure Application

These are the available parameters when configuring a node using the WebSocket plugin.

| Parameter                       | Description                                                  |
| ------------------------------- | ------------------------------------------------------------ |
| **Upload Format**               | JSON format of reported data, required. <br />In *values-format*, data are split into `values` and `errors` sub-objects. <br />In *tags-format*, tag data are put in a single array. |
| **Server URL**                  | WebSocket server address, required. Example: `ws://127.0.0.1:8000`, `wss://example.com`. |
| **CA**                          | CA certificate which signs the server certificate, required when using `wss` scheme and self-signed certificates. |
| **Client Cert**                 | Client certificate, required only when using `wss` scheme and two way authentication. |
| **Client Private Key**          | Client private key, required only when using `wss` scheme and two way authentication. |
| **Client Private Key Password** | Client private key password, required only when **Client Private Key**, if provided, is encrypted. |

## Add Subscription

After plugin configuration, data forwarding can be enabled via southbound device subscriptions.

Click the device card or row on the **North Apps** page, then **Add Subscription** on the **Group List** page. And set the following:

- **South device**: Select the southbound device you want to subscribe to.
- **Group**: Select a group from the southbound device'.

## Data upload

The Neuron WebSocket plugin, acting as the WebSocket client, pushes data collected from devices as JSON to the WebSocket server at the address specified by the **Server URL** parameter.

The exact format of the data reported is controlled by the **Upload Format** parameter. There are two formats, *tags-format* and *values-format*. Both
formats are the same as that of the [MQTT plugin], see [MQTT API tags format].


[WebSocket]: https://en.wikipedia.org/wiki/WebSocke://en.wikipedia.org/wiki/WebSocket
[RFC 6455]: https://datatracker.ietf.org/doc/html/rfc6455
[MQTT plugin]: ../mqtt/overview.md
[MQTT API tags format]: ../mqtt/api.md#tags-format

## Operation and Maintenance

On the device card or device row, you can click on the **Data Statistics** icon to review the application's operation status and track the data received and sent. For explanations on statistical fields, refer to the [Create a Northbound Application](../north-apps.md) section.

If there are any issues with device operation, you can click on the DEBUG log chart. The system will automatically print DEBUG level logs for that node and switch back to the system default log level after ten minutes. Later, you can click on **System Information** -> **Logs** at the top of the page to view logs and perform troubleshooting. For a detailed interpretation of system logs, see [Managing Logs](../../../admin/log-management.md).
