# Using rpm package

## Download

Download the installation package according to different versions and architectures, E.g.

```bash
$ wget https://www.emqx.com/en/downloads/neuron/2.4.0/neuron-2.4.0-linux-amd64.rpm
```

## Install

Install according to different versions and architectures, E.g.

```bash
$ sudo rpm -i neuron-2.4.0-linux-amd64.rpm
```

::: tip
After successful installation of the rpm package, Neuron is automatically started.
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
$ sudo rpm -e neuron
```