# Apply for and install license

Neuron is an open source project. We encourage our community to develop their own pluggable modules.

Core framework, dashboard and a few plugin modules such as modbus-tcp, mqtt and eKuiper are open source under LGPLv3 license. Neuron may run with these open source modules without an EMQ license. But all other commercial plugin modules require an official EMQ license to run without limitation.

A trial EMQ license can be download from our [official website](https://www.emqx.com/en/apply-licenses/neuron). All available modules could be used with limitation on 100 connections and 1000 data tags for 15 days. If trial EMQ license is expired, you can apply the trial EMQ license via our official website again. However, a mailbox can only apply for a trial license up to two times.

Of course, you can also directly [contact us](https://www.emqx.com/en/contact?product=neuron) to obtain the official license.

## Step 1 Check the hardware token

Click **System Information -> About** to view the hardware logo and copy it.

## Step 2 Apply for license

Go to the [official website](https://www.emqx.com/en/apply-licenses/neuron) and fill in relevant information to apply for the license. The license will be sent to your mailbox.

## Step 3 Install license

To install a license, as shown below.

![license-null](./assets/license-null.png)

* Click `License` from the System Information drop-down box in the upper-right corner.
* Click `Upload` button to select the license file and then submit.

::: tip
When applying for a valid license, you need to fill in the hardware token.

The pluggable modules of the commercial version cannot be used when the license has not been uploaded or the license has expired.

Users can apply for a trial license from official website by clicking `Apply`, or contact our sales representatives to purchase a commercial license by clicking `Contact us`.
:::

## Step 4 Check over the license details

After the license is successfully installed, it will display the license information.

The license page details includes following items.

|Content|Description|
| :----------- | :----------------------------------- | 
| Effective data | Time when Neuron applied for License to take effect |
| Expire date | If the license has expired, the system would not work correctly anymore. Users must obtain a new valid license from official website, Re-upload the new license as procedure above |
| Limit on the maximum number of nodes | The maximum number of connection nodes that Neuron can create, a node can be either a southbound device or a northbound application |
| Limit on the maximum number of tags | The maximum number of total data tags that Neuron can create |
| Enabled Plugins | List of all the authorized pluggable modules for this license.Each commercial plugin module can be authorized independently in EMQ license |
