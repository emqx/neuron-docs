# IEC61850

IEC61850 is an international communication standard protocol that achieves station-wide communication uniformity through a series of standardization of devices. IEC61850 is widely used in the power industry.

The MMS message specification is applied between the IEC61850 standard station control layer and the interval layer. MMS achieves interoperability between different manufacturing devices in a network environment through an object-oriented modeling approach to the actual devices.

The IEC61850 plug-in is used for read/write to the IEC61850 server and currently supports access to the MMS protocol.

## Add Device

Go to **Configuration -> South Devices**, then click **Add Device** to add the driver. Configure the following settings in the popup dialog box.

- Name: The name of this device node.
- Plugin: Select the **IEC61850** plugin.

## Device Configuration

After clicking **Create**, you will be redirected to the **Device Configuration** page, where we will set up the parameters required for Neuron to establish a connection with the northbound application. You can also click the device configuration icon on the southbound device card to enter the **Device Configuration** interface.

|   Parameters   | Description                      |
| -------- | -------------------------- |
| **Device IP Address** |  Target device IP             |
| **Device Port** | Target device port, Default 102 |
| **GI Interval** | The interval at which the device sends a general interrogation. Set to 0 to disable general interrogation. Unit: seconds |
## Configure Data Groups and Tags

After the plugin is added and configured, the next step is to establish communication between your device and IEC61850 driver by adding groups and tags to the Southbound driver.

The IEC61850 plugin only supports the automatic addition of groups and tags by importing an SCL file. The Report block in the SCL file generates readable data groups, and the points are generated based on the referenced DataSet. Points are generated for data with FC as CO, SP, and SG. Writable points are generated in a separate Control group.

IEC61850 plugin defines a special data reporting structure according to industry standards, with timestamp and quality fields in addition to the point value.

```json
{
 "timestamp": 1647497389075,
 "node": "iec61850",
 "group": "grp1",
 "tags": [{
   "name": "tag1",
   "value": 123,
   "q": 3,
   "t": 129401039041
  },
  {
   "name": "tag2",
   "value": 123,
   "q": 3,
   "t": 129401039088
  }
 ]
}
```

::: tip 

Since the IEC61850 plugin uses a special data reporting structure, when selecting the data format for the northbound plugin, you need to select the **Tags-format** format.

:::

## Use Case

You can access the LibIEC61850 server through the Neuron IEC61850 plugin. For specific steps, refer to [libiec61850](../iec61850/libiec61850.md).

## Data Monitoring

After completing the point configuration, you can click **Monitoring** -> **Data Monitoring** to view device information and control devices. For details, refer to [Data Monitoring](../../../admin/monitoring.md).
