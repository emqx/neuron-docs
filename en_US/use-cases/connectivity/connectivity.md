# Industrial Device Connectivity
Neuron is usually used for factory digitized transformation, connecting disparate native protocol devices to multiple industrial information applications that support MQTT or API, such as MES, ERP, SCADA, IIoT platform and analytics system. Neuron also allows these industrial applications send back command to monitor, manage and control the field devices. 

Multiple Neuron can be deployed on the edge side of the district site for real-time data collection of various IIoT devices. Some devices are connected directly, others may be connected via DTU. Real-time data are reported to the data center or cloud for relevant analysis system and application, through the EMQX Broker.

![district-site](./assets/district-site.png)

Single Neuron can be depolyed on the edge side of the small local site.

![small-site](./assets/small-site.png)

Neuron can support connections up to thousands of devices and forward messages to hundreds of industrial applications. Each application can access to all devices information in a single point of connection to EMQX broker.

As Neuron may contains up to ten thousands of data tags, tools must be provided to accelerate deployment. Neuron provides Excel file configuration capability, users can export, and import to define the data tags. Neuron also provides API configuration for applications to manage data tags. 
