# Introduction and Usage of BACnet/IP

## Parameter Configuration

| Parameter      | Description                     |
|--------- | ------------------------------------- |
| **host** | BACnet device ip                   |
| **port** | BACnet device port, default 47808  |

## Support Data Type

* float
* bit

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
| MSI  | 0 - 0x3fffff  | read       | bit       | multi state input  |
| MSO  | 0 - 0x3fffff  | read/write | bit       | multi state output |
| MSV  | 0 - 0x3fffff  | read/write | bit       | multi state value  |

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
| MSI10  | bit     | MAI area, address is 10 |
| MSI20  | bit     | MSI area, address is 20 |
| MSI30  | bit     | MSI area, address is 30 |