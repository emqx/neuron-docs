# Module List

## Southbound Plugin Modules

### Global Standards

|Icon| Protocol Name           | Interface  | Type        | Available | Remark |
|----| ----------------------- | ---------- | ----------- | --------- | -------------------------------- |
|![modbus](./assets/Modbus.png)| <div style="width:220pt">Modbus TCP</div>              | <div style="width:40pt">Ethernet</div>   | <div style="width:40pt">Open Source</div> | <div style="width:50pt">Yes</div>       |  |
|![modbus](./assets/Modbus.png)| <div style="width:220pt">Modbus RTU</div>              | <div style="width:40pt">Serial</div>     | <div style="width:110pt">Commercial</div>  | <div style="width:50pt">Yes</div>        |  |
|![modbus](./assets/Modbus.png)| <div style="width:220pt">Modbus RTU over TCP</div>     | <div style="width:40pt">Ethernet</div>   | <div style="width:110pt">Commercial</div>  | <div style="width:50pt">Yes</div>       |  |
|![opc-ua](./assets/OPCUA.png)| <div style="width:220pt">OPC UA</div>                  | <div style="width:40pt">Ethernet</div>   | <div style="width:110pt">Commercial</div>  | <div style="width:50pt">Yes</div>       |  |
|![ethernet](./assets/EtherNet.png)| <div style="width:220pt">CIP Ethernet/IP</div>         | <div style="width:40pt">Ethernet</div>   | <div style="width:110pt">Commercial</div>  | <div style="width:50pt">No</div>        | <div style="width:110pt">CIP – Common Industrial Protocol</div>  |

### PLC Drivers

