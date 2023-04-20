# Introduction to Modbus TCP

Modbus=MBAP(Modbus application protocol header)+PDU(Protocol data unit)

Modbus TCP uses the TCP protocol to transmit data in Modbus format.

The client transmits data in hexadecimal, two bits at a time; The server also receives data in hexadecimal format, receiving two bits at a time. For example, 0X00, a two-digit hexadecimal number is an 8-bit binary number.

## MBAP

|Transaction identifier | Protocol identifier | Length | Unit identifier|
|----|----|----|----|
|2 bytes | 2 bytes | 2 bytes | 1 byte|
|00 00|00 00|00 00|01|

* Transaction identifier: It can be interpreted as the serial number of the message. For example, the Modbus Poll client used in the test always sends data, so each time the data identifier is sent, it is added with one. The server will return this data unopened when it receives it.
* Protocol representation: 00 00 represents the TCP protocol.
* Length: Indicates the length of data starting from the unit identifier. For example, 00 06 represents data with a length of 0X06 bytes.
* Unit identifier: Equivalent to the address of the device. Typically 01.

## PDU

PDU=function code+data

|Function Code | Data|
|----|----|
|1 byte | Function dependent|

### Function code:

There are four types of operating objects for modbus: coils, discrete inputs, input registers, and hold registers.
* Coil: equivalent to a switch, readable and writable in MODBUS, with only 00 and 01 data.
* Discrete value: Input bit, switching value, read-only in MODBUS.
* Input register: A register that can only be changed from the analog input terminal and is read-only in MODBUS.
* Holding register: A register used to output analog signals, readable and writable in MODBUS.

According to different objects, the function codes of modbus include:
* 0x01: Reading coil
* 0x05: Write a single coil
* 0x0F: Write multiple coils
* 0x02: Read Discrete Input
* 0x04: Read Input Register
* 0x03: Read Holding Register
* 0x06: Write Single Holding Register
* 0x10: Write Multiple Holding Registers

### Detailed interpretation of messages

Here, we only take reading content of holding register as an example. The following data are all hexadecimal data.

Request: 00 01 00 00 00 06 01 03 00 02 00 04 (client)

* 00 01: Transaction identifier
* 00 00: Modbus TCP protocol
* 00 06: followed by 00 06 bytes of data
* 01: Unit identifier
* 03: Function code (read hold register)
* 00 02: Address of the data to start reading. Start reading data from 00 02.
* 00 04: Note that instead of reading 00 04, 00 04 register data is read from the start position.

Response: 00 01 00 00 00 09 01 03 08 00 00 00 37 00 00 00 00 00 (server)

* 00 01: Transaction identifier
* 00 00: Modbus TCP protocol
* 00 09: followed by 00 09 bytes of data
* 01: Unit identifier
* 03: Function code
* 08: There are 08 bytes of data followed, and every two bytes of data represent one register data.
* 00 00: First register data
* 00 37: Second register data
* 00 00: Third register data
* 00 00: Fourth register data