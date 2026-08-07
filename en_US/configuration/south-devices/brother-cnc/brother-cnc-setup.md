# Brother CNC Device-Side Configuration

This guide describes how to configure the Brother CNC machine's communication and network parameters so that the Neuron Brother CNC plugin can connect and collect data via TCP/IP.

## Prerequisites

Before starting, ensure the following:

- The Brother CNC control panel is accessible.
- You have the necessary permissions to modify machine communication parameters.
- The machine is connected to a network with an Ethernet cable.
- You have a static IP address, subnet mask, and gateway ready for the machine.

## Configuring Network and Communication Parameters

### Step 1: Enter the Communication Parameter Page

1. Press the **Database** button on the control panel.
2. Press **F6** to select **Communication Parameters**.

### Step 2: Configure Remote Access

On the communication parameter page, configure the following:

| Parameter | Setting | Description |
| ----------------------- | -------- | ------------------------------------------------ |
| **Data Rewrite (Slave)** | Yes | Allow external devices to read data from the CNC. |
| **Remote Operation** | Valid | Enable remote access to the machine. |

### Step 3: Configure Network Settings

Set the machine's network parameters:

| Parameter | Value |
| -------------- | ---------------------------------------- |
| **IP Address** | Enter the desired static IP address. |
| **Gateway** | Enter the network gateway address. |
| **Subnet Mask** | Enter the subnet mask (e.g., 255.255.255.0). |

::: tip
The IP address must be in the same subnet as the Neuron host machine, and the default communication port is **10000**.
:::

### Step 4: Enable Ethernet Access

Change the **Restrict Ethernet Access** parameter from **Yes** to **No** to allow external TCP/IP connections.

### Step 5: Save the Settings

1. After modifying all parameters, press **Complete Mode** (完成模式).
2. Then press **Exit Edit** (退出编辑) to save the configuration.

## Verifying Network Connectivity

After completing the configuration:

1. Record the IP address configured on the Brother CNC.
2. From the Neuron host machine, ping the Brother CNC IP address to verify basic network connectivity:
   ```shell
   ping <BROTHER_CNC_IP_ADDRESS>
   ```
3. Verify that TCP port **10000** is reachable from the Neuron host.

Once the connection is verified, configure the Neuron Brother CNC plugin on the Neuron side. See [Brother CNC](./brother-cnc.md) for details.

## Troubleshooting

### Cannot Connect to Brother CNC

**Possible causes:**
- Incorrect IP address configured in Neuron.
- Restrict Ethernet Access is still set to Yes.
- Data Rewrite is set to No.
- Remote Operation is set to Invalid.
- Firewall blocking TCP port 10000.
- The machine and Neuron host are not on the same network segment.

**Solutions:**
1. Verify the IP address configured on the Brother CNC.
2. Confirm the network parameters in Step 3 and Step 4 above are correctly set.
3. Check that Restrict Ethernet Access is set to No.
4. Ensure Data Rewrite is set to Yes and Remote Operation is Valid.
5. Confirm that TCP port 10000 is not blocked by a firewall.
6. Ping the Brother CNC IP address from the Neuron host to verify network connectivity.

### Settings Not Saved After Restart

**Possible causes:**
- The parameter save procedure was not completed correctly.

**Solutions:**
1. Re-enter the Communication Parameter page.
2. Verify that all settings are still in place.
3. Make sure to press **Complete Mode** followed by **Exit Edit** after making changes.
4. Restart the machine if necessary and re-check the settings.
