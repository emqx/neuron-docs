# Siemens MPI

MPI is a communication protocol based on the Siemens MPI interface, which allows a PLC to exchange data with other devices (e.g. SCADA systems, HMI devices, other PLCs, etc.) The MPI interface is typically built into S7300 and S7400 PLCs.

The MPI interface is typically built into S7300 and S7400 PLCs. MPI requires a special cable to be accessed by the PC. The MPI needs to be converted to RS232 serial protocol using a 6ES7-972-0CA23-0XA0 module (or a compatible module), and then connected to the PC using a USB-RS232 module, or if the PC has an RS232 interface the second conversion step is not required.

Neuron's MPI plug-in is available for data access on S7300 and S7400 PLCs.

## Add Device

In **Configuration -> Southbound Devices**, click **Add Device** to create the device node, enter the plug-in name, and select **Siemens MPI** for the plug-in type to enable the plug-in.

## Device Configuration

Click on the Plugin card or Plugin column to go to the **Device Configuration** page. Configure the parameters required for Neuron to establish a connection with the device, the table below shows the plugin related configuration items.


| Parameter                  | Description                                                    |
| ------------ | --------------------------- |
| Connection Timeout  |  Connection timeout(ms)     |
| Send Interval  |  Send reading instruction interval(ms) |
| Target Station     |   Target station, Default is 2 |
| Serial Device     |   Serial device path, Default is /dev/ttyUSB0 |
| Stop Bits       |   Stop bits, Default and only 1 |
| Parity       |   Parity, Default and only Odd |
| Baud Rate       |   Baud Rate, Default and only 38400 |
| Data Bits       |   Data Bits, Default and only 8 |

## Configure Data Groups and Tags

After completing the plugin addition and configuration, to establish communication between the device and Neuron, first add groups and points for the southbound driver.

After completing the device configuration, on the **Southbound Devices** page, click on the Device Card/Device column to go to the **Group List** page. Click **Create** to create the group, set the group name and acquisition interval. After completing the creation of the group, click the group name to enter the **Tag List** page to add the device points to be collected, including point address, point attributes, data type, etc.

For the public configuration item section, you can refer to [Connecting Southbound Devices](../south-devices.md), this page will introduce the supported data type and address format section.

### Data types

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
* STRING

### Address format

> AREA ADDRESS\[.BIT][.LEN]

#### AREA ADDRESS

| Area |  Data Type                                                     | Attribute  |   Discription                   |
| ---- | ------------------------------------------------------------ | ----- | ----------------------- |
| DB.DBB   |int8，uint8，int16，uint16，bit，int32，uint32，int64，uint64，float，double，string | Read/Write    | Main memory data block, read/write bytes |
| M        | int8，uint8，int16，uint16，bit，int32，uint32，int64，uint64，float，double，string | Read/Write | Memory block, read/write bytes  |

#### .BIT

Optional, refers to a bit of an address, range 0~7.

#### .LEN

Required when the data type is string, indicating the length of the string.

### Example Addresses

|  Address        | Data Type | Description                                         |
| ------------ | -------- | -------------------------------------------- |
| DB1.DBB10 | int16    | DB1 Area，Starting data address is 10 |
| DB2.DBB10 | uint16   | DB2 Area，Starting data address is 10 |
| DB1.DBB12 | float    | DB1 Area，Starting data address is 12 |
| DB1.DBB14 | double   | DB1 Area，Starting data address is 14 |
| DB1.DBB19.1 | bit      | DB1 Area，Starting data address is 19，2nd bit |
| DB1.DBB19.7 | bit      | DB1 Area，Starting data address is 19，8th bit |
| DB1.DBB20.20 | string   | DB1 Area，Starting data address is 20，string length is 20 |
| M98  | int8     | M Area，Starting data address is 98 |
| M99  | uint8    | M Area，Starting data address is 99 |
| M100 | int16    | M Area，Starting data address is 100 |
| M102 | uint16   | M Area，Starting data address is 102 |
| M104 | float    | M Area，Starting data address is 104 |
| M106 | double   | M Area，Starting data address is 106 |
| M111.3 | bit      | M Area，Starting data address is 111，4th bit |
| M112.20 | string   | M Area，Starting data address is 20，string length is 20 |
| I2.1 | bit   | I Area，Starting data address is 2，1st bit |
| Q0.7 | bit   | Q Area，Starting data address is 0，7th bit |


## Data Monitoring

After completing the point configuration, you can click **Monitoring** -> **Data Monitoring** to view device information and control devices. For details, refer to [Data Monitoring](../../../admin/monitoring.md).