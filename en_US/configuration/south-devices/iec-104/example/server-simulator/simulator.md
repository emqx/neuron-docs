# IEC 60870-5-104 Server Simulator Connection Example

This article will use the IEC60870-5-104 plugin of Neuron to connect to [IEC60870-5-104 Server Simulator](https://www.freyrscada.com/iec-60870-5-104-Client-Simulator.php), which supports the collection of multiple data types and control.

## Download IEC 60870-5-104 Server Simulator

You can download the IEC6087-5-104 Server Simulator from [here](https://sourceforge.net/projects/iec-104-client-simulator/), the trial version of the emulator will automatically shut down after 15 minutes of operation, save the configuration data in time. 
Download and unzip the IEC6087-5-104 Server Simulator executable file, click install.

### Simulator configuration

* Open **IEC 60870-5-104 Server Simulator**.
* Click `Add Server` to create a server.
* Modify the configuration in table **IEC104-SERVER_1**, modify the value of the **Source IP Address** to 0.0.0.0 .
* In table **Configuration_1**, click `Add Row` to create a tag, **IEC60870-5 Group to Choose** menu selection **Measured Normalized**, **Event Report Type Id** menu selection **M_ME_NA_1=9**.
* Other parameters keep their default value, **IOA** default 1, **Common Address** default 1.

![simulator-tag](./assets/tag.png)

* Click `Load Configuration` and then click `Start Communication` to run server.

### Use Neuron connect simulator

* Go to Neuron Dashboard, create a south node with **IEC60870-5-104 plugin**.
* Click `Device Configuration` and then **Device IP Address** fill in the simulator address, other parameters keep default value.
* Create a group, and then create a tag in that group with tag address **1**.
* In **Monitoring -> Data Monitoring** page, you can see the tag value after selecting **South device** and **Group name**.