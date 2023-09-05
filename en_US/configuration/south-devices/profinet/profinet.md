# Profinet IO

PROFINET is an open industrial Ethernet communication protocol proposed by the PROFIBUS & PROFINET International Association. PROFINET applies TCP/IP related standards and is a real-time industrial Ethernet. PROFINET has a modular structure, and users can choose cascading skills according to their needs.

The PROFINET IO system includes several parts: IO controller, IO device, and IO monitor. The IO controller is used to control the automation task; the IO device is generally a field device, controlled and monitored by the IO controller, and an IO device may include several modules and sub-modules; the IO monitor is a PC software that can set parameters and diagnose the status of individual modules.

::: tip
Because the PROFINET IO real-time message uses the Ethernet protocol defined in PROFINET (real-time message is transmitted based on Ethernet frames), when using the PROFINET driver, you need to deploy Neuron directly with physical devices, and cannot use virtual deployment, such as Docker image or virtual machine.
:::

## Add Device

Go to **Configuration -> South Devices**, then click **Add Device** to add the driver. Configure the following settings in the popup dialog box.

- Name: The name of this device node.
- Plugin: Select the **Profinet IO** plugin.

## Device Configuration

After clicking **Create**, you will be redirected to the **Device Configuration** page, where we will set up the parameters required for Neuron to establish a connection with the northbound application. You can also click the device configuration icon on the southbound device card to enter the **Device Configuration** interface.

| Parameter | Description |
| -------------------- | ------------------------------------------------------- |
| **Device Name** | IO device name|
| **Local Interface** | Local interface name  |
| **Device IP Address** | IO device IPv4 address|
| **Device Port** | IO device port, default 34964 |
| **API** | IO device module API |
| **Slot** | IO device module slot |
| **Sub Slot** | IO device module sub slot |
| **Ident** | IO device module ident |
| **Sub Ident** | IO  device sub ident |
| **Properties** | IO device properties |
| **Input Data Length** | IO device module input data length |
| **Output Data Length** | IO device module output data length |

## Configure Data Groups and Tags

After the plug-in is added and configured, the next step is to establish communication between your device and Neuron by adding groups and tags to the Southbound driver.

Once device configuration is completed, navigate to the **South Devices** page. Click on the device card or device row to access the **Group List** page. Here, you can create a new group by clicking on **Create**, then specifying the group name and data collection interval.

Upon successfully creating a group, click on its name to proceed to the **Tag List** page. This page allows you to add device tags for data collection. You'll need to provide information such as the tag address, attributes, and data type.

For information on general configuration items, see [Connect to Southbound Devices](../south-devices.md). The subsequent section will concentrate on configurations specific to the driver.

### Data Types

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
* BIT

### Address Format

> SLOT:SUB_SLOT:INDEX\[.BIT][#ENDIAN]

#### **SLOT**

Required, the slot number of the module inserted into the module.

#### **SUB_SLOT**

Required, the sub-slot number of the module inserted into the module.

#### **INDEX**

Required, the data index in the module (which byte, starting from 0).

### Example Addresses

|Address         | Data Type | Description|
| ----------- | ------- | --------- |
| 3:1:0   | int16    | slot 3, subslot 1, module 0, 1 bytes |
| 3:1:1   | uint16    | slot 3, subslot 1, module 1, 2 bytes |
| 3:2:3   | uint32    | slot 3, subslot 2, module 3, 4, 5, 6 bytes |
| 3:2:10   | float    | slot 3, subslot 2, module 10, 11, 12, 13 bytes |
| 3:2:2   | uint64    | slot 3, subslot 2, module 2, 3, 4, 5, 6, 7, 8, 9 bytes |
| 3:2:2   | double    | slot 3, subslot 2, module 2, 3, 4, 5, 6, 7, 8, 9 bytes |

## Data Monitoring

After completing the point configuration, you can click **Monitoring** -> **Data Monitoring** to view device information and control devices. For details, refer to [Data Monitoring](../../../usage/monitoring.md).