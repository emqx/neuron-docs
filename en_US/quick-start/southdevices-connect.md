# Connect to southbound devices

## Step 1, Add a southbound device

Create a southbound device node to connect to a real device or simulator.

Select **South Devices -> Configuration** menu to enter the southbound device management interface, and click `Add Device` to add deivce nodes and add a new southbound device:

* Name: fill in the name of the device, such as modbus-tcp-1;
* Plugin: select the plugin of modbus-tcp from the drop-down box.

## Step 2, Setting southbound device's parameters

Configure the parameters required for Neuron to establish a connection with the device. In the upper right corner, you can select a list or card to display southward equipment

Click the `Device Configuration` button on the southbound device card to enter the device configuration interface:

* Device IP Address: fill in the IP of the PC where PeakHMI Slave Simulators software is installed;
* Device Port: fill in the port used by the simulator. Port 502 is used by default;
* Recv Timeout: The unit is ms, and the default is 3,000. If no message is received after the set time, an error will be reported;
* Click `Submit` to complete the equipment configuration, and the equipment card will automatically enter the working state of **Running**.

:::tip
The configuration parameters required by each device are different. Please refer to [Southbound Drivers](../south-devices/modbus-tcp/modbus-tcp.md) for detailed description of southbound device parameters.
:::