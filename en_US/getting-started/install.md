# Installation

The following section describes how to install the Neuron package on X86/ARM Linux devices.

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

## Installation conditions

The rpm/deb package uses systemd to manage the neuron process and it is recommended that the rpm/deb package is used in preference.

| Linux distribution/device                                    | Required packages  |
| ------------------------------------------------------------ | ------------------ |
| **Debian package system**</br>Ubuntu 20.xx </br>Ubuntu 18.xx | deb/tar.gz         |
| **Redhat package system**</br>Contos 8</br>Centos 9          | rpm/tar.gz         |

## Installation steps

This section describes how to install the Neuron software for the first time on a Linux system.

### Using the deb package

#### Install

```bash
sudo dpkg -i xxx.deb
```

Install depending on the version, e.g.

```bash
sudo dpkg -i neuron-2.0.1-linux-armhf.deb
```

*Note*  After successful installation of the deb package, Neuron is automatically started.

#### Uninstall

```bash
sudo dpkg -r neuron
```

### Using the rpm package

#### Install

```bash
sudo rpm -i xxx.rpm --nodeps --force
```

Install depending on the version, e.g.

```bash
sudo rpm -i neuron-2.0.1-linux-armhf.rpm --nodeps --force
```

*Note* After successful installation of the rpm package, Neuron is automatically started.

#### Uninstall

```bash
sudo rpm -e neuron
```

### Using the .tar.gz package

#### Unpacking

```bash
sudo tar -zxvf xxx.tar.gz
cd xxx
```

Install depending on the version, e.g.

```bash
sudo tar -zxvf neuron-2.0.1-linux-armhf.tar.gz
cd neuron-2.0.1-linux-armhf
```

#### Start

The following command can be executed to boot from the current terminal：

```bash
./neuron
```

If you want to run as a daemon, you can execute the following command：

```bash
./neuron -d
```

Execute the following command to see all the parameters available on the command line：

```bash
./neuron -h
```

### Running with Docker

#### Get the image

The docker image can be downloaded from the docker hub website.[https://hub.docker.com](https://hub.docker.com)

```bash
docker pull neugates/neuron:2.0.0
```

#### Start

```bash
docker run -d --name neuron -p 7000:7000 -p 7001:7001 --privileged=true --restart=always neugates/neuron:2.0.0
```

* tcp 7000: Used to access the web.
* tcp 7001: http api port. (api port is web port + 1, e.g. when web port is mapped to 8000, api port should be mapped to 8001)
* --restart=always: Automatically restart the neuron container when the docker process is restarted.
* --privileged=true：Easy to troubleshoot problems.
* --device /dev/ttyUSB0:/dev/ttyS0: Used to map the serial port to docker.

### Neuron Operation

For rpm and deb installations, Neuron can view/start/stop the status with the following commands：

#### View Neuron Status

```bash
sudo systemctl status neuron
```

#### Stop Neuron

```bash
sudo systemctl stop neuron
```

#### Reatart Neuron

```bash
sudo systemctl restart neuron
```
