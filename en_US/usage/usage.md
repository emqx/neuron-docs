# Usage

This chapter introduces the usage of Neuron after configuration.

## Navigating the Dashboard

### Menu Bar
Monitoring - This is data monitoring screen.

* [Data Monitoring](./monitoring.md)

Configuration - This is used to configure the Neuron usage.
Configuration/North Apps - This is to set up the northbound application parameters
Configuration/South Drivers - This is to set up the southbound driver parameters, groups and tags details.
Configuration/Plugin - This is a management interface for those northbound and southbound plugins.

* [Configuration](../configuration/configuration.md)

Data Streaming - This is used to set up the SQL streaming rules and configure to integrate with the external AI/ML platfrom (for NeuronEX only). 

* [Data Streaming](../data-streaming/data-streaming.md)

Administration - This menu gives you access to a variety of functions, including log management, password change.

* [Administration](./admin/admin.md)

### Header Bar
The header bar gives you access to various statistic in terms of message inbound and outbound figures.

* [Performance Statistics](./dashboard/data-statistics.md)

Note: Parameters marked with `*` are required, and each parameter is followed by a field description key. Hover the mouse over it to explain the field in detail.

## Configuring the Delivery Message Streams
There are two message streams when configuring data delivery plugins such as MQTT client.
* data message stream (Telemetry)
* status message stream (Heartbeat)

If the tag attribute is set to Subscribe, the value will be reported to the cloud only when the value changes. Otherwise, the value will be reported in cyclic time base as polling interval setting in the group.

Offline data cache is another important feature to prevent the data loss when network is offline or temporary unavailable. The cache capacity depends on the physical storage size available for queuing the messages.

* [Offline Data Cache](./offline-data-cache.md)

### Telemetry
Telemetry is the time series metric data stream publishing to the predefined destination like cloud platform or on-premise application. For each group defined in configuration process, it will create an telemetry message to destination application.

### Heartbeat
Heartbeat is the time series states of both devices and Neuron instance itself. It contains the device status and alarms, running mode, communication link status, etc. Moreover, if the platform or application can't receive this message stream for a certain time (10 seconds or above), those connections to devices from the Neuron can be regarded as broken.

## Delivering the Control Command to Devices
Neuron offer the southbound node command and control capability. This southbound control and command enables the issuance of commands or actions to devices on behalf of:

* other northbound nodes within same instance (for example, an edge analytics or rules engine service)
* other applications that may exist on the same system with Neuron instance (for example, a management agent that needs to open a valve)
* any external system that needs to command those devices (for example, a cloud-based application that determined the need to modify the settings on a collection of devices)

There are three ways to deliver command to a device.
* Users can issue an command on the dashboard monitoring screen.
* other applications can deliver the command through the RESTful APIs
* any external system like cloud-based platform can publish the command to specific topic where the command would be sent to Neuron and then to the device.

* [Control Device](./device-control.md)
Note: The write attribute must be activated when configuring the tags details. Otherwise, there is no way to control the device.

