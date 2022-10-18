# Installation

In order to meet customer needs, Neuron is divided into two types, one that integrates eKuiper and carries a data stream processing engine interface, named Neuron-plus, and the other that does not integrate eKuiper, named Neuron. Users can choose according to their own needs.Neuron-plus version now only supports docker installation.

## Download

Neuron software packages can be downloaded from the Neuron website [https://neugates.io/downloads](https://neugates.io/downloads) according to the actual system, or download via [Github](https://github.com/emqx/neuron/releases).

| Download files                    | Architecture  |
| --------------------------------- | ------------- |
| neuron-x.y.z-linux-amd64.deb      | X86_64        |
| neuron-x.y.z-linux-armhf.deb      | ARM_32        |
| neuron-x.y.z-linux-arm64.deb      | ARM_64        |

Version number x.y.z Description:

* x is the major version number, which may change if the entire system architecture has been enhanced.
* y is the minor version number, which may change if certain additional features exist.
* z is the patch number for bug fixes in the Neuron software.

## Installation Conditions

| Linux distribution/device                                    | Required packages  |
| ------------------------------------------------------------ | ------------------ |
| **Debian package system**</br>Ubuntu 20 </br>Ubuntu 18               | deb/tar.gz         |
| **Redhat package system**</br>Contos stream 8</br>Centos stream 9    | rpm/tar.gz         |

:::tip
The rpm/deb package uses systemd to manage the neuron process and it is recommended that the rpm/deb package is used in preference.
:::

## Install using deb package

### Install

Install according to different versions and architectures, E.g.

```bash
$ sudo dpkg -i neuron-2.2.0-linux-armhf.deb
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
$ sudo rpm -i neuron-2.2.0-linux-armhf.rpm
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
$ wget https://www.emqx.com/en/downloads/neuron/2.2.0/neuron-plus-2.2.0-linux-armhf.tar.gz
```

### Unpacking

```bash
$ sudo tar -zxvf neuron-2.2.0-linux-armhf.tar.gz
$ cd neuron-2.1.0-linux-armhf
```

### Start

The following command can be executed to start Neuron：

```bash
$ ./neuron
```

## Running with Docker

### Get the image

The neuron docker image can be downloaded from the docker hub website.[https://hub.docker.com](https://hub.docker.com/r/emqx/neuron)

```bash
## pull neuron
$ docker pull emqx/neuron:latest
```

The neuron-plus docker image can be downloaded from the docker hub website.[https://hub.docker.com](https://hub.docker.com/r/emqx/neuron-plus)

```bash
## pull neuron-plus
$ docker pull emqx/neuron-plus:latest
```

### Start

Start neuron.

```bash
## run neuron
$ docker run -d --name neuron -p 7000:7000 -p 7001:7001 --privileged=true --restart=always emqx/neuron:latest
```

Start neuron-plus

```bash
## run neuron-plus
$ docker run -d --name neuron-plus -p 7000:7000 -p 7001:7001 --privileged=true --restart=always emqx/neuron-plus:latest
```

* tcp 7000: Used to access the web.
* tcp 7001: http api port. (api port is web port + 1, e.g. when web port is mapped to 8000, api port should be mapped to 8001)
* --restart=always: Automatically restart the neuron container when the docker process is restarted.
* --privileged=true: Optional parameter for easy troubleshooting.
* --env DISABLE_AUTH=true: Optional parameter to turn off authentication.
* -v /host/dir:/opt/neuron/persistence: Used to store Neuron configuration information in docker to a local directory, e.g. /host/dir.
* --device /dev/ttyUSB0:/dev/ttyS0: Used to map the serial port to docker.

## Operate Neuron in command line

For rpm and deb installations, Neuron can perform the operation with following commands：

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
