# Mazak Device-Side Configuration

This guide describes how to configure the Mazak CNC to send operating data over UDP so that the Neuron Mazak CNC plugin can collect it. The communication relies on the **Mazak Fusion Client** application running on the Windows PC of the Mazak controller.

## Applicable Controls

The following Mazak control types are supported:

- **Fusion 640** (may require a 16-bit PCMCIA network card)
- **Matrix**
- **Nexus**
- **Preview 3**
- **Smooth**

::: warning
The **Preview G**, **Smooth G**, and **Smart** controls require MTConnect instead of Fusion Client. Please contact Mazak to purchase MTConnect for these controls.
:::

## Prerequisites

Before starting, ensure the following are ready:

1. **Mazak Machine Requirements:**
   - Mazak control with Windows PC
   - Network connectivity (Ethernet)
   - Static or reserved DHCP IP address assigned to the machine
   - Mazak Fusion Client application (version 2.1 or later)
2. **Network Requirements:**
   - The Neuron host machine must be able to reach the Mazak CNC IP address
   - **UDP port 51001** must be allowed through the firewall (both inbound and outbound)
   - Bi-directional communication between Neuron and the Mazak CNC
3. **Access Requirements:**
   - Administrator access to the Windows PC on the Mazak control
   - Ability to install and configure the Fusion Client application

## Accessing the Windows Desktop

The Fusion Client runs on the Windows side of the Mazak controller. The method for accessing the Windows desktop depends on your control type.

### Nexus, Fusion, and Matrix Controls

1. Using the cursor pad or knob, move the cursor to the **bottom-left corner of the screen** as far as it will go.
2. Left-click to bring up the Windows taskbar from the bottom.

### Smooth Controls

1. Tap the **gear icon** in the top-right corner of the screen.
2. Select **Setup**, then **Show Windows**. If nothing appears, repeat this step — it sometimes takes a second attempt.
3. Swipe in from the right side of the screen to reveal the Windows menu.

## Installing and Launching Fusion Client

### Step 1: Launch Fusion Client

1. Navigate to `C:\CPCU\fmcnc` in Windows Explorer.
2. Double-click `FusionClient.exe`.
3. The application will launch and appear in the Windows system tray (bottom-right corner).

> **Note:** If the `C:\CPCU` folder does not exist on your machine, contact Mazak to obtain the Fusion Client application.

### Step 2: Open Fusion Client Settings

1. In the Windows system tray, locate the Fusion Client icon.
2. Double-click the Fusion Client icon to open the configuration window.

## Configuring the Connection

### Step 1: Configure Connection Settings

1. In the Fusion Client configuration window, click **Change Settings**.
2. Click **Add** to create a new connection.
3. Enter the following information:

| Parameter | Description |
| --------------------- | ---------------------------------------------------- |
| **Network Name** | Leave blank. |
| **IP Address** | Enter the **static IP address of the Neuron host machine**. |
| **UDP Receive Port** | Enter `51001`. |
| **Host Compatibility** | Select **Level 4** from the dropdown. |

4. Click **OK** or **Apply** to save the connection settings.

### Step 2: Configure Parameter Settings

1. In the Fusion Client main menu, go to the **Parameter** tab.
2. **Deselect** the **Close Button** checkbox to prevent the Fusion Client from being accidentally closed.
3. Click **OK** or **Apply**.

### Step 3: Configure Windows Firewall

If the Windows firewall is enabled on the Mazak CNC, configure it to allow UDP traffic on port 51001.

| Setting | Value |
| ------------ | ---------------------------------- |
| **Protocol** | UDP |
| **Port** | 51001 |
| **Direction** | Both inbound and outbound |
| **Source** | Neuron host machine IP address |
| **Destination** | Mazak CNC IP address |

Alternatively, if the firewall is not required, you may disable it completely.

## Verifying Network Connectivity

After completing the configuration:

1. From the Neuron host machine, ping the Mazak CNC IP address to verify basic network connectivity:
   ```shell
   ping <MAZAK_CNC_IP_ADDRESS>
   ```
2. Verify that the Mazak CNC can reach the Neuron host machine.
3. Ensure UDP port 51001 is open between the two machines.

Once the connection is verified, configure the Neuron Mazak CNC plugin on the Neuron side. See [Mazak CNC](./mazak-udp.md) for details.

## Troubleshooting

### No Data Received

**Possible causes:**
- Fusion Client is not running
- Incorrect IP address configured in Fusion Client
- Firewall blocking the connection
- Outdated Fusion Client version

**Solutions:**
1. Verify that the Fusion Client is running (check the Windows system tray).
2. Check that the IP address in Fusion Client matches the Neuron host machine IP.
3. Confirm that UDP port 51001 is allowed through the firewall in both directions.
4. Check the Fusion Client version — versions older than 2.1 may not work correctly.

### Fusion Client Not in Taskbar

If the Fusion Client icon is not visible in the system tray:

- Navigate to `C:\CPCU\fmcnc` and double-click `FusionClient.exe` to launch it.
- If the folder or executable is missing, contact Mazak to obtain the Fusion Client application.

### Machine Status Shows Disconnected

**Possible causes:**
- Network interruption
- Fusion Client has stopped
- IP address changed

**Solutions:**
1. Check network connectivity.
2. Restart the Fusion Client application.
3. Restart the Windows PC on the machine control.
4. Verify that a static IP address is assigned to the Mazak CNC.
5. Check that the Neuron host machine can reach the Mazak CNC IP address.
