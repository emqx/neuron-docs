# GE Historian

Neuron can use the Neuron HUB driver and NeuronHUB Windows program to indirectly access GE Historian servers running on Windows systems. GE Historian is an industrial historian database used for storing and retrieving industrial process data.


## NEURON HUB Windows Program Parameters

| Parameter       | Description                                             |
| --------------- | ------------------------------------------------------- |
| Node Name       | Node name, must be unique to distinguish multiple nodes |
| Server          | Target host identifier (IP or hostname)                 |
| UserName        | user name                                               |
| PassWrod        | password                                                |
| update interval | Cache update interval, default 1000 milliseconds        |


## Supported Data Types

* uint8
* int8
* uint16
* int16
* uint32
* int32
* uint64
* int64
* float
* double
* bool
* string


## Address Format
When selecting the GE Historian node type in the Neuron HUB driver, the address is the Tag Name in the GE Historian server. You can use the `Export` function to export all point information as a table and import it directly into NEURON.


## NOTE
Before using the NeuronHUB Windows program to collect data, you need to install the Historian OLE DB Provider Components from the GE Historian installation package.
