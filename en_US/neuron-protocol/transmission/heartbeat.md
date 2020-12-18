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

**_Neuron heartbeat syntax_**

```json
{

"tstp": 1581515618,

"comm": "UP",

"mach": "MANU",

"mode": "ACTIVE",

"mqcn": "MQCONNECT",

"dalm": "NON-EXIST",

"galm": "UNACKNOWLEDGE",

"ngal": 4,

"grow": \[{

"acat": "alarm",

"astt": "OFF",

"amod": "UNACKALARM",

"atim": 1581513580,

"alid": 1,

"comt": "temp1@Temp (812) < low@Temp (800)"

}, {

"acat": "alarm",

"astt": "ON",

"amod": "UNACKALARM",

"atim": 1581515415,

"alid": 3,

"comt": "temp2@Temp (791) < low@Temp (800)"

}, {

"acat": "critical",

"astt": "ON",

"amod": "UNACKALARM",

"atim": 1581515415,

"alid": 4,

"comt": "temp3@Temp (864) > high@Temp (850)"

}, {

"acat": "alarm",

"astt": "OFF",

"amod": "UNACKALARM",

"atim": 1581513592,

"alid": 5,

"comt": "temp3@Temp (864) < low@Temp (800)"

}]

}
```

| Heartbeat |                                                       |
| --------- | ----------------------------------------------------- |
| **tstp**  | TimeStamp                                             |
| **comm**  | PLC or hardware communication status                  |
|           | UP                                                    |
|           | DOWN                                                  |
| **mach**  | Machine Mode                                          |
|           | AUTO                                                  |
|           | MANU                                                  |
|           | SERV                                                  |
| **mode**  | Please refer to Status Mode section.                  |
|           | Inactive Mode                                         |
|           | Standby Mode / Semi-Standby Mode                      |
|           | Active Mode / Semi-Active Mode                        |
| **mqcn**  | MQ broker connection status                           |
|           | MQCONNECT                                             |
|           | MQDISCONNECT                                          |
| **dalm**  | Device Alarm which specify which device has           |
|           | communication problem.                                |
| **ndal**  | Number of device alarms                               |
| **drow**  | Device alarm rows                                     |
| **chnl**  | Channel number of devices                             |
| **addr**  | Address of devices                                    |
| **galm**  | General Alarm which user define their own alarms and  |
|           | triggers                                              |
| **ngal**  | Number of general alarms                              |
| **grow**  | General alarm rows                                    |
| **acat**  | Alarm Category                                        |
|           | critical                                              |
|           | alarm                                                 |
|           | warning                                               |
|           | event                                                 |
|           | view                                                  |
| **astt**  | Alarm Status                                          |
|           | ON                                                    |
|           | OFF                                                   |
| **amod**  | Alarm Mode                                            |
|           | UNACKALARM                                            |
|           | DISABLE                                               |
| **atim**  | Alarm TimeStamp                                       |
| **alid**  | Alarm ID                                              |
|           | must be copied this ID when user acknowledge function |
|           | 80                                                    |
| **comt**  | Alarm Comments                                        |
