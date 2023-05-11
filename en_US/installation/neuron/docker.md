# Running with Docker

## Get the image

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

## Start

```bash
## run Neuron
$ docker run -d --name neuron --log-opt max-size=100m -p 7000:7000 --privileged=true -v /host/dir:/opt/neuron/persistence --device /dev/ttyUSB0:/dev/ttyS0 --restart=always emqx/neuron:latest
```

* tcp 7000: Used to access the web and http api port.
* --restart=always: Automatically restart the neuron container when the docker process is restarted.
* --privileged=true: Optional parameter for easy troubleshooting.
* --env DISABLE_AUTH=1: Optional parameter to turn off authentication.
* -v /host/dir:/opt/neuron/persistence: Used to store Neuron configuration information in docker to a local directory, e.g. /host/dir to /opt/neuron/persistence.
* --device /dev/ttyUSB0:/dev/ttyS0: Used to map the serial port to docker. /dev/ttyUSB0 // Serial port device under Ubuntu; /dev/ttyS0 // Serial port device under Docker.
* --ulimit nofile=65535: The default value is 1024. When there are many connected devices, increase the value of this field, such as 65535.
* --log-opt: Limit the size of Docker standard output (stdout) (e.g., --log-opt max-size=100m).