|Icon| Protocol Name                                                | Interface | Type       | Available  | Remark                           |
|----| ------------------------------------------------------------ | --------- | ---------- | ---------- | -------------------------------- |
|![omron](./assets/OMRON.png)| <div style="width:220pt">Omron FINS on TCP</div>                                            | <div style="width:40pt">Ethernet</div>  | <div style="width:110pt">Commercial</div> | <div style="width:50pt">Yes</div>        | |
|![siemens](./assets/SIEMENS.png)| <div style="width:220pt">Siemens Industrial Ethernet ISO for S7-200/300/400/1200/1500</div> | <div style="width:40pt">Ethernet</div>  | <div style="width:110pt">Commercial</div> | <div style="width:50pt">Yes</div>        | |
|![mitsubishi](./assets/MITSUBISHI.png)| <div style="width:220pt">Mitsubishi MC Protocol for Q series and E71 module</div>           | <div style="width:40pt">Ethernet</div>  | <div style="width:110pt">Commercial</div> | <div style="width:50pt">Yes</div>        | |
|![rockwell](./assets/Rockwell.png)| <div style="width:220pt">Allen-Bradley DF1 half-duplex for PLC2</div>     | <div style="width:40pt">Serial</div>    | <div style="width:110pt">Commercial</div> | <div style="width:50pt">V1.x only</div>  | <div style="width:110pt">For PLC2 and PLC5</div>                |
|![schneider](./assets/Schneider.png)| <div style="width:220pt">Schneider PLC Modbus RTU</div>                                     | <div style="width:40pt">Serial</div>    | <div style="width:110pt">Commercial</div> | <div style="width:50pt">V1.x only</div>  | |
|![schneider](./assets/Schneider.png)| <div style="width:220pt">Schneider PLC Modbus TCP</div>                                     | <div style="width:40pt">Ethernet</div>  | <div style="width:110pt">Commercial</div> | <div style="width:50pt">V1.x only</div>  | |
|![schneider](./assets/Schneider.png)| <div style="width:220pt">Schneider Telemecanique UNI-TE</div>                               | <div style="width:40pt">Serial</div>    | <div style="width:110pt">Commercial</div> | <div style="width:50pt">V1.x only</div>  | |
|![abb](./assets/ABB.png)| <div style="width:220pt">ABB SattControl Comli</div>                                        | <div style="width:40pt">Serial</div>    | <div style="width:110pt">Commercial</div> | <div style="width:50pt">V1.x only</div>  | |
|![omron](./assets/OMRON.png)| <div style="width:220pt">Omron Host Link</div>                                              | <div style="width:40pt">Serial</div>    | <div style="width:110pt">Commercial</div> | <div style="width:50pt">V1.x only</div>  | <div style="width:110pt">For Single and Multiple connection</div> |
|![omron](./assets/OMRON.png)| <div style="width:220pt">Omron FINS on Host Link</div>                                      | <div style="width:40pt">Serial</div>    | <div style="width:110pt">Commercial</div> | <div style="width:50pt">V1.x only</div>  | |
|![siemens](./assets/SIEMENS.png)| <div style="width:220pt">Siemens 3964R/RK512</div>                                          | <div style="width:40pt">Serial</div>    | <div style="width:110pt">Commercial</div> | <div style="width:50pt">V1.x only</div>  | <div style="width:110pt">For S5 and S7</div> |
|![siemens](./assets/SIEMENS.png)| <div style="width:220pt">Siemens Fetch Write for S7-300/400 and CP443 module</div>          | <div style="width:40pt">Ethernet</div>  | <div style="width:110pt">Commercial</div> | <div style="width:50pt">V1.x only</div>  | |
|![mitsubishi](./assets/MITSUBISHI.png)| <div style="width:220pt">Mitsubishi FX Series</div>                                         | <div style="width:40pt">Serial</div>    | <div style="width:110pt">Commercial</div> | <div style="width:50pt">V1.x only</div>  | |
|![mitsubishi](./assets/MITSUBISHI.png)| <div style="width:220pt">Mitsubishi MC Protocol for Q series and C24 module</div>           | <div style="width:40pt">Serial</div>    | <div style="width:110pt">Commercial</div> | <div style="width:50pt">V1.x only</div>  | |
|![mitsubishi](./assets/MITSUBISHI.png)| <div style="width:220pt">Mitsubishi 232ADP/485BD: Serial/RS485</div>                        | <div style="width:40pt">Serialv</div>   | <div style="width:110pt">Commercial</div> | <div style="width:50pt">No</div>         | |
|![mitsubishi](./assets/MITSUBISHI.png)| <div style="width:220pt">Mitsubishi FX3U-ENET-ADP</div>                                     | <div style="width:40pt">Ethernet</div>  | <div style="width:110pt">Commercial</div> | <div style="width:50pt">No</div>         | <div style="width:110pt">For FX only</div> |
|![panasonic](./assets/Panasonic.png)| <div style="width:220pt">Panasonic FP series MEWTOCOL-COM</div>                             | <div style="width:40pt">Serial</div>    | <div style="width:110pt">Commercial</div> | <div style="width:50pt">No</div>         | |
|![panasonic](./assets/Panasonic.png)| <div style="width:220pt">Panasonic FP series MEWTOCOL-COM</div>                             | <div style="width:40pt">Ethernet</div>  | <div style="width:110pt">Commercial</div> | <div style="width:50pt">No</div>         | |
|![panasonic](./assets/Panasonic.png)| <div style="width:220pt">Panasonic FP series MEWTOCOL-DAT</div>                             | <div style="width:40pt">Ethernet</div>  | <div style="width:110pt">Commercial</div> | <div style="width:50pt">No</div>         | |
|![beckhoff](./assets/BECKHOFF.png)| <div style="width:220pt">Beckhoff ADS/AMS TCPIP</div>                                       | <div style="width:40pt">Ethernet</div>  | <div style="width:110pt">Commercial</div> | <div style="width:50pt">No</div>         | |
|![keyence](./assets/KEYENCE.png)| <div style="width:220pt">Keyence CIP Ethernet/IP</div>                                      | <div style="width:40pt">Ethernet</div>  | <div style="width:110pt">Commercial</div> | <div style="width:50pt">No</div>         | <div style="width:110pt">CIP – Common Industrial Protocol</div> |
|![keyence](./assets/KEYENCE.png)| <div style="width:220pt">Keyence MC Protocol</div>                                          | <div style="width:40pt">Ethernet</div>  | <div style="width:110pt">Commercial</div> | <div style="width:50pt">No</div>         | <div style="width:110pt">Mitsubishi MC Protocol</div> |
|![aelta](./assets/AELTA.png)| <div style="width:220pt">Delta DVP communication protocol</div>                             | <div style="width:40pt">Serial</div>    | <div style="width:110pt">Commercial</div> | <div style="width:50pt">No</div>         | |
|![aelta](./assets/AELTA.png)| <div style="width:220pt">Delta Modbus TCP</div>                                             | <div style="width:40pt">Ethernet</div>  | <div style="width:110pt">Commercial</div> | <div style="width:50pt">No</div>         | |
|![aelta](./assets/AELTA.png)| <div style="width:220pt">Delta CIP Ethernet/IP</div>                                        | <div style="width:40pt">Ethernet</div>  | <div style="width:110pt">Commercial</div> | <div style="width:50pt">No</div>         | |
|![fatek](./assets/FATEK.png)| <div style="width:220pt">Fatek FACON serial</div>                                           | <div style="width:40pt">Serial</div>    | <div style="width:110pt">Commercial</div> | <div style="width:50pt">No</div>         | |
|![fatek](./assets/FATEK.png)| <div style="width:220pt">Fatek FACON ethernet</div>                                         | <div style="width:40pt">Ethernet</div>  | <div style="width:110pt">Commercial</div> | <div style="width:50pt">No</div>         | |
|![fanuc](./assets/FANUC.png)| <div style="width:220pt">GE FANUC 90-30 SNPX</div>                                          | <div style="width:40pt">Serial</div>    | <div style="width:110pt">Commercial</div> | <div style="width:50pt">No</div>         | |
|![fanuc](./assets/FANUC.png)| <div style="width:220pt">GE FANUC 90-30 Ethernet SRTP</div>                                 | <div style="width:40pt">Ethernet</div>  | <div style="width:110pt">Commercial</div> | <div style="width:50pt">No</div>         | |

### Electricity

