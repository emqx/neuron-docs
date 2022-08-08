# What is Neuron?

Neuron is an modern industrial IoT connectivity server running on all kinds of limited resource IoT edge hardware. It aims to solve the problem of difficult unified access to device data, and boost up the interoperability between devices and Industrial IoT platforms and the scalability of Industrial IoT infrastructure, in the context of Industry 4.0.

Neuron realize the interconnection between Industrial IoT platforms and various devices by converting a wide variety of industrial protocols into a standard unified IoT MQTT messages. These common data sources can be widely used for data centric automation and AI/ML analytic, ultimately providing foundational support for the intelligent manufacturing.

# Neuron product features

**Edge Native**

Neuron is designed based on asynchourous real-time processing to take full advantage of the low-latency network approach to realize 100 millisecond or lower response time. It has very low memory footprints, less than 10M, suitable for running on low-profile edge gateway near machines.

**Loosely-coupled Modularity**

Neuron design framework is based on decoupled modular plugin [architecture](./architecture.md) which allows more extension services by hot-plugging more modules. Each pluggable module has its own specific capability of services and would works independently without interfering with each other.

**Diverse Connectivity**

Neuron offers extensive and diverse southbound pluggable communication modules for various industries, including building automation, CNC machines, Robotics, Electricity, various PLCs and even smart sensors, since it supports broadest range access to 30+ kinds of industrial protocols such as Modbus, OPCUA, Ethernet/IP, IEC104, BACnet, Siemens, Mitsubishi and [more](./module-plugins/module-list.md). Northbound pluggable modules include MQTT and Websocket for cloud and on-premise industrial IoT platform connection.

**Multi-source Aggregation**

Neuron can simultaneously make a 1000 or above connections to various industrial devices. All data from these sources would be collected concurrently and forwarded to a designated MQTT message broker based on user-specified configuration. That means Neuron can provide a single point of entry of all information to data consumers via a designated MQTT broker like an [unified namespace](./use_cases.md) architecture, thus streamlining the data acquisition of industrial IoT platform and industrial applications.

**Streaming Process Engine**

Neuron has integrated with [eKuiper](https://www.lfedge.org/projects/ekuiper) rule-based processing engine to implement edge side AI/ML analytics and [device control](./data-processing-engine/device-control.md) logic for those collected industrial data by executing the streaming SQL statements. The filtered industrial data from AI/ML analytics would be stored in local time-series database and the control command would be delivered to the device.

**Portable Deployment**

With ultra-low resource consumption, Neuron executables can be deployed natively in various edge devices like X86, ARM, RISC-V and other limited resource hardware architectures. It also supports containerized deployment, running with other co-located application containers in K8s and KubeEdge environment.

**API and MQTT Services**

Neuron offers cloud industrial IoT platform or on-premise industrial applications various [HTTP-API](./reference/http-api.md) and [MQTT-API](./reference/mqtt-api.md) services to send the control command to connected machines and devices, or make changes to device parameters based on big data, AI/ML analysis results, and to modify configuration to accomodate more data tags, machines and devices without onsite operation.

**Better Integration**

Neuron has better [integration](./integration.md) with industrial IoT platform, big data, and AI/ML analytic software into private cloud, EMQX Cloud, AWS, Google Cloud, Azure, or on-premise server via dedicated northbound MQTT modules.

**Unified DataOps**

Neuron supports [Sparkplug B communication](./use_cases.md) and assists the connected "data polling" devices to be smarter to report Sparkplug B format data message in asynchronous way, eliminating the complexity of ERP, MES, SCADA and historian to access the device data by using an open, unified, interoperable standard for industrial data exchange. 

**Data Tags Optimization**

Duplicate or consecutive data tags would be merged into a single read/write command to increase the efficiency of data transmission. Such a data tag conditioning mechanism can reduces network and device workload.

**Configuration Import/Export**

Neuron provides [Excel sheet import and export](./console-management/configuration-import-export.md) capability to accelerate the setup of data tags configuration. Users can use favorite Excel editor to prepare those data tags details at once according to the format as mentioned and then import the Excel sheet to Neuron. Excel sheet also help to keep these data tags information in outside storage for backup.

**Authentication and Security**

Neuron supports TLS and HTTPS encryption to ensure the data security in transmission and employ JWT auth mechanism to verify the data owner.

**Web-based Dashboard**

Neuron provides Web-based management dashboard for users to monitor data and device status, to manange online connection configuration setup and to send [control command](./console-management/device-control.md) to a specific device.All these operations can be handled in an one-stop browser interface.
