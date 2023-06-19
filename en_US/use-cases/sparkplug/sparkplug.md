# MQTT Sparkplug Solution

Sparkplug is an extended open interoperability protocol based on MQTT. It enables devices and applications to send and receive messages over MQTT in a stateful way. MQTT doesn't ensure that all message received by device or application is valid and current. Sparkplug improve this by using "last will" mechanism of MQTT for ensuring the message is valid and current. This makes MQTT more adaptable to use in industrial environment. 

The Sparkplug specification was developed by Cirrus Link Solutions and then Eclipse Foundation, but it is openly available and not proprietary to a single company or organization.

In MQTT Sparkplug, an EMQX is used as the central broker for handling the communication between devices and applications in an IIoT environment. The EMQX is responsible for receiving messages from devices, forwarding them to the appropriate subscribers, and storing messages for later retrieval if necessary.

Neuron is an edge node that acts as an intermediary between devices and the EMQX. It can handle local data processing and aggregation, as well as buffering and forwarding data to the EMQX in asynchronous way. Neuron are typically used in IIoT environments where there are numerous devices that generate large amounts of data, and where resource and network bandwidth is limited.

In the context of MQTT Sparkplug, Neuron are responsible for implementing the Sparkplug specification, which includes handling the registration of devices, encoding and decoding data using the Sparkplug payload format, and organizing data using the Sparkplug topic namespace format. The Neuron communicates with the EMQX using the MQTT protocol, and it may also run additional software to perform local analytics or processing on the data.

![sparkplug](./assets/sparkplug.png)
 
## Benefits of using Sparkplug

<u>Plug-and-Play Integration</u>
One of the key benefits of Sparkplug is its plug-and-play integration capability. It follows a self-describing payload format, allowing devices to dynamically register themselves with the system. This simplifies the process of adding new devices to the network, reducing configuration efforts and promoting interoperability across different vendors and devices.

<u>Standardization and Interoperability</u>
Sparkplug follows a standardized data model and topic namespace, promoting interoperability between different devices and applications. This standardization simplifies integration efforts and allows for seamless communication across a wide range of industrial systems and platforms.

<u>Scalability and Flexibility</u>
Sparkplug offers scalability to accommodate large-scale IIoT deployments. It supports hierarchical architectures and can handle a high volume of devices and data streams. Additionally, Sparkplug is flexible and extensible, allowing for custom data definitions and payload structures to suit specific application requirements.
 
<u>Efficient and Reliable Communication</u>
Sparkplug utilizes the MQTT protocol, which is a lightweight and efficient messaging protocol. It ensures efficient transmission of data between devices and applications, making it suitable for resource-constrained environments. Additionally, Sparkplug incorporates features such as message acknowledgement and quality of service (QoS) levels, ensuring reliable and guaranteed delivery of messages.

## IT and OT Convergence
IT and OT systems have been separate and distinct, with IT systems focused on data processing and management, and OT systems focused on controlling physical processes and machinery. By introducing EMQX and Neuron together as a center data hub for the IT and OT infrastructure, all host systems and devices are equally connected to this center data hub for data exchange. Sparkplug host systems like ERP and MES and cloud platform can directly consume the data message from PLC, devices, machines, and robots, realizing the IT and OT convergence.


