# Modbus RTU FAQ

## Unable to Read Tag Value, Error Code 3002
---
* Enable DEBUG logging, check the log, inspect the data flow, and verify if the device has responded with data. If there is a response, check if the data is correct (serial devices may produce exceptions when multiple upstream masters collect data).
* Check if the station number is correct.
* Verify if the address is correct (Modbus address for Neuron starts from 1).
* Some devices may not support reading a single point at a time, so all points need to be configured (Neuron automatically optimizes batch reading).
* Serial wiring issues.
* Incorrect serial port configuration.
* The device supports Modbus TCP protocol instead of Modbus RTU. Try using Modbus TCP plugin.

## Tag Value Invalid, Error Code 3008
---
* The device is offline, and data cannot be updated.
* The device does not respond with data within a certain period.
* The device supports Modbus TCP protocol instead of Modbus RTU. Try using Modbus TCP plugin.

## Tag Value Read does not Match Expecations
---
* Incorrect data type.
* Incorrect byte order.
* Presence of multiple upstream masters collecting data resulting in data corruption.
* The DTU has enabled registration or heartbeat packets, causing Neuron to consider data flow data as incorrect.
* The device actively uploads data, but the standard Modbus only supports requesting and then responding with corresponding data.
* The device supports Modbus TCP protocol instead of Modbus RTU. Try using Modbus TCP plugin.
