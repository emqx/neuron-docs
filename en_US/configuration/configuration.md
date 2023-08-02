# Data Acquisition and Forwarding Process

Neuron is an advanced industrial protocol gateway software designed to operate on various IoT edge gateway hardware. Its primary objective is to address the challenge of unifying device data access in the context of Industry 4.0. By efficiently converting diverse industrial device data with different protocols into standardized IoT MQTT messages, Neuron enables seamless interconnectivity between devices and industrial IoT systems. This, in turn, facilitates remote control and information retrieval for intelligent manufacturing and data-driven decision-making.

Neuron offers extensive support for a wide range of communication protocols and industrial standards, making it a one-stop solution for data acquisition and MQTT protocol conversion. Its resource-efficient design allows easy deployment on various architectures, including X86 and ARM. The platform's user-friendly web-based management console empowers users with convenient gateway configuration management. With remarkable performance capabilities, Neuron can effortlessly connect to hundreds of industrial devices and efficiently handle over 10,000 data points.

## Data Acquisition

1. [View Available Plugins](../introduction/plugin-list/plugin-list.md): Neuron's southbound plugins are communication drivers that enable specific protocols for accessing external devices. After installing and activating the corresponding plugin licenses (refer to the [license policy](../introduction/license/license-policy.md)), users can effectively utilize these driver plugins. Neuron's loosely coupled architecture ensures that each plugin operates independently as a separate thread, avoiding interference and enabling users to choose the plugins that best suit their business requirements.
   
   The comprehensive list of supported plugins for various southbound devices, along with their specific configuration parameters, can be quickly accessed via the provided table links.

   | Application Area       | Plugin                                                     | Application Area     | Plugin                                                     |
   | -------------- | ------------------------------------------------------------ | ------------ | ------------------------------------------------------------ |
   | **Global Standard**   | [Modbus TCP <br />Modbus TCP QH](./south-devices/modbus-tcp/modbus-tcp.md) | **PLC Driver** | [Siemens S7 ISO TCP](./south-devices/siemens-s7/s7.md)       |
   |                | [Modbus RTU](./south-devices/modbus-rtu/modbus-rtu.md)       |              | [Siemens S5 FetchWrite](./south-devices/siemens-fetchwrite/fetchwrite.md) |
   |                | [OPC UA](./south-devices/opc-ua/overview.md)                 |              | [Mitsubishi 3E](./south-devices/mitsubishi-3e/overview.md)   |
   |                | [OPC DA](./south-devices/opc-da/overview.md)                 |              | [Mitsubishi 1E](./south-devices/mitsubishi-1e/mitsubishi-1e.md) |
   |                | [EtherNet/IP(CIP)](./south-devices/ethernet-ip/ethernet-ip.md) |              | [Mitsubishi FX](./south-devices/mitsubishi-fx/overview.md)   |
   | **Electricity**       | [IEC60870-5-104](./south-devices/iec-104/iec-104.md)         |              | [Omron FINS TCP](./south-devices/omron-fins/omron-fins.md)   |
   |                | [IEC61850](./south-devices/iec61850/overview.md)             |              | [Omron FINS UDP](./south-devices/omron-fins/omron-fins-udp.md) |
   |                | [DL/T645-2007](./south-devices/dlt645-2007/dlt645-2007.md)   |              | [Beckhoff ADS](./south-devices/ads/ads.md)                   |
   |                | [DL/T645-1997](./south-devices/dlt645-1997/dlt645-1997.md)   |              | [Panasonic Mewtocol](./south-devices/panasonic-mewtocol/overview.md) |
   | **Building Automation** | [BACnet/IP](./south-devices/bacnet-ip/bacnet-ip.md)          |              | [Profinet IO](./south-devices/profinet/profinet.md)          |
   |                | [KNXnet/IP](./south-devices/knxnet-ip/knxnet-ip.md)          |              | <!--Allen-Bradley DF1 with doc to be added-->                |
   | **Environmental Monitoring**   | [HJ212-2017](./south-devices/hj212-2017/hj212-2017.md)       | **Petroleum Industry** | [NON A11](./south-devices/nona11/nona11.md)                  |

2. [Creating Southbound Drivers](./south-devices/south-devices.md): Choose required southbound plugins for device communication based on industrial protocols. Each plugin can connect to a single device or multiple devices associated with a message bus, adhering to protocol standards. Users can create southbound drivers with plugins or [templates](./templates/templates.md) as per their preferences.

3. [Connecting Southbound Devices](./south-devices/south-devices.md#configure-data-groups-and-tags): Connect southbound devices by creating groups and points. Once groups and points are set up, users can monitor the real-time values of the data points through data monitoring. For easy configuration, Neuron supports [offline Excel file batch imports](./import-export/import-export.md) of relevant configuration information.

::: tip

Repeat steps 2 and 3 until all necessary drivers, groups, and points are created.
:::

## Data Forwarding

1. [Creating Northbound Applications](./north-apps/north-apps.md): Choose the relevant northbound plugins to enable seamless data forwarding. Each northbound plugin can connect to a single destination, such as a proxy or application. Currently, Neuron supports the following northbound applications:
   - [MQTT](./north-apps/mqtt/overview.md)
   - [eKuiper](./north-apps/ekuiper/ekuiper.md)
   - [SparkPlugB](./north-apps/sparkplugb/overview.md)
   - [WebSocket](./north-apps/websocket/websocket.md)
   - [Monitor](./north-apps/monitor/overview.md)
   
2. [Subscribe to Southbound Devices](./north-apps/north-apps.md#subscribe-to-southbound-data): After creating northbound devices, subscribe to groups from southbound nodes. No further group or point setup is needed. Subscribed northbound nodes will receive continuous data updates from the corresponding groups at the specified frequency.

The diagram below provides a visual representation of the entire process.

![Configuration Steps](./assets/config.png)


## Configuration APIs

Alternatively, a set of [configuration APIs](../http-api/http-api.md) is provided for integrating with industrial IoT platforms, MES, or other controlling systems.

