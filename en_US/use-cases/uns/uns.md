# Unified Namespace

Unified namespace is a suit of solution software (EMQX Broker + Neuron) that acts as central repository where any application and device can publish or subscirbe contextualized data for a specific need. This simplifies dataops at scale since it is possible to interact with different industrial applications using the same namespace and communication interface. This makes your industrial information system to scale up easily.

Unified Namespace Solution offers below advantages:
* Integration Simplification
* Easy Devices Additions

The EMQX Broker or Cluster allows the communication between the various industrial applications, which are data producers and data consumers at the same time. Neuron will connect to various IIoT devices and process the collected data in eKuiper stream processing engine to generate contextualized data. This contextualized data will be published to EMQX Broker or Cluster, and can be visualized by single point of MQTT connection in all industrial applications such as SCADA tools, BI analytic software, MES, ERP. 

![uns](./assets/uns.png)

EMQX Broker or Cluster and Neuron together can form an UNS. Industrial applications such as MES, ERP can uitilize the benefits of UNS. For example, UNS eliminates massive point to point connections and minimizes the load on data transmission. 
