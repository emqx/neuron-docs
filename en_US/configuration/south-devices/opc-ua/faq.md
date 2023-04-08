## FAQ

## The device status is "Disconnected" for a long time or Error code - ERROR(3002): Plug-in is not connected

* Test whether the OPC UA server port is available by Telnet tool, command `telnet target-ip target-port`, if it fails to connect, you need to check whether the OPC UA server is listening to the right network, and check whether the network firewall setting is open the relevant port.

* You can use other OPC UA testing software, such as UaExpert, to test if the OPC UA server cannot be connected.

* PLC devices need to turn on the "Accept client certificate" option when OPC UA Server is enabled.

* OPC Server needs to set NeuronClient in the "Trusted Clients" list to be trusted if anonymous login is not used.

* Abnormal connection, need to check whether Neuron OPC UA device configuration is correct.

* Provide Neuron device logs to developers to help troubleshoot issues.

## Error code - ERROR(3008): Plug-in Tag value is invalid

* Read timeout, you can adjust the Interval value of Group appropriately.
