# NeuOPC Settings

## Native OPCDA server access

This example uses windows 7 SP1 32-bit system to demonstrate

::: tip
Neuopc can only run on Windows 7 SP1 and above and requires the installation of the [KB3063858](https://www.microsoft.com/zh-CN/download/details.aspx?id=47409)  and [KB2999226](https://www.microsoft.com/zh-cn/download/details.aspx?id=49077) updates.
:::

### Install the neuopc runtime environment

1. Enter neuopc [project releases page](https://github.com/neugates/neuopc/releases) to download the latest version component package "neuopc-package.zip". After decompression, you can see the following files:

![](./assets/package.png)

* neuopc - the main program to run OPCDA to convert OPCUA;
* dotnetfx-1.1——.Net framework 1.1, you need to correct this program before installing OPC DAAuto;
* OPC DA Auto 2.02 Source Code 5.30.msi - the official component of the OPC Foundation, Install using "Windows Task Manager";
* OPC Core Components Redistributable (x64) 3.00.108.msi - OPC Foundation official components, no need to install;
* OPC Core Components Redistributable (x86) 3.00.108.msi - OPC Foundation official components, no need to install;

2. Check if .Net framework 1.1 has been installed, if not, install dotnetfx-1.1;

3. Use the task manager to install OPC DA Auto 2.02 Source Code 5.30.msi, open the "Windows Task Manager", open "File" - "New Task", enter the MSI file path, and check "Create this task with system administrative rights";

![](./assets/install-auto.png)

4. Check if the component is installed

* If it is a 32-bit operating system, enter the C:\Windows\System32 directory, if it is a 64-bit operating system, enter the C:\Windows\SysWOW64 directory, and check whether the following files exist:

![](./assets/core-components.png)

::: tip
If the file does not exist then contact sales for support.
:::

* Open "Windows Task Manager" to check whether the OpcEnum system service is running, as shown in the figure:

![](./assets/opcenum.png)

::: tip
If it works normally, it means that OPC DA Auto 2.02 has been installed normally.
:::

5. Install the MatrikonOPCSimulation simulator program locally, if the installation fails, you can install KepServerEX for testing;

6. Run the neuopc.exe program, select DA Host and DA Server and click Connect, set the parameters of UA and click Run, the operation is successful, as shown in the figure:

![](./assets/local-neuopc.png)

## Remote host OPCDA server access

In this example, the host set above is used as a client to connect to another host in the LAN to realize cross-host OPCDA data reading and conversion. The remote host uses the Windows 10 x64 operating system for demonstration.

### Remote host DCOM settings

Install MatrikonOPC Server for Simulation on the remote host, and close the firewall of the computer. The demo uses the Administrator account.

1. Press the WIN + R keys and enter dcomcnfg in the pop-up dialog box to confirm and enter the component service, as shown in the figure:

![](./assets/comcnf.png)

2. First set the overall properties of the machine, expand "Component Services\Computers\My Computer", right-click My Computer to open the Properties setting in the menu:

![](./assets/comcnf1.png)

Check "Enable Distributed COM on this computer" in "Default Properties", and set "Default Authentication Level" to "None":

![](./assets/comcnf2.png)

In "Default Protocols" keep only "Connection-oriented TCP/IP":

![](./assets/comcnf3.png)

In "COM Security", add "Everyone", "Administrators", and "ANONYMOUS LOGON" users to "Edit Limits" and "Edit Default Limits" in "Access Permissions" and "Launch and Activation Permissions" respectively, and set them Check all permissions below:

![](./assets/comcnf4.png)

3. Expand "Component Services\Computers\My Computer\DCOM Config", set the properties of "OpcEnum" and "MatrikonOPC Server for Simulation and Testing" respectively, and select "None" in "General"-"Authentication Level":

![](./assets/comcnf5.png)

在"Location"中勾选"Run application on the computer where the data is located"和"Run application on this computer"：

![](./assets/comcnf6.png)

In "Security", select Custom for all permissions and add users "Everyone", "Administrators", and "ANONYMOUS LOGON" respectively, and check all permissions under them:

![](./assets/comcnf7.png)

4. Make sure to close the system firewall or add a security policy to allow programs such as OpcEnum and Matrikon to pass through.

So far, the remote host test environment of OPCDA has been set up.

### Localhost DCOM Settings

In order to remotely access the set remote host, it is also necessary to perform DCOM settings on the local host. Here, continue to use the windows 7 SP1 32-bit system demo configured in [Local OPCDA Server Access] above, except for the configuration content "MatrikonOPC Server for Simulation and Testing ", consistent with the remote host, close the firewall of the local host before starting.

1. First set the overall properties of the machine, expand "Component Services\Computers\My Computer", right-click My Computer to open the Properties setting in the menu, the content and method of setting are consistent with the remote host:

![](./assets/client-cfg1.png)

![](./assets/client-cfg2.png)

![](./assets/client-cfg3.png)

2. Expand "Component Services\Computers\My Computer\DCOM Config", set "OpcEnum", the content and method of setting are consistent with the remote host:

![](./assets/client-cfg4.png)

![](./assets/client-cfg5.png)

![](./assets/client-cfg6.png)

3. Make sure to close the system firewall or add a security policy to allow the OpcEnum program to pass.

So far, the local host test environment of OPCDA has been set up.

![](./assets/client-worked.png)

