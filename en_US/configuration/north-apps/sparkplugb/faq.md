# FAQ

## Sparkplug B plugin cannot connect to broker and is not connected

* Make sure you create the Sparkplug B plug-in with the correct parameters, such as the broker address, username, and password.
* If SSL is enabled, make sure you are using the correct certificate. Also check that the broker is properly configured.

## Sparkplug B plugin switches back and forth between connected and unconnected states

* The probability is that the broker is kicking out the MQTT client. Please check that the configured [**client-id**] parameter
are not conflicting with other clients, or that the broker is configured correctly.

[**client-id**]: ../mqtt/overview.md#parameters

## Sparkplug B Application side does not see the northbound data set

* Make sure that the Sparkplug B node is subscribed to the southbound node and that all nodes are up.
