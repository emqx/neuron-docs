# Architecture

Neuron is an edge-native software designed to handle data collection, forwarding, and aggregation for the Industrial IoT platform. It focuses on ultra-low latency processing at the edge, ensuring fast and efficient handling of diverse data from multiple sources.

## Efficient Multi-thread

Neuron adopts an edge-native design optimized for modern CPUs' multi-core architecture, including ARM and RISC-V embedded systems.

At the core of Neuron's efficiency lies our adept multi-thread management, which enables Neuron to deliver real-time performance and execute tasks concurrently within specific time constraints. Inter-thread communication is achieved through the NNG library, offering optimized asynchronous I/O processing for rapid and reliable data message exchange between threads. NNG offers the following features.

* Asynchronous I/O - Neuron utilizes the NNG library's optimized asynchronous I/O framework for swift data processing.
* SMP & Multi-threading - Scale out easily to engage multiple cores in the modern SMP system.
* Brokerless - With lightweight deployment and easy integration into components, Neuron enables seamless incorporation into various systems.

## Message Bus

Neuron's core message bus is based on the pairs-1 feature of NNG library to organize a star-like scalable framework, with a message router core at the center and two types of adapters surrounding it. 

The southbound driver nodes work as the data producer, they are the nodes to communicate with devices; the northbound application nodes are the data consumer to process or forward data messages. 

Each node (southbound or northbound) consists of a plugin adapter and plugin module. Communication between nodes relies on NNG high-efficiency asynchronous I/O to make good use of multi-core CPU capability. 

![arch-overview](./assets/arch-overview.png)

## Scatter-Gather Processing

Neuron incorporates Scatter-Gather processing, which is ideal for asynchronous I/O processing, as it allows messages to be processed concurrently by sending them to desired nodes simultaneously through a parallel thread pool. Southbound driver nodes (data producers) are therefore requested to group data streams together so that northbound application nodes (data consumers) can subscribe to the desired data stream groups from various nodes.

![arch-bus-topo](./assets/arch-dataflow.png)

## Hot Plugin

Neuron's nodes operate as loosely-coupled threading services, allowing for dynamic creation or destruction of nodes without affecting other running nodes, except for the built-in web server node. This flexible design enables the loading or off-loading of plugin modules in real time, facilitating the addition or upgrade of plugin modules and increasing the application's feature set. However, the "hot-plugin" module mechanism is dependent on the CPU processing capacity of the host platform or container. 

![arch-dataflow](./assets/arch-bus-topo.png)
