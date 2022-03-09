# Neuron 2.x Application And Driver Instructions

This document mainly introduces some parameter configuration and point information configuration specifications for northbound applications and southbound drives.

---

## Common Address Format Option

Common options supported by each driver's address format.

---

**#** endian

```
 - B  = 2,1     int16/uint16
 - L  = 1,2     int16/uint16 (default)
 - LL = 1,2,3,4 int32/uint32/float (default)
 - LB = 2,1,4,3 int32/uint32/float
 - BB = 3,4,1,2 int32/uint32/float
 - BL = 4,3,2,1 int32/uint32/float
```

**.**  \[bit][len\[H]\[L]\[D]\[E]]  bit operation or string len

```
- H = high-to-low endian (default)
- L = low-to-high endian
- D = a high byte is stored in an int16
- E = a low byte is stored in an int16
```

---

## MQTT

The data collected from the device can be transmitted to the mqtt broker through mqtt application, and instructions can be sent to neuron throuth mqtt application.

---

### Parameter Setting

**client-id** is mqtt client id.

**ssl** enable mqtt ssl, default false.

**host** is mqtt broker host.

**port** is mqtt broker port.

**username** is the user used when connecting to the broker.

**password** is the password used when connecting to the broker.

**ca-path** is ca path.

**ca-file** is ca file.

---

## Modbus

The modbus protocol includes three drivers: modbus RTU, modbus tcp, and modbus RTU over TCP.

---

### Support Data Type

* INT16
* INT32
* UINT16
* UINT32
* FLOAT
* BIT
* STRING

---

### Parameter Setting

**connection mode**: The way the driver connects to the device, the default is client, which means that the neuron driver is used as the client.

**host**：When neuron is used as a client, host means the ip of the remote device. When used as a server, it means the ip used by neuron locally, and 0.0.0.0 can be filled in by default.

**port**:  When neuron is used as client, port means the tcp port of the remote device. When used as a server, it means the tcp port used by neuron locally. default 502.

---

### Address Format

> SLAVE!ADDRESS\[.BIT][#ENDIAN]\[.LEN\[H]\[L]\[D]\[E]]</span>

---

**SLAVE** is slave id.

**ADDRESS** is the register address.

| Area           | Address Range   | Attribute  | Register size | Function     |
| -------------- | --------------- | ---------- | ------------- | ------------ |
| coil           | 000001 ~ 065536 | read/write | 1bit          | 0x1,0x5,0x0f |
| input          | 100001 ~ 165536 | read       | 1bit          | 0x2          |
| input register | 300001 ~ 365536 | read       | 16bit         | 0x4          |
| hold register  | 400001 ~ 465536 | read/write | 16bit         | 0x3,0x6,0x10 |

| Data Type          | Area                         | Attribute                                               |
| ------------------ | ---------------------------- | ------------------------------------------------------- |
| uint16/int16       | input register\hold register | input register(r), hold register(w)                     |
| uint32/int32/float | input register\hold register | input register(r), hold register(w)                     |
| bit                | all area                     | input(r), coil(rw), input register(r), hold register(w) |
| string             | input register\hold register | input register(r), hold register(w)                     |

#### **example**

```
bit:
 1!00001
 1!00007
 1!10001
 1!10005
 1!30004.0
 1!40010.4
 1!40001.15

int16/uint16:
 1!30004(default #L)
 1!30004#B
 1!30004#L
 1!40004(default #L)
 1!40004#L
 1!40004#B

int32/uint32/float:
 1!30004(default #LL)
 1!30004#BB
 1!30004#LB
 1!30004#BL
 1!30004#LL
 1!40004(default #LL)
 1!40004#LB
 1!40004#BB
 1!40004#LL
 1!40004#BL

string:
 1!30001.10(default H)
 1!30001.10H
 1!30001.10L
 1!40001.10(default H)
 1!40001.10H
 1!40001.10L
```

**!** Some device documents use function and register addresses to describe instructions. First, determine the highest digit of the address according to function. And add 1 to the register address to be the address used by neuron.

example: function is 0x3, and register address is 0, then address used by neuron is 400001.

---

## OPC UA

---

### Support Data Type

* BYTE
* INT8
* INT16
* INT32
* INT64
* UINT8
* UINT16
* UINT32
* UINT64
* FLOAT
* DOUBLE
* BOOL
* BIT
* STRING

---

### Parameter Setting

**host** is remote plc host.

**port** is remote plc port. default 4840.

**username** is the user used when connecting to plc.

**password** is the password used when connecting to plc.

**cert-file** is the certificate to provide login user authentication.

**key-file** is the private key to provide signature and encrypted transmission.s

---

### Addresses Format

> IX!NODEID</span>

---

**IX** is the namespace index.

**NODEID** is the node id.

*example*:

* 2!Device1.Module1.Tag1 represents namespace index is 2 and node ID is Device1.Module1.Tag

**!** Please refer to OPC UA standard for the explanation of namespace index and node id.
