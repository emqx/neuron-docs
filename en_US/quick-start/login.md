# Login Neuron

Open a Web browser and enter the address and port number of the gateway running Neuron to enter the management console dasboard. The default port number is 7000.

Access format, http://x.x.x.x:7000 x.x.x.x represents the address of the gateway where Neuron is installed.

After the page opens, enter the login interface, and users can log in with their initial user name and password (initial user name: admin, initial password: 0000).

:::tip
If the page cannot be opened, execute the following command at the terminal to detect:

* Use the ping command to test whether the network can be connected;
* Use the telnet command to test whether port 7000 can be accessed;
* Execute the following command to check the process status of neuron.

```
$ systemctl status neuron
```
:::