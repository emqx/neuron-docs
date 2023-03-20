# Product Overview

## What is Neuron?

Neuron provides extensive and diverse driver support for various industries. It can simultaneously connect to devices with multiple different driver protocols for data acquisition and control, enabling interconnection between industrial IoT platforms and various devices, and ultimately providing data support for data-centric automation and intelligent manufacturing.

Neuron is a lightweight industrial protocol gateway software based on the LGPL license open source, which can add new driver or application support to Neuron through extension plugins. Its aim is to solve the problem of difficult unified access to device data in the context of Industry 4.0.

### What is NeuronEX?

NeuronEX is a version of the Neuron integrated data stream processing engine eKuiper. With the NeuronEX UI, it is easy to create data streams and perform other stream processing operations.

## Product Functions and Features

### Diversified Connectivity

Neuron provides diversified driver protocol support for various industries, including building automation, CNC machines, Robotics, Electricity, various PLCs, and even intelligent sensors, such as Modbus, OPCUA, Ethernet/IP, IEC104, BACnet, Siemens, Mitsubishi, and more.</br>
Neuron supports applications that connect to various cloud or IIoT platforms, such as MQTT, WebSocket, SparkPlug B, and other custom applications.</br>
With MQTT, IIoT platforms, big data, and AI/ML analysis software can be better integrated into private clouds, EMQX Cloud, AWS, Google Cloud, Azure, or local servers.</br>
Through SparkPlug B, unified data operations will be provided for industrial applications, eliminating the complexity of ERP, MES, SCADA, and historian accessing device data.

### Lightweight

Neuron is developed entirely in C language and supports running on devices with hardware architectures such as X86, ARM, MIPS, RISC-V, as well as containerized deployments such as K8s, KubeEdge, and more. Neuron can achieve data acquisition at the level of 100 milliseconds or even 10 milliseconds on devices with limited hardware resources, and on servers with sufficient hardware resources, Neuron can fully utilize multi-core CPUs to simultaneously collect data from hundreds of thousands of data points at a frequency of 100 milliseconds and perform point writing control.

### Stream Processing

NeuronEX integrates the stream SQL processing rule engine eKuiper, which enables edge-side AI/ML analysis and control logic on the collected industrial data. It can also store the filtered industrial data in local time-series databases or quickly implement rule-based device control.

### Web-based Dashboard

Neuron provides users with a simple and easy-to-use web-based user interface that allows users to manage device connections, view real-time device data, and perform control operations on devices through a browser on any device. Users can also monitor devices in real-time to check whether devices are online and whether data points are abnormal.

### Multi-source Aggregation

Neuron can simultaneously establish 1,000 or more connections with various industrial devices. It collects all the data from these connections and forwards it to the specified MQTT message broker based on user-defined configurations. In other words, by specifying an MQTT broker, Neuron provides a single entry point for data consumers to access all information, simplifying the process for IIoT platforms or industrial applications to retrieve data from various sources, such as a unified namespace architecture.

### API Services

Neuron provides HTTP-API and MQTT-API services, allowing users to operate Neuron and industrial devices remotely. This enables cloud and local IIoT platforms to send commands to connected machines/devices, change their parameter settings based on big data analysis results, or modify data label configurations to adapt to more machines/devices, without the need for on-site operations.

### Data Security

Neuron supports TLS/SSL encrypted data to ensure data security during transmission.

### Device Monitoring

Neuron provides monitoring API that conform to the Prometheus specification, which can provide real-time monitoring data on device connection and operation status. Neuron can also be integrated into the Prometheus monitoring system, and alert notifications can be promptly sent when devices experience exceptions based on predefined alert rules.

### Driver Applications Modularization

Neuron is designed to facilitate the extension of southbound drivers and northbound applications. Based on the core framework of Neuron, users can easily customize and develop southbound and northbound plugins according to their needs.

### Data Tags Optimization

Neuron automatically optimizes the read and write of configured data points to improve data transmission and efficiency. This tag adjustment and reduction mechanism can reduce the workload on networks and devices.
