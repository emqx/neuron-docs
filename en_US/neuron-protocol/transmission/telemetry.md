# Telemetry

Telemetry is where the time series data sending to IIoT platform in time
series. Telemetry structure will depend on how object and data tags are
defined by users in the configuration. Basically, telemetry would
contain timestamp in the message.

**_MQTT Topics for Neuron_**

Publish: Neuron/Telemetry /%UUID%

**_MQTT Topics for IIoT platform_**

Subscribe: Neuron/Telemetry /%UUID%

![](../assets/timeseries-telemetry-on-mqtt.png)

![](../assets/timeseries-telemetry-on-websockets.png)

**_Neuron telemetry syntax_**

```json
{
  "tele": [
    {
      "objn": "Tank[0]",
      "tstp": 1552532233,
      "temperature": 81.2,
      "energy": 2181.8,
      "switch": 1,
      "buzzer": 0
    },
    {
      "objn": "Tank[1]",
      "tstp": 1552532233,
      "temperature": 79.1,
      "energy": 3176.2,
      "switch": 1,
      "buzzer@": 0
    },
    {
      "objn": "Tank[2]",
      "tstp": 1552532233,
      "temperature": 86.4,
      "energy": 1146.3,
      "switch": 0,
      "buzzer": 1
    },
    {
      "objn": "Temp[0]",
      "tstp": 1552532233,
      "high": 85,
      "temp1": 81.2,
      "temp2": 79.1,
      "temp": 86.4,
      "low": 80
    },
    {
      "objn": "Energy[0]",
      "tstp": 1552532233,
      "energy1": 2181.8,
      "energy2": 3176.2,
      "energy3": 1146.3
    }
  ]
}
```

OR

```json
{
  "Tank[0].temperature": 81.2,
  "Tank[0].energy@Tank_1": 2181.8,
  "Tank[0].switch@Tank_1": 1,
  "Tank[0].buzzer@Tank_1": 0,
  "Tank[1].temperature": 79.1,
  "Tank[1].energy": 3176.2,
  "Tank[1].switch": 1,
  "Tank[1].buzzer": 0,
  "Tank[2].temperature": 86.4,
  "Tank[2].energy": 1146.3,
  "Tank[2].switch": 0,
  "Tank[2].buzzer": 1,
  "Temp[0].high": 85,
  "Temp[0].temp1": 81.2,
  "Temp[0].temp2": 79.1,
  "Temp[0].temp3": 86.4,
  "Temp[0].low": 80,
  "Energy[0].energy1": 2181.8,
  "Energy[0].energy2": 3176.2,
  "Energy[0].energy3": 1146.3
}
```



| Telemetry |                 |
| --------- | --------------- |
| **tele**  | Telemetry Array |
| **objn**  | Object Name     |
| **tstp**  | TimeStamp       |
