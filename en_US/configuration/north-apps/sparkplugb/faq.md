# FAQ

## SparkplugB Plugin Disconnected from Broker

* Ensure you create the Sparkplug B plug-in with the correct parameters, such as the broker address, username, and password.
* If SSL is enabled, make sure you are using the correct certificate. Also, check that the broker is properly configured.

## Why is my MQTT node intermittently shifting between connected and disconnected states?

This issue is likely due to the broker forcing the MQTT client to disconnect. Please ensure the configured [**Client ID**] parameter is unique, or that the broker is set up properly.

[**Client ID**]: ./overview.md#parameters

## Why the SparkplugB application side does not see the northbound data set?

* Make sure that the Sparkplug B node is subscribed to the southbound node and that all nodes are up.
