# Mitsubishi FX

The Mitsubishi FX plug-in is used to access Mitsubishi's FX0, FX2, FX3 and other PLC series via the FX programming port.

## Add Device

Go to **Configuration -> South Devices**, then click **Add Device** to add the driver. Configure the following settings in the popup dialog box.

- Name: The name of this device node.
- Plugin: Select the **Mitsubishi FX** plugin.

## Device Configuration

After clicking **Create**, you will be redirected to the **Device Configuration** page, where we will set up the parameters required for Neuron to establish a connection with the northbound application. You can also click the device configuration icon on the southbound device card to enter the **Device Configuration** interface.

|  Parameter    |  Description              |
| -------- | ------------------------------ |
| **Connection Timeout** | Connection timeout, default is 3000 milliseconds |
| **Send Interval** | Command transmission interval, default 20 ms     |
| **Serial Device** | Serial device path                               |
| **Stop Bits** | Stop bits, default is 1                          |
| **Parity**  | Parity, default is even                          |
| **Baud Rate** | Baud rate, default is 9600                       |
| **Data Bits** | Data Bits, default is 7                          |

## Configure Data Groups and Tags

After the plug-in is added and configured, the next step is to establish communication between your device and Neuron by adding groups and tags to the Southbound driver.

Once device configuration is completed, navigate to the **South Devices** page. Click on the device card or device row to access the **Group List** page. Here, you can create a new group by clicking on **Create**, then specifying the group name and data collection interval.

Upon successfully creating a group, click on its name to proceed to the **Tag List** page. This page allows you to add device tags for data collection. You'll need to provide information such as the tag address, attributes, and data type.

For information on general configuration items, see [Connect to Southbound Devices](../south-devices.md). The subsequent section will concentrate on configurations specific to the driver.

### Data Types

* INT16
* UINT16
* INT32
* UINT32
* FLOAT
* DOUBLE
* BIT
* STRING


### Address Format

> AREA ADDRESS\[.BIT]\[.LEN\[H]\[L]]

#### AREA ADDRESS

| AREA | TYPE | ATTRIBUTE  |  REMARK                                  |
| ---- | -------- | ----- | -------------------------------------- |
| X    | bit      | read/write | Input relay (FX3U)                |
| Y    | bit      | read/write | Output relay (FX3U)               |
| M    | bit      | read/write | Internal relay (FX3U)             |
| S    | bit      | read/write | Status relay (FX3U)               |
| TS   | bit      | read/write | Timer Contact (FX3U)              |
| CS   | bit      | read/write | Counter Contact (FX3U)            |
| TN   | all      | read/write | Timer Current value (FX3U)        |
| CN   | all      | read/write | Counter Current value (FX3U)      |
| D    | all      | read/write | Data register (FX3)               |

#### .BIT

Only available for **non-bit type area**, means read the specified binary bit of the specified address, the binary bit index interval is [0, 15].

| Address  | Data Type |  Description                      |
| ----- | -------- | -------------------------- |
| D20.0 | bit      | D Area, address 20, bit 0 |
| D20.2 | bit      | D Area, address 20, bit 2 |

#### .LEN\[H]\[L]

When the data type is string type, **.LEN** indicates the length of the string; you can optionally fill in **H** and **L** to indicate two byte orders, and the default is the byte order of **H**.

### Example Addresses

| Address      | Data Type |  Description                                          |
| --------- | -------- | -------------------------------------------- |
| X0    | bit      | X Area, address is 0   |
| X1    | bit      | X Area, address is 1   |
| Y0    | bit      | Y Area, address is 0   |
| Y1    | bit      | Y Area, address is 1   |
| D100  | int16    | D Area, address is 100 |
| D120  | uint16   | D Area, address is 120 |
| D200  | uint32   | D Area, address is 200 |
| D10   | float    | D Area, address is 10  |
| D20   | double   | D Area, address is 20  |
| D152.16L | string   | D Area, address is 152, string length is 16, endianness is L |
| D183.16  | string   | D Area, address is 183, string length is 16, endianness H |

## Data Monitoring

After completing the point configuration, you can click **Monitoring** -> **Data Monitoring** to view device information and control devices. For details, refer to [Data Monitoring](../../../usage/monitoring.md).
