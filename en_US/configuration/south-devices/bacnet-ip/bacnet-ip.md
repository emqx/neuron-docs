# BACnet/IP

BACnet (Building Automation and Control Networks) is a communication protocol used in smart buildings. It is defined by the International Organization for Standardization (ISO), the American National Standards Institute (ANSI) and the American Society of Heating, Venting, and Air-conditioning Engineers (ASHRAE). BACnet is designed specifically for smart buildings and control systems, and can be used for heating, ventilation, and air conditioning (HVAC), lighting control, access control, fire detection systems, and related equipment. Its advantages include reducing the cost of maintenance systems and making installation simpler than general industrial communication protocols. In addition, BACnet also provides five standard protocols commonly used in the industry, which can prevent equipment and system suppliers from monopolizing the market and increase the scalability and compatibility of future systems. BACnet supports multiple communication methods, including serial ports, IP, Ethernet, and ZigBee.

Neuron supports BACnet IP protocol and can communicate with BACnet devices through UDP protocol.

## Add Device

Go to **Configuration -> South Devices**, then click **Add Device** to add the driver. Configure the following settings in the popup dialog box.

- Name: The name of this device node.
- Plugin: Select the **BACnet/IP** plugin.

## Device Configuration

After clicking **Create**, you will be redirected to the **Device Configuration** page, where we will set up the parameters required for Neuron to establish a connection with the northbound application. You can also click the device configuration icon on the southbound device card to enter the **Device Configuration** interface.

| Parameter      | Description                     |
|--------- | ------------------------------------- |
| **Device IP Address** | BACnet device IP                 |
| **Device Port** | BACnet device port, default 47808  |

## Configure Data Groups and Tags

After the plug-in is added and configured, the next step is to establish communication between your device and Neuron by adding groups and tags to the Southbound driver.

Once device configuration is completed, navigate to the **South Devices** page. Click on the device card or device row to access the **Group List** page. Here, you can create a new group by clicking on **Create**, then specifying the group name and data collection interval.

Upon successfully creating a group, click on its name to proceed to the **Tag List** page. This page allows you to add device tags for data collection. You'll need to provide information such as the tag address, attributes, and data type.

For information on general configuration items, see [Connect to Southbound Devices](../south-devices.md). The subsequent section will concentrate on configurations specific to the driver.

### Data Types

* float
* bit
* int8
* uint8
* uint16
* bool
* string

### Address Format

> AREA ADDRESS(.PROPERTY_ID)

support Area

| AREA | ADDRESS RANGE | ATTRIBUTE  | DATA TYPE | REMARK             |
| ---- | ------------- | ---------- | --------- | ------------------ |
| AI   | 0 - 0x3fffff  | read       | float     | analog input       |
| AO   | 0 - 0x3fffff  | read/write | float     | analog output      |
| AV   | 0 - 0x3fffff  | read/write | float     | analog value       |
| BI   | 0 - 0x3fffff  | read       | bit       | binary input       |
| BO   | 0 - 0x3fffff  | read/write | bit       | binary output      |
| BV   | 0 - 0x3fffff  | read/write | bit       | binary value       |
| MSI  | 0 - 0x3fffff  | read       | uint8     | multi state input  |
| MSO  | 0 - 0x3fffff  | read/write | uint8     | multi state output |
| MSV  | 0 - 0x3fffff  | read/write | uint8     | multi state value  |
| DEV  | 0 - 0x3fffff  | read       |           | device             |
| ACC  | 0 - 0x3fffff  | read/write | uint8     | accumulator        |


support standard property

| property                        | address                         | type   |
| ------------------------------- | ------------------------------- | ------ |
| object name                     | Object_Name                     | string |
| object type                     | Object_Tyep                     | uint8  |
| description                     | Description                     | string |
| device type                     | Device_Type                     | string |
| status flags                    | Status_Flags                    | string |
| event state                     | Event_State                     | uint8  |
| out of service                  | Out_Of_Service                  | bool   |
| update interval                 | Update_Interval                 | uint8  |
| minimum                         | Min_Pres_Value                  | float  |
| aximum                          | Max_Pres_Value                  | float  |
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

### Example Addresses

| Address               | Data Type | Description                                          |
| --------------------- | --------- | ---------------------------------------------------- |
| AI0                   | float     | AI area, address is 0                                |
| AI1                   | float     | AI area, address is 1                                |
| AV30                  | bit       | AV area, address is 30                               |
| BO10                  | bit       | BO area, address is 10                               |
| BO20                  | bit       | BO area, address is 20                               |
| BO10.NULL             | bit       | BO area, address is 10，write NULL                   |
| BI0                   | bit       | BI area, address is 0                                |
| BI1                   | bit       | BI area, address is 1                                |
| BV3                   | bit       | BV area, address is 3                                |
| MSI10                 | uint8     | MAI area, address is 10                              |
| MSI20                 | uint8     | MSI area, address is 20                              |
| MSI30                 | uint8     | MSI area, address is 30                              |
| ACC1                  | string    | ACC area，address is 1                               |
| AI0.Object_Name       | string    | AI area, address is property is Object_Name          |
| AI0.custom.1234       | ALL       | AI area, address is 0，property is 1234              |
| DEV400001.Vendor_Name | string    | DEV area，address is 400001，property is vendor name |
