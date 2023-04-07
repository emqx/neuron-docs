# Siemens S7 ISOTCP FAQ

## COTP connection is disconnected, error code 10150

* Check whether the S7 node configuration parameters configured in Neuron match the PLC, such as CPU rack number (slot), CPU slot number (rack), etc.
* S7 lower layer protocol cannot be recognized, and the protocol layer connection cannot be established. Check whether the connection port supports the standard S7 protocol.

## Read tag value error, error code 10103

* Protected tag, need to configure permissions in PLC.

## Read tag value error, error code 10105

* The tag in PLC does not exist

## Read tag value error, error code 3002

 * Check whether the server where Neuron is installed can communicate with PLC. If it can ping, you can try to use the telnet tool to test the PLC port.