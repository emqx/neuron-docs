# Overview

[WebSocket] is a network protocol that provides full-duplex communication
channels over a single TCP connection. The WebSocket protocol was standardized
by the IETF as [RFC 6455] in 2011. The WebSocket protocol specification defines
two schemes, **ws** (WebSocket) and **wss** (WebSocket Secure), for unsecure
and secure connections respectively. WebSocket has several advantages over
traditional polling-based techniques, including lower latency, reduced network
traffic, and improved scalability.

The Neuron WebSocket plugin is a commercial north bound plugin, which enables
users to push collected data to WebSocket servers.

## Parameters

These are the available parameters when configuring a node using the WebSocket plugin.

| Parameter                       | Description                                                  |
| ------------------------------- | ------------------------------------------------------------ |
| **Upload Format**               | JSON format of reported data, required. There are *values-format* and *tags-format*. In *values-format*, data are split into `values` and `errors` sub objects. In *tags-format*, tag data are put in a single array. |
| **Server URL**                  | WebSocket server address, required. Example: `ws://127.0.0.1:8000`, `wss://example.com`. |
| **CA**                          | CA certificate which signs the server certificate, required when using `wss` scheme and self signed certificates.     |
| **Client Cert**                 | Client certificate, required only when using `wss` scheme and two way authentication.    |
| **Client Private Key**          | Client private key, required only when using `wss` scheme and two way authentication.    |
| **Client Private Key Password** | Client private key password, required only when **Client Private Key**, if provided, is encrypted. |

## Data upload

The Neuron WebSocket plugin, acting as the WebSocket client, pushes data
collected from devices as JSON to the WebSocket server at the address specified
by the **Server URL** parameter.

The exact format of the data reported is controlled by the **Upload Format**
parameter. There are two formats, *tags-format* and *values-format*. Both
formats are the same as that of the [MQTT plugin], see [MQTT API tags format].


[WebSocket]: https://en.wikipedia.org/wiki/WebSocke://en.wikipedia.org/wiki/WebSocket
[RFC 6455]: https://datatracker.ietf.org/doc/html/rfc6455
[MQTT plugin]: ../mqtt/overview.md
[MQTT API tags format]: ../mqtt/api.md#tags-format
