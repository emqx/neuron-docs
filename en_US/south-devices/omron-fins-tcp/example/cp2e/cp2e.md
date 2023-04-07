# Connect to Omron CP2E PLC

This article will use the Omron FINS TCP plugin to connect to the Omron CP2E PLC and read and write tag values in the PLC.

![cp2ec](./assets/cp2ec.jpg)

The Omron FINS TCP plugin can connect to the Omron PLC via the local LAN or Internet, but note that if the PLC and the Neuron server are not on the same LAN, you need to configure port forwarding on the PLC.

## Omron CP2E PLC tags

This article assumes that you can connect to the CP2E PLC using the Omron programming software CX-Programmer and view the tags in the PLC.

* Select **Settings** from the left menu bar to open the PLC Settings window and find the **Built-in Ethernet** tab.
Configure the IP address, subnet mask, etc. for the PLC.
* Select **Memory** from the left menu to open the PLC Memory window. You can see the data areas and address ranges supported by the PLC, as shown in the following figure. This PLC has multiple data areas, including CIO, A, W, etc.

## Neuron configuration node connects to CP2E PLC

* Click `Add Device` in the southbound device, select the plugin `Omron FINS TCP` to create a node that connects to the CP2E PLC.
* After creating the node, click `Device Configuration` to enter the device configuration page and configure the node information according to the actual situation,
	* `PLC IP Address`: The IP address of the PLC
	* `PLC Port`: The port of the PLC, the default is 9600
* Create a group under the created southbound device node, and create tags under the group.
* Enter the Neuron **Monitoring Page** and select the corresponding device and group to view the tags.
