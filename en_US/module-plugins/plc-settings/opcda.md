# NeuOPC Settings

## Native OPCDA server access

This example uses windows 7 SP1 32-bit system to demonstrate

### Install the neuopc runtime environment

1. Enter neuopc [project page](https://github.com/neugates/neuopc) to download the latest Release component package "neuopc-package.zip". After decompression, you can see the following files:

   ![](assets-opcda/package.png)

   * neuopc - the main program to run OPCDA to convert OPCUA;
   * OPC Core Components Redistributable (x64) 3.00.108.msi - OPC Foundation official components, need to be installed under x64 system;
   * OPC Core Components Redistributable (x86) 3.00.108.msi - OPC Foundation official components, need to be installed under x86 system;
   * OPC DA Auto 2.02 Source Code 5.30.msi - the official component of the OPC Foundation, which cannot be installed normally in most systems, but the OPCDAAuto.dll component can be extracted from it using the msi extraction tool;
   * OPCDAAuto.dll - the official component of the OPC Foundation, is a COM component that provides OPCDA service access specifically for the .NET platform;

2. Check if the component is installed

   * If it is a 32-bit operating system, enter the C:\Windows\System32 directory, if it is a 64-bit operating system, enter the C:\Windows\SysWOW64 directory, and check whether the following files exist:

   ![](assets-opcda/core-components.png)

   ::: tip

   If the file does not exist, install the OPC Core Components Redistributable component of the corresponding platform, and if it exists, do not install it.

   :::

   * Open "Windows Task Manager" to check whether the OpcEnum system service is running, as shown in the figure:

   ![](assets-opcda/opcenum.png)

   ::: tip

   If it works normally, it means that OPC Core Components Redistributable has been installed normally.

   :::

   * Copy the OPCDAAuto.dll file to the system directory. If it is a 32-bit operating system, copy it to the C:\Windows\System32 directory. If it is a 64-bit operating system, copy it to the C:\Windows\SysWOW64 directory. After the copy is completed, use Open powershell with administrator privileges and enter the following command:

   ```powershell
   cd C:/Windows/System32 # x86 System
   cd C:/Windows/SysWOW64 # x64 System
   ./regsvr32 OPCDAAuto.dll
   ```

   ::: tip

   After success, as shown in the figure below:

   :::

   ![](assets-opcda/regist.png)

3. Install the MatrikonOPCSimulation simulator program on this machine;

4. Run the neuopc.exe program, select DA Host and DA Server and click Connect, set the parameters of UA and click Run, the operation is successful, as shown in the figure:

   ![](assets-opcda/local-neuopc.png)

## Remote host OPCDA server access

In this example, the host set above is used as a client to connect to another host in the LAN to realize cross-host OPCDA data reading and conversion. The remote host uses the Windows 10 x64 operating system for demonstration.

### Remote host DCOM settings

Install MatrikonOPC Server for Simulation on the remote host, and close the firewall of the computer. The demo uses the Administrator account.

1. Press the WIN + R keys and enter dcomcnfg in the pop-up dialog box to confirm and enter the component service, as shown in the figure:

   ![](assets-opcda/comcnf.png)

2. First set the overall properties of the machine, expand "Component Services\Computers\My Computer", right-click My Computer to open the Properties setting in the menu:

   ![](assets-opcda/comcnf1.png)

   Check "Enable Distributed COM on this computer" in "Default Properties", and set "Default Authentication Level" to "None":

   ![](assets-opcda/comcnf2.png)

   In "Default Protocols" keep only "Connection-oriented TCP/IP":

   ![](assets-opcda/comcnf3.png)

   In "COM Security", add "Everyone", "Administrators", and "ANONYMOUS LOGON" users to "Edit Limits" and "Edit Default Limits" in "Access Permissions" and "Launch and Activation Permissions" respectively, and set them Check all permissions below:

   ![](assets-opcda/comcnf4.png)

3. Expand "Component Services\Computers\My Computer\DCOM Config", set the properties of "OpcEnum" and "MatrikonOPC Server for Simulation and Testing" respectively, and select "None" in "General"-"Authentication Level":

   ![](assets-opcda/comcnf5.png)

   在"Location"中勾选"Run application on the computer where the data is located"和"Run application on this computer"：

   ![](assets-opcda/comcnf6.png)

   In "Security", select Custom for all permissions and add users "Everyone", "Administrators", and "ANONYMOUS LOGON" respectively, and check all permissions under them:

   ![](assets-opcda/comcnf7.png)

4. Make sure to close the system firewall or add a security policy to allow programs such as OpcEnum and Matrikon to pass through.

So far, the remote host test environment of OPCDA has been set up.

### Localhost DCOM Settings

In order to remotely access the set remote host, it is also necessary to perform DCOM settings on the local host. Here, continue to use the windows 7 SP1 32-bit system demo configured in [Local OPCDA Server Access] above, except for the configuration content "MatrikonOPC Server for Simulation and Testing ", consistent with the remote host, close the firewall of the local host before starting.

1. First set the overall properties of the machine, expand "Component Services\Computers\My Computer", right-click My Computer to open the Properties setting in the menu, the content and method of setting are consistent with the remote host:

   ![](assets-opcda/client-cfg1.png)

   ![](assets-opcda/client-cfg2.png)

   ![](assets-opcda/client-cfg3.png)

2. Expand "Component Services\Computers\My Computer\DCOM Config", set "OpcEnum", the content and method of setting are consistent with the remote host:

   ![](assets-opcda/client-cfg4.png)

   ![](assets-opcda/client-cfg5.png)

   ![](assets-opcda/client-cfg6.png)

3. Make sure to close the system firewall or add a security policy to allow the OpcEnum program to pass.

So far, the local host test environment of OPCDA has been set up.

![](assets-opcda/client-worked.png)

