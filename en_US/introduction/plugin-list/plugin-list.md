# Plugin List

## View All Available Plugins

The plugin management page displays all the pluggable modules available and detailed information, including the name of the plug-in, associated node type, plug-in category, driver library name and description, as shown in the following figure.

![plugin-options](./assets/plugin-options.png)

Click the `Document` button in the upper right corner of the plugin card to jump to the documentation for the specific use and description of the driver.

The plug-in types include the following 3 modes:

* Static: cannot be deleted
* System: cannot be deleted, native
* Custom: Deletable, user-developed or custom-developed

:::tip
Users can filter out the plugins for northbound applications or southbound devices from the dropdown box.
:::

## Add a New Pluggable Module

Click on the `Add Plugin` button in the upper right corner as shown below

![plugin-add](./assets/plugin-add.png)

To add a new Pluggable module,

* Fill in the path and file name of the .so file that needs to be added.
* Click on the `Create` button to move .so file to the build directory.

:::tip
Please make sure that the plugin .so file you have written is placed under the neuron/build/plugins directory before adding it. For specific plugin development tutorials, please refer to [SDK Tutorial](../../dev-guide/sdk-tutorial/sdk-tutorial.md).
:::

## Southbound Plugin Modules

### Global Standards

| Protocol Name           | Interface  | Type        | Available | Remark |
| ----------------------- | ---------- | ----------- | --------- | -------------------------------- |
| <div style="width:220pt">Modbus TCP</div>              | <div style="width:40pt">Ethernet</div>   | <div style="width:40pt">Open Source</div> | <div style="width:50pt">Yes</div>       |  |
| <div style="width:220pt">Modbus RTU</div>              | <div style="width:40pt">Serial</div>     | <div style="width:110pt">Open Source</div>  | <div style="width:50pt">Yes</div>        |  |
| <div style="width:220pt">Modbus RTU over TCP</div>     | <div style="width:40pt">Ethernet</div>   | <div style="width:110pt">Open Source</div>  | <div style="width:50pt">Yes</div>       |  |
| <div style="width:220pt">OPC UA</div>                  | <div style="width:40pt">Ethernet</div>   | <div style="width:110pt">Commercial</div>  | <div style="width:50pt">Yes</div>       |  |
| <div style="width:220pt">CIP Ethernet/IP</div>         | <div style="width:40pt">Ethernet</div>   | <div style="width:110pt">Commercial</div>  | <div style="width:50pt">Yes</div>        | <div style="width:110pt">CIP – Common Industrial Protocol</div>  |

### PLC Drivers

