# Product Overview

## What is Neuron?

Neuron is a modern industrial IoT connectivity server that simultaneously communicates with many diverse industrial devices through the standard or its own dedicated protocols, realizing the multiple device connections to the Industrial IoT platform.

Neuron is a very lightweight industrial software running all kinds of limited resource IoT edge hardware. It aims to solve the problem of difficult unified access to device data for data-centric automation, providing foundational support for the intelligent manufacturing.

## Edge Native

Neuron is a real-time asynchronous processing server that delivers a response time as low as 100 milliseconds, taking full advantage of the low-latency network approach at the edge. 

## Diverse Connectivity

Neuron offers many diverse pluggable modules such as Modbus, OPCUA, Ethernet/IP, IEC104, BACnet, Siemens, Mitsubishi, and more. These modules are widely used in building automation, CNC machines, Robotics, Electricity, and various PLCs communication.

## Large-scale Concurrency

Neuron can simultaneously make unlimited connections to diverse industrial devices. This benefits from decoupled modular architecture design to run each connection individually. The practical number of concurrent connections depend on the allocated processing resources.

## Portable Deployment

Neuron has very low memory footprints, less than 7M at startup, suitable for running on low-profile architecture devices like x86, ARM, RISC-V, and so on. It also supports docker-like containerized deployment, running with other co-located containers in K8s environments.

## Better Integration

Neuron has seamless integration with industrial IoT applications, big data, and AI/ML analytic software into the platforms like private cloud, EMQX Cloud, AWS, Microsoft Azure, or on-premises servers via API and MQTT connection.

## Unified DataOps

Neuron assists the legacy industrial devices to deliver data messages in an asynchronous way as the edge node specified in Sparkplug B standard. Sparkplug B is an open, unified, interoperable standard for industrial data exchange between industrial information systems like ERP, MES, SCADA and historian via an MQTT broker.

## Authentication and Security

Neuron supports TLS and HTTPS encryption for API services to ensure the data security in transmission and use JWT authentication mechanism to verify the data owner.
