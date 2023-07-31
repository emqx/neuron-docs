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
| **host** | BACnet device ip                   |
| **port** | BACnet device port, default 47808  |

## Configure Data Groups and Tags

After the plug-in is added and configured, the next step is to establish communication between your device and Neuron by adding groups and tags to the Southbound driver.

Once device configuration is completed, navigate to the **South Devices** page. Click on the device card or device row to access the **Group List** page. Here, you can create a new group by clicking on **Create**, then specifying the group name and data collection interval.

Upon successfully creating a group, click on its name to proceed to the **Tag List** page. This page allows you to add device tags for data collection. You'll need to provide information such as the tag address, attributes, and data type.

For information on general configuration items, see [Connect to Southbound Devices](../south-devices.md). The subsequent section will concentrate on configurations specific to the driver.

### Data Types

* float
* bit
* uint8

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

### Example Addresses

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