| Protocol Name                                                | Interface | Type       | Available  | Remark                           |
| ------------------------------------------------------------ | --------- | ---------- | ---------- | -------------------------------- |
| <div style="width:220pt">Siemens 3964R/RK512</div>                                          | <div style="width:40pt">Serial</div>    | <div style="width:110pt">Commercial</div> | <div style="width:50pt">V1.x only</div>  | <div style="width:110pt">For S5 and S7</div> |
| <div style="width:220pt">Siemens Industrial Ethernet ISO for S7-200/300/400/1200/1500</div> | <div style="width:40pt">Ethernet</div>  | <div style="width:110pt">Commercial</div> | <div style="width:50pt">Yes</div>        | |
| <div style="width:220pt">Siemens Fetch Write for S7-300/400 and CP443 module</div>          | <div style="width:40pt">Ethernet</div>  | <div style="width:110pt">Commercial</div> | <div style="width:50pt">Yes</div>  | |
| <div style="width:220pt">Allen-Bradley DF1 half-duplex</div>     | <div style="width:40pt">Serial</div>    | <div style="width:110pt">Commercial</div> | <div style="width:50pt">Yes</div>  | <div style="width:110pt">For PLC2 and PLC5</div>                |
| <div style="width:220pt">Allen-Bradley CIP EtherNet/IP</div>     | <div style="width:40pt">Ethernet</div>    | <div style="width:110pt">Commercial</div> | <div style="width:50pt">Yes</div>  | <div style="width:110pt">CIP – Common Industrial Protocol</div>                |
| <div style="width:220pt">Schneider PLC Modbus RTU</div>                                     | <div style="width:40pt">Serial</div>    | <div style="width:110pt">Commercial</div> | <div style="width:50pt">V1.x only</div>  | |
| <div style="width:220pt">Schneider PLC Modbus TCP</div>                                     | <div style="width:40pt">Ethernet</div>  | <div style="width:110pt">Commercial</div> | <div style="width:50pt">V1.x only</div>  | |
| <div style="width:220pt">Schneider Telemecanique UNI-TE</div>                               | <div style="width:40pt">Serial</div>    | <div style="width:110pt">Commercial</div> | <div style="width:50pt">V1.x only</div>  | |
| <div style="width:220pt">ABB SattControl Comli</div>                                        | <div style="width:40pt">Serial</div>    | <div style="width:110pt">Commercial</div> | <div style="width:50pt">Yes</div>  | |
| <div style="width:220pt">Omron Host Link</div>                                              | <div style="width:40pt">Serial</div>    | <div style="width:110pt">Commercial</div> | <div style="width:50pt">V1.x only</div>  | <div style="width:110pt">For Single and Multiple connection</div> |
| <div style="width:220pt">Omron FINS on Host Link</div>                                      | <div style="width:40pt">Serial</div>    | <div style="width:110pt">Commercial</div> | <div style="width:50pt">V1.x only</div>  | |
| <div style="width:220pt">Omron FINS on TCP</div>                                            | <div style="width:40pt">Ethernet</div>  | <div style="width:110pt">Commercial</div> | <div style="width:50pt">Yes</div>        | |
| <div style="width:220pt">Omron FINS on UDP</div>                                            | <div style="width:40pt">Ethernet</div>  | <div style="width:110pt">Commercial</div> | <div style="width:50pt">Yes</div>        | |
| <div style="width:220pt">Mitsubishi MC Protocol for Q series and C24 module</div>           | <div style="width:40pt">Serial</div>    | <div style="width:110pt">Commercial</div> | <div style="width:50pt">V1.x only</div>  | |
| <div style="width:220pt">Mitsubishi MC Protocol for Q series and E71 module</div>           | <div style="width:40pt">Ethernet</div>  | <div style="width:110pt">Commercial</div> | <div style="width:50pt">Yes</div>        | <div style="width:110pt">3E frame</div> |
| <div style="width:220pt">Mitsubishi FX Series</div>                                         | <div style="width:40pt">Serial</div>    | <div style="width:110pt">Commercial</div> | <div style="width:50pt">V1.x only</div>  | |
| <div style="width:220pt">Mitsubishi FX3U-ENET-ADP</div>                                     | <div style="width:40pt">Ethernet</div>  | <div style="width:110pt">Commercial</div> | <div style="width:50pt">Yes</div>         | <div style="width:110pt">1E frame</div> |
| <div style="width:220pt">Mitsubishi 232ADP/485BD: Serial/RS485</div>                        | <div style="width:40pt">Serial</div>    | <div style="width:110pt">Commercial</div> | <div style="width:50pt">No</div>         | |
| <div style="width:220pt">Panasonic FP series MEWTOCOL-COM</div>                             | <div style="width:40pt">Serial</div>    | <div style="width:110pt">Commercial</div> | <div style="width:50pt">No</div>         | |
| <div style="width:220pt">Panasonic FP series MEWTOCOL-COM</div>                             | <div style="width:40pt">Ethernet</div>  | <div style="width:110pt">Commercial</div> | <div style="width:50pt">Yes</div>         | |
| <div style="width:220pt">Panasonic FP series MEWTOCOL-DAT</div>                             | <div style="width:40pt">Ethernet</div>  | <div style="width:110pt">Commercial</div> | <div style="width:50pt">No</div>         | |
| <div style="width:220pt">Beckhoff ADS/AMS TCPIP</div>                                       | <div style="width:40pt">Ethernet</div>  | <div style="width:110pt">Commercial</div> | <div style="width:50pt">Yes</div>         | |
| <div style="width:220pt">Keyence CIP Ethernet/IP</div>                                      | <div style="width:40pt">Ethernet</div>  | <div style="width:110pt">Commercial</div> | <div style="width:50pt">Yes</div>         | <div style="width:110pt">CIP – Common Industrial Protocol</div> |
| <div style="width:220pt">Keyence MC Protocol</div>                                          | <div style="width:40pt">Ethernet</div>  | <div style="width:110pt">Commercial</div> | <div style="width:50pt">Yes</div>         | <div style="width:110pt">Mitsubishi MC Protocol</div> |
| <div style="width:220pt">Delta DVP communication protocol</div>                             | <div style="width:40pt">Serial</div>    | <div style="width:110pt">Commercial</div> | <div style="width:50pt">No</div>         | |
| <div style="width:220pt">Delta Modbus TCP</div>                                             | <div style="width:40pt">Ethernet</div>  | <div style="width:110pt">Commercial</div> | <div style="width:50pt">Yes</div>         | |
| <div style="width:220pt">Delta CIP Ethernet/IP</div>                                        | <div style="width:40pt">Ethernet</div>  | <div style="width:110pt">Commercial</div> | <div style="width:50pt">Yes</div>         | <div style="width:110pt">CIP – Common Industrial Protocol</div> |
| <div style="width:220pt">Fatek FACON serial</div>                                           | <div style="width:40pt">Serial</div>    | <div style="width:110pt">Commercial</div> | <div style="width:50pt">No</div>         | |
| <div style="width:220pt">Fatek FACON ethernet</div>                                         | <div style="width:40pt">Ethernet</div>  | <div style="width:110pt">Commercial</div> | <div style="width:50pt">No</div>         | |
| <div style="width:220pt">GE FANUC 90-30 SNPX</div>                                          | <div style="width:40pt">Serial</div>    | <div style="width:110pt">Commercial</div> | <div style="width:50pt">No</div>         | |
| <div style="width:220pt">GE FANUC 90-30 Ethernet SRTP</div>                                 | <div style="width:40pt">Ethernet</div>  | <div style="width:110pt">Commercial</div> | <div style="width:50pt">No</div>         | |

