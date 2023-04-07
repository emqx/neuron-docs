# Installation

Neuron and NeuronEX supports 32-bit/64-bit ARM and 64-bit x86 architectures on Linux-based operating systems and is available in the following formats:

* Debian Software Package (DEB) format for Debian, Ubuntu Linux-based operating systems.

* Redhat Package Manager (RPM) format for Red Hat, CentOS Linux-based operating systems.


## Systems for Installation Packages

| Linux distribution                                    | Required packages  |
| ------------------------------------------------------------ | ------------------ |
| Ubuntu 20.04 </br>Ubuntu 18.04 </br>Ubuntu16.04</br>Debian 11</br>Debian 10</br>Debian 9</br>Debian 8               | **Debian Software Package** (.deb)         |
| CentOS Stream 9</br>CentOS Stream 8</br>CentOS 7    | **Redhat Package Manager** (.rpm)         |

:::tip
The installation of the rpm/deb package is recommended to set up the system service manager (systemd) to monitor the Neuron running instance.
:::


## Hardware Requirements

|Tag Limits|Minimum Memory Recommendation|Hardware Architecture|Remarks|
| :-------------------- | :------------------------------ | :---------------------------------- | :----------------------------------- |
| 100 tags    | 128M memory | CPU architecture such as ARM, X86, MIPS, and RISC-V; Linux system or Docker container | Small gateway device |
| 1,000 tags  | 256M memory | CPU architecture such as ARM, X86, MIPS, and RISC-V; Linux system or Docker container | Medium gateway device |
| 10,000 tags | 512M memory | CPU architecture such as ARM, X86, MIPS, and RISC-V; Linux system or Docker container | Medium gateway, industrial computer, etc |
| More than 10,000 tags | 1G memory | CPU architecture such as ARM, X86, MIPS, and RISC-V; Linux system or Docker container | Medium or large gateway, industrial computer, servers, etc |


## Download

Neuron software packages can be downloaded from the Neuron website [https://neugates.io/downloads](https://neugates.io/downloads). You can also download Neuron from [Github](https://github.com/emqx/neuron/releases).

| Download files                    | Architecture  |
| --------------------------------- | ------------- |
| neuron-x.y.z-linux-amd64.deb      | X86_64        |
| neuron-x.y.z-linux-armhf.deb      | ARM_32        |
| neuron-x.y.z-linux-arm64.deb      | ARM_64        |
| neuron-x.y.z-linux-amd64.rpm      | X86_64        |
| neuron-x.y.z-linux-armhf.rpm      | ARM_32        |
| neuron-x.y.z-linux-arm64.rpm      | ARM_64        |
| neuronex-x.y.z-linux-amd64.deb    | X86_64        |
| neuronex-x.y.z-linux-armhf.deb    | ARM_32        |
| neuronex-x.y.z-linux-arm64.deb    | ARM_64        |
| neuronex-x.y.z-linux-amd64.rpm    | X86_64        |
| neuronex-x.y.z-linux-armhf.rpm    | ARM_32        |
| neuronex-x.y.z-linux-arm64.rpm    | ARM_64        |

Neuron has two distributions:

* neuron: Industrial IIoT Server

* neuronex: Industrial IIoT Server with eKuiper processing engine

Release number x.y.z have following description:

* x is the major release number: the change in this number means that the software architecture has changed. Therefore, upgrading to a major release does not guarantee compatibility with the previous major release.

* y is the minor release number: the change in this number introduces some new features. Upgrading to a minor release would ensure backward compatibility.

* z is the maintenance release number: this new release number only contains patches, bug fixes, etc.