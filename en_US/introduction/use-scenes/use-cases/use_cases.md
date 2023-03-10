# Use Cases

Neuron is an Industrial IoT connectivity solution capable of meeting the requirements of several data acquisition and manipulation use cases for discrete, and process manufacturers.

## Industrial Device Connectivity
Neuron is usually used for factory digitized transformation, connecting disparate native protocol devices to multiple industrial information applications that support MQTT or API, such as MES, ERP, SCADA, IIoT platform and analytics system. Neuron also allows these industrial applications send back command to monitor, manage and control the field devices. 

Multiple Neuron can be deployed on the edge side of the district site for real-time data collection of various IIoT devices. Some devices are connected directly, others may be connected via DTU. Real-time data are reported to the data center or cloud for relevant analysis system and application, through the EMQX Broker.

![district-site](./assets/district-site.png)

Single Neuron can be depolyed on the edge side of the small local site.

![small-site](./assets/small-site.png)

Neuron can support connections up to thousands of devices and forward messages to hundreds of industrial applications. Each application can access to all devices information in a single point of connection to EMQX broker.

As Neuron may contains up to ten thousands of data tags, tools must be provided to accelerate deployment. Neuron provides Excel file configuration capability, users can export, and import to define the data tags. Neuron also provides API configuration for applications to manage data tags. 

## MQTT SparkplugB Solution
Sparkplug B is an extended open interoperability protocol based on MQTT. It enables devices and applications to send and receive messages over MQTT in a stateful way. MQTT doesn't ensure that all message received by device or application is valid and current. Sparkplug improve this by using "last will" mechanism of MQTT for ensuring the message is valid and current. This makes MQTT more adaptable to use in industrial environment.

MQTT SparkplugB offers below advantages:
* Plug and Play IIoT Solution
* High scalability
* Unified Infrastructure

Neuron is a EoN nodes of Sparkplug solution in the below infrastructure. It is an EoN nodes gateway to convert various diverse industrial data to Sparkplug message and deliver to industrial application through EMQX MQTT Broker or Cluster. Another reason to use Neuron in Sparkplug solution is to assist some “data polling” devices to be smarter and to report data in asynchronous way.

![sparkplugB](./assets/sparkplugB.png)
 
EMQX Broker or Cluster is the main component of infrastruture to manage all MQTT message traffic. Devices and sensors through the Neuron (EoN node) can communicate with application node such as SCADA systems, data historians and analysis programs.

## Unified Namespace
Unified namespace is a suit of solution software (EMQX Broker + Neuron) that acts as central repository where any application and device can publish or subscirbe contextualized data for a specific need. This simplifies dataops at scale since it is possible to interact with different industrial applications using the same namespace and communication interface. This makes your industrial information system to scale up easily.

Unified Namespace Solution offers below advantages:
* Integration Simplification
* Easy Devices Additions

The EMQX Broker or Cluster allows the communication between the various industrial applications, which are data producers and data consumers at the same time. Neuron will connect to various IIoT devices and process the collected data in eKuiper stream processing engine to generate contextualized data. This contextualized data will be published to EMQX Broker or Cluster, and can be visualized by single point of MQTT connection in all industrial applications such as SCADA tools, BI analytic software, MES, ERP. 

![uns](./assets/uns.png)

EMQX Broker or Cluster and Neuron together can form an UNS. Industrial applications such as MES, ERP can uitilize the benefits of UNS. For example, UNS eliminates massive point to point connections and minimizes the load on data transmission. 