### Electricity

| Protocol Name       | Interface | Type       | Available | Remark     |
| ------------------- | --------- | ---------- | --------- | ---------- |
| <div style="width:220pt">DL/T645-1997</div>          | <div style="width:40pt">Serial</div>    | <div style="width:110pt">Commercial</div> | <div style="width:50pt">Yes</div>       | <div style="width:110pt">Chinese standards for power meters</div>  |
| <div style="width:220pt">DL/T645-2007</div>          | <div style="width:40pt">Serial</div>    | <div style="width:110pt">Commercial</div> | <div style="width:50pt">Yes</div>       | <div style="width:110pt">Chinese standards for power meters</div>  |
| <div style="width:220pt">IEC 60870-5-101</div>      | <div style="width:40pt">Serial</div>     | <div style="width:110pt">Commercial</div>  | <div style="width:50pt">No</div>         | |
| <div style="width:220pt">IEC 60870-5-102</div>      | <div style="width:40pt">Serial</div>     | <div style="width:110pt">Commercial</div>  | <div style="width:50pt">No</div>         | |
| <div style="width:220pt">IEC 60870-5-103</div>      | <div style="width:40pt">Serial</div>     | <div style="width:110pt">Commercial</div>  | <div style="width:50pt">No</div>         | |
| <div style="width:220pt">IEC 60870-5-104</div>      | <div style="width:40pt">Ethernet</div>  | <div style="width:110pt">Commercial</div> | <div style="width:50pt">Yes</div>       | |
| <div style="width:220pt">IEC 61850</div>           | <div style="width:40pt">Ethernet</div>  | <div style="width:110pt">Commercial</div> | <div style="width:50pt">Yes</div>        | |
| <div style="width:220pt">DNP3</div>                | <div style="width:40pt">Ethernet</div>  | <div style="width:110pt">Commercial</div> | <div style="width:50pt">No</div>        | |

### Building Automation

