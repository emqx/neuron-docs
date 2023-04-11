# Modbus TCP FAQ

## Unable to Read Tag Value, Error Code 3002
---
* Turn on DEBUG logs, check the logs, data flow, and whether the device has responded with correct data (if multiple upstream devices are collecting data from the same serial device, exceptions may occur).
* Check if the station number is correct.
* Check if the address is correct (Neuron Modbus address starts from 1).
* Some devices may not support reading only one point at a time, so all points need to be configured (Neuron will automatically optimize batch reading).
* Check if the connection is valid. Use the telnet command to detect if there are any abnormalities in the link.
* The device supports the Modbus RTU protocol, not Modbus TCP. Try using the Modbus RTU plugin.

## Tag value Invalid, Error Code 3008
---
* The device is offline and the data cannot be updated.
* The device does not respond within a certain period of time.
* The device supports the Modbus RTU protocol, not Modbus TCP. Try using the Modbus RTU plugin.

## Tag Value Read does not Match Expecations
---
* Incorrect data type.
* Incorrect byte order.
* Presence of multiple upstream masters collecting data resulting in data corruption.
* The DTU has enabled registration or heartbeat packets, causing Neuron to consider data flow data as incorrect.
* The device actively uploads data, but the standard Modbus only supports requesting and then responding with corresponding data.
* The device supports Modbus RTU protocol instead of Modbus TCP. Try using Modbus RTU plugin.
