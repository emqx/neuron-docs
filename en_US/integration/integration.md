# Integrations

Neuron is a versatile tool that forms a crucial part of the IoT and Industrial IoT (IIoT) ecosystem. It serves as a bridge between on-site field equipment and various data processing and analysis platforms. This chapter delves into the steps involved in how Neuron interacts with various components of this ecosystem.

## Connect Southbound Devices

Southbound devices, including Programmable Logic Controllers (PLCs), Remote Terminal Units (RTUs), smart sensors, CNC machines, robotics, electricity equipment, and building automation systems, are the primary sources of data in industrial settings. Neuron collects data from these on-site field equipment, leveraging its compatibility with a wide range of communication protocols. This data collection process is the first step in transforming raw data into actionable insights.

## Integrate with EMQX/eKuiper

Once the data is collected, Neuron forwards it to platforms like eKuiper or EMQX broker for further processing. 

eKuiper, a real-time streaming data processing system, is used for time series database processing. Neuron's integration with eKuiper allows for the analysis of data in real-time, enabling immediate responses to changes in the data stream. So our users can leverage the benefit of low-latency processing at the edge side. Output stream data can be stored in the time series database like InfluxDB at the edge side.

EMQX broker, a fully open-source MQTT broker, can forward the data to Enterprise Resource Planning (ERP) systems or Manufacturing Execution Systems (MES), facilitating efficient resource management and production control.

Besides, you can also leverage the capability [EMQX ECP (EMQX Edge-to-Cloud Platform)](https://www.emqx.com/en/products/emqx-ecp), the advanced MQTT platform designed for edge-cloud collaboration to centrally manage the integration between Neuron and EMQX/eKuiper. 

## Integrate with the Cloud

Neuron also supports integration with major cloud platforms such as EMQX Cloud, Microsft Azure, Google Cloud, and AWS to seamlessly stream real-time industrial data directly into industrial applications such as MES, ERP, Big data, analytic software and etc. This integration enables a host of advanced data processing and storage capabilities. 

![integrations](./assets/integration.png)

This chapter elabrates on:

- [Neuron integration with eKuiper](./ekuiper/ekuiper.md) to provide edge processing capabilities
- [Neuron integration with EMQX broker](./sparkplug/sparkplug.md) to provide Industrial Communication with Sparkplub support. 




