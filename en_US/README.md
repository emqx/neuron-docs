# Product Overview

Neuron is a modern industrial IoT connectivity server that communicates with many diverse industrial devices through the standard or its dedicated protocols, realizing the multiple device connections to the Industrial IoT platform.

<img src="./introduction/assets/neuron.png" alt="Neuron" style="zoom:50%;" />

As a lightweight industrial software running all kinds of limited resource IoT edge hardware, neuron aims to solve the problem of difficult unified access to industrial device data for data-centric automation, providing foundational support for intelligent manufacturing.

## Key Benefits

**Edge Native**: Neuron is an advanced real-time asynchronous processing server designed to achieve response times as low as 100 milliseconds. Neuron ensures rapid and efficient data processing by leveraging the benefits of edge computing and low-latency network architectures.

**Diverse Connectivity**: Neuron offers many diverse pluggable connectivity and processing modules such as Modbus, OPCUA, Ethernet/IP, IEC104, BACnet, Siemens, Mitsubishi, and more. These modules would be classified into building automation, CNC machines, Robotics, Electricity, and various PLCs communication. For a complete list of supported plugin modules, please see [Plugin List](./introduction/plugin-list/plugin-list.md).

**Large-Scale Concurrency**: Neuron is capable of establishing unlimited connections with a wide range of industrial devices concurrently because it adopts the modern decoupled modular [Architecture](./introduction/architecture/architecture.md) design. 

Note: The number of simultaneous connections depends on the processing resources allocated.

**Portable Deployment**: Neuron has very low memory footprints, less than 7M at startup, suitable for running on low-profile architecture devices like x86, ARM, RISC-V, and so on. It also supports docker-like containerized deployment, running with other co-located containers in K8s environments. For details on how to install, see [Installation](./installation/installation.md). 

**Better Integration**: Neuron has seamless [Integration](./integration/integration.md) with other industrial IoT applications, big data, and AI/ML analytic software into the platforms like private cloud, EMQX Cloud, AWS, Microsoft Azure, or on-premises servers via API and MQTT connection.

**Unified DataOps**: Neuron assists the legacy industrial devices to deliver data messages in an asynchronous way as the edge node specified in Sparkplug standard. [Sparkplug](./use-cases/sparkplug/sparkplug.md) is an open, unified, interoperable standard for industrial data exchange between industrial information systems like ERP, MES, SCADA, and historian via an MQTT broker.

Authentication and Security: Neuron supports TLS and HTTPS encryption for API services to ensure data security in transmission and use the [JWT authentication](./http-api/jwt.md) mechanism to verify the data owner.

## Key Concepts

The configuration key concepts are to help understand how to set up various industrial protocol conversions in Neuron.

### Core

A Neuron core is a framework to provide a foundation to build and adopt various plugins in terms of diverse industrial communication protocols. This core framework includes NNG high-speed bus, a data manager to control data flow, and adapters for plugin integration. 

### Plugin

Neuron can be divided into a core framework and a number of pluggable modules. Pluggable means that these modules can be added and removed dynamically, even supporting hot plugging in the running state. Plugins would be classified into northbound applications and southbound drivers. The northbound plugin is usually used for connecting to a cloud platform, or to an external application like a processing engine. The southbound plugin is a communication driver that implements specific protocols to access external devices. 

All these modules are written in C language and SDK is provided for users who are interested in secondary development. A plugin is just a dynamic linked library (.so) file built by the SDK. At least one northbound plugin and one southbound plugin are required for data delivery and data acquisition respectively to implement the protocol format conversion.

### Adapter

An adapter is a communication routine providing two interfaces for plugin data exchange. On one side, it has a communication interface for NNG high-speed bus that can exchange data messages with other adapters. On the other side, it provides a plugin interface for the integration of a plugin module. This makes two unrelated components, NNG high-speed bus and a plugin, can work together. 

There are two kinds of adapters. A driver adapter is used for integration with a southbound driver plugin. An app adapter is used for integration with a northbound application plugin. An app adapter and a driver adapter are different as they have different logic in handling data message exchange.

### Node

When a plugin is inserted into the core framework, a connection node would be created to communicate with external devices or applications. Node here in Neuron is defined as merging framework interface with communication routines. There may be a lot of nodes created for communication with various parties in a single running instance. It is the core framework to manage the message routing between those nodes. 

A node is simply a combination of an adapter and a plugin module. Message exchange between nodes is based on NNG high-speed bus.

![Architecture](/Users/lena/Documents/GitHub/neuron-docs/en_US/configuration/assets/concepts.png)

The diagram shows a loosely-decoupled designed architecture. All nodes work independently to exchange data with each other, and to communicate with external devices or clouds according to its implemented industrial protocol.

### Tag

A tag is a non-hierarchical unique keyword assigned to a piece of information including data storing location in the device, and data operation properties, which helps describe an item and allows it to be found in the device or processed to be read/written automatically. Users would identify those interested tags in a device to read data from the device or to write data to the device.

### Group

The collection of user-interested tags in a device is divided into several groups to have better management. The routing mechanism is based on these groups as an information unit to be exchanged between nodes. A northbound node can subscribe to any groups in any southbound node. These subscriptions would be used for routing data messages between nodes. Moreover, there is a group polling frequency for controlling the time interval of the device polling.
