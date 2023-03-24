# FAQ

## My MQTT node cannot connect to the broker and keeps in disconnected state

Please ensure that you provide the correct arguments when setting up the node
using the MQTT plugin, such as broker address, user name, and password. Add if
you enable SSL, make sure using the right certificates. Also, make sure the
broker is properly set up to accept connections from the node.

## My MQTT node keeps switching between connected and disconnected state

This is highly probably the broker is kicking the MQTT client. Please check
that the configured [**client-id**] parameter is unique, or that the broker
is setup properly.

[**client-id**]: ./overview.md#parameters

## My MQTT node reports no data

Please make sure your node is started, and you subscribe to some south nodes.
