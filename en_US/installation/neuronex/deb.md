# Using deb package

## Download

Download the installation package according to different versions and architectures, E.g.

```bash
$ wget https://www.emqx.com/en/downloads/neuron/2.4.0/neuronex-2.4.0-linux-amd64.deb
```

## Install

Install according to different versions and architectures, E.g.

```bash
$ sudo dpkg -i neuronex-2.4.0-linux-amd64.deb
```

To avoid replacing the neuron package due to the ubuntu system perform the package updated automatically, you also need to execute the following command to keep the neuron package in the apt upgrade.

```bash
$ sudo apt-mark hold neuron
```

::: tip
After successful installation of the deb package, Neuron is automatically started.
:::

## Status

```bash
$ sudo systemctl status neuron
```

## Stop

```bash
$ sudo systemctl stop neuron
```

## Restart

```bash
$ sudo systemctl restart neuron
```

## Uninstall

```bash
$ sudo dpkg -r neuron
```
