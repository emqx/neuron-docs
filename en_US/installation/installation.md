# Installation

Neuron supports 32-bit/64-bit ARM and 64-bit x86 architectures on Linux-based operating systems and are available in the following installation package formats:

* Debian Software Package (.deb) format for Debian, Ubuntu Linux-based operating systems.

* Redhat Package Manager (.rpm) format for Red Hat, CentOS Linux-based operating systems.


## Installation Packages for Linux Distro

| Linux Distribution                                    | Required Package  |
| ------------------------------------------------------------ | ------------------ |
| Ubuntu 20.04 </br>Ubuntu 18.04 </br>Ubuntu16.04</br>Debian 11</br>Debian 10</br>Debian 9</br>Debian 8               | **Debian Software Package** (.deb)         |
| CentOS Stream 9</br>CentOS Stream 8</br>CentOS 7    | **Redhat Package Manager** (.rpm)         |
| Other Linux | **Tape Archiver** (tar.gz) |

:::tip
The rpm/deb packages installation is recommended for setting up the system service manager (systemd) to monitor the Neuron running instance.
:::


## Hardware Requirements

Neuron is fully developed in C language and supports running on x86, ARM and other hardware architectures as well as container deployment, such as K8s, KubeEdge, etc. On devices with limited hardware resources, it can also achieve data acquisition of 100 ms or even 10 ms level. On servers with sufficient hardware resources, Neuron can also make full use of multi-core CPUs, and can simultaneously conduct data acquisition and point write control of hundreds of thousands of points at the frequency of 100 ms.

The following table lists the hardware conditions required for the minimum demand of Neuron at different number of tags.

|Tag Limits|Minimum Memory Recommendation|Hardware Architecture|Remarks|
| :-------------------- | :------------------------------ | :---------------------------------- | :----------------------------------- |
| 100 tags    | 128M memory | 32-bit/64-bit ARM and 64-bit x86 architectures | Raspberry Pi 3 |
| 1,000 tags  | 256M memory | 32-bit/64-bit ARM and 64-bit x86 architectures | Raspberry Pi 4 |
| 10,000 tags | 512M memory | 64-bit ARM and 64-bit x86 architectures | Industrial PC, etc |
| More than 10,000 tags | 1G memory | 64-bit x86 architectures | Powerful Industrial PC, Server, etc |

:::tip
Neuron has no upper limitation on the number of tags. It depends on the allocated CPU and memory resources. Neuron is very portable to run on limited resource like single board hardware, or on powerful servers. The following figures are the results of Neuron performance test for your reference and these benchmark results are still not the upper limits. A more powerful server can be used for more tags.

Platform                         : Intel(R) Xeon(R) Gold 6266C@3.00GHz</br>
Memory                           : 4G</br>
Architecture                     : x86</br>
OS Support                       : Ubuntu 20.04</br>
No. of connections               : 1000 connections</br>
No. of tags for each connection  : 300 tags</br>
Total tags                       : 300,000 tags</br>
Memory Usage                     : 300M</br>
CPU Usage                        : 90%</br>

:::



## Download

Neuron software packages can be downloaded from the Neuron website [https://neugates.io/downloads](https://neugates.io/downloads). You can also download Neuron from [Github](https://github.com/emqx/neuron/releases).

## Debian Software Package

| Download files               | Architecture |
| ---------------------------- | ------------ |
| neuron-x.y.z-linux-amd64.deb | X86_64       |
| neuron-x.y.z-linux-armhf.deb | ARM_32       |
| neuron-x.y.z-linux-arm64.deb | ARM_64       |
| neuronex-x.y.z-linux-amd64.deb | X86_64       |
| neuronex-x.y.z-linux-armhf.deb | ARM_32       |
| neuronex-x.y.z-linux-arm64.deb | ARM_64       |


## Redhat Package Manager

| Download files               | Architecture |
| ---------------------------- | ------------ |
| neuron-x.y.z-linux-amd64.rpm | X86_64       |
| neuron-x.y.z-linux-armhf.rpm | ARM_32       |
| neuron-x.y.z-linux-arm64.rpm | ARM_64       |
| neuronex-x.y.z-linux-amd64.rpm | X86_64       |
| neuronex-x.y.z-linux-armhf.rpm | ARM_32       |
| neuronex-x.y.z-linux-arm64.rpm | ARM_64       |


## Tape Archive

| Download files               | Architecture |
| ---------------------------- | ------------ |
| neuron-x.y.z-linux-amd64.rpm | X86_64       |
| neuron-x.y.z-linux-armhf.rpm | ARM_32       |
| neuron-x.y.z-linux-arm64.rpm | ARM_64       |
| neuronex-x.y.z-linux-amd64.rpm | X86_64       |
| neuronex-x.y.z-linux-armhf.rpm | ARM_32       |
| neuronex-x.y.z-linux-arm64.rpm | ARM_64       |


## Docker Image

| Download files      | Architecture |
| ------------------- | ------------ |
| neuron-x.y.z-alpine | Docker       |


## Build from Source

| Download files                | Remark        |
| ----------------------------- | ------------- |
| http://github.com/emqx/neuron | Github Source |

Release number x.y.z have following description:

* x is the major release number: the change in this number means that the software architecture has changed. Therefore, upgrading to a major release does not guarantee compatibility with the previous major release.

* y is the minor release number: the change in this number introduces some new features. Upgrading to a minor release would ensure backward compatibility.

* z is the maintenance release number: this new release number only contains patches, bug fixes, etc.


## License

At present, Neuron has open source MQTT, RESTful API and Modbus TCP, and users can directly use the open source driver protocols. However, by uploading a valid license, users can use more driving protocols such as OPC UA, Modbus RTU, Mitsubishi PLC and Omron PLC.

Please refer to [Module List](../introduction/plugin-list/plugin-list.md) for the driver protocols supported by Neuron.

