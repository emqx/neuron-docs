# Offline Data Cache

Neuron can store data in memory and also support caching data on disk, making it convenient for users to store larger amounts of data. The size of disk storage data is set in the ```Cache disk size``` section of **Northbound Application Management -> Application Configuration**.

When MQTT is offline, Neuron will preferentially store the data in memory. After MQTT is restored to online status, the cached data will be sent to MQTT Broker. The size of cache data is set in the ```Cache memory size``` section of **Northbound Application Management -> Application Configuration**.