# Installation

This section describes how to install the Neuron package on X86/ARM Linux devices.

## Download

Neuron software packages can be downloaded from the Neuron website [https://neugates.io/downloads](https://neugates.io/downloads) according to the actual system.

| Download files               | Architecture  |
| ---------------------------- | ------------- |
| neuron-x.y.z-linux-amd64.deb | X86_64        |
| neuron-x.y.z-linux-armhf.deb | ARM_32        |
| neuron-x.y.z-linux-arm64.deb | ARM_64        |

Version number x.y.z Description:

* x is the major version number, which may change if the entire system architecture has been enhanced.
* y is the minor version number, which may change if certain additional features exist.
* z is the patch number for bug fixes in the Neuron software.

## Installation Conditions

| Linux distribution/device                                    | Required packages  |
| ------------------------------------------------------------ | ------------------ |
| **Debian package system**</br>Ubuntu 20.xx </br>Ubuntu 18.xx | deb/tar.gz         |
| **Redhat package system**</br>Contos 8</br>Centos 9          | rpm/tar.gz         |

The rpm/deb package uses systemd to manage the neuron process and it is recommended that the rpm/deb package is used in preference.

## Install using deb package

### Install

Install according to different versions and architectures, E.g.

```bash
$ sudo dpkg -i neuron-2.1.0-linux-armhf.deb
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
$ sudo rpm -i neuron-2.1.0-linux-armhf.rpm
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
$ wget https://www.emqx.com/en/downloads/neuron/2.1.0/neuron-2.1.0-linux-armhf.tar.gz
```

### Unpacking

```bash
$ sudo tar -zxvf neuron-2.1.0-linux-armhf.tar.gz
$ cd neuron-2.1.0-linux-armhf
```

### Start

The following command can be executed to start Neuron：

```bash
$ ./neuron-helper.sh  start
```

### Stop

The following command can be executed to stop Neuron：

```bash
$ ./neuron-helper.sh  stop
```

## Running with Docker

### Get the image

The docker image can be downloaded from the docker hub website.[https://hub.docker.com](https://hub.docker.com)

```bash
$ docker pull emqx/neuron
```

### Start

```bash
$ docker run -d --name neuron -p 7000:7000 -p 7001:7001 -p 9081:9081 --privileged=true --restart=always emqx/neuron
```

* tcp 7000: Used to access the web.
* tcp 7001: http api port. (api port is web port + 1, e.g. when web port is mapped to 8000, api port should be mapped to 8001)
* tcp 9081: eKuiper api port.
* --restart=always: Automatically restart the neuron container when the docker process is restarted.
* --privileged=true：Easy to troubleshoot problems.
* -v /host/dir:/opt/neuron/persistence: Used to store Neuron configuration information in docker to a local directory, e.g. /host/dir.
* --device /dev/ttyUSB0:/dev/ttyS0: Used to map the serial port to docker.

## Neuron Operation

For rpm and deb installations, Neuron can view/start/stop the status with the following commands：

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
