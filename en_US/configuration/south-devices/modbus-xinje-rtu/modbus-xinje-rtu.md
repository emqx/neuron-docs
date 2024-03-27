# XINJE Modbus RTU

The Neuron XINJE Modbus RTU plugin is for collecting XINJE PLC tags using the Modbus RTU protocol,
supporting XINJE XC/XD/XL PLC models.


## Add Device

Go to **Configuration -> South Devices**, then click **Add Device** to add the driver. Configure the following settings in the popup dialog box.

- Name: The name of this device node.
- Plugin: Select the **XINJE Modbus RTU** plugin.

## Device Configuration


After clicking **Create**, you will be redirected to the **Device Configuration** page, where we will set up the parameters required for Neuron to establish a connection with the device. You can also click the device configuration icon on the southbound device card to enter the **Device Configuration** interface.

| Parameter                  | Description                                                                            |
| -------------------------- | -------------------------------------------------------------------------------------- |
| **PLC Model**              | Selects the XINJE PLC model.                                                           |
| **Physical Link**          | Selects the communication medium, either serial or Ethernet.                           |
| **Connection Timeout**     | The time the system waits for a device to respond to a command.                        |
| **Maximum Retry Times**    | The maximum number of retries after a failed attempt to send a read command.           |
| **Retry Interval**         | Resend reading instruction interval(ms) after a failed attempt to send a read command. |
| **Send Interval**          | The waiting time between sending each read/write command. Some serial devices may discard certain commands if they receive consecutive commands in a short period of time. |
| **Serial Device**          | Only needed in **Serial** mode, the path to the serial device when using a serial connection, e.g., /dev/ttyS0 in Linux systems. |
| **Stop Bits**              | Only for the **Serial** mode, the serial connection parameter.                         |
| **Parity**                 | Only for the **Serial** mode, the serial connection parameter.                         |
| **Baud Rate**              | Only for the **Serial** mode, the serial connection parameter.                         |
| **Data Bits**              | Only for the **Serial** mode, the serial connection parameter.                         |
| **Connection Mode**        | Only for the **Ethernet** mode, you can choose Neuron as the TCP client or server.     |
| **IP Address**             | Only for the **Ethernet** mode,  the IP address of the device when using TCP connection with Neuron as the client, or the IP address of Neuron when using TCP connection with Neuron as the server. The default value is 0.0.0.0. |
| **Port**                   | Only for the **Ethernet** mode, the port number of the device when using TCP connection with Neuron as the client, or the port number of Neuron when using TCP connection with Neuron as the server. |
| **Maximum Retry Times**    | The maximum number of retries after a failed attempt to send a read command.           |
| **Retry Interval**         | Resend reading instruction interval(ms) after a failed attempt to send a read command. |

The XINJE Modbus RTU plugin configuration is similar to that of the [Modbus RTU driver module](../modbus-rtu/modbus-rtu.md).

## Configure Data Groups and Tags

After the plugin is added and configured, the next step is to establish communication between your device and Neuron by adding groups and tags to the Southbound driver.

Once device configuration is completed, navigate to the **South Devices** page. Click on the device card or device row to access the **Group List** page. Here, you can create a new group by clicking on **Create**, then specifying the group name and data collection interval.

Upon successfully creating a group, click on its name to proceed to the **Tag List** page. This page allows you to add device tags for data collection. You'll need to provide information such as the tag address, attributes, and data type.

For information on general configuration items, see [Connect to Southbound Devices](../south-devices.md). The subsequent section will concentrate on configurations specific to the driver.

### Data types

* BIT
* INT8
* UINT8
* INT16
* UINT16
* INT32
* UINT32
* INT64
* UINT64
* FLOAT
* DOUBLE
* STRING
* BYTES

### Address format

