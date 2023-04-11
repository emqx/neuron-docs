# Configuration

## Configuration Key Concepts

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

![Architecture](./assets/concepts.png)

The diagram shows a loosely-decoupled designed architecture. All nodes work independently to exchange data with each other, and to communicate with external devices or clouds according to its implemented industrial protocol.

### Tag

A tag is a non-hierarchical unique keyword assigned to a piece of information including data storing location in the device, and data operation properties, which helps describe an item and allows it to be found in the device or processed to be read/written automatically. Users would identify those interested tags in a device to read data from the device or to write data to the device.

### Group

The collection of user-interested tags in a device is divided into several groups to have better management. The routing mechanism is based on these groups as an information unit to be exchanged between nodes. A northbound node can subscribe to any groups in any southbound node. These subscriptions would be used for routing data messages between nodes. Moreover, there is a group polling frequency for controlling the time interval of the device polling.

## Configuration Procedures

This procedure is an idea of work flow how to set up he Neuron for various industrial protocol conversions.

![Configuration Steps](./assets/config.png)

### Step 1. Checking over All Available Plugins

Neuron data acquisition and delivery are enabled using various industrial plugins. A specific feature can be used only when corresponding plugin has installed and activated by the License. Since Neuron is a loosely-decoupled architecture, each plugin runs as an independent process thread without interfering each others. 

[Check over the available plugins](./plugin-management/plugin-management.md)

### Step 2. Creating a Southbound Driver

After checking out the available plugins, select all necessary southbound plugins for device communications according to industrial protocols. Each southbound plugin has only one connection to a device or a bus of multiple devices, depending on the specification of protocols.

[Create a southbound driver](./south-devices/south-devices.md)

### Step 3. Adding Groups and Tags to a Driver

In this step, add groups and tags to the southbound driver. Tag is a unique keyword to locate the data storage in the device. The tag also contains some meta-data information for the data such as scaling, precise, and read/write attributes. Those tags will be assigned into groups. Each group has an independent polling frequency to read data from the device. 

[Add groups and tags to a driver](./groups-tags/groups-tags.md)

Usually, there will be a very large number of tags to be handled in Neuron. Instead of adding groups and tags one by one in the dashboard, these groups and tags can be prepared in an offline Excel sheet and then imported into Neuron.

[Import and Export the groups and tags](./import-export/import-export.md)

Once the groups and tags have been created, the real-time values of the tags will be available from the monitoring menu.

[Monitoring the groups and tags](../usage/monitoring.md)

:::tip
Step 2 and 3 would be repeated until all necessary drivers, groups and tags are created.
:::

### Step 4. Creating a Northbound Application

Select the necessary northbound plugins for destination of data delivery. Each northbound plugin has only one connection to a destination such as a broker or an application.

[Create a northbound application](./north-apps/north-apps.md)

### Step 5. Subscribing a Group

In this step, there is no longer to set up groups and tags. Instead, a northbound node can subscribe to any group created in the southbound nodes. Once the subscription has been set up, the corresponding group's data will be published to the northbound node continuously according to the frequency of the group.

[Subscribe a group](./subscription/subscription.md)

## Configuration APIs

Alternatively, a set of configuraiton APIs is provided for integrating with industrial IoT platform, MES or other controlling systems.


