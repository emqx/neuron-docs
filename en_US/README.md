# Product Overview

## What is Neuron?

Neuron is a modern industrial IoT connectivity server that simultaneously communicates with many diverse industrial devices through the standard or its own dedicated protocols, realizing the multiple device connections to the Industrial IoT platform.

![Neuron](./introduction/assets/neuron.png)

As a lightweight industrial software running all kinds of limited resource IoT edge hardware, neuron aims to solve the problem of difficult unified access to industrial device data for data-centric automation, providing foundational support for intelligent manufacturing.

### Edge Native

Neuron is an advanced real-time asynchronous processing server designed to achieve response times as low as 100 milliseconds. By leveraging the benefits of edge computing and low-latency network architectures, it ensures rapid and efficient data processing.

### Diverse Connectivity

Neuron offers many diverse pluggable connectivity and processing modules such as Modbus, OPCUA, Ethernet/IP, IEC104, BACnet, Siemens, Mitsubishi, and more. These modules would be classified into building automation, CNC machines, Robotics, Electricity, and various PLCs communication. For a complete list of supported plugin modules, please see [Plugin List](./introduction/plugin-list/plugin-list.md).

### Large-Scale Concurrency

Neuron is capable of establishing unlimited connections with a wide range of industrial devices concurrently, because it adopts the modern decoupled modular [Architecture](./introduction/architecture/architecture.md) design. 

Note: The actual number of simultaneous connections is contingent upon the processing resources allocated.

### Portable Deployment

Neuron has very low memory footprints, less than 7M at startup, suitable for running on low-profile architecture devices like x86, ARM, RISC-V, and so on. It also supports docker-like containerized deployment, running with other co-located containers in K8s environments. For details on how to install, see [Installation](./installation/installation.md). 

### Better Integration

Neuron has seamless [Integration](./integration/integration.md) with other industrial IoT applications, big data, and AI/ML analytic software into the platforms like private cloud, EMQX Cloud, AWS, Microsoft Azure, or on-premises servers via API and MQTT connection.

### Unified DataOps

Neuron assists the legacy industrial devices to deliver data messages in an asynchronous way as the edge node specified in Sparkplug standard. [Sparkplug](./use-cases/sparkplug/sparkplug.md) is an open, unified, interoperable standard for industrial data exchange between industrial information systems like ERP, MES, SCADA and historian via an MQTT broker.

### Authentication and Security

Neuron supports TLS and HTTPS encryption for API services to ensure the data security in transmission and use [JWT authentication](./http-api/jwt.md) mechanism to verify the data owner.

