# What is Neuron?

Neuron is an industrial protocol gateway software running on various IoT edge gateway hardware. It aims to solve the problem of difficult unified access to device data in the context of Industry 4.0.

Neuron can realize the interconnection between various Industrial IoT platform and devices by converting a wide varity of protocols into a standard unified IoT MQTT message, performing remote control command and data acquisition, utimately providing data support for the intelligent manufacturing.

Neuron supports one-stop access to multiple devices with dozens of industrial protocols, and converts to MQTT protocol. With ultra-low resource consumption, it can be deployed natively or containerized in various edge hardware like X86, ARM, RISC-V and other architectures. However, users can achieve online gateway configuration management through the Web-based management dashboard.

Neuron offers the following product features.

- Support for numerous protocols and devices such as [Modbus, OPCUA, Ethernet/IP, IEC104, BACnet and more](module-plugins/module-list.md).
- Deliver data through northbound standard MQTT to a designated MQTT message server based on user-specified configurations.
- Listen to southbound control device for data reporting and control the device by forwarding relevant control commands back to devices.
- Has low memory footprint, less than 10M, can run on low configuration hardware.
- Combine with the rule engine function provided by [eKuiper](https://www.lfedge.org/projects/ekuiper) to quickly implement rule-based device control.
- Integrate with other application to control industrial devices, or to change parameters or labels, through [API](api.md) or [MQTT](mqtt.md) services.
- Provide management dashboard for users to monitor data, device status and to manange configuration in a browser, enabling access to cross-industrial device data.
- Support for encrypted TLS, HTTPS and JWT auth to ensure data security in transmission.
