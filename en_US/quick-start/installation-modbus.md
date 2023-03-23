# Install modbus simulator

Install PeakHMI Slave Simulators software, and the installation package can be downloaded from [PeakHMI official website ](https://hmisys.com). Enter **Download ->PeakHMI Slave Simulators** on the official website, and click **Slave Simulator Installer** to download.

* After installation, run Modbus TCP slave EX. 
* Enter **Windows -> Register data**, and first select the site number, for example, 1. Click **OK** and select the register, for example, 40001. Then the corresponding address is 1!40001, where you can enter a tag value.

::: tip
Make sure that the network between Neuron and simulator can be connected.

Try to turn off the firewall in Windows, otherwise Neuron may not connect to the simulator.
Because the simulator uses port 502 (privileged port below 1024) by default, Windows Firewall will block port 502 data. You can choose to turn off Windows Firewall, or modify the simulator port to be greater than 1024 in the simulator settings, and restart the simulator.
:::