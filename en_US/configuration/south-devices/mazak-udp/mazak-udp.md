# Mazak CNC

The Mazak CNC plugin collects real-time operating data from Mazak CNC via a passive UDP listener. The Mazak CNC sends status data packets over UDP, and the plugin parses the packet fields into individual data tags. The driver does not send any requests to the CNC; it only listens for incoming UDP data.

::: tip
The Mazak CNC plugin is read-only. It only supports data collection (read) and does not support control (write).
:::

## Add Device

Go to **Configuration -> South Devices**, then click **Add Device** to add the driver. Configure the following settings in the popup dialog box.

- Name: The name of this device node.
- Plugin: Select the **Mazak CNC** plugin.

## Device Configuration

After clicking **Create**, you will be redirected to the **Device Configuration** page, where you set up the parameters required for Neuron to establish a connection with the device. You can also click the device configuration icon on the southbound device card to enter the **Device Configuration** interface.

| Parameter | Description |
| ----------------------- | ------------------------------------------------------------------------------------------------ |
| **Bind IP** | The local IP address to bind the UDP listener. Default is `0.0.0.0` (listen on all interfaces). |
| **Port** | The UDP port to listen on, ranging from 1 to 65535. Default is `51001`. |
| **Connection Timeout (ms)** | UDP receive timeout, ranging from 1 to 60000. Default is `3000`. |

## Configure Data Groups and Tags

After the plugin is added and configured, the next step is to establish communication between your device and Neuron by adding groups and tags to the southbound driver.

Once device configuration is completed, navigate to the **South Devices** page. Click on the device card or device row to access the **Group List** page. Here, you can create a new group by clicking **Create**, then specifying the group name and data collection interval.

After successfully creating a group, click on its name to proceed to the **Tag List** page. This page allows you to add device tags for data collection. You'll need to provide information such as the tag address, attributes, and data type.

For information on general configuration items, see [Connect to Southbound Devices](../south-devices.md). The subsequent section will concentrate on configurations specific to the driver.

::: tip
The Mazak CNC plugin only supports the **read-only** tag attribute. All tag addresses are flat string names; there are no data areas or indexes.
:::

### Data Types

* STRING
* INT32

### Address Format

The Mazak CNC plugin defines a fixed set of tag addresses. Each address corresponds to a specific field parsed from the incoming UDP data packet.

| Address | Data Type | Attribute | Description |
| --------------------- | --------- | --------- | ------------------------------------------------- |
| machine_name | STRING | Read | Machine name |
| machine_ip | STRING | Read | Machine IP address |
| status | STRING | Read | Machine status (STOPPED, ACTIVE, FEED_HOLD) |
| mode | STRING | Read | Operation mode (AUTOMATIC, MANUAL_DATA_INPUT, MANUAL, EDIT) |
| program_number | STRING | Read | Current program number |
| program_name | STRING | Read | Current program name |
| subprogram_number | STRING | Read | Current subprogram number |
| subprogram_name | STRING | Read | Current subprogram name |
| alarm_number | STRING | Read | Alarm number |
| alarm_message | STRING | Read | Alarm message text |
| alarm_fore_color | STRING | Read | Alarm foreground color |
| alarm_back_color | STRING | Read | Alarm background color |
| part_count | INT32 | Read | Workpiece count |
| tool | STRING | Read | Current tool identifier |
| rapid_rate | INT32 | Read | Rapid traverse override rate |
| feed_sp_rate | INT32 | Read | Feed / spindle override rate |
| feed_rate | INT32 | Read | Feed rate |

#### Status Values

The `status` address returns one of the following string values:

| Value | Meaning |
| -------- | -------------------- |
| STOPPED | Machine is stopped |
| ACTIVE | Machine is running |
| FEED_HOLD | Feed hold is active |
| UNKNOWN | Unknown status |

#### Mode Values

The `mode` address returns one of the following string values:

| Value | Meaning |
| -------------------- | -------------------------------------------- |
| AUTOMATIC | Automatic operation mode |
| MANUAL_DATA_INPUT | Manual Data Input (MDI) mode |
| MANUAL | Manual operation mode |
| EDIT | Program editing mode |
| UNKNOWN | Unknown operation mode |

### Address Examples

| Address | Data Type | Description |
| --------------- | --------- | ---------------------------- |
| machine_name | STRING | Machine name |
| status | STRING | Machine status |
| mode | STRING | Operation mode |
| program_number | STRING | Current program number |
| alarm_number | STRING | Alarm number |
| alarm_message | STRING | Alarm message text |
| part_count | INT32 | Workpiece count |
| tool | STRING | Current tool identifier |
| rapid_rate | INT32 | Rapid traverse override rate |
| feed_rate | INT32 | Feed rate |

## Data Monitoring

After configuring the tags, you can click **Monitoring** -> **Data Monitoring** to view device information. For more details, see [Data Monitoring](../../../admin/monitoring.md).
