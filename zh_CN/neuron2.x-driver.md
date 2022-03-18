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

| AREA           | ADDRESS RANGE   | ATTRIBUTE  | REGISTER SIZE | FUNCTION     |
| -------------- | --------------- | ---------- | ------------- | ------------ |
| coil           | 000001 ~ 065536 | read/write | 1bit          | 0x1,0x5,0x0f |
| input          | 100001 ~ 165536 | read       | 1bit          | 0x2          |
| input register | 300001 ~ 365536 | read       | 16bit         | 0x4          |
| hold register  | 400001 ~ 465536 | read/write | 16bit         | 0x3,0x6,0x10 |

| DATA TYPE          | AREA                         | ATTRIBUTE                                               |
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

**endpoint url** is the address of the remote access plc, the default value is `opc.tcp://127.0.0.1:4840/` .

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

---

## S7COMM

The s7comm plugin is used for Siemens PLCs with network port, such as s7-200/300/400/1200/1500.

---

### Support Data Type

* INT16
* UINT16
* INT32
* UINT32
* FLOAT
* DOUBLE
* BIT
* STRING

---

### Parameter Setting

**host** is remote plc ip.

**ip** is remote plc port, default 102.

**rack** plc rack number, default 0.

**slot** plc cpu slot, default 1.

---

### Address Format

> AREA ADDRESS\[.BIT][.LEN]</span>

---

| AREA | DATA TYPE                                         | ATTRIBUTE  | REMARK          |
| ---- | ------------------------------------------------- | ---------- | --------------- |
| I    | int16/uint16/bit                                  | read       | input           |
| O    | int16/uint16/bit                                  | read/write | output          |
| F    | int16/uint16/bit                                  | read/write | flag            |
| T    | int16/uint16/bit                                  | read/write | timer           |
| C    | int16/uint16/bit                                  | read/write | counter         |
| DB   | int16/uint16/bit/int32/uint32/float/double/string | read/write | global DB block |

*example*

```
bit:
    I0.0
    I0.1
    O1.0
    O1.2
    F2.1
    F2.2
    T3.3
    T3.4
    C4.5
    C4.6
    DB1.DBW10.1
    DB2.DBW1.15

int16/uint16:
    I0
    I1
    O2
    O3
    F4
    F5
    T6
    T7
    C8
    C9
    DB10.DBW10
    DB12.DBW10

int32/uint32/float/double:
    DB10.DBW10

string:
    DB1.DBW12.20
```

**!**  When using the S7COMM plugin to access the S7 1200/1500 PLC,  you need to use Siemens software(TIA16) to make some settings for the PLC.

* The optimized block access must be turned off.
* The access level must be "full" and the "connection mechanism" must allow GET/PUT.

---

## FINS on TCP

The fins plugin is used for Omron PLCs with network port, such as CP2E.

---

### Support Data Type

* INT16
* UINT16
* INT32
* UINT32
* FLOAT
* DOUBLE
* BIT
* STRING

---

### Parameter Setting

**host** is remote plc ip.

**port** is remote plc port, default 9600.

---

### Address Format

> AREA ADDRESS\[.BIT]\[.LEN\[H]\[L]]</span>

---

| AREA | DATA TYPE    | ATTRIBUTE  | REMARK           |
| ---- | ------------ | ---------- | ---------------- |
| CIO  | all          | read/write | CIO Area         |
| A    | all          | read/write | Auxiliary Area   |
| W    | all          | read/write | Work Area        |
| H    | all          | read/write | Holding Area     |
| D    | all          | read/write | Data Memory Area |
| P    | int16/uint16 | read/write | PVs              |
| F    | int16/uint16 | read/write | Completion Flag  |
| EM   | all          | read/write | Extended Memory  |

example

```
bit:
    CIO0.0
    CIO1.2
    A2.1
    A2.3
    W3.4
    W3.0
    H4.15
    H4.10
    D5.2
    D5.3
    EM10W0.0

int16/uint16/int32/uint32/float/double:
    CIO1
    CIO2
    A2
    A4
    W5
    W10
    H20
    H30
    D10
    D20
    EM10W20
 
string:
    CIO0.20
    CIO1.20
    A2.10
    A2.30
    W3.40
    W3.10
    H4.15
    H4.10
    D5.20
    D5.30
    EM10W0.10
```

---

## QnA3E

The qna3e plugin is used to access Mitsubishi's QnA compatible PLCs via Ethernet, including Q series (MC), iQ-F series (SLMP) and iQ-L series.

---

### Support Data Type

* INT16
* UINT16
* INT32
* UINT32
* FLOAT
* DOUBLE
* BIT
* STRING

---

### Parameter Setting

**host** is remote plc ip.

**ip** is remote plc port, default 2000.

---

### Address Format

> AREA ADDRESS\[.BIT]\[.LEN\[H]\[L]]</span>

---

| AREA | DATA TYPE | ATTRIBUTE  | REMARK                           |
| ---- | --------- | ---------- | -------------------------------- |
| X    | bit       | read/write | Input relay (Q/iQ-F)             |
| DX   | bit       | read/write | (Q/iQ-F)                         |
| Y    | bit       | read/write | Output relay (Q/iQ-F)            |
| DY   | bit       | read/write | (Q/iQ-F)                         |
| B    | bit       | read/write | Link relay (Q/iQ-F)              |
| SB   | bit       | read/write | Link special relay               |
| M    | bit       | read/write | Internal relay (Q/iQ-F)          |
| SM   | bit       | read/write | Special relay (Q/iQ-F)           |
| L    | bit       | read/write | Latch relay (Q/iQ-F)             |
| F    | bit       | read/write | Annunciator (Q/iQ-F)             |
| V    | bit       | read/write | Edge relay (Q/iQ-F)              |
| S    | bit       | read/write | (Q/iQ-F)                         |
| TS   | bit       | read/write | Timer Contact (Q/iQ-F)           |
| TC   | bit       | read/write | Timer Coil (Q/iQ-F)              |
| SS   | bit       | read/write | (Q/iQ-F)                         |
| STS  | bit       | read/write | Retentive timer Contact (Q/iQ-F) |
| SC   | bit       | read/write | (Q/iQ-F)                         |
| CS   | bit       | read/write | Counter Contact (Q/iQ-F)         |
| CC   | bit       | read/write | Counter Coil (Q/iQ-F)            |
| TN   | all       | read/write | Timer Current value (Q/iQ-F)     |
| STN  | all       | read/write | Retentive timer (Q/iQ-F)         |
| SN   | all       | read/write | (Q/iQ-F)                         |
| CN   | all       | read/write | Counter Current value  (Q/iQ-F)  |
| D    | all       | read/write | Data register (Q/iQ-F)           |
| DSH  |           |            |                                  |
| DSL  |           |            |                                  |
| SD   | all       | read/write | Specical register (Q/iQ-F)       |
| W    | all       | read/write | Link register (Q/iQ-F)           |
| WSH  |           |            |                                  |
| WSL  |           |            |                                  |
| SW   | all       | read/write | Link special register (Q/iQ-F)   |
| R    | all       | read/write | File register (Q/iQ-F)           |
| ZR   | all       | read/write | File register (Q/iQ-F)           |
| RSH  |           |            |                                  |
| ZRSH |           |            |                                  |
| RSL  |           |            |                                  |
| ZRSL |           |            |                                  |
| Z    | all       | read/write | Index register (Q/iQ-F)          |

example

```
bit:
    X0
    X1
    Y0
    Y1

int16/uint16/int32/uint32/float/double:
    D100
    D1000
 
string:
    D1002.16
```