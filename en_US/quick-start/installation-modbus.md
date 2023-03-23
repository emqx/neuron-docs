# Install Modbus Simulator

Install PeakHMI Slave Simulators software, and the installation package can be downloaded from [PeakHMI official website ](https://hmisys.com). Enter **Download ->PeakHMI Slave Simulators** on the official website, and click **Slave Simulator Installer** to download.

* After installation, run Modbus TCP slave EX. 
* Enter **Windows -> Register data**, and first select the site number, for example, 1. Click **OK** and select the register, for example, 40001. Then the corresponding address is 1!40001, where you can enter a tag value.

## Modbus Poll
Modbus Poll is a Modbus master simulator designed primarily to help developers of Modbus slave devices or others that want to test and simulate the Modbus protocol.


Modbus Poll read/write data from devices using:
* Modbus RTU or ASCII on RS232 or RS485 networks. (USB/RS232/485 Converter)
* Modbus TCP/IP
* Modbus Over TCP/IP. (Modbus RTU/ASCII encapsulated in a TCP packet)
* Modbus UDP/IP
* Modbus Over UDP/IP. (Modbus RTU/ASCII encapsulated in a UDP packet)
  
Install Modbus Poll software, and the installation package can be download form
[modbus tool download](https://www.modbustools.com/download.html), choose the appropriate version based on the operating environment.
* After installation, run Modbus Poll.
* Press F3 or enter **Connection -> Connect**, choose a connection method based on actual circumstances and set up the connection parameters, clicking **OK** will complete the configuration.
* Press F8, enter **Setup -> Read/Write Definition**, or click![Read/Write Definition](assets/mbpoll-definition-button.png) on toolbar set read/write definition. Setting up address parameters based on the read/write requirements, clicking **ok** will complete configuration.
* The data about read/write definition show on single document interface. If you want to see data for multiple read/write definition, click **File -> New**, create a new document windows, repeat step 3. You can input site number, address, and value to modify data on slave using double-clicking item in table.
* If you need to connect multiple slave devices simultaneously, run Modbus Poll on multiple instances.Repeat the above steps.

## Modbus Slave
Modbus Slave is a Modbus slave simulator. Speed up your PLC programming with this simulating tools. Start programming and test before you receive your slave device from supplier.

Modbus Slave read/write data from devices using:
* Modbus RTU or ASCII on RS232 or RS485 networks. (USB/RS232/485 Converter)
* Modbus TCP/IP
* Modbus Over TCP/IP. (Modbus RTU/ASCII encapsulated in a TCP packet)
* Modbus UDP/IP
* Modbus Over UDP/IP. (Modbus RTU/ASCII encapsulated in a UDP packet)
* 
Install Modbus Slave software, and the installation package can be download form
[modbus tool download](https://www.modbustools.com/download.html), choose the appropriate version based on the operating environment.
* After installation, run Modbus Slave.
* Press F3 or enter **Connection -> Connect**, choose a connection method based on actual circumstances and set up the connection parameters, clicking **OK** will complete the configuration.
* Press F8, enter **Setup -> Slave Definition**, or click![Slave Definition](assets/mbpoll-definition-button.png) on toolbar set slave definition. Setting up address parameters based on the read/write requirements, clicking **ok** will complete configuration.
* The data about slave definition show on single document interface. If you want to see data for multiple slave definition, click **File -> New**, create a new document windows, repeat step 3. You can input value to modify data using double-clicking item in table.
* If you need to simulate multiple slave devices simultaneously, run Modbus Slave on multiple instances.Repeat the above steps.


::: tip
Make sure that the network between Neuron and simulator can be connected.

Try to turn off the firewall in Windows, otherwise Neuron may not connect to the simulator.
Because the simulator uses port 502 (privileged port below 1024) by default, Windows Firewall will block port 502 data. You can choose to turn off Windows Firewall, or modify the simulator port to be greater than 1024 in the simulator settings, and restart the simulator.
:::