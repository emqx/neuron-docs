# NeuOPC remote access 

In this example, the host set above is used as a client to connect to another host in the LAN to realize cross-host OPC DA data reading and conversion. The remote host uses the Windows 10 x64 operating system for demonstration.

## Remote host DCOM settings

Install MatrikonOPC Server for Simulation on the remote host, and close the firewall of the computer. The demo uses the Administrator account.

1. Press the **WIN + R** keys and enter `dcomcnfg` in the pop-up dialog box to confirm and enter the component service, as shown in the figure:

![comcnf](./assets/comcnf.png)

2. First set the overall properties of the machine, expand **Component Services\Computers\My Computer**, right-click My Computer to open the **Properties** setting in the menu:

![comcnf1](./assets/comcnf1.png)

Check `Enable Distributed COM on this computer` in **Default Properties**, and set `Default Authentication Level` to `None`:

![comcnf2](./assets/comcnf2.png)

In **Default Protocols** keep only `Connection-oriented TCP/IP`:

![comcnf3](./assets/comcnf3.png)

In **COM Security**, add `Everyone`, `Administrators`, and `ANONYMOUS LOGON` users to `Edit Limits` and `Edit Default Limits` in `Access Permissions` and `Launch and Activation Permissions` respectively, and set them Check all permissions below:

![comcnf4](./assets/comcnf4.png)

3. Expand **Component Services\Computers\My Computer\DCOM Config**, set the properties of `OpcEnum` and `MatrikonOPC Server for Simulation and Testing` respectively, and select `None` in **General** -> `Authentication Level`:

![comcnf5](./assets/comcnf5.png)

In **Location** select `Run application on the computer where the data is located` and `Run application on this computer`：

![comcnf6](./assets/comcnf6.png)

In **Security**, select Custom for all permissions and add users `Everyone`, `Administrators`, and `ANONYMOUS LOGON` respectively, and check all permissions under them:

![comcnf7](./assets/comcnf7.png)

4. Make sure to close the system firewall or add a security policy to allow programs such as OpcEnum and Matrikon to pass through.

So far, the remote host test environment of OPC DA has been set up.

## Localhost DCOM Settings

In order to remotely access the set remote host, it is also necessary to perform DCOM settings on the local host. Here, except for the configuration content `MatrikonOPC Server for Simulation and Testing`, consistent with the remote host, close the firewall of the local host before starting.

1. First set the overall properties of the machine, expand **Component Services\Computers\My Computer**, right-click **My Computer** to open the **Properties** setting in the menu, the content and method of setting are consistent with the remote host:

![client-cfg1](./assets/client-cfg1.png)

![client-cfg2](./assets/client-cfg2.png)

![client-cfg3](./assets/client-cfg3.png)

2. Expand **Component Services\Computers\My Computer\DCOM Config**, set `OpcEnum`, the content and method of setting are consistent with the remote host:

![client-cfg4](./assets/client-cfg4.png)

![client-cfg5](./assets/client-cfg5.png)

![client-cfg6](./assets/client-cfg6.png)

3. Make sure to close the system firewall or add a security policy to allow the OpcEnum program to pass.

So far, the local host test environment of OPC DA has been set up.

![client-worked](./assets/client-worked.png)

![client-worked](./assets/client-worked1.png)

