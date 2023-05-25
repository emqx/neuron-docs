# Product Overview

## What is Neuron?

Neuron is a modern industrial IoT connectivity server that simultaneously communicates with many diverse industrial devices through the standard or its own dedicated protocols, realizing the multiple device connections to the Industrial IoT platform.

As a lightweight industrial software running all kinds of limited resource IoT edge hardware, neuron aims to solve the problem of difficult unified access to device data for data-centric automation, providing foundational support for intelligent manufacturing.

## What is NeuronEX?

NeuronEX is another distribution version that implements the data stream processing at the edge side by integrating the LF Edge eKuiper rules-based engine. LF Edge eKuiper is a lightweight IoT data analytics and stream processing engine running on resource-constraint edge devices. Go [LF Edge ekuiper](https://ekuiper.org/) for more details.

![NeuronEX](./introduction/assets/neuronex.png)

NeuronEX is designed to be a complete edge server that can fully exploit data stream processing and data acquisition together as a whole for edge computing.

The advantages of NeuronEX instead of Neuron + eKuiper
* A direct data channel is established between Neuron and eKuiper instead of using a broker as middleware to transfer data indirectly.
* A single WebUI makes it easy for users to operate both Neuron and eKuiper without changing the user interface.
* A single installation package is provided for both Neuron and eKuiper installation and configuration.
* A NeuronEX docker image with both Neuron and eKuiper installed is provided and can be used with a single image pull.

## Edge Native

Neuron is an advanced real-time asynchronous processing server designed to achieve response times as low as 100 milliseconds. By leveraging the benefits of edge computing and low-latency network architectures, it ensures rapid and efficient data processing.

## Diverse Connectivity

Neuron offers many diverse pluggable modules such as Modbus, OPCUA, Ethernet/IP, IEC104, BACnet, Siemens, Mitsubishi, and more. These modules are widely used in building automation, CNC machines, Robotics, Electricity, and various PLCs communication. For a complete list of supported plugin modules, see [Plugin List](./introduction/plugin-list/plugin-list.md).

## Large-Scale Concurrency

Neuron is capable of establishing unlimited connections with a wide range of industrial devices concurrently, thanks to its [decoupled modular architecture design](./introduction/architecture/architecture.md). Note: The actual number of simultaneous connections is contingent upon the processing resources allocated.

## Portable Deployment

Neuron has very low memory footprints, less than 7M at startup, suitable for running on low-profile architecture devices like x86, ARM, RISC-V, and so on. It also supports docker-like containerized deployment, running with other co-located containers in K8s environments. For details on how to install, see [Installation](./installation/installation.md). 

## Better Integration

Neuron has [seamless integration](./integration/integration.md) with industrial IoT applications, big data, and AI/ML analytic software into the platforms like private cloud, EMQX Cloud, AWS, Microsoft Azure, or on-premises servers via API and MQTT connection.

## Unified DataOps

Neuron assists the legacy industrial devices to [deliver data messages in an asynchronous way](./use-cases/use_cases.md#mqtt-sparkplugb-solution) as the edge node specified in Sparkplug B standard. Sparkplug B is an open, unified, interoperable standard for industrial data exchange between industrial information systems like ERP, MES, SCADA and historian via an MQTT broker.

## Authentication and Security

Neuron supports TLS and HTTPS encryption for API services to ensure the data security in transmission and use [JWT authentication](./http-api/jwt.md) mechanism to verify the data owner.

## Streaming Process Engine (NeuronEX only)

NeuronEX includes eKuiper rule-based processing engine to implement AI/ML analytics, data filtration, data manipulation, device control, and data persistence in time-series database via streaming SQL statements at the edge side.
