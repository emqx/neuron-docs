# Bridging Data to AWS IoT using Neuron

This article will introduce how to use the Neuron to bridge data to AWS IoT through the public network so that you can easily build IoT applications.

## Introduction to AWS IoT

### What is AWS IoT

Amazon IoT Core is a hosted cloud platform that makes it easy for connected devices to securely interact with cloud applications and other devices. Amazon IoT can support billions of devices and trillions of messages and can process and securely route them to Amazon Cloud Technologies endpoint nodes and other devices. With Amazon IoT, your applications can track and communicate with all your devices at all times, even when they are not connected.

<figure align="center">
  <img src="./assets/aws-iot.png" style="border:thin solid #E0DCD9; width: 60%" alt="AWS IoT">
</figure>

### Benefits of the AWS IoT platform

1. Broad and deep: AWS has broad and deep IoT services from the edge to the cloud, providing local data collection and analysis capabilities as well as data management and rich analytics integration services on the cloud designed for IoT.
2. Multiple layers of security: including preventive security mechanisms (such as encryption and access control of device data), continuous monitoring and auditing of security configurations, etc.
3. Superior AI integration: AWS brings AI and IoT together to make devices smarter. Multiple machine learning frameworks are supported.
4. Proven at scale: AWS IoT is built on a scalable, secure, and proven cloud infrastructure that scales to billions of different devices and trillions of messages.

## Configure AWS IoT

### 1. Create policy

Find **Security -> Policy**, create a policy named neuron, and write the policy with the following configuration.
<figure align="center">
  <img src="./assets/aws_creat_policy.png" style="border:thin solid #E0DCD9; width: 60%" alt="AWS IoT create policy">
