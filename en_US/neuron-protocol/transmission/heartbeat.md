# Heartbeat

For each certain period, Neuron would send a heartbeat to the IIoT
platform for aliveness. If IIoT platform can't receive this heartbeat in
certain time (e.g. 5 seconds), it may treat the Neuron as dead. In
addition, heartbeat message may contain some useful information such as
alarm status, running mode, communication status and data usage.

**_MQTT Topics for Neuron_**

Publish: Neuron/Heartbeat/%UUID%

**_MQTT Topics for IIoT platform_**

Subscribe: Neuron/Heartbeat/%UUID%

![](../assets/heartbeat-on-mqtt.png)

![](../assets/heartbeat-on-websockets.png)

**Neuron agent heartbeat status syntax**

```json
{
    "type": "status",
    "tstp":	1581515618,
    "comm":	"UP",
    "mach":	"MANU",
    "mode":	"ACTIVE",
    "mqcn":	"MQCONNECT",
    "galm":	"UNACKNOWLEDGE"
}
```

| Heartbeat  |                                                              |
| ---------- | ------------------------------------------------------------ |
| **tstp** | TimeStamp                                                    |
| **comm** | PLC or hardware communication statusUPDOWN                   |
| **mach** | Machine ModeAUTOMANUSERV                                     |
| **mode** | Please refer to Status Mode section.Inactive ModeStandby Mode / Semi-Standby ModeActive Mode / Semi-Active Mode |
| **mqcn** | MQ broker connection statusMQCONNECTMQDISCONNECT             |
| **galm** | General Alarm which user define their own alarms and triggers |



***Neuron agent heartbeat alarm syntax***

```json
{
  "type": "alarm",
  "ngal": 4,
  "grow": [
    {
      "acat": "alarm",
      "astt": "OFF",
      "amod": "UNACKALARM",
      "atim": 1581513580,
      "alid": 1,
      "comt": "Temp[0].temp1 (812) < Temp[0].low (800)"
    },
    {
      "acat": "alarm",
      "astt": "ON",
      "amod": "UNACKALARM",
      "atim": 1581515415,
      "alid": 3,
      "comt": "Temp[0].temp2 (791) < Temp[0].low (800)"
    },
    {
      "acat": "critical",
      "astt": "ON",
      "amod": "UNACKALARM",
      "atim": 1581515415,
      "alid": 4,
      "comt": "Temp[0].temp3 (864) > Temp[0].high (850)"
    },
    {
      "acat": "alarm",
      "astt": "OFF",
      "amod": "UNACKALARM",
      "atim": 1581513592,
      "alid": 5,
      "comt": "Temp[0].temp3 (864) < Temp[0].low (800)"
    }
  ]
}
```

| Heartbeat                |                                                              |
| ------------------------ | ------------------------------------------------------------ |
| **ngal**           | Number of general alarms                                     |
| **grow** | General alarm rows                                           |
| **acat** | Alarm Categorycriticalalarmwarningeventview                  |
| **astt**           | Alarm Status ONOFF                                           |
| **amod** | Alarm Mode UNACKALARMDISABLE                                 |
| **atim** | Alarm TimeStamp                                              |
| **alid** | Alarm ID must be copied this ID when user acknowledge function 80 |
| **comt** | Alarm Comments                                               |

 