# Installation

Following section describes how to install the Neuron software package on a Linux system device.

## Download

Neuron software package is available in EMQ website [https://www.emqx.com/en](https://www.emqx.com/en).

| Package Name                                     | Architecture System   |
| ------------------------------------------------ | --------------------- |
| _neuron-x.y.z-linux-x86_64.tar.gz_               | x86 64-bit            |
| _neuron-x.y.z-linix-armv7l.tar.gz_               | ARM hardware floating |
| _neuron-x.y.z-linix-aarch64.tar.gz_              | ARM 64-bit            |

For the version number x.y.z, x is major version number which may change if the entire system structure enhancement, y is minor version number which may change if there will be some additional features. z is the patch number for bug fix in the Neuron software.

## Pre-requisites

The following Linux distros or devices have been tested for Neuron.

| Linux distros or devices                                                             | Neuron package required           |
| ------------------------------------------------------------------------------------ | --------------------------------- |
| **Debian package system for x86_64** </br>Ubuntu 20.xx</br>Ubuntu 18.xx Desktop</br>Ubuntu 16.xx Desktop (install openssl1.1)</br>Ubuntu 14.xx Desktop (install openssl1.1)  | neuron-x.y.z-linux-x86_64.tar.gz |
| **Redhat package system for x86_64** </br>Centos 8</br>Centos 7.x (install openssl1.1) | neuron-x.y.z-linux-x86_64.tar.gz  |
| **Raspberry Pi 2** </br>Pi 4b+</br>Pi 3b+</br>Pi 2b+ (install openssl1.1)               | neuron-x.y.z-linux-armv7l.tar.gz  |
| armv7l Ubuntu Linux System                                                           | neuron-x.y.z-linux-armv7l.tar.gz  |
| aarch64 Ubuntu Linux System                                                          | neuron-x.y.z-linux-aarch64.tar.gz |

Note: Some Linux distros require **openssl1.1** installation.
For Debian package, wget [http://archive.ubuntu.com/ubuntu/pool/main/o/openssl/libssl1.1_1.1.0g-2ubuntu4_amd64.deb](http://archive.ubuntu.com/ubuntu/pool/main/o/openssl/libssl1.1_1.1.0g-2ubuntu4_amd64.deb)</br>
For Redhat package, [https://linuxscriptshub.com/update-openssl-1-1-0-centos-6-9-7-0](https://linuxscriptshub.com/update-openssl-1-1-0-centos-6-9-7-0/)</br>

Ensure that openssl is upgraded to version 1.1.If rpm -ivh neuron-1.3.0-linux-amd64.rpm prompts a missing dependency, run rpm -ivh neuron-1.3.0-linux-amd64.rpm --nodeps --force

## New Installation

New Neuron software can be installed in a home directory of any user account. In case a user account is needed, we recommand &quot;neuron&quot; for installation.

1. Extracting the software package to any directory, (i.e. /home/neuron ):

   ```bash
   ~\$ tar -zxvf neuron-x.y.z-linux-x86_64.tar.gz
   ```

2. Run Neuron for the first time to buildup Neuron data directories _dat_:

   ```bash
   ~\$ {PATH}/neuron start
   Directory {PATH}/dat created
   Directory {PATH}/dat/0 created
   Directory {PATH}/dat/0/adm created
   Directory {PATH}/dat/0/adm/usr created
   Directory {PATH}/dat/0/alm created
   Directory {PATH}/dat/0/cfg created
   Directory {PATH}/dat/0/log created
   Directory {PATH}/dat/0/scp created
   Directory {PATH}/dat/0/scp/subr created
   Directory {PATH}/dat/0/obj created
   Directory {PATH}/dat/0/trd created
   Neuron instance 0 is now running with PID:6312 Port:7000
   ```

## Starting the Neuron System

To start Neuron system by the command:

```bash
~\$ {PATH}/neuron start
Neuron instance 0 is now running with PID:6037 Port:7000
```

## Stopping the Neuron System

To stop the running of Neuron System by the command:

```bash
~\$ {PATH}/neuron stop
Neuron instance 0 is stopping ...
Stopped !
```

## Starting the specific Neuron System

To start specific Neuron instance by the command:

```bash
~\$ {PATH}/neuron start -i7
Neuron instance 7 is now running with PID:8097 Port:7007
```

## Stopping the specific Neuron System

To stop the running of specific Neuron by the command:

```bash
~\$ {PATH}/neuron stop -i7
Neuron instance 7 is stopping ...
Stopped !
```

## Starting multiple Neuron Systems

To start multiple Neuron system instances by the command

```bash
~\$ {PATH}/neuron start -a5
Neuron instance 0 is now running with PID:6066 Port:7000
Neuron instance 1 is now running with PID:6069 Port:7001
Neuron instance 2 is now running with PID:6076 Port:7002
Neuron instance 3 is now running with PID:6087 Port:7003
Neuron instance 4 is now running with PID:6090 Port:7004
```

## Stopping multiple Neuron Systems

To stop the running of multiple Neuron systems by the command:

```bash
~\$ {PATH}/neuron stop -a5
Neuron instance 0 is stopping ...
Stopped !
Neuron instance 1 is stopping ...
Stopped !
Neuron instance 2 is stopping ...
Stopped !
Neuron instance 3 is stopping ...
Stopped !
Neuron instance 4 is stopping ...
Stopped !
```

## Checking the Neuron System

To checkup the status of Neuron systems:

```bash
~\$ {PATH}/neuron status
Neuron instance 0 is running with PID:6118 Port:7000
Neuron instance 1 is running with PID:6121 Port:7001
Neuron instance 2 is running with PID:6132 Port:7002
Neuron instance 3 is running with PID:6139 Port:7003
Neuron instance 4 is running with PID:6144 Port:7004
```

## Optional Switches

Some more useful switches for &quot;neuron&quot; is available.

Usage: neuron [start|stop|status] [options]
| options:                        | description:                          |
| ------------------------------- | ------------------------------------- |
| -a or --allinstance `<number>`  | no. of instances `<2-10>`             |
| -i or --instance `<instanceno>` | instance no `<0-9>`                   |
| -u or --uuid `<uuid>`           | universal unique id `<max 36 chars>`  |
where [-a|-i] are exclusive options.

## Running in Docker

To get the docker image from [https://hub.docker.com](https://hub.docker.com)

```bash
~\$ docker pull emqx/neuron:1.0.0
```

To start docker container

```bash
~\$ docker run -d --name neuron -p 7000:7000 emqx/neuron:1.0.0
```
