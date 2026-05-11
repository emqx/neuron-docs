# OPCAE

Neuron can use the Neuron HUB driver and NeuronHUB Windows program to indirectly access OPC AE (Alarms and Events) servers running on Windows systems, supporting Simple, Conditional, and Tracking events. OPC AE is primarily used to retrieve alarm and event information from devices.


## NEURON HUB Windows Program Parameters

| Parameter | Description                                                                                                                           |
| --------- | ------------------------------------------------------------------------------------------------------------------------------------- |
| Node Name | Node name, must be unique to distinguish multiple nodes                                                                               |
| Host      | Target host identifier (IP or hostname)                                                                                               |
| UserName  | user name                                                                                                                             |
| PassWrod  | password                                                                                                                              |
| Domain    | domain                                                                                                                                |
| Server    | AE server name (e.g., `opcae://192.168.10.133/Matrikon.OPC.Alarms`). After filling in Host, click the dropdown to fetch server lists. |


## Supported Data Types

* string

Data example:
```json
{
  "source": "GEAK Source",
  "condition": "",
  "subCondition": "",
  "message": "GEAK",
  "time": "2026-01-06T13:40:25.6375708+08:00",
  "severity": 2,
  "eventType": 1,
  "categoryId": 3,
  "ackRequired": false,
  "activeTime": "0001-01-01T00:00:00",
  "newState": 0,
  "actorId": "",
  "clientHandle": "ae",
  "changeMask": 0,
  "quality": 0,
  "cookie": 0,
  "attributes": [
    100,
    200,
    300
  ]
}
```


## Address Format
When selecting the OPCAE node type in the Neuron HUB driver, the address is the event source path in the OPC AE server. You can use the `Export` function to export all point information as a table and import it directly into NEURON.


## Alarm Acknowledgment
Supports acknowledgment of Conditional alarms and writing comments.
