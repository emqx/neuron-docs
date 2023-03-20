# MQTT

## Module Description

The data collected from the device can be transmitted to the mqtt broker through mqtt application, and instructions can be sent to neuron through mqtt application.

## Parameter Configurations

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
