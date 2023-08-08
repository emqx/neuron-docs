# Connect to Cogent

Cogent, an advanced artificial intelligence and data analytics software platform designed to unlock the power of data-driven decision-making. With its cutting-edge AI capabilities, Cogent enables businesses to extract valuable insights from diverse datasets, identify patterns, and make informed decisions. 

## Install Cogent

1. Download the CogentDataHub installation package from the official Cogent website and install it according to the official documentation.

2. Start an EMQX broker instance locally with the start command:

   ```bash
   ./bin/emqx start
   ```

3. Right-click on the Cogent icon in the system tray to open **Cogent DataHub**.

4. Open **MQTT Broker** and deselect **Enable MQTT Broker**.

5. Open **MQTT Client**, select **Enable MQTT client connections**, click **Add** button to add a new connection, select **Sparkplug B**, set **Type** to **Non-primary application**, set **Host Name/IP** to **localhost** and **Port** to **1883**.
![cogent1](./assets/cogent1.jpg)
![cogent2](./assets/cogent2.jpg)

## Configure Neuron

### Southbound Device

This section assumes that the southbound OCP UA plugin has been installed, the group and point configurations are complete, and communication with Neuron functions normally. For details on the installation and configuration of the OCP UA plugin, refer to the [OCP UA section](../../south-devices/opc-ua/overview.md).

### Northbound Application

1. Add a Sparkplug B application to the Neuron **Northbound Application Manager**.

2. Fill in the **Client ID**, **Group ID**, **Node ID**, **Server Address** and **Server Port** in **Application Configuration**, click **Submit** and start the connection.
![ignition2](./assets/ignition2_en.jpg)

3. Add the **Southbound devices** and **Groups** to the **Group** list that you want to subscribe to.
    ![ignition3](./assets/ignition3_en.jpg)

  

## View Data Forwarding

Click the **View Data** button on the Cogent DataHub main interface to see the test data being uploaded instantly.
  ![cogent3](./assets/cogent3.jpg)
