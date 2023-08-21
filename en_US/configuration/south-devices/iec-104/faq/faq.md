# FAQ

## Unable to Read Tag Value, Error Code 3002
* Check Common Address.
* Check IOA.
* See if there are any errors in the log.
* It takes some time to establish a connection with devices.
* Receive a message of an unsupported type id.

## Data Type Mismatch, Error Code 3007
* The value read from the device does not match the data type in Neuron. For example, if the device returns a single point when IOA=100, but the Float type is configured in Neuron, such an error will occur.