> SLAVE!ADDRESS\[.BIT][#ENDIAN]\[.LEN\[H]\[L]\[D]\[E]]\[.BYTES]

The address format is nearly the same to that of the [Modbus RTU driver module](../modbus-rtu/modbus-rtu.md), the only difference is in the **ADDRESS** part.

#### **SLAVE**

Required, Slave is the slave address or site number.

#### **ADDRESS**

XINJE PLC maps memory data unit (input/output relay, timer, counter etc) onto the Modbus address space for access through the Modbus RTU protocol.
Depending on the PLC model, such address mapping may vary.
The Neuron XINJE Modbus RTU plugin frees users from details of the address mapping, and designates the PLC data unit name as the **ADDRESS**.

Users could check the address mapping according to the PLC model from [XINJE official documents](https://m.xinje.com/xj_service/xj_xzzx.html),
and the following tables are listed here for convenience.

::: warning NOTICE
The X and Y area' data units are numbered in octal.

As an example, for XC1/XC2/XC3/XC5/XCM/XCC PLC models:
* X0~X7：16384~16384+7
* X10~X17：16384+8~16384+15
* X70~X77：16384+56~16384+63
:::

* XC1/XC2/XC3/XC5/XCM/XCC PLC models:

| Area                            | Modbus Address Range           | Quantity   | Attribute  | Register Size | Data Type |
| ------------------------------- | ------------------------------ | ---------- | ---------- | ------------- | --------- |
| M0-M7999 (Coils)                | 0x0000-0x1F3F  (0-7999)        | 8000       | Read/Write | 1Bit          |  BIT      |
| X0-X1037 (Coils)                | 0x4000-0x421F  (16384-16927)   | 543        | Read/Write | 1Bit          |  BIT      |
| Y0-Y1037 (Coils)                | 0x4800-0x4A1F  (18432-18975)   | 543        | Read/Write | 1Bit          |  BIT      |
| S0-S1023 (Coils)                | 0x5000-0x53FF  (20480-21503)   | 1024       | Read/Write | 1Bit          |  BIT      |
| M8000-M8511 (Coils)             | 0x6000-0x61FF  (24576-25087)   | 512        | Read/Write | 1Bit          |  BIT      |
| T0-T618 (Coils)                 | 0x6400-0x666A  (25600-26218)   | 619        | Read/Write | 1Bit          |  BIT      |
| C0-C634 (Coils)                 | 0x6C00-0x6E7A  (27648-28282)   | 635        | Read/Write | 1Bit          |  BIT      |
| D0-D7999 (Hold Registers)       | 0x0000-0x1F3F  (0-7999)        | 8000       | Read/Write | 16Bit,2Byte   |  Various  |
| TD0-TD618 (Hold Registers)      | 0x3000-0x326A  (12288-12906)   | 619        | Read/Write | 16Bit,2Byte   |  Various  |
| CD0-CD634 (Hold Registers)      | 0x3800-0x3A7A  (14336-14970)   | 635        | Read/Write | 16Bit,2Byte   |  Various  |
| D8000-D8511 (Hold Registers)    | 0x4000-0x41FF  (16384-16895)   | 512        | Read/Write | 16Bit,2Byte   |  Various  |
| FD0-FD5000 (Hold Registers)     | 0x4800-0x5B88  (18432-23432)   | 5000       | Read/Write | 16Bit,2Byte   |  Various  |
| FD8000-FD8511 (Hold Registers)  | 0x6800-0x69FF  (26624-27135)   | 512        | Read/Write | 16Bit,2Byte   |  Various  |
| ED0-ED36863 (Hold Registers)    | 0x7000-0xFFFF  (28672-65535)   | 36864      | Read/Write | 16Bit,2Byte   |  Various  |


* XD1/XD2/XD3/XL1/XL3 PLC models:

| Area                                | Modbus Address Range           | Quantity   | Attribute  | Register Size | Data Type |
| ----------------------------------- | ------------------------------ | ---------- | ---------- | ------------- | --------- |
| M0-M7999 (Coils)                    | 0x0000-0x1F3F  (0-7999)        | 8000       | Read/Write | 1Bit          |  BIT      |
| X0-X77 (Coils)                      | 0x5000-0x503F  (20480-20543)   | 64         | Read/Write | 1Bit          |  BIT      |
| X10000-X11177 (Coils)               | 0x5100-0x537F  (20736-21375)   | 640        | Read/Write | 1Bit          |  BIT      |
| X20000-X20177 (Coils)               | 0x58D0-0x594F  (22736-22863)   | 128        | Read/Write | 1Bit          |  BIT      |
| X30000-X30077 (Coils)               | 0x5BF0-0x5C2F  (23536-23599)   | 64         | Read/Write | 1Bit          |  BIT      |
| Y0-Y77 (Coils)                      | 0x6000-0x603F  (24576-24639)   | 64         | Read/Write | 1Bit          |  BIT      |
| Y10000-Y11177 (Coils)               | 0x6100-0x637F  (24832-25471)   | 640        | Read/Write | 1Bit          |  BIT      |
| Y20000-Y20177 (Coils)               | 0x68D0-0x694F  (26832-26959)   | 128        | Read/Write | 1Bit          |  BIT      |
| Y30000-Y30077 (Coils)               | 0x6BF0-0x6C2F  (27632-27695)   | 64         | Read/Write | 1Bit          |  BIT      |
| S0-S1023 (Coils)                    | 0x7000-0x73FF  (28672-29695)   | 1024       | Read/Write | 1Bit          |  BIT      |
| SM0-SM2047 (Coils)                  | 0x9000-0x97FF  (36864-38911)   | 2048       | Read/Write | 1Bit          |  BIT      |
| T0-T575 (Coils)                     | 0xA000-0xA23F  (40960-41535)   | 576        | Read/Write | 1Bit          |  BIT      |
| C0-C575 (Coils)                     | 0xB000-0xB23F  (45056-45631)   | 576        | Read/Write | 1Bit          |  BIT      |
| ET0-ET31 (Coils)                    | 0xC000-0xC01F  (49152-49183)   | 32         | Read/Write | 1Bit          |  BIT      |
| SEM0-SEM31 (Coils)                  | 0xC080-0xC09F  (49280-49311)   | 32         | Read/Write | 1Bit          |  BIT      |
| HM0-HM959 (Coils)                   | 0xC100-0xC4BF  (49408-50367)   | 960        | Read/Write | 1Bit          |  BIT      |
| HS0-HS127 (Coils)                   | 0xD900-0xD97F  (55552-55679)   | 128        | Read/Write | 1Bit          |  BIT      |
| HT0-HT95 (Coils)                    | 0xE100-0xE15F  (57600-57695)   | 96         | Read/Write | 1Bit          |  BIT      |
| HC0-HC95 (Coils)                    | 0xE500-0xE55F  (58624-58719)   | 96         | Read/Write | 1Bit          |  BIT      |
| HSC0-HSC31 (Coils)                  | 0xE900-0xE91F  (59648-59679)   | 32         | Read/Write | 1Bit          |  BIT      |
| D0-D7999 (Hold Registers)           | 0x0000-0x1F3F  (0-7999)        | 8000       | Read/Write | 16Bit,2Byte   |  Various  |
| ID0-ID99 (Hold Registers)           | 0x5000-0x5063  (20480-20579)   | 100        | Read/Write | 16Bit,2Byte   |  Various  |
| ID10000-ID10999 (Hold Registers)    | 0x5100-0x54E7  (20736-21735)   | 1000       | Read/Write | 16Bit,2Byte   |  Various  |
| ID20000-ID20199 (Hold Registers)    | 0x58D0-0x5997  (22736-22935)   | 200        | Read/Write | 16Bit,2Byte   |  Various  |
| ID30000-ID30099 (Hold Registers)    | 0x5BF0-0x5C53  (23536-23635)   | 100        | Read/Write | 16Bit,2Byte   |  Various  |
| QD0-ID99 (Hold Registers)           | 0x6000-0x6063  (24576-24675)   | 100        | Read/Write | 16Bit,2Byte   |  Various  |
| QD10000-QD10999 (Hold Registers)    | 0x6100-0x64E7  (24832-25831)   | 1000       | Read/Write | 16Bit,2Byte   |  Various  |
| QD20000-QD20199 (Hold Registers)    | 0x68D0-0x6997  (26832-26931)   | 200        | Read/Write | 16Bit,2Byte   |  Various  |
| QD30000-QD30099 (Hold Registers)    | 0x6BF0-0x6C53  (27632-27731)   | 100        | Read/Write | 16Bit,2Byte   |  Various  |
| SD0-SD2047 (Hold Registers)         | 0x7000-0x77FF  (28672-30719)   | 2048       | Read/Write | 16Bit,2Byte   |  Various  |
| TD0-TD575 (Hold Registers)          | 0x8000-0x823F  (32768-33343)   | 576        | Read/Write | 16Bit,2Byte   |  Various  |
| CD0-CD575 (Hold Registers)          | 0x9000-0x923F  (36864-37439)   | 576        | Read/Write | 16Bit,2Byte   |  Various  |
| ETD0-ETD31 (Hold Registers)         | 0xA000-0xA01F  (40960-40991)   | 32         | Read/Write | 16Bit,2Byte   |  Various  |
| HD0-HD999 (Hold Registers)          | 0xA080-0xA467  (41088-42087)   | 1000       | Read/Write | 16Bit,2Byte   |  Various  |
| HSD0-HSD499 (Hold Registers)        | 0xB880-0xBA73  (47232-47731)   | 500        | Read/Write | 16Bit,2Byte   |  Various  |
| HTD0-HTD95 (Hold Registers)         | 0xBC80-0xBCDF  (48256-48351)   | 96         | Read/Write | 16Bit,2Byte   |  Various  |
| HCD0-HCD95 (Hold Registers)         | 0xC080-0xC0DF  (49280-49375)   | 96         | Read/Write | 16Bit,2Byte   |  Various  |
| HSCD0-HSCD31 (Hold Registers)       | 0xC480-0xC49F  (50304-50335)   | 32         | Read/Write | 16Bit,2Byte   |  Various  |
| FD0-FD5119 (Hold Registers)         | 0xC4C0-0xD8BF  (50368-55487)   | 5120       | Read/Write | 16Bit,2Byte   |  Various  |
| SFD0-SFD1999 (Hold Registers)       | 0xE4C0-0xEC8F  (58560-60559)   | 2000       | Read/Write | 16Bit,2Byte   |  Various  |
| FS0-FS47 (Hold Registers)           | 0xF4C0-0xF4EF  (62656-62703)   | 48         | Read/Write | 16Bit,2Byte   |  Various  |


* XD5/XDM/XDC/XD5E/XDME/XL5/XL5E/XL5H/XLME PLC models:

| Area                                | Modbus Address Range           | Quantity   | Attribute  | Register Size | Data Type |
| ----------------------------------- | ------------------------------ | ---------- | ---------- | ------------- | --------- |
| M0-M20479 (Coils)                   | 0x0000-0x4FFF  (0-20479)       | 20480      | Read/Write | 1Bit          |  BIT      |
| X0-X77 (Coils)                      | 0x5000-0x503F  (20480-20543)   | 64         | Read/Write | 1Bit          |  BIT      |
| X10000-X11777 (Coils)               | 0x5100-0x54FF  (20736-21759)   | 1024       | Read/Write | 1Bit          |  BIT      |
| X20000-X20177 (Coils)               | 0x58D0-0x594F  (22736-22863)   | 128        | Read/Write | 1Bit          |  BIT      |
| X30000-X30077 (Coils)               | 0x5BF0-0x5C2F  (23536-23599)   | 64         | Read/Write | 1Bit          |  BIT      |
| Y0-Y77 (Coils)                      | 0x6000-0x603F  (24576-24639)   | 64         | Read/Write | 1Bit          |  BIT      |
| Y10000-Y11777 (Coils)               | 0x6100-0x64FF  (24832-25855)   | 1024       | Read/Write | 1Bit          |  BIT      |
| Y20000-Y20177 (Coils)               | 0x68D0-0x694F  (26832-26959)   | 128        | Read/Write | 1Bit          |  BIT      |
| Y30000-Y30077 (Coils)               | 0x6BF0-0x6C2F  (27632-27695)   | 64         | Read/Write | 1Bit          |  BIT      |
| S0-S7999 (Coils)                    | 0x7000-0x8F3F  (28672-36671)   | 8000       | Read/Write | 1Bit          |  BIT      |
| SM0-SM4095 (Coils)                  | 0x9000-0x9FFF  (36864-40959)   | 4096       | Read/Write | 1Bit          |  BIT      |
| T0-T4095 (Coils)                    | 0xA000-0xAFFF  (40960-45055)   | 4096       | Read/Write | 1Bit          |  BIT      |
| C0-C4095 (Coils)                    | 0xB000-0xBFFF  (45056-49151)   | 4096       | Read/Write | 1Bit          |  BIT      |
| ET0-ET39 (Coils)                    | 0xC000-0xC027  (49152-49183)   | 40         | Read/Write | 1Bit          |  BIT      |
| SEM0-SEM127 (Coils)                 | 0xC080-0xC0FF  (49280-49407)   | 128        | Read/Write | 1Bit          |  BIT      |
| HM0-HM6143 (Coils)                  | 0xC100-0xD8FF  (49408-55551)   | 6144       | Read/Write | 1Bit          |  BIT      |
| HS0-HS999 (Coils)                   | 0xD900-0xDCEF  (55552-56551)   | 1000       | Read/Write | 1Bit          |  BIT      |
| HT0-HT1023 (Coils)                  | 0xE100-0xE4FF  (57600-58623)   | 1024       | Read/Write | 1Bit          |  BIT      |
| HC0-HC1023 (Coils)                  | 0xE500-0xE8FF  (58624-59647)   | 1024       | Read/Write | 1Bit          |  BIT      |
| HSC0-HSC39 (Coils)                  | 0xE900-0xE927  (59648-59687)   | 40         | Read/Write | 1Bit          |  BIT      |
| D0-D20479 (Hold Registers)          | 0x0000-0x4FFF  (0-20479)       | 20480      | Read/Write | 16Bit,2Byte   |  Various  |
| ID0-ID99 (Hold Registers)           | 0x5000-0x5063  (20480-20579)   | 100        | Read/Write | 16Bit,2Byte   |  Various  |
| ID10000-ID11599 (Hold Registers)    | 0x5100-0x573F  (20736-22335)   | 1600       | Read/Write | 16Bit,2Byte   |  Various  |
| ID20000-ID20199 (Hold Registers)    | 0x58D0-0x5997  (22736-22935)   | 200        | Read/Write | 16Bit,2Byte   |  Various  |
| ID30000-ID30099 (Hold Registers)    | 0x5BF0-0x5C53  (23536-23635)   | 100        | Read/Write | 16Bit,2Byte   |  Various  |
| QD0-ID99 (Hold Registers)           | 0x6000-0x6063  (24576-24675)   | 100        | Read/Write | 16Bit,2Byte   |  Various  |
| QD10000-QD11599 (Hold Registers)    | 0x6100-0x673F  (24832-26431)   | 1600       | Read/Write | 16Bit,2Byte   |  Various  |
| QD20000-QD20199 (Hold Registers)    | 0x68D0-0x6997  (26832-26931)   | 200        | Read/Write | 16Bit,2Byte   |  Various  |
| QD30000-QD30099 (Hold Registers)    | 0x6BF0-0x6C53  (27632-27731)   | 100        | Read/Write | 16Bit,2Byte   |  Various  |
| SD0-SD4095 (Hold Registers)         | 0x7000-0x7FFF  (28672-32767)   | 4096       | Read/Write | 16Bit,2Byte   |  Various  |
| TD0-TD4095 (Hold Registers)         | 0x8000-0x8FFF  (32768-36863)   | 4096       | Read/Write | 16Bit,2Byte   |  Various  |
| CD0-CD4095 (Hold Registers)         | 0x9000-0x9FFF  (36864-40959)   | 4096       | Read/Write | 16Bit,2Byte   |  Various  |
| ETD0-ETD39 (Hold Registers)         | 0xA000-0xA027  (40960-40999)   | 40         | Read/Write | 16Bit,2Byte   |  Various  |
| HD0-HD6143 (Hold Registers)         | 0xA080-0xB87F  (41088-47231)   | 6144       | Read/Write | 16Bit,2Byte   |  Various  |
| HSD0-HSD1023 (Hold Registers)       | 0xB880-0xBC7F  (47232-48255)   | 1024       | Read/Write | 16Bit,2Byte   |  Various  |
| HTD0-HTD1023 (Hold Registers)       | 0xBC80-0xC07F  (48256-49279)   | 1024       | Read/Write | 16Bit,2Byte   |  Various  |
| HCD0-HCD1023 (Hold Registers)       | 0xC080-0xC47F  (49280-50303)   | 1024       | Read/Write | 16Bit,2Byte   |  Various  |
| HSCD0-HSCD39 (Hold Registers)       | 0xC480-0xC4A7  (50304-50343)   | 40         | Read/Write | 16Bit,2Byte   |  Various  |
| FD0-FD8199 (Hold Registers)         | 0xC4C0-0xE4BF  (50368-58559)   | 8192       | Read/Write | 16Bit,2Byte   |  Various  |
| SFD0-SFD4095 (Hold Registers)       | 0xE4C0-0xF4BF  (58560-62655)   | 4096       | Read/Write | 16Bit,2Byte   |  Various  |
| FS0-FS47 (Hold Registers)           | 0xF4C0-0xF4EF  (62656-62703)   | 48         | Read/Write | 16Bit,2Byte   |  Various  |


* XDH/XLH PLC models:

| Area                                | Modbus Address Range           | Quantity   | Attribute  | Register Size | Data Type |
| ----------------------------------- | ------------------------------ | ---------- | ---------- | ------------- | --------- |
| M0-M20479 (Coils)                   | 0x0000-0x4FFF  (0-20479)       | 20480      | Read/Write | 1Bit          |  BIT      |
| X0-X77 (Coils)                      | 0x5000-0x503F  (20480-20543)   | 64         | Read/Write | 1Bit          |  BIT      |
| X10000-X11777 (Coils)               | 0x5100-0x54FF  (20736-21759)   | 1024       | Read/Write | 1Bit          |  BIT      |
| X20000-X20177 (Coils)               | 0x58D0-0x594F  (22736-22863)   | 128        | Read/Write | 1Bit          |  BIT      |
| X30000-X30077 (Coils)               | 0x5BF0-0x5C2F  (23536-23599)   | 64         | Read/Write | 1Bit          |  BIT      |
| Y0-Y77 (Coils)                      | 0x6000-0x603F  (24576-24639)   | 64         | Read/Write | 1Bit          |  BIT      |
| Y10000-Y11777 (Coils)               | 0x6100-0x64FF  (24832-25855)   | 1024       | Read/Write | 1Bit          |  BIT      |
| Y20000-Y20177 (Coils)               | 0x68D0-0x694F  (26832-26959)   | 128        | Read/Write | 1Bit          |  BIT      |
| Y30000-Y30077 (Coils)               | 0x6BF0-0x6C2F  (27632-27695)   | 64         | Read/Write | 1Bit          |  BIT      |
| S0-S7999 (Coils)                    | 0x7000-0x8F3F  (28672-36671)   | 8000       | Read/Write | 1Bit          |  BIT      |
| SM0-SM4095 (Coils)                  | 0x9000-0x9FFF  (36864-40959)   | 4096       | Read/Write | 1Bit          |  BIT      |
| T0-T4095 (Coils)                    | 0xA000-0xAFFF  (40960-45055)   | 4096       | Read/Write | 1Bit          |  BIT      |
| C0-C4095 (Coils)                    | 0xB000-0xBFFF  (45056-49151)   | 4096       | Read/Write | 1Bit          |  BIT      |
| ET0-ET39 (Coils)                    | 0xC000-0xC027  (49152-49183)   | 40         | Read/Write | 1Bit          |  BIT      |
| SEM0-SEM127 (Coils)                 | 0xC080-0xC0FF  (49280-49407)   | 128        | Read/Write | 1Bit          |  BIT      |
| HM0-HM6143 (Coils)                  | 0xC100-0xD8FF  (49408-55551)   | 6144       | Read/Write | 1Bit          |  BIT      |
| HS0-HS999 (Coils)                   | 0xD900-0xDCEF  (55552-56551)   | 1000       | Read/Write | 1Bit          |  BIT      |
| HT0-HT1023 (Coils)                  | 0xE100-0xE4FF  (57600-58623)   | 1024       | Read/Write | 1Bit          |  BIT      |
| HC0-HC1023 (Coils)                  | 0xE500-0xE8FF  (58624-59647)   | 1024       | Read/Write | 1Bit          |  BIT      |
| HSC0-HSC39 (Coils)                  | 0xE900-0xE927  (59648-59687)   | 40         | Read/Write | 1Bit          |  BIT      |
| D0-D20479 (Hold Registers)          | 0x0000-0x4FFF  (0-20479)       | 20480      | Read/Write | 16Bit,2Byte   |  Various  |
| ID0-ID99 (Hold Registers)           | 0x5000-0x5063  (20480-20579)   | 100        | Read/Write | 16Bit,2Byte   |  Various  |
| ID10000-ID11599 (Hold Registers)    | 0x5100-0x573F  (20736-22335)   | 1600       | Read/Write | 16Bit,2Byte   |  Various  |
| ID20000-ID20199 (Hold Registers)    | 0x58D0-0x5997  (22736-22935)   | 200        | Read/Write | 16Bit,2Byte   |  Various  |
| ID30000-ID30099 (Hold Registers)    | 0x5BF0-0x5C53  (23536-23635)   | 100        | Read/Write | 16Bit,2Byte   |  Various  |
| QD0-ID99 (Hold Registers)           | 0x6000-0x6063  (24576-24675)   | 100        | Read/Write | 16Bit,2Byte   |  Various  |
| QD10000-QD11599 (Hold Registers)    | 0x6100-0x673F  (24832-26431)   | 1600       | Read/Write | 16Bit,2Byte   |  Various  |
| QD20000-QD20199 (Hold Registers)    | 0x68D0-0x6997  (26832-26931)   | 200        | Read/Write | 16Bit,2Byte   |  Various  |
| QD30000-QD30099 (Hold Registers)    | 0x6BF0-0x6C53  (27632-27731)   | 100        | Read/Write | 16Bit,2Byte   |  Various  |
| SD0-SD4095 (Hold Registers)         | 0x7000-0x7FFF  (28672-32767)   | 4096       | Read/Write | 16Bit,2Byte   |  Various  |
| TD0-TD4095 (Hold Registers)         | 0x8000-0x8FFF  (32768-36863)   | 4096       | Read/Write | 16Bit,2Byte   |  Various  |
| CD0-CD4095 (Hold Registers)         | 0x9000-0x9FFF  (36864-40959)   | 4096       | Read/Write | 16Bit,2Byte   |  Various  |
| ETD0-ETD39 (Hold Registers)         | 0xA000-0xA027  (40960-40999)   | 40         | Read/Write | 16Bit,2Byte   |  Various  |
| HD0-HD6143 (Hold Registers)         | 0xA080-0xB87F  (41088-47231)   | 6144       | Read/Write | 16Bit,2Byte   |  Various  |
| HSD0-HSD1023 (Hold Registers)       | 0xB880-0xBC7F  (47232-48255)   | 1024       | Read/Write | 16Bit,2Byte   |  Various  |
| HTD0-HTD1023 (Hold Registers)       | 0xBC80-0xC07F  (48256-49279)   | 1024       | Read/Write | 16Bit,2Byte   |  Various  |
| HCD0-HCD1023 (Hold Registers)       | 0xC080-0xC47F  (49280-50303)   | 1024       | Read/Write | 16Bit,2Byte   |  Various  |
| HSCD0-HSCD39 (Hold Registers)       | 0xC480-0xC4A7  (50304-50343)   | 40         | Read/Write | 16Bit,2Byte   |  Various  |
| FD0-FD8199 (Hold Registers)         | 0xC4C0-0xE4BF  (50368-58559)   | 8192       | Read/Write | 16Bit,2Byte   |  Various  |
| SFD0-SFD4095 (Hold Registers)       | 0xE4C0-0xF4BF  (58560-62655)   | 4096       | Read/Write | 16Bit,2Byte   |  Various  |
| FS0-FS255 (Hold Registers)          | 0xF4C0-0xF5BF  (62656-62911)   | 256        | Read/Write | 16Bit,2Byte   |  Various  |

#### **.BIT**

Optional, specify a specific bit in a register

| Address     | Data Type | Description                     |
| ----------- | --------- | ------------------------------- |
| D4.0        | bit       | PLC data register D4, bit 0     |
| D10.4       | bit       | PLC data register D10, bit 4    |
| D1.15       | bit       | PLC data register D1, bit 15    |

#### **#ENDIAN**

Optional, byte order, applicable to data types int16/uint16/int32/uint32/float, see the table below for details.
| Symbol | Byte Order | Supported Data Types | Note                                |
| ------ | ---------- | -------------------- | ----------------------------------- |
| #B     | 2,1        | int16/uint16         |                                     |
| #L     | 1,2        | int16/uint16         | Default byte order if not specified |
| #LL    | 1,2,3,4    | int32/uint32/float   | Default byte order if not specified |
| #LB    | 2,1,4,3    | int32/uint32/float   |                                     |
| #BL    | 3,4,1,2    | int32/uint32/float   |                                     |
| #BB    | 4,3,2,1    | int32/uint32/float   |                                     |

::: tip
The byte order can be illustrated using the notation ABCD, which corresponds directly to the sequence 1234. As an example, the ABCD designation represents the standard or default Endianness 1234. (#LL).
:::


#### .LEN\[H]\[L]

When the data type is STRING, `.LEN` is a required field, indicating the number of bytes the string occupies. Each register contains four storage methods: H, L, D, and E, as shown in the table below.

| Symbol | Description                                                     |
| ------ | --------------------------------------------------------------- |
| H      | One register stores two bytes, with the high byte first         |
| L      | One register stores two bytes, with the low byte first          |
| D      | One register stores one byte, and it is stored in the low byte  |
| E      | One register stores one byte, and it is stored in the high byte |


#### **.BYTES**

Optional, read and write the length of bytes type data, applicable to bytes data type.

::: tip
A register of the Modbus driver contains 2 bytes. When reading and writing Modbus register data in the bytes data type, please ensure that the bytes parameter is set to an even number.
:::

### Example Addresses

| Address        | Data Type | Description                               |
| -------------- | --------- | ----------------------------------------- |
| D4             | int16     | PLC data register D4, byte order #L       |
| D4#L           | int16     | PLC data register D4, byte order #L       |
| D4#B           | uint16    | PLC data register D4, byte order #B       |
| D4             | int32     | PLC data register D4, byte order #LL      |
| D4#LB          | uint32    | PLC data register D4, byte order #LB      |
| D4#BB          | uint32    | PLC data register D4, byte order #BB      |
| D4#LL          | int32     | PLC data register D4, byte order #LL      |
| D4#BL          | float     | PLC data register D4, byte order #BL      |
| D1.10          | String    | PLC data register D1, character length 10, byte order L, which occupies addresses D1 to D5|
| D1.10H         | String    | PLC data register D1, character length 10, byte order H, which occupies addresses D1 to D5|
| D1.10L         | String    | PLC data register D1, character length 10, byte order L, which occupies addresses D1 to D5|
| M8             | bit       | Auxiliary relay M8                        |
| X10            | bit       | Input relay X10                           |


## Data Monitoring

After completing the point configuration, you can click **Monitoring** -> **Data Monitoring** to view device information and control devices. For details, refer to [Data Monitoring](../../../admin/monitoring.md).
