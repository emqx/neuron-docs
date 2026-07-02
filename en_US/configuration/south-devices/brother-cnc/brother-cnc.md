# Brother CNC

The Brother CNC plugin is used to access Brother CNC machining centers via the Brother NC protocol. It collects machine operating data such as axis coordinates, spindle, tool, alarms, workpiece count, program number, PLC devices, and tool offset data. The plugin supports connecting to the device over either a serial (Serial) or Ethernet link.

::: tip
The Brother CNC plugin is read-only. It only supports data collection (read) and does not support control (write).
:::

## Add Device

Go to **Configuration -> South Devices**, then click **Add Device** to add the driver. Configure the following settings in the popup dialog box.

- Name: The name of this device node.
- Plugin: Select the **Brother CNC** plugin.

## Device Configuration

After clicking **Create**, you will be redirected to the **Device Configuration** page, where you set up the parameters required for Neuron to establish a connection with the device. You can also click the device configuration icon on the southbound device card to enter the **Device Configuration** interface.

| Parameter | Description |
| ------------------ | ----------------------------------------------------------- |
| **Physical Link** | Select Serial or Ethernet as the communication medium. Default is Ethernet. |
| **Connection Timeout (ms)** | Time to wait for the device to respond to a request, ranging from 1000 to 30000. Default is 3000. |
| **Serial Device** | In serial mode, the path of the serial device, e.g. /dev/ttyS0 on Linux. |
| **Baud Rate** | Serial connection parameter. Options: 115200/57600/38400/19200/9600/4800. Default is 9600. |
| **Data Bits** | Serial connection parameter. Options: 7/8. Default is 8. |
| **Stop Bits** | Serial connection parameter. Options: 1/2. Default is 1. |
| **Parity** | Serial connection parameter. Options: none/odd/even. Default is none. |
| **CNC IP Address** | In Ethernet mode, the IPv4 address of the target CNC device. |
| **CNC Port** | In Ethernet mode, the port of the target CNC device, ranging from 1 to 65535. Default is 10000. |

## Configure Data Groups and Tags

After the plugin is added and configured, the next step is to establish communication between your device and Neuron by adding groups and tags to the southbound driver.

Once device configuration is completed, navigate to the **South Devices** page. Click on the device card or device row to access the **Group List** page. Here, you can create a new group by clicking **Create**, then specifying the group name and data collection interval.

After successfully creating a group, click on its name to proceed to the **Tag List** page. This page allows you to add device tags for data collection. You'll need to provide information such as the tag address, attributes, and data type.

For information on general configuration items, see [Connect to Southbound Devices](../south-devices.md). The subsequent section will concentrate on configurations specific to the driver.

::: tip
The Brother CNC plugin only supports the **read-only** tag attribute. During collection, the plugin batches requests for tags of the same data area (PDSP, ALARM, PLCD, etc.). Grouping tags of the same area together is recommended to improve collection efficiency.
:::

### Data Types

* INT16
* UINT16
* INT32
* UINT32
* INT64
* UINT64
* FLOAT
* DOUBLE
* BIT
* BOOL
* STRING

### Address Format

The Brother CNC plugin organizes tag addresses by data area. The address format and supported data types vary between areas.

#### PDSP (Machine Operating Data)

| Address | Data Type | Attribute | Description |
| ----------------------- | --------------------------------------------------- | --------- | --------------- |
| PDSP.MACHINE_X | INT16/UINT16/INT32/UINT32/INT64/UINT64/FLOAT/DOUBLE | Read | Machine X-axis coordinate |
| PDSP.MACHINE_Y | INT16/UINT16/INT32/UINT32/INT64/UINT64/FLOAT/DOUBLE | Read | Machine Y-axis coordinate |
| PDSP.MACHINE_Z | INT16/UINT16/INT32/UINT32/INT64/UINT64/FLOAT/DOUBLE | Read | Machine Z-axis coordinate |
| PDSP.FEED_SPEED | INT16/UINT16/INT32/UINT32/INT64/UINT64/FLOAT/DOUBLE | Read | Feed speed |
| PDSP.SPINDLE_SPEED | INT16/UINT16/INT32/UINT32/INT64/UINT64/FLOAT/DOUBLE | Read | Spindle speed |
| PDSP.TOOL_NO | INT16/UINT16/INT32/UINT32/INT64/UINT64 | Read | Current tool number |
| PDSP.NEXT_TOOL_NO | INT16/UINT16/INT32/UINT32/INT64/UINT64 | Read | Next tool number |
| PDSP.RAPID_OVERRIDE | INT16/UINT16/INT32/UINT32/INT64/UINT64 | Read | Rapid traverse override |
| PDSP.FEED_OVERRIDE | INT16/UINT16/INT32/UINT32/INT64/UINT64 | Read | Feed override |
| PDSP.SPINDLE_OVERRIDE | INT16/UINT16/INT32/UINT32/INT64/UINT64 | Read | Spindle override |

