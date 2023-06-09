# MQTT SparkplugB Solution

Sparkplug B is an extended open interoperability protocol based on MQTT. It enables devices and applications to send and receive messages over MQTT in a stateful way. MQTT doesn't ensure that all message received by device or application is valid and current. Sparkplug improve this by using "last will" mechanism of MQTT for ensuring the message is valid and current. This makes MQTT more adaptable to use in industrial environment.

MQTT SparkplugB offers below advantages:
* Plug and Play IIoT Solution
* High scalability
* Unified Infrastructure

Neuron is a EoN nodes of Sparkplug solution in the below infrastructure. It is an EoN nodes gateway to convert various diverse industrial data to Sparkplug message and deliver to industrial application through EMQX MQTT Broker or Cluster. Another reason to use Neuron in Sparkplug solution is to assist some “data polling” devices to be smarter and to report data in asynchronous way.

![sparkplugB](./assets/sparkplugB.png)
 
EMQX Broker or Cluster is the main component of infrastruture to manage all MQTT message traffic. Devices and sensors through the Neuron (EoN node) can communicate with application node such as SCADA systems, data historians and analysis programs.

