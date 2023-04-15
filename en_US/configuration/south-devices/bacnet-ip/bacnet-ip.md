# Overview

BACnet (Building Automation and Control Networks) is a communication protocol used in smart buildings. It is defined by the International Organization for Standardization (ISO), the American National Standards Institute (ANSI) and the American Society of Heating, Venting, and Air-conditioning Engineers (ASHRAE). BACnet is designed specifically for smart buildings and control systems, and can be used for heating, ventilation, and air conditioning (HVAC), lighting control, access control, fire detection systems, and related equipment. Its advantages include reducing the cost of maintenance systems and making installation simpler than general industrial communication protocols. In addition, BACnet also provides five standard protocols commonly used in the industry, which can prevent equipment and system suppliers from monopolizing the market and increase the scalability and compatibility of future systems. BACnet supports multiple communication methods, including serial ports, IP, Ethernet, and ZigBee.

Neuron supports BACnet IP protocol and can communicate with BACnet devices through UDP protocol.

## Parameter Configuration

| Parameter      | Description                     |
|--------- | ------------------------------------- |
| **host** | BACnet device ip                   |
| **port** | BACnet device port, default 47808  |

## Support Data Type

* float
* bit
* uint8

## Usage of Address Fromat

### Address Format

> AREA[ADDRESS]</span>

| AREA | ADDRESS RANGE | ATTRIBUTE  | DATA TYPE  | REMARK             |
| ---- | ------------- | ---------- | ------------- | ------------------ |
| AI   | 0 - 0x3fffff  | read       | float     | analog input       |
| AO   | 0 - 0x3fffff  | read/write | float     | analog output      |
| AV   | 0 - 0x3fffff  | read/write | float     | analog value       |
| BI   | 0 - 0x3fffff  | read       | bit       | binary input       |
| BO   | 0 - 0x3fffff  | read/write | bit       | binary output      |
| BV   | 0 - 0x3fffff  | read/write | bit       | binary value       |
| MSI  | 0 - 0x3fffff  | read       | uint8       | multi state input  |
| MSO  | 0 - 0x3fffff  | read/write | uint8       | multi state output |
| MSV  | 0 - 0x3fffff  | read/write | uint8       | multi state value  |

### Address Examples

| Address     | Data Type  | Description          |
| ------- | ------- | --------------- |
| AI0    | float   | AI area, address is 0  |
| AI1    | float   | AI area, address is 1  |
| BO10   | float   | BO area, address is 10 |
| BO20   | float   | BO area, address is 20 |
| AV30   | float   | AV area, address is 30 |
| BI0    | bit     | BI area, address is 0  |
| BI1    | bit     | BI area, address is 1  |
| BV3    | bit     | BV area, address is 3  |
| MSI10  | uint8     | MAI area, address is 10 |
| MSI20  | uint8     | MSI area, address is 20 |
| MSI30  | uint8     | MSI area, address is 30 |