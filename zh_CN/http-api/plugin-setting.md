# 插件设置

## MQTT

```json
{
    "node": "",
    "params": {
        // required, subscription data reporting channel
        "upload-topic": "",
        // required, the json format selection of the reported data, 0 values (default), 1 tags
        "format": 1,
        // required, the size limit of memory cache
        "cache-mem-size": 0,
        // required, the size limit of disk cache 
        "cache-disk-size":  0,

        // required, MQTT Broker host
        "host": "",
        // required, MQTT Broker port number
        "port": 1883,
        // optional, username to use when connecting to the broker
        "username": "",
        // optional, the password to use when connecting to the broker
        "password": "",

        // optional, whether to enable mqtt ssl
        "ssl": true,
        // ca file, only enabled when the ssl value is true, in which case it is required
        "ca": "",
        // optional, cert file, only enabled when the ssl value is true
        "cert": "",
        // optional, key file, only enabled when the ssl value is true
        "key": "",
        // optional, key file password, only enabled when the ssl value is true
        "keypass": ""
    }
}

```

## Modbus

### Modbus TCP QH

```json
{
    "node": "modbus-tcp",
    "params": {
        // required, the ip of the remote device
        "host": "127.0.0.1",
        // required, the tcp port of the remote device
        "port": 502,
        // required, timeout for sending requests to the device
        "timeout": 3000,
         // required, 0 the neuron driver is used as the client, 1 the neuron driver is used as the server
        "connection_mode": 0
    }
}
```

### Modbus TCP

```json
{
    "node": "modbus-tcp",
    "params": {
        // required, 0 the neuron driver is used as the client, 1 the neuron driver is used as the server
        "connection_mode": 0,
        // required, client: host means the ip of the remote device. server: it means the ip used by neuron locally
        "host": "127.0.0.1",
        // required, client: port means the tcp port of the remote device. server: it means the tcp port used by neuron locally
        "port": 502,
        // required, timeout for sending requests to the device
        "timeout": 3000,
        // required, send reading instruction interval(ms)
        "interval": 20,
        // required, TCP transfer(0) or UDP transfer(1)
        "transport_mode": 0,
        // required, the maximum number of retries after a failed attempt to send a read command
        "max_retries": 0,
        // required, resend reading instruction interval(ms) after a failed attempt to send a read command
        "retry_interval": 0
    }
}
```

### Modbus RTU

#### 串口连接设置

```json
{
    "node": "modbus-rtu",
    "params": {
        // required, connection method, 0 serial port, 1 tcp,
        "link": 0,
        // required, timeout for sending requests to the device
        "timeout": 3000,
        // serial port required, use a serial device
        "device": "dev/ttyUSB0",
        // serial port required, stopbits
        "stop": 0,
        // serial port required, parity bit
        "parity": 0,
        // serial port required, baudrate
        "baud": 4,
        // serial port required, bytesize
        "data": 3
    }
}
```

#### TCP 连接设置

```json
{
    "node": "modbus-rtu",
    "params": {
        // required, connection method, 0 serial port, 1 tcp,
        "link": 1,
        // required, timeout for sending requests to the device
        "timeout": 3000,
        // tcp required, client: host means the ip of the remote device. server: it means the ip used by neuron locally
        "host": "127.0.0.1",
        // tcp required, client: port means the tcp port of the remote device. server: it means the tcp port used by neuron locally
        "port": 502,
        // tcp required, 0 the neuron driver is used as the client, 1 the neuron driver is used as the server
        "connection_mode": 0,
        // required, send reading instruction interval(ms)
        "interval": 20,
        // required, the maximum number of retries after a failed attempt to send a read command
        "max_retries": 0,
        // required, resend reading instruction interval(ms) after a failed attempt to send a read command
        "retry_interval": 0
    }
}
```

## OPC UA

```json
{
    "node": "opc ua",
    "params": {
        // required, the address of the remote access plc
        "url": "opc.tcp://127.0.0.1:4840/",
        // optional, the user used when connecting to plc
        "username": "",
        // optional, the password used when connecting to plc
        "password": "",
        // optional, the certificate to provide login user authentication
        "cert": "",
        // optional, the private key to provide signature and encrypted transmissions
        "key": ""
    }
}
```

