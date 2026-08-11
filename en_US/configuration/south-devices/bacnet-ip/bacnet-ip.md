# BACnet/IP

BACnet (Building Automation and Control Networks) is a communication protocol used in smart buildings. It is defined by the International Organization for Standardization (ISO), the American National Standards Institute (ANSI) and the American Society of Heating, Venting, and Air-conditioning Engineers (ASHRAE). BACnet is designed specifically for smart buildings and control systems, and can be used for heating, ventilation, and air conditioning (HVAC), lighting control, access control, fire detection systems, and related equipment. Its advantages include reducing the cost of maintenance systems and making installation simpler than general industrial communication protocols. In addition, BACnet also provides five standard protocols commonly used in the industry, which can prevent equipment and system suppliers from monopolizing the market and increase the scalability and compatibility of future systems. BACnet supports multiple communication methods, including serial ports, IP, Ethernet, and ZigBee.

The BACnet/IP driver talks to a single device at a known address by unicast, reading with ReadPropertyMultiple and writing with WriteProperty. It does no discovery of its own: Who-Is/I-Am broadcasts and cross-subnet discovery through a BBMD (BACnet Broadcast Management Device) belong to the [Device Scanning](#device-scanning) plugin. Using the two together is the recommended approach - let the scan plugin find the devices and tags on the network, then have it generate a fully configured BACnet/IP node for you.

## Add Device

Go to **Configuration -> South Devices**, then click **Add Device** to add the driver. Configure the following settings in the popup dialog box.

- Name: The name of this device node.
- Plugin: Select the **BACnet/IP** plugin.

## Device Configuration

After clicking **Create**, you will be redirected to the **Device Configuration** page, where we will set up the parameters required for Neuron to establish a connection with the northbound application. You can also click the device configuration icon on the southbound device card to enter the **Device Configuration** interface.

| Parameter                 | Description                                                                                                                                     |
| ------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------- |
| **Target Device IP Address** | IP of the BACnet device. When the device sits behind a BACnet router, put the **router's** IP here                                            |
| **Target Device Port**    | Port of the BACnet device, default 47808                                                                                                        |
| **Target Device Network** | Network number (DNET) of the BACnet network the device is on, 0 - 65534. Only used when a device MAC is given; leave at 0 for a direct device    |
| **Target Device MAC**     | MAC (DADR) of the device behind the router, as hex without separators. Leave **empty** for a device on this network                              |

### Reaching a Device on Another BACnet Network

Crossing IP subnets and crossing BACnet networks are two different things, and they are configured differently:

* **Across IP subnets** but still within the same BACnet/IP network - this only affects broadcasts; unicast reads and writes are unaffected. Give this driver the device's own IP; no BBMD is involved.
* **Across BACnet networks**, where the device hangs off an MS/TP network or another B/IP network behind a BACnet router - the device has no directly reachable IP and every message has to be forwarded by the router. This is when the target device network and MAC are needed.

The MAC length depends on the network the device is on: an MS/TP station number is one octet such as `05`, while a B/IP address is six octets of IP plus port, e.g. `C0A80164BAC0` for 192.168.1.100:47808.

| Scenario                                        | Target Device IP Address | Target Device Network | Target Device MAC |
| ----------------------------------------------- | ------------------------ | --------------------- | ----------------- |
| Device on this network, directly reachable      | Device IP                | 0                     | empty             |
| Device on MS/TP network 2001 behind a router    | Router IP                | 2001                  | `05`              |
| Device on another B/IP network behind a router  | Router IP                | That network's number | `C0A80164BAC0`    |

::: tip
When in doubt, run a scan first with [Device Scanning](#device-scanning). Every device it reports carries `address`, `port`, `dnet` and `dadr`, which map one to one onto the four settings above - or call its apply endpoint and skip filling them in by hand.
:::

## Configure Data Groups and Tags

After the plug-in is added and configured, the next step is to establish communication between your device and Neuron by adding groups and tags to the Southbound driver.

Once device configuration is completed, navigate to the **South Devices** page. Click on the device card or device row to access the **Group List** page. Here, you can create a new group by clicking on **Create**, then specifying the group name and data collection interval.

Upon successfully creating a group, click on its name to proceed to the **Tag List** page. This page allows you to add device tags for data collection. You'll need to provide information such as the tag address, attributes, and data type.

For information on general configuration items, see [Connect to Southbound Devices](../south-devices.md). The subsequent section will concentrate on configurations specific to the driver.

### Data Types

* FLOAT
* DOUBLE
* BIT
* BOOL
* INT8
* INT32
* UINT8
* UINT16
* UINT32
* STRING

### Address Format

> AREA ADDRESS(.PROPERTY_ID)

AREA is the area abbreviation, ADDRESS the object instance number, and PROPERTY_ID an optional property name. With no property given, the current value (Present_Value) is read or written, except in the DEV area.

support Area

| AREA | OBJECT TYPE            | ADDRESS RANGE | ATTRIBUTE  | DATA TYPE              | REMARK                 |
| ---- | ---------------------- | ------------- | ---------- | ---------------------- | ---------------------- |
| AI   | analog-input           | 0 - 0x3fffff  | read       | FLOAT                  | analog input           |
| AO   | analog-output          | 0 - 0x3fffff  | read/write | FLOAT                  | analog output          |
| AV   | analog-value           | 0 - 0x3fffff  | read/write | FLOAT                  | analog value           |
| BI   | binary-input           | 0 - 0x3fffff  | read       | BIT                    | binary input           |
| BO   | binary-output          | 0 - 0x3fffff  | read/write | BIT                    | binary output          |
| BV   | binary-value           | 0 - 0x3fffff  | read/write | BIT                    | binary value           |
| MSI  | multi-state-input      | 0 - 0x3fffff  | read       | UINT8                  | multi state input      |
| MSO  | multi-state-output     | 0 - 0x3fffff  | read/write | UINT8                  | multi state output     |
| MSV  | multi-state-value      | 0 - 0x3fffff  | read/write | UINT8                  | multi state value      |
| ACC  | accumulator            | 0 - 0x3fffff  | read/write | UINT32 (UINT8 accepted)| accumulator            |
| LAV  | large-analog-value     | 0 - 0x3fffff  | read/write | DOUBLE                 | large analog value     |
| IV   | integer-value          | 0 - 0x3fffff  | read/write | INT32                  | integer value          |
| PIV  | positive-integer-value | 0 - 0x3fffff  | read/write | UINT32                 | positive integer value |
| CSV  | characterstring-value  | 0 - 0x3fffff  | read/write | STRING                 | character string value |
| LO   | lighting-output        | 0 - 0x3fffff  | read/write | FLOAT                  | lighting output        |
| BLO  | binary-lighting-output | 0 - 0x3fffff  | read/write | BIT                    | binary lighting output |
| DV   | date-value             | 0 - 0x3fffff  | read/write | STRING                 | date value             |
| TV   | time-value             | 0 - 0x3fffff  | read/write | STRING                 | time value             |
| DEV  | device                 | 0 - 0x3fffff  | read       | see property table     | device                 |

::: tip
The data type follows from the object type and cannot be chosen freely. An AI tag must be FLOAT and an MSV tag must be UINT8; the wrong type is rejected with a type-not-supported error. The ACC area is UINT32 per the standard, with UINT8 kept only so tags configured earlier still validate.

Input objects (AI, BI, MSI) reflect a measured quantity and are not writable - adding one with the write attribute is refused.
:::

support standard property

| property                        | address                         | type   |
| ------------------------------- | ------------------------------- | ------ |
| object name                     | Object_Name                     | string |
| object type                     | Object_Type                     | uint8  |
| description                     | Description                     | string |
| device type                     | Device_Type                     | string |
| status flags                    | Status_Flags                    | string |
| event state                     | Event_State                     | uint8  |
| out of service                  | Out_Of_Service                  | bool   |
| update interval                 | Update_Interval                 | uint8  |
| minimum                         | Min_Pres_Value                  | float  |
| maximum                         | Max_Pres_Value                  | float  |
| resolution                      | Resolution                      | float  |
| COV increment                   | COV_Increment                   | float  |
| time delay                      | Time_Delay                      | uint8  |
| notification class              | Notification_Class              | uint8  |
| notify type                     | Notify_Type                     | uint8  |
| unit                            | Units                           | uint8  |
| high limit                      | High_Limit                      | float  |
| low limit                       | Low_Limit                       | float  |
| deadband                        | Deadband                        | float  |
| reliability                     | Reliability                     | uint8  |
| polarity                        | Polarity                        | uint8  |
| system status                   | System_Status                   | uint8  |
| vendor name                     | Vendor_Name                     | string |
| vendor identifier               | Vendor_Identifier               | uint8  |
| model name                      | Model_Name                      | string |
| firmware revision               | Firmware_Revision               | string |
| application software version    | Application_Software_Version    | string |
| location                        | Location                        | string |
| protocol version                | Protocol_Version                | uint16 |
| protocol conformance class      | Protocol_Conformance_Class      | uint8  |
| supported protocol service      | Protocol_Service_Supported      | string |
| supported protocol object types | Protocol_Object_Types_Supported | string |
| serial number                   | Serial_Number                   | string |
| max accepted apdu length        | Max_APDU_Length_Accepted        | uint16 |
| supported segmentation          | Segmentation_Supported          | uint8  |
| local time                      | LOCAL_TIME                      | string |
| local date                      | LOCAL_DATE                      | string |
| utc offset                      | UTC_Offset                      | int8   |
| daylight savings status         | Daylight_Savings_Status         | bool   |
| APDU segment timeout            | APUD_Segment_Timeout            | uint8  |
| APDU timeout                    | APUD_Timeout                    | uint16 |
| number of APDU retries          | Number_Of_APDU_Retries          | uint8  |
| max master                      | Max_Master                      | uint8  |
| max info frame                  | Max_Info_Frame                  | uint8  |
| profile name                    | Profile_Name                    | string |
| pluse rate                      | Pulse_Rate                      | uint8  |
| scale                           | Scale                           | float  |
| prescale                        | Prescale                        | float  |
| value before change             | Value_Before_Change             | uint8  |
| value change time               | Value_Change_Time               | string |


If no property is specified, the default property is Present_Value.

support custom property

PROPERTY_ID consists of two parts: a custom flag and the value (integer) of the property, with the overall format being AREA ADDRESS.custom.id.

Support Present Value zeroing operation, currently supporting AO and BO regions. The address format is "(AO|BO)xxx.NULL", and only write operations are supported. Depending on the type of region, write the zero value of the corresponding type.

::: tip
A `.NULL` tag is write-only. Adding one with the read or subscribe attribute is refused with an attribute-not-supported error.
:::

### Example Addresses

| Address               | Data Type | Description                                          |
| --------------------- | --------- | ---------------------------------------------------- |
| AI0                   | FLOAT     | AI area, address is 0                                |
| AI1                   | FLOAT     | AI area, address is 1                                |
| AV30                  | FLOAT     | AV area, address is 30                               |
| BO10                  | BIT       | BO area, address is 10                               |
| BO20                  | BIT       | BO area, address is 20                               |
| BO10.NULL             | BIT       | BO area, address is 10, write NULL                   |
| BI0                   | BIT       | BI area, address is 0                                |
| BI1                   | BIT       | BI area, address is 1                                |
| BV3                   | BIT       | BV area, address is 3                                |
| MSI10                 | UINT8     | MSI area, address is 10                              |
| MSI20                 | UINT8     | MSI area, address is 20                              |
| MSI30                 | UINT8     | MSI area, address is 30                              |
| ACC1                  | UINT32    | ACC area, address is 1                               |
| LAV5                  | DOUBLE    | LAV area, address is 5                               |
| IV7                   | INT32     | IV area, address is 7                                |
| PIV8                  | UINT32    | PIV area, address is 8                               |
| CSV2                  | STRING    | CSV area, address is 2                               |
| AI0.Object_Name       | STRING    | AI area, address is 0, property is Object_Name       |
| AI0.custom.1234       | ALL       | AI area, address is 0, property is 1234              |
| DEV400001.Vendor_Name | STRING    | DEV area, address is 400001, property is vendor name |

## Device Scanning

BACnet/IP devices can be discovered by broadcasting Who-Is messages and listening for I-Am responses. The scan plugin implements this discovery, and can also re-enumerate the tags of known devices. It is a separate plugin from the BACnet/IP driver, and is used to generate fully configured BACnet/IP nodes.

The usual workflow is three steps:

1. Enable scanning in system settings, choosing the scan modes according to your network topology
2. Look at the devices and tags found by the scan
3. Select a device and the tags you want, and click to generate a BACnet/IP node with all its tags


### Enable Scanning

In **System Settings -> BACnet/IP Device Scan**, enable scanning.

### Scan Configuration

| Parameter                 | Default           | Description                                                                                      |
| ------------------------- | ----------------- | ------------------------------------------------------------------------------------------------ |
| **Local Bind Address**    | `0.0.0.0`         | Local interface to bind. `0.0.0.0` binds every interface; name one on a multi-homed host           |
| **Local Bind Port**       | `47808`           | Local port used to send and receive BACnet messages. This normally has to be 47808, see below      |
| **Device Scan Interval**  | `600`             | How often to broadcast Who-Is to find devices, in seconds, 30 - 86400                             |
| **Point Scan Interval**   | `1200`            | How often to re-enumerate the tags of known devices, in seconds, 60 - 86400                     |
| **Local Broadcast Scan**  | Enabled           | Send Who-Is as an Original-Broadcast-NPDU                                                         |
| **Global Broadcast Scan** | Disabled          | Send Who-Is with DNET 0xFFFF, which BACnet routers forward to every network they serve             |
| **Broadcast Address**     | `255.255.255.255` | Destination of both broadcast modes. A subnet-directed address such as `192.168.1.255` is better   |
| **Scan via BBMD**         | Disabled          | Register as a foreign device with a BBMD and send Who-Is as Distribute-Broadcast-To-Network         |
| **BBMD IP Address**       | empty             | Only needed when Scan via BBMD is enabled                                                         |
| **BBMD Port**             | `47808`           | Only needed when Scan via BBMD is enabled                                                         |

#### Choosing the Scan Modes

The three modes correspond to three different places a device can be. They may be enabled together, and duplicate discoveries are merged.

| Where the device is                                        | Mode to enable        | Why                                                                   |
| ---------------------------------------------------------- | --------------------- | --------------------------------------------------------------------- |
| On the same IP subnet as Neuron                            | Local Broadcast Scan  | The common case; the broadcast reaches it directly                     |
| On the same BACnet/IP network but a different IP subnet    | Scan via BBMD         | IP broadcasts do not cross subnets, so a BBMD there has to relay them   |
| On an MS/TP or other BACnet network behind a BACnet router | Global Broadcast Scan | A router receiving a Who-Is with DNET 0xFFFF forwards it onward         |

If you cannot tell which applies, enable all three and look at the result. A device found across a BACnet network is reported with `routed` set to `true` plus a `dnet` and `dadr`, which go straight into the target device network and MAC above.
