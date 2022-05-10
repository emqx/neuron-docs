# Quick Start

## Environment setup

### Package Installation Neuron

The environment used in this example is Ubuntu 20.04.3, armv71.

Neuron packages can be downloaded from the Neuron website [https://neugates.io/zh/downloads](https://neugates.io/zh/downloads)

Unzip the package into any directory (e.g. /home/Neuron) and enter the command：

```bash
sudo dpkg -i neuron-2.0.0-beta.2-linux-armhf.deb
```

*Note*  After successful installation of the deb package, Neuron is automatically started.

#### Checking Neuron Status

```bash
systemctl status neuron
```

#### Stop Neuron

```bash
systemctl stop neuron
```

#### Restart Neuron

```bash
systemctl restart neuron
```

### Running EMQX Edge in Docker

We need to deploy an MQTT Broker to do the connection processing of messages, here we recommend using [EMQX Edge](https://www.emqx.cn/downloads#edge), a lightweight messaging middleware for edge computing. Again EMQX Edge can be installed and used quickly using a Docker container.

Get the Docker image (Please get the latest version from the [official website](https://hub.docker.com)).

```bash
docker pull emqx/emqx-edge:4.2.2
```

Start the Docker container

```bash
docker run -d --name emqx -p 1883:1883 -p 18083:18083 emqx/emqx-edge:4.2.2
```

### Resource Preparation

Install PeakHMI Slave Simulator, download the software from the [official website](https://hmisys.com).
After installation, open the Modbus TCP slave.

*Node* Try to disable the firewall on Windows, otherwise the Neuron may not be able to connect to the simulator.

## Operation and use

When the environment and resources are ready, open a web browser and enter the gateway address and port number where you are running Neuron to get to the administration console page, the default port number is 7000, e.g [http://127.0.0.1:7000](http://127.0.0.1:7000)。

### 1.Login

The page opens to the login screen, where users can log in using their initial username and password (initial username: admin, initial password: 0000) as shown below.

![login](./assets/login.png)

### 2.License

Neuron cannot read/write/upload data without a license uploaded or when the license has expired, please apply for a valid license in the interface first, as shown below.

*Note* In the commercial version, there is a default license that expires on 22/07/2022, after this date, please apply for a new license and update it in the interface.

1. In the top right hand corner of the page, select License from the `About` drop down box.

2. Enter the License screen, which displays the default license information. After the license has expired, you will need to reapply, we offer both free trial and official use, after receiving the license file, click on the `Reupload` button to upload the license as shown below.

![license](./assets/license.png)

### 3.South Configuration

1. Add south devices：

* Select `Southbound Device Management` in the `Configuration` menu to go to the Southbound Device Management interface, no devices have been added at this point.
* Click on the `Add Device` button to add a device manually, fill in the device name and drop down to select the plug-in, in this case we create a Modbus TCP device connection and select modbus-tcp-plugin for the plug-in, as shown in the figure below.

![add-south-device](./assets/south-devices-add.png)
2. Successful creation of a south device：
After successful creation of the device, a card of the just created device will appear in the southbound device management interface, at this time the device's working state is in the initialisation state and the connection state is in the disconnection state, as shown in the figure below.

![south-device](./assets/south-devices.png)
3. Device Configuration.
In the newly created device card select `Device Configuration` to configure the device as shown below, the fields with " * " are mandatory and each of them is followed by a field description key, mouse over it will display detailed description information. In this case we are using a Modbus TCP emulator, the Host field should be filled in with the IP address of the emulator that is running, and the Port with the corresponding port number.
Note: The Neuron and the simulator must be running on the same network segment.

![south-setting](./assets/south-setting.png)
4. Complete the configuration:
After the configuration is completed, if the information filled in is correct, the working status of the device will be set to running and the connection status will change to **Connected** and the device will enter the working state as shown in the figure below, or the user can stop the device by pressing the switch button.
5. To set up Groups：
Once you have done so, you can enter the Group configuration by tapping on any blank space on the device card to enter the list of Groups for that device, click on the `Create` button to create a Group, fill in the Group name and the time interval for reporting data, as shown in the figure below.

![add-group](./assets/group-create.png)

Once the Group has been created, the new Group will be displayed in the corresponding Group list, as shown in the figure below. The user can also click on the Edit button at this point to view the configuration of the Group that has just been created.

![group-list](./assets/group-list.png)
6. To set up tags：
Next click on the tags list button to enter the tags list interface, as shown below. At this point we can either create tags manually by selecting the `Create` button, or import tags in bulk by clicking on the `Import` button using Excel.

![tag-list-null](./assets/tag-add.png)

Click on the `Create` button to go to the Create Tags page and fill in the Tag information accordingly. On the Create Tags page, click the `Add` button to create a new Tag, thus enabling you to create multiple Tags at the same time, as shown in the image below.

Once created, as shown below, the Tag can be edited/deleted at this point.

![tag-list](./assets/tag-list.png)

此时南向配置已全部完成，用户可在`监控`菜单下选择`数据监控`，下拉框选择想要查看的南向设备及 Group，页面将会对应显示监测到的数据，如下图所示。对照模拟器，可以看到监控到的数据与模拟器的数值一致，如下图所示。

![data-monitoring](./assets/data-monitoring.png)

At this point the southbound configuration is complete, the user can select "Data Monitoring" under the `Monitoring' menu, the drop down box to select the southbound device and Group you want to view, the page will display the corresponding monitored data, as shown in the figure below. The monitored data will be displayed on the page, as shown below.

![write](./assets/write.png)

### 4.North Configuration

1. Add a northbound application：
Select `Northbound Application Management` in the `Configuration` menu to enter the northbound application management interface. When you first open this interface, there are no applications, so you need to add applications manually at this time, click the `Add Configuration` button in the top right corner, fill in the application name and select the application plug-in, as shown in the figure below.
![add-north](./assets/north-app-add.png)

After adding, the page will automatically jump back to the northbound application management interface. At this time, the working status of the added application is initialized and the connection status is disconnected, next click on the `Application Configuration` button to enter the application configuration interface, fill in the relevant information according to the interface to complete the application configuration, as shown below.

![north-setting](./assets/north-setting.png)

At this point, the working status of the application turns to ready, open the working button of the application to bring the device into the working status. If the application is configured correctly, the connection status should turn to connected, as shown in the figure below, and the user can also stop the application manually.

![north-app](./assets/north-app.png)
2. Subscribe to the Group：
Next, click on any blank space on the application card to enter the Subscribe to Group screen, click on the `Add Subscription' button in the top right corner to add a subscription, and select the Southbound device and the Group you want to subscribe to from the drop-down box, as shown in the image below.

![add-subscriptions](./assets/subscription-add.png)

Once the subscription is complete, we can use the MQTT client (MQTTX is recommended here) to connect to the EMQX Edge we have just deployed to view the reported data. Open MQTTX to add a new connection and fill in the correct name and Port of the EMQX Edge you have just deployed to complete the connection. Next, add a new subscription, the topic format of the Topic is `neuron/{mqtt_clientid}/upload`, where {mqtt_clientid} is the `Client-id` configured in the Neuron interface in the Northbound application. After a successful subscription, you can see that MQTTX can receive data directly from Neuron, as shown below (see the MQTT-Topics documentation for detailed subscription topics).

![mqttx](./assets/mqttx.png)
