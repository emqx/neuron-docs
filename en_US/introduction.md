# What is Neuron?

Neuron is an modern industrial IoT connectivity server running on all kinds of IoT edge hardware. It aims to solve the problem of difficult unified access to device data in the context of Industry 4.0.

Neuron can realize the interconnection between Industrial IoT platforms and various devices by converting a wide variety of industrial protocols into a standard unified IoT MQTT message, performing remote control command and data acquisition, ultimately providing data support for the data centric automation and intelligent manufacturing.

Neuron offers the following product features.

## Edge Native

Neuron is designed based on real-time asynchourous event-driven processing to take full advantage of the low-latency network approach to 100 millisecond response time. It has very low memory footprints, less than 10M, suitable for running on low-profile edge gateway near machines.

## Loosely-coupled Modularity

Neuron design framework is based on decoupled modular plugin [architecture](./architecture.md) which allows more functional extensions by hot-plugging more service modules. Each pluggable module works independently without interference to each other and has its own specific capability of service.

## Diverse Connectivity

Neuron offers extensive and diverse southbound pluggable modules for various industries, including building automation, CNC machines, Robotics, Electricity, various PLCs and even smart sensors, since it supports broadest range access to 30+ kinds of industrial protocols such as Modbus, OPCUA, Ethernet/IP, IEC104, BACnet, Siemens, Mitsubishi and [more](./module-plugins/module-list.md). Northbound pluggable modules include MQTT and Websocket for cloud and on-premise IIoT platform connection.

## Multi-source Aggregation

Neuron can simultaneously make 1000 or above connections to various industrial devices. All data from these sources would be collected concurrently and forwarded to a designated MQTT message broker based on user-specified configuration. That is to provide a single point of entry of all information to data consumers via a designated MQTT broker, thus streamlining the IIoT platform or industrial applications acquiring those data from various sources, like an [unified namespace](./use_cases.md) architecture.

## Streaming Process Engine

Neuron has integrated with [eKuiper](https://www.lfedge.org/projects/ekuiper) streaming SQL processing rule engine to implement edge side AI/ML analytics and control logic for those collected industrial data, and store the filtered industrial data in local time series database or quickly implement [rule-based device control](./data-processing-engine/device-control.md).

## Portable Deployment

With ultra-low resource consumption, Neuron executables can be deployed natively in various edge devices like X86, ARM, RISC-V and other limited resource hardware architectures. It also supports containerized deployment, running with other co-located application containers in K8s and KubeEdge environment.

## API and MQTT Services

Neuron offers [HTTP-API](./reference/http-api.md) and [MQTT-API](./reference/mqtt-api.md) services to manipulate Neuron and industrial devices without onsite operation. This allows cloud and on-premise IIoT platform to deliver the command to connected machines/devices, or make changes to their parameter settings based on big data analysis results, or to modify configuration setup to accomodate more machines/devices.

## Better Integration

Neuron has better [integration](./integration.md) with IIoT platform, big data, and AI/ML analytic software into private cloud, EMQX Cloud, AWS, Google Cloud, Azure, or on-premise server via dedicated northbound MQTT modules.

## Unified DataOps

Neuron supports SparkplugB protocol so it can act like an EoN node of [SparkplugB unified industrial architecture](./use_cases.md) via EMQX broker, providing unified dataops for industrial application, and eliminating the complexity ERP, MES, SCADA and historian to access the device data.

## Data Tags Optimization

Duplicate or consecutive data tags would be merged into a single read/write command to increase the efficiency of data transmission. Such a data tag conditioning mechanism can reduces network and device workload.

## Configuration Import/Export

Neuron provides configuration [Excel sheet import and export](./console-management/configuration-import-export.md) capability to accelerate the data tags configuration setup and to keep data tags information in outside storage.

## Authentication and Security

Neuron supports encryption TLS, HTTPS to ensure the data security in transmission and employ JWT auth mechanism to verify the data owner.

## Web-based Dashboard

Neuron provides Web-based management dashboard for users to monitor data, device status and to manange online connection setup configuration and to deliver [device control](./console-management/device-control.md) command in a browser, enabling access to cross-industrial device data.
