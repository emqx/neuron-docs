# WebSocket

## Module Description

Through this plugin, collected data can be transmitted to WebSocket servers using *ws*/*wss* protocol.

## Parameter Configurations

| Parameter           | Description                                                  |
| ------------------- | ------------------------------------------------------------ |
| **format**          | The json format selection of the reported data, required, there are values mode and tags mode, the default is values mode |
| **url**             | WebSocket server address, required. Example: ws://127.0.0.1:8000, wss://example.com |
| **ca**              | ca file, only enabled when using *wss* protocol, in which case it is required       |
| **cert**            | cert file, only enabled when using *wss* protocol, optional                         |
| **key**             | key file, only enabled when using *wss* protocol, optional                          |
| **keypass**         | key file password, only enabled when using *wss* protocol, optional                 |