|Icon| Protocol Name       | Interface | Type       | Available | Remark     |
|----| ------------------- | --------- | ---------- | --------- | ---------- |
|![dlt645](./assets/GB.png)| <div style="width:220pt">DL/T645-07</div>          | <div style="width:40pt">Serial</div>    | <div style="width:110pt">Commercial</div> | <div style="width:50pt">Yes</div>       | <div style="width:110pt">Chinese standards for power meters</div>  |
|![iec](./assets/IEC.png)| <div style="width:220pt">IEC 60870-5-104</div>     | <div style="width:40pt">Ethernet</div>  | <div style="width:110pt">Commercial</div> | <div style="width:50pt">Yes</div>       | |
|![iec](./assets/IEC.png)| <div style="width:220pt">IEC 60870-5-101</div>      | <div style="width:40pt">Serial</div>     | <div style="width:110pt">Commercial</div>  | <div style="width:50pt">No</div>         | |
|![iec](./assets/IEC.png)| <div style="width:220pt">IEC 61850</div>           | <div style="width:40pt">Ethernet</div>  | <div style="width:110pt">Commercial</div> | <div style="width:50pt">No</div>        | |
|![dnp3](./assets/DNP3.png)| <div style="width:220pt">DNP3</div>                | <div style="width:40pt">Ethernet</div>  | <div style="width:110pt">Commercial</div> | <div style="width:50pt">No</div>        | |

### Building Automation

|Icon| Protocol Name  | Interface  | Type       | Available | Remark |
|----| -------------- | ---------- | ---------- | --------- | --------- |
|![knxnet](./assets/KNX.png)| <div style="width:220pt">KNXnet IP</div>      | <div style="width:40pt">Ethernet</div>   | <div style="width:110pt">Commercial</div> | <div style="width:50pt">Yes</div> |  |
|![bacnet](./assets/BACnet.png)| <div style="width:220pt">BACnet IP</div>      | <div style="width:40pt">Ethernet</div>   | <div style="width:110pt">Commercial</div> | <div style="width:50pt">Yes</div> |  |
|![bacnet](./assets/BACnet.png)| <div style="width:220pt">BACnet MS/TP</div>    | <div style="width:40pt">Serial</div>      | <div style="width:110pt">Commercial</div>  | <div style="width:50pt">No</div>  | <div style="width:110pt"> </div> |
|![lon](./assets/LonWorks.png)| <div style="width:220pt">LON</div>            | <div style="width:40pt">Ethernet</div>   | <div style="width:110pt">Commercial</div> | <div style="width:50pt">No</div> |  |

### CNC Machines & Robotics

|Icon| Protocol Name  | Interface  | Type       | Available | Remark |
|----| ------------- | ------- | ----- | --------- | ------- |
|![mt-connect](./assets/MT.png)| <div style="width:220pt">MTConnect</div>      | <div style="width:40pt">Ethernet</div>    | <div style="width:110pt">Commercial</div>    | <div style="width:50pt">No</div>         | <div style="width:110pt"> </div> |

## Northbound Plugin Modules

### Cloud Connectivity

|Icon| Protocol Name         | Type        | Available | Remark |
|----| --------------------- | ----------- | --------- | ------- |
|![restful-api](./assets/RESTFUL-API.png)| <div style="width:295pt">RESTful API</div>           | <div style="width:110pt">Open Soure</div>  | <div style="width:50pt">Yes</div>       |  |
|![mqtt](./assets/MQTT.png)| <div style="width:295pt">MQTT</div>                   | <div style="width:110pt">Open Source</div>  | <div style="width:50pt">Yes</div>        | <div style="width:110pt"> </div> |
|![sparkplug](./assets/Sparkplug.png)| <div style="width:295pt">MQTT + Sparkplug B</div>    | <div style="width:110pt">Commercial</div>  | <div style="width:50pt">Yes</div>       |  |
|![websocket](./assets/Websocket.png)| <div style="width:295pt">Websocket</div>             | <div style="width:110pt">Commercial</div>  | <div style="width:50pt">No</div>        |  |

### Application

|Icon| Protocol Name         | Type        | Available | Remark |
|——| --------------------- | ----------- | --------- | ------- |
|![ekuiper](./assets/ekuiper.png)| <div style="width:295pt">eKuiper Stream Processing Engine</div>    | <div style="width:110pt">Open Source</div>  | <div style="width:50pt">Yes</div>        | <div style="width:110pt"> </div> |

## EMQ License for commercial modules

* Core framework, dashboard and modbus, mqtt and eKuiper pluggable modules are open source under LGPLv3 license. Neuron could run with these modules without a license installed. A valid trial or official EMQ license must be installed if you need any one or more of the commercial modules as mentioned above.

* A trial EMQ license can be download from our official website [https://www.emqx.com/en/apply-licenses/neuron](https://www.emqx.com/en/apply-licenses/neuron). All available modules could be used with limitation on 100 connections and 1000 data tags for 15 days. If trial EMQ license is expired, you can re-apply the trial EMQ license via our official website again. However, a mailbox can only apply for a trial license up to two times.

* Each plugin module can be authorized independently in EMQ license.

