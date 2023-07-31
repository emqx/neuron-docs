# KNXnet/IP

## Add Device

Go to **Configuration -> South Devices**, then click **Add Device** to add the driver. Configure the following settings in the popup dialog box.

- Name: The name of this device node.
- Plugin: Select the **Modbus RTU** plugin.

## Device Configuration

After clicking **Create**, you will be redirected to the **Device Configuration** page, where we will set up the parameters required for Neuron to establish a connection with the northbound application. You can also click the device configuration icon on the southbound device card to enter the **Device Configuration** interface.

| Parameter | Description                               |
| --------- | ----------------------------------------- |
| **host**  | KNXnet/IP device ip, default 224.0.23.12  |
| **port**  | KNXnet/IP device port, default 3671       |

Note that setting with the multicast address *224.0.23.12* normally requires that the
KNXnet/IP device and Neuron are in the same sub network.

Due to the way how KNXnet/IP protocol works, the KNX plugin may not be able to work correctly
if Neuron is installed using some virtualisation technology such as virtual machines or docker.
In a Linux host with docker, using the docker option `--net=host` is required. In other cases,
we recommend that you install Neuron using binary packages.

## Configure Data Groups and Tags

After the plug-in is added and configured, the next step is to establish communication between your device and Neuron by adding groups and tags to the Southbound driver.

Once device configuration is completed, navigate to the **South Devices** page. Click on the device card or device row to access the **Group List** page. Here, you can create a new group by clicking on **Create**, then specifying the group name and data collection interval.

Upon successfully creating a group, click on its name to proceed to the **Tag List** page. This page allows you to add device tags for data collection. You'll need to provide information such as the tag address, attributes, and data type.

For information on general configuration items, see [Connect to Southbound Devices](../south-devices.md). The subsequent section will concentrate on configurations specific to the driver.

### Data Types

* bit
* bool
* int8
* uint8
* int16
* uint16
* float

### Address Format

* > GROUP_ADDRESS,INDIVIDUAL_ADDRESS</span>

Represents a KNX individual address that is a member of the group address.
When reading the KNX plugin sends a `GroupValueRead` tunnelling request using
the specified group address, and updates the tag value upon receiving a `GroupValueResp`
matching the specified individual address.
When writing the KNX plugin sends a `GroupValueWrite` tunnelling request using
the specified group address.

*Example:*

`0/0/1,1.1.1` represents a KNX individual address `1.1.1` that is a member
  of the group address `0/0/1`.

</br>
</br>
* > GROUP_ADDRESS,INDIVIDUAL_ADDRESS,BIT</span>

Same as above, but for `uint8` values with fewer than 8 bits, such as KNX data point
types `B2` and `B1U3`, etc. *BIT* represents the number of bits.

*Example:*

`0/0/1,1.1.1,2` represents a KNX individual address `1.1.1` that is a member
  of the group address `0/0/1`, the data is of 2 bit.