## Simemens S7 ISOTCP

```json
{
    "node": "s7",
    "params": {
        // required, remote plc ip
        "host": "127.0.0.1",
        // required, remote plc port
        "port": 102,
        // required, plc rack number
        "rack": 0,
        // required, plc cpu slot
        "slot": 1
    }
}
```

## OMRON FINS on TCP

```json
{
    "node": "fins",
    "params": {
        // required, remote plc ip
        "host": "127.0.0.1",
        // required, remote plc port
        "port": 9600
    }
}
```

## Mitsubishi MELSEC-Q E71

```json
{
    "node": "e71",
    "params": {
        // required, remote plc ip
        "host": "127.0.0.1",
        // required, remote plc port
        "port": 2000
    }
}
```

## IEC 60870-5-104

```json
{
    "node": "iec104",
    "params": {
        // required, device ip
        "host": "127.0.0.1",
        // required, device port
        "port": 2404,
        // required, common address
        "ca": 1,
        // required, station interrogation interval
        "interval": 10
    }
}
```

## BACnet/IP

```json
{
    "node": "bacnet",
    "params": {
        // required, BACnet device ip
        "host": "127.0.0.1",
        // required, BACnet device port
        "port": 47808
    }
}
```

## DL/T645-2007

### 串口连接设置

```json
{
    "node": "dlt645-1",
    "params": {
        // required, connection method, 0 serial port, 1 tcp
        "link": 0,
        // required, contact address
        "mail_address": 210220003011,
        // required, timeout for sending requests to the device
        "timeout": 3000,
        // serial port required, use a serial device
        "device": "dev/ttyUSB0",
        // serial port required, stopbits
        "stop": 0,
        // serial port required, parity bit
        "parity": 2,
        // serial port required, baudrate
        "baud": 4,
        // serial port required, bytesize
        "data": 3
    }
}
```

### TCP 连接设置

```json
{
    "node": "dlt645-1",
    "params": {
        // required, connection method, 0 serial port, 1 tcp
        "link": 1,
        // required, contact address
        "mail_address": 210220003011,
        // required, timeout for sending requests to the device
        "timeout": 3000,
        // tcp required, client: host means the ip of the remote device. server: it means the ip used by neuron locally
        "host": "127.0.0.1",
        // tcp required, client: port means the tcp port of the remote device. server: it means the tcp port used by neuron locally
        "port": 502,
        // tcp required, 0 the neuron driver is used as the client, 1 the neuron driver is used as the server
        "connection_mode": 0
    }
}
```

## Sparkplug_B

```json
{
    "node": "sparkplugb",
    "params": {
        // required, MQTT client ID, A unique identifier that can represent the edge end
        "client-id": "saprk-test",
        // required, the top-level logical group in Sparkplug_B
        "group-id": "test",
        // required, the egde node id
        "node-id": "neuron1"
        // required, whether to enable mqtt ssl,
        "ssl": false,
        // required, MQTT Broker host
        "host": "broker.emqx.io",
        // required, MQTT Broker port number
        "port": 1883,
        // optional, username to use when connecting to the broker
        "username": "",
        // optional, the password to use when connecting to the broker
        "password": "",
        // required, ca file, only enabled when the ssl value is true
        "ca": "",
        // optional, cert file, only enabled when the ssl value is true
        "cert": "",
        // optional, key file, only enabled when the ssl value is true
        "key": "",
        // optional, key file password, only enabled when the ssl value is true
        "keypass": ""
    }
}
```

## NON A11

```json
{
    "node": "nona11",
    "params": {
        // required, 0 the neuron driver is used as the client, 1 the neuron driver is used as the server
        "connection_mode": 0,
        // required, client: port means the tcp port of the remote device. server: it means the tcp port used by neuron locally
        "host": "127.0.0.1",
        // required, client: port means the tcp port of the remote device. server: it means the tcp port used by neuron locally
        "port": 10,
        // required, NON-A11 device site number
        "site": 1
    }
}
```
