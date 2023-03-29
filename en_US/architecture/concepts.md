# Concept

## Node

In Neuron, each node can establish a connection with a device or a northbound application.
* In the device node, you can add and manage device tags.
* In the northbound node, you can select the data group to subscribe to.

## Group

Under each node, multiple data groups can be created to classify tags. For example, if a device is connected to multiple temperature sensors and multiple humidity sensors, temperature and humidity data groups can be created to classify the collected tags. Neuron uploads the collected data to the northbound application based on groups.

## Tag

Under each group, multiple collection tags can be created. For example, a temperature sensor may collect multiple temperature values, with each temperature value treated as a collection tag.

## Plugin

In Neuron, each plugin corresponds to an implementation of a protocol. For example, one Modbus TCP protocol corresponds to one plugin, and one MQTT protocol corresponds to one plugin.