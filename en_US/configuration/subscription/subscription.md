# Key Concepts

## Plugin
Neuron can be divided into a core framework and a number of plugin modules. Plugin module would be classified into northbound and southbound plugin. Northbound plugin is usually used for connecting cloud platform or is an application like processing engine, or a proxy to other external application. Southbound plugin is a communication driver that implement specific protocols to access external devices. 

All these modules are written in C-language and SDK is provided for users who interest in secondary development. At least one northbound plugin and one southbound plugin are required for protocol format conversion.

## Node
When a plugin is inserted into the core framework, a connection node would be created to communicate with external devices or applications. Node here in Neuron is defined as merging framework interface with communication routines. There may be a lot of nodes created for communication with various parties in a single running instance. It is the core framework to manage the message routing between those nodes.

## Tag
A tag is a non-hierarchical unique keyword assigned to a piece of information including data storing location in the device, and data operation properties, which helps describe an item and allows it to be found in the device or processed to be read/written automatically. Users would identify those interested tags in a device to read data from the device or to write data to the device.

## Group
The collection of user-interested tags in a device is divided into several groups to have better management. The routing mechanism is based on these groups as an information unit to be exchanged between nodes. A northbound node can subscribe to any groups in any southbound node. These subscriptions would be used for routing data messages between nodes.
