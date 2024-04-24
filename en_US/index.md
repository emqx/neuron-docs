# Product Overview

Neuron is an open-source, lightweight IIoT connectivity server that empowers industrial devices with the key IoT connectivity capabilities in the Industry 4.0 era. It translates diverse protocol data from industrial devices into standardized IoT MQTT messages, ensuring seamless interconnection between devices and the IoT system for remote control and information gathering.

Supporting simultaneous access and MQTT conversion for varied communication protocols, Neuron is resource-efficient and deployable on physical machines with X86, ARM, RISC-V, and other architectures, either natively or through containers. Its web-based console allows easy configuration management. With robust performance, Neuron can connect hundreds of industrial devices and manage over 10,000 data points.

<img src="./introduction/assets/neuron.png" alt="Neuron" style="zoom:30%;" />

## Why Neuron

**Edge Native**: Neuron is an advanced real-time asynchronous processing server designed to achieve response times as low as 100 milliseconds. It ensures rapid and efficient data processing by leveraging the benefits of edge computing and low-latency network architectures.

**Diverse Connectivity:** Neuron offers many diverse pluggable connectivity and processing modules such as Modbus, OPCUA, Ethernet/IP, IEC104, BACnet, Siemens, Mitsubishi, and more. These modules would be classified into building automation, CNC machines, Robotics, Electricity, and various PLCs communication. For a complete list of supported plugin modules, please see [Plugin List](./introduction/plugin-list/plugin-list.md).

**Large-Scale Concurrency**: Neuron is capable of establishing unlimited connections with a wide range of industrial devices concurrently because it adopts the modern decoupled modular [Architecture](./introduction/architecture/architecture.md) design. Note: The actual number of simultaneous connections is contingent upon the processing resources allocated.

**Portable Deployment**: Neuron has very low memory footprints, less than 7M at startup, suitable for running on low-profile architecture devices like x86, ARM, RISC-V, and so on. It also supports docker-like containerized deployment, running with other co-located containers in K8s environments. For details on how to install, see [Installation](./installation/installation.md). 

**Better Integration**: Neuron has seamless integration with other industrial IoT applications, big data, and AI/ML analytic software into the platforms like private cloud, EMQX Cloud, AWS, Microsoft Azure, or on-premises servers via API and MQTT connection.

**Unified DataOps**: Neuron assists the legacy industrial devices to deliver data messages in an asynchronous way as the edge node specified in Sparkplug standard. [Sparkplug](./use-cases/sparkplug/sparkplug.md) is an open, unified, interoperable standard for industrial data exchange between industrial information systems like ERP, MES, SCADA, and historian via an MQTT broker.

**Authentication and Security**: Neuron supports TLS and HTTPS encryption for API services to ensure data security in transmission and use [JWT authentication](./api/jwt.md) mechanism to verify the data owner.

## Key Concepts

The configuration key concepts are to help understand how to set up various industrial protocol conversions in Neuron.

### Core

A Neuron core is a framework to provide a foundation to build and adopt various plugins in terms of diverse industrial communication protocols. This core framework includes NNG high-speed bus, a data manager to control data flow, and adapters for plugin integration. 

### Plugin

Neuron can be conceptually separated into a core framework and a series of dynamic, or pluggable, modules. These modules, which can be added, removed, and even hot-swapped while in operation, fall into two categories: northbound applications and southbound drivers.

Northbound plugins typically serve as a connection point to a cloud platform or an external application like a processing engine. Conversely, southbound plugins act as communication drivers, implementing specific protocols to facilitate access to external devices.

All these modules are coded in the C language. For users interested in customization, an SDK is provided for secondary development. Each plugin is essentially a dynamic linked library (.so) file constructed using the SDK. To accomplish data delivery and acquisition, and thus the protocol format conversion, at least one northbound plugin and one southbound plugin are necessary.

For guidance on how to develop your own plugins, please refer to the [SDK Tutorial](./dev-guide/sdk-tutorial/sdk-tutorial.md).

### Adapter

An adapter is a communication routine providing 2 interfaces for plugin data exchange:

- NNG high-speed bus communication interface: to exchange data messages with other adapters. 
- Plugin interface: to integrate with plugin modules. 

Neuron also offers 2 types of adapters:

- Driver adapter: to integrate with a southbound driver plugin. 
- APP adapter: to integrate with a northbound application plugin. An app adapter and a driver adapter have different logic when handling data message exchange.
### Node

When a plugin is inserted into the core framework, a connection node would be created to communicate with external devices or applications. Node here in Neuron is defined as merging framework interface with communication routines. There may be a lot of nodes created for communication with various parties in a single running instance. It is the core framework to manage the message routing between those nodes. 

A node is simply a combination of an adapter and a plugin module. Message exchange between nodes is based on NNG high-speed bus. The diagram shows a loosely-decoupled designed architecture. All nodes work independently to exchange data with each other, and to communicate with external devices or clouds according to its implemented industrial protocol.

![Architecture](./assets/concepts-node.png)

### Tag

In Neuron, a "tag" represents a specific data point or variable within a device. This tag information encompasses the data type, its location or address within the device, and its read/write attributes. By configuring these tags, users can create a link between the device's internal data and the collection points within Neuron. This facilitates the extraction or injection of data from or into the device, respectively.

### Group

To improve management efficiency, the collection of user-interest tags within a device is divided into several groups. These groups serve as the primary units of information exchange between nodes in our routing mechanism. Northbound nodes can subscribe to any groups found in southbound nodes, enabling the routing of data messages between nodes. Additionally, each group features a polling frequency, which controls the time interval for device polling, ensuring regular data updates.
