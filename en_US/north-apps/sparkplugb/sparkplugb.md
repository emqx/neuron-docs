# Introduction and Usage of Sparkplug B

## Module Description

Data collected by Neuron from the device can be transmitted from the edge to the Sparkplug_B application using the Sparkplug_B protocol. Users can also send data modification instructions to Neuron from the application. Sparkplug_B is an application-type protocol that runs on top of MQTT, so the setup in Neuron is similar to the MQTT driver.

## Parameter Configuration

| Parameter     | Description                                                  |
| ------------- | ------------------------------------------------------------ |
| **client-id** | MQTT client ID, A unique identifier that can represent the edge end, required |
| **group-id**  | The top-level logical group in Sparkplug_B, which can represent an entity such as a factory or workshop, required |
| **node-id**   | The unique identifier of the edge node in the Sparkplug_B protocol, required |
| **ssl**       | Whether to enable mqtt ssl, default false                    |
| **host**      | MQTT Broker host, required                                   |
| **port**      | MQTT Broker port number, required                            |
| **username**  | Username to use when connecting to the broker, optional      |
| **password**  | The password to use when connecting to the broker, optional  |
| **ca**        | ca file, only enabled when the ssl value is true, in which case it is required |
| **cert**      | cert file, only enabled when the ssl value is true, optional |
| **key**       | key file, only enabled when the ssl value is true, optional  |
| **keypass**   | key file password, only enabled when the ssl value is true, optional |