#### ALARM (Alarm Data)

| Address | Data Type | Attribute | Description |
| ----------- | -------------------------------- | --------- | ----------------------------------------- |
| ALARM.\<N\> | INT32/UINT32/INT64/UINT64 | Read | Alarm data, where N is the column index (0-based) |

#### WKCNTR (Workpiece Count Data)

| Address | Data Type | Attribute | Description |
| ------------ | -------------------------------------- | --------- | --------------- |
| WKCNTR.COUNT | INT16/UINT16/INT32/UINT32/INT64/UINT64 | Read | Workpiece count |

#### PRDC2 (Production Time Data)

| Address | Data Type | Attribute | Description |
| ----------------- | -------------------------------------- | --------- | ------------ |
| PRDC2.CYCLE_TIME | INT16/UINT16/INT32/UINT32/INT64/UINT64 | Read | Cycle time |
| PRDC2.CUTTING_TIME | INT16/UINT16/INT32/UINT32/INT64/UINT64 | Read | Cutting time |

#### PRGN (Program Number Data)

| Address | Data Type | Attribute | Description |
| ------------ | ---------------------- | --------- | -------------------- |
| PRGN.CURRENT | INT32/UINT16/STRING | Read | Current program number |
| PRGN.MAIN | INT32/UINT16/STRING | Read | Main program number |
| PRGN.BLOCK | INT32/UINT16/STRING | Read | Current block number |

#### PLCD (PLC Devices)

| Address | Data Type | Attribute | Description |
| ------------- | --------------------------------------------- | --------- | -------------------------------- |
| PLCD.D.\<N\> | INT16/UINT16/INT32/UINT32/FLOAT/DOUBLE | Read | D data register, N is the register address |
| PLCD.M.\<N\> | BIT/BOOL | Read | M relay, N is the register address |

#### TOLSD (Tool Offset Data)

| Address | Data Type | Attribute | Description |
| ------------------------- | -------------------------------------------------------- | --------- | -------------------------------------------------- |
| TOLSD.\<DB\>.\<ID\>.\<N\> | INT16/UINT16/INT32/UINT32/INT64/UINT64/FLOAT/DOUBLE | Read | Tool offset data, DB ranges 1-10, ID ranges 1-99, N is the column index |

### Address Examples

| Address | Data Type | Description |
| ----------------- | --------- | -------------------------------------- |
| PDSP.MACHINE_X | FLOAT | Machine X-axis coordinate |
| PDSP.SPINDLE_SPEED | INT32 | Spindle speed |
| PDSP.TOOL_NO | INT16 | Current tool number |
| PDSP.FEED_OVERRIDE | INT32 | Feed override |
| ALARM.1 | INT32 | Alarm data column 1 |
| WKCNTR.COUNT | INT32 | Workpiece count |
| PRDC2.CYCLE_TIME | INT32 | Cycle time |
| PRGN.CURRENT | INT32 | Current program number |
| PRGN.MAIN | STRING | Main program number |
| PLCD.D.100 | INT16 | D register at address 100 |
| PLCD.M.2048 | BIT | M relay at address 2048 |
| TOLSD.1.1.2 | FLOAT | DB 1, tool ID 1, column index 2 |

## Data Monitoring

After configuring the tags, you can click **Monitoring** -> **Data Monitoring** to view device information. For more details, see [Data Monitoring](../../../admin/monitoring.md).
