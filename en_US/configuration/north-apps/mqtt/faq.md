# FAQ

## Why does my MQTT node consistently fail to connect to the broker?

Ensure you've provided the correct information when configuring the node with the MQTT plugin. This includes details like the broker address, username, and password. If SSL is enabled, confirm the appropriate certificates are in use. Additionally, ensure the broker is correctly set up to accept node connections.

## Why is my MQTT node intermittently shifting between connected and disconnected states?

This issue is likely due to the broker forcing the MQTT client to disconnect. Please ensure the configured [**Client ID**] parameter is unique, or that the broker is set up properly.

[**Client ID**]: ./overview.md#parameters

## Why isn't my MQTT node reporting any data?

Confirm your node has been initiated and that it is subscribed to relevant south nodes.
