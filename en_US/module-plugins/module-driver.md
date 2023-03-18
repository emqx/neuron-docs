# Module Setting

This document introduces how to setup parameter and data tag point information in configuration for northbound applications and southbound drivers.

::: tip
uint16 corresponds to the word type. uint32 corresponds to dword type.
:::

## MQTT

The data collected from the device can be transmitted to the mqtt broker through mqtt application, and instructions can be sent to neuron through mqtt application.

### Parameter Setting

| Parameter           | Description                                                  |
| ------------------- | ------------------------------------------------------------ |
| **client-id**       | MQTT client id for communication, required. (default to node name) |
| **upload-topic**    | Subscription data reporting topic, required                  |
| **format**          | The json format selection of the reported data, required, there are values mode and tags mode, the default is values mode |
| **cache-mem-size**  | In-memory cache limit (MB) in case of communication failure, required. Range in [0, 1024], default 0. Should not be larger than *cache-disk-size*. |
| **cache-disk-size** | In-disk cache limit (MB) in case of communication failure, required. Range in [0, 10240], default 0. If nonzero, *cache-mem-size* should also be nonzero. |
| **host**            | MQTT Broker host, required                                   |
| **port**            | MQTT Broker port number, required                            |
| **username**        | Username to use when connecting to the broker, optional      |
| **password**        | The password to use when connecting to the broker, optional  |
| **ssl**             | Whether to enable mqtt ssl, default false                    |
| **ca**              | ca file, only enabled when the ssl value is true, in which case it is required |
| **cert**            | cert file, only enabled when the ssl value is true, optional |
| **key**             | key file, only enabled when the ssl value is true, optional  |
| **keypass**         | key file password, only enabled when the ssl value is true, optional |



## Sparkplug_B

Data collected by Neuron from the device can be transmitted from the edge to the Sparkplug_B application using the Sparkplug_B protocol. Users can also send data modification instructions to Neuron from the application. Sparkplug_B is an application-type protocol that runs on top of MQTT, so the setup in Neuron is similar to the MQTT driver.

### Parameter Setting

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
