# Installation

Neuron is divided into two installation packages:

* NeuronEX: Integrated eKuiper, which carries the function of data stream processing engine, allows users to collect and process data at the same time.

* Neuron: Without integrating eKuiper, it mainly realizes the collection of industrial data.

Users can choose according to their own needs.

## Hardware requirement

|Specifications|Minimum configuration recommendation|Hardware architecture|remarks|
| :-------------------- | :------------------------------ | :---------------------------------- | :----------------------------------- |
| 100 tags    | 128M memory | CPU architecture such as ARM, X86, MIPS, and RISC-V; Linux system or Docker container | Small gateway device |
| 1,000 tags  | 256M memory | CPU architecture such as ARM, X86, MIPS, and RISC-V; Linux system or Docker container | Medium gateway device |
| 10,000 tags | 512M memory | CPU architecture such as ARM, X86, MIPS, and RISC-V; Linux system or Docker container | Medium gateway, industrial computer, etc |
| More than 10,000 tags | 1G memory | CPU architecture such as ARM, X86, MIPS, and RISC-V; Linux system or Docker container | Medium or large gateway, industrial computer, servers, etc |

## Installation Conditions

| Linux distribution                                    | Required packages  |
| ------------------------------------------------------------ | ------------------ |
| **Debian package system**</br>Ubuntu 20.04 </br>Ubuntu 18.04 </br>Ubuntu16.04</br>Debian 11</br>Debian 10</br>Debian 9</br>Debian 8               | deb         |
| **Redhat package system**</br>CentOS Stream 9</br>CentOS Stream 8</br>CentOS 7    | rpm         |

:::tip
The rpm/deb package uses systemd to manage the neuron process and it is recommended that the rpm/deb package is used in preference.
:::

## Download

Neuron software packages can be downloaded from the Neuron website [https://neugates.io/downloads](https://neugates.io/downloads). You can also download Neuron from [Github](https://github.com/emqx/neuron/releases).

| Download files                    | Architecture  |
| --------------------------------- | ------------- |
| neuron-x.y.z-linux-amd64.deb      | X86_64        |
| neuron-x.y.z-linux-armhf.deb      | ARM_32        |
| neuron-x.y.z-linux-arm64.deb      | ARM_64        |

Version number x.y.z Description:

* x is the major version number: in general, this version will introduce some important functions, such as the introduction of architectural changes. The upgrade of the major version does not guarantee the compatibility with the old version.

* y is the minor version number: in general, this type of version will introduce some new functions, but the compatibility under this major version number will be guaranteed.

* z is the maintenance version number: in general, this version only contains patches of bug fixes in the software, etc.