| Protocol Name  | Interface  | Type       | Available | Remark |
| -------------- | ---------- | ---------- | --------- | --------- |
| <div style="width:220pt">KNXnet IP</div>      | <div style="width:40pt">Ethernet</div>   | <div style="width:110pt">Commercial</div> | <div style="width:50pt">Yes</div> |  |
| <div style="width:220pt">BACnet IP</div>      | <div style="width:40pt">Ethernet</div>   | <div style="width:110pt">Commercial</div> | <div style="width:50pt">Yes</div> |  |
| <div style="width:220pt">BACnet MS/TP</div>    | <div style="width:40pt">Serial</div>      | <div style="width:110pt">Commercial</div>  | <div style="width:50pt">No</div>  | <div style="width:110pt"> </div> |
| <div style="width:220pt">LON</div>            | <div style="width:40pt">Ethernet</div>   | <div style="width:110pt">Commercial</div> | <div style="width:50pt">No</div> |  |

### CNC Machines & Robotics

| Protocol Name  | Interface  | Type       | Available | Remark |
| -------------- | ---------- | ---------- | --------- | ------ |
| <div style="width:220pt">MTConnect</div>      | <div style="width:40pt">Ethernet</div>    | <div style="width:110pt">Commercial</div>    | <div style="width:50pt">No</div>         | <div style="width:110pt"> </div> |
| <div style="width:220pt">Fanuc 0i, 30i, 31i, 32i and 35i</div>      | <div style="width:40pt">Ethernet</div>    | <div style="width:110pt">Commercial</div>    | <div style="width:50pt">Yes</div>         | <div style="width:110pt"> </div> |
| <div style="width:220pt">Mitsubishi M800/M80</div>      | <div style="width:40pt">Ethernet</div>    | <div style="width:110pt">Commercial</div>    | <div style="width:50pt">No</div>         | <div style="width:110pt"> </div> |
| <div style="width:220pt">Siemens 840D、810、828D</div>      | <div style="width:40pt">Ethernet</div>    | <div style="width:110pt">Commercial</div>    | <div style="width:50pt">No</div>         | <div style="width:110pt"> </div> |

## Northbound Plugin Modules

### Cloud Connectivity

| Protocol Name         | Type        | Available | Remark |
| --------------------- | ----------- | --------- | ------- |
| <div style="width:295pt">RESTful API</div>           | <div style="width:110pt">Open Source</div>  | <div style="width:50pt">Yes</div>       |  |
| <div style="width:295pt">MQTT</div>                   | <div style="width:110pt">Open Source</div>  | <div style="width:50pt">Yes</div>        | <div style="width:110pt"> </div> |
| <div style="width:295pt">MQTT Sparkplug B</div>    | <div style="width:110pt">Commercial</div>  | <div style="width:50pt">Yes</div>       |  |
| <div style="width:295pt">Websocket</div>             | <div style="width:110pt">Commercial</div>  | <div style="width:50pt">Yes</div>        |  |

### Application

| Protocol Name         | Type        | Available | Remark |
| --------------------- | ----------- | --------- | ------- |
| <div style="width:295pt">eKuiper Stream Processing</div>    | <div style="width:110pt">Open Source</div>  | <div style="width:50pt">Yes</div>        | <div style="width:110pt"> </div> |

## EMQ License Policy for Commercial Modules

Core framework, dashboard, and a few plugin modules such as Modbus TCP, MQT, and eKuiper are open source under LGPLv3 license. Neuron may run with these open-source modules without an EMQ license. But all other commercial plugin modules require an official EMQ license to run without limitation. 

:::tip 30 Connections forever free

For these commercial modules, Neuron also provides a forever free quota (with 30 connections and 30 data tags) for your exploration. 

Note: The Fanuc Focas Ethernet and Mitsubishi CNC plugins are not within the scope of the 30-point free-for-life offer. If you wish to try them out, you can directly [contact us](https://www.emqx.com/en/contact?product=neuron).

:::

## Apply for License

A trial EMQ license can be downloaded from our official website [https://www.emqx.com/en/apply-licenses/neuron](https://www.emqx.com/en/apply-licenses/neuron). All available modules could be used with a limitation of 100 connections and 1000 data tags for 15 days. If the trial EMQ license is expired, you can re-apply for the trial EMQ license via our official website again. However, a mailbox can only apply for a trial license up to two times.

* Each plugin module can be authorized independently in the EMQ license.
