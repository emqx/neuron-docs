# Operations Guide

This chapter primarily covers some operations related to the maintenance of Neuron, including logging in, changing passwords, managing logs, viewing licenses, and system information, etc.

## Login

Open a Web browser and enter the address and port number of the gateway running Neuron to enter the management console dashboard. The default port number is 7000.

Access format, http://x.x.x.x:7000 x.x.x.x represents the address of the gateway where Neuron is installed.

After the page opens, enter the login interface, and users can log in with their initial user name and password (initial user name: admin, initial password: 0000).

:::tip
If the page cannot be opened, execute the following command at the terminal to detect:

* Use the ping command to test whether the network can be connected;
* Use the telnet command to test whether port 7000 can be accessed;
* Execute the following command to check the process status of Neuron.

```
$ systemctl status neuron
```
:::

## Change Password

Select the function of **Change Password** in **Administration** to change the login password, as shown in the figure below.

![change_password](./assets/change_password.png)

If the user forgets the changed password, the user can reset the password by executing the command.

```shell
./neuron --reset-password
```

## System Usage

After logging into Neuron, click on **System Information** -> **About** in the toolbar at the top of the page. Here, you can view information about the system version, status, runtime, content usage, hardware flags, and the date the project was built, as shown in the figure below.

![image-20230802172853368](./assets/usage.png)

## [Data Monitoring and Device Control](../monitoring.md)

This section discusses how to monitor data and control devices through Neuron. It details how to access and understand the data monitoring interface, as well as how to modify and validate changes in device values directly from the Neuron dashboard.

## [Data Statistics](../dashboard/data-statistics.md)

Neuron supports south-north node data statistics based on the Prometheus data model, which is used to monitor node running status. 

## [Log Management](./log-management.md)

Starting with Neuron version 2.3, we have introduced a function to download all log files with a single click. Users can download Neuron-related logs from the Neuron Web page with one click. 
