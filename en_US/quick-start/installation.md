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

## Running with Docker

### Get the image

The neuron docker image can be downloaded from the docker hub website.[docker hub](https://hub.docker.com/r/emqx/neuron)

```bash
## pull Neuron
$ docker pull emqx/neuron:latest
```

To support the Alpine image with smaller occupation, please download it from the [docker hub](https://hub.docker.com/r/emqx/neuron/tags) website.

```bash
## pull Neuron
$ docker pull emqx/neuron:2.3.0-alpine
```

The NeuronEX docker image can be downloaded from the docker hub website.[docker hub](https://hub.docker.com/r/emqx/neuronex)

```bash
## pull NeuronEX
$ docker pull emqx/neuronex:latest
```

### Start

Start Neuron.

```bash
## run Neuron
$ docker run -d --name neuron -p 7000:7000 --privileged=true -v /host/dir:/opt/neuron/persistence --device /dev/ttyUSB0:/dev/ttyS0 --restart=always emqx/neuron:latest
```

Start NeuronEX

```bash
## run NeuronEX
$ docker run -d --name neuronex -p 7000:7000 --privileged=true -v /host/dir:/opt/neuron/persistence --device /dev/ttyUSB0:/dev/ttyS0 --restart=always emqx/neuronex:latest
```

|Parameter|Description|
| :-------------------- | :----------------------------------- |
| tcp 7000 | Used to access the web and http api port |
|--restart=always|Automatically restart the neuron container when the docker process is restarted |
|--privileged=true|Optional parameter for easy troubleshooting|
|--env DISABLE_AUTH=1|Optional parameter to turn off authentication|
|-v /host/dir:/opt/neuron/persistence|Used to store Neuron configuration information in docker to a local directory, E.g. /host/dir to /opt/neuron/persistence|
|--device /dev/ttyUSB0 | Used to map the serial port to docker. /dev/ttyUSB0 is Serial port device under Ubuntu; /dev/ttyS0 is Serial port device under Docker|
|--ulimit nofile=65535|The default value is 1024. When there are many connected devices, increase the value of this field, such as 65535|
|--log-opt|Limit the size of Docker standard output (stdout), E.g. --log-opt max-size=10m|

## Install using deb package

### Install

Install according to different versions and architectures, E.g.

```bash
$ sudo dpkg -i neuron-2.3.0-linux-armhf.deb
```

To avoid replacing the neuron package due to the ubuntu system perform the package updated automatically, you also need to execute the following command to keep the neuron package in the apt upgrade.

```bash
$ sudo apt-mark hold neuron
```

::: tip
After successful installation of the deb package, Neuron is automatically started.
:::

### Uninstall

```bash
$ sudo dpkg -r neuron
```

## Install using rpm package

### Install

Install according to different versions and architectures, E.g.

```bash
$ sudo rpm -i neuron-2.3.0-linux-armhf.rpm
```

::: tip
After successful installation of the rpm package, Neuron is automatically started.
:::

### Uninstall

```bash
$ sudo rpm -e neuron
```

## Install using .tar.gz package

### Download the installation package

Download the installation package according to different versions and architectures, E.g.

```bash
$ wget https://www.emqx.com/en/downloads/neuron/2.3.0/neuron-2.3.0-linux-armhf.tar.gz
```

### Unpacking

```bash
$ tar -zxvf neuron-2.3.0-linux-armhf.tar.gz
$ cd neuron-2.3.0-linux-armhf
```

### Start

The following command can be executed to start Neuron：

```bash
$ ./neuron
```

## Operate Neuron in command line

For rpm and deb installations, Neuron can perform the operation with following commands:

### View Neuron Status

```bash
$ sudo systemctl status neuron
```

### Stop Neuron

```bash
$ sudo systemctl stop neuron
```

### Reatart Neuron

```bash
$ sudo systemctl restart neuron
```