</figure>

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": "iot:Connect",
      "Resource": "arn:aws-cn:iot:cn-northwest-1:153045624426:client/neuron_*"
    },
    {
      "Effect": "Allow",
      "Action": "iot:Publish",
      "Resource": "arn:aws-cn:iot:cn-northwest-1:153045624426:topic//neuron/aws"
    },
    {
      "Effect": "Allow",
      "Action": "iot:Publish",
      "Resource": "arn:aws-cn:iot:cn-northwest-1:153045624426:topic//neuron/*/write/resp"
    },
    {
      "Effect": "Allow",
      "Action": "iot:Receive",
      "Resource": "arn:aws-cn:iot:cn-northwest-1:153045624426:topic//neuron/*/write/req"
    },
    {
      "Effect": "Allow",
      "Action": "iot:Subscribe",
      "Resource": "arn:aws-cn:iot:cn-northwest-1:153045624426:topicfilter//neuron/*/write/req"
    },
    {
      "Effect": "Allow",
      "Action": "iot:Publish",
      "Resource": "arn:aws-cn:iot:cn-northwest-1:153045624426:topic//neuron/*/read/resp"
    },
    {
      "Effect": "Allow",
      "Action": "iot:Receive",
      "Resource": "arn:aws-cn:iot:cn-northwest-1:153045624426:topic//neuron/*/read/req"
    },
    {
      "Effect": "Allow",
      "Action": "iot:Subscribe",
      "Resource": "arn:aws-cn:iot:cn-northwest-1:153045624426:topicfilter//neuron/*/read/req"
    }
  ]
}
```

### 2. Create a thing

Go to the AWS IoT control panel, find **Manage -> Things**, and click **Create things** to create a thing named _neuron_.
<figure align="center">
  <img src="./assets/aws_creat_thing.png" style="border:thin solid #E0DCD9; width: 60%" alt="AWS IoT create thing">
</figure>

Select **Auto-generate a new certificate**.
<figure align="center">
  <img src="./assets/aws_gen_cert.png" style="border:thin solid #E0DCD9; width: 60%" alt="AWS IoT generate certificate">
</figure>

After the certificate is created, you need to download the certificate on this page for device two-way authentication.
<figure align="center">
  <img src="./assets/aws_dowload_certs.png" style="border:thin solid #E0DCD9; width: 60%" alt="AWS IoT download certificate">
</figure>

Finally, associate the policy created earlier with the thing.
<figure align="center">
  <img src="./assets/aws_select_policy.png" style="border:thin solid #E0DCD9; width: 60%" alt="AWS IoT select policy">
</figure>

### 3. Lookup the device data endpoint

In the **Settings** tab, get the device data endpoint for device connection.
<figure align="center">
  <img src="./assets/aws_endpoint.png" style="border:thin solid #E0DCD9; width: 60%" alt="AWS IoT data endpoint">
</figure>


## Configure Neuron

### South device

We need some south devices to collect data from. Any Neuron southbound plugin will do for this tutorial, for example, the [Modbus TCP plugin].

#### Add the *modbus-tcp* Node

Click **South Devices -> Add Device** to add a node using the Modbus TCP plugin.
This tutorial will connect to a modbus simulator at port `60502`.
<figure align="center">
  <img src="./assets/neuron_create_driver.png" style="border:thin solid #E0DCD9; width: 60%" alt="Add modbus node in Neuron dashboard">
</figure>

#### Create a Group

Click the *modbus-tcp* node to create a group. We set the group name to *group* and the interval to *1000*.
<figure align="center">
  <img src="./assets/neuron_driver_group.png" style="border:thin solid #E0DCD9; width: 60%" alt="Add a group to the modbus node in Neuron dashboard">
</figure>

#### Add Tag

Click the created *group* group to create a tag with the name *tag0* and with type *INT16*.
<figure align="center">
  <img src="./assets/neuron_driver_tags.png" style="border:thin solid #E0DCD9; width: 60%" alt="Add a tag to the modbus node in Neuron dashboard">
</figure>

Finally, check that the *modbus-tcp* node is in **Connected** state.
<figure align="center">
  <img src="./assets/neuron_driver_list.png" style="border:thin solid #E0DCD9; width: 60%" alt="Neuron dashboard sourth devices tab showing modbus node connected">
</figure>

### North app

#### Add the *aws* Node

Click **North Apps -> Add Application** to add a node using the AWS IoT plugin.
<figure align="center">
  <img src="./assets/neuron_create_app.png" style="border:thin solid #E0DCD9; width: 60%" alt="Add aws node in Neuron dashboard">
</figure>

In the **Application Configuration** tab, configure the *aws* node with the AWS data endpoint and device certificates.
<figure align="center">
  <img src="./assets/neuron_app_conf.png" style="border:thin solid #E0DCD9; width: 60%" alt="Neuron dashboard north apps tab">
</figure>

Once the configuration is submitted, the *aws* node connects to AWS IoT Core successfully.
<figure align="center">
  <img src="./assets/neuron_app_list.png" style="border:thin solid #E0DCD9; width: 60%" alt="aws node connected state in Neuron dashboard">
</figure>

#### Subscribe to the *modbus-tcp* Node

Click the *aws* node, then click **Add subscription**, select the *modbus-tcp* node and the *group* group.
Set the data upload topic to */neuron/aws*, which is the MQTT topic to publish south device data.
<figure align="center">
  <img src="./assets/neuron_aws_sub.png" style="border:thin solid #E0DCD9; width: 60%" alt="aws node subscribe to modbus node">
</figure>

<figure align="center">
  <img src="./assets/neuron_aws_sub_list.png" style="border:thin solid #E0DCD9; width: 60%" alt="aws node subscribe list">
</figure>


## Monitor Data

After subscribing to the *group* group of the *modbus-tcp* node, the *aws* node will begin pushing data to the AWS IoT Core.
Click **Monitoring**, then select the *modbus-tcp* node and the *group* group. We see that Neuron reports a initial value *0* for *tag0*.

<figure align="center">
  <img src="./assets/neuron_monitor_1.png" style="border:thin solid #E0DCD9; width: 60%" alt="Neuron dashboard data monitoring tab">
</figure>

In the AWS IoT console, using **MQTT test client** to subscribe to the */neuron/aws* topic. We can check that AWS IoT Core receives the data correctly.
<figure align="center">
  <img src="./assets/aws_neuron_pub_1.png" style="border:thin solid #E0DCD9; width: 60%" alt="AWS IoT test client sub1">
</figure>

## Write Data

In the AWS IoT console, use the **MQTT test client** to send a write request to the topic */neuron/aws/write/req*, which writes value *42* to the tag *tag0*.
<figure align="center">
  <img src="./assets/aws_neuron_write.png" style="border:thin solid #E0DCD9; width: 60%" alt="AWS IoT test client write">
</figure>

Now we can see that Neuron updates *tag0* correctly in the **Data monitoring** tab.
<figure align="center">
  <img src="./assets/neuron_monitor_2.png" style="border:thin solid #E0DCD9; width: 60%" alt="Neuron dashboard data monitoring tab">
</figure>

And AWS IoT Core receives the correct tag data, *42*, which is expected.
<figure align="center">
  <img src="./assets/aws_neuron_pub_2.png" style="border:thin solid #E0DCD9; width: 60%" alt="AWS IoT test client sub2">
</figure>

[Modbus TCP plugin]: ../../south-devices/modbus-tcp/modbus-tcp.md
