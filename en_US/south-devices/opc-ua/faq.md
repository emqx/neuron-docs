## FAQ

## The device status is "Disconnected" for a long time.

* You can use other OPC UA testing software, such as UaExpert, to test if the OPC UA server cannot be connected;

* PLC devices need to turn on the "Accept client certificate" option when OPC UA Server is enabled;

* OPC Server needs to set NeuronClient in the "Trusted Clients" list to be trusted if anonymous login is not used;

## Error code - ERROR(3002): Plug-in is not connected

* Abnormal connection, need to check whether Neuron OPC UA device configuration is correct.

## Error code - ERROR(3008): Plug-in Tag value is invalid

* Read timeout, you can adjust the Interval value of Group appropriately.

## Error code - 10001

* The set measurement point address does not exist in OPC UA Server.

## Error Code - 10004

* The set measurement point is not readable.

## Error Code - 10005

* The set measurement point is not writable.

## Error Code - 10006

* The set data type is not supported by Neuron.