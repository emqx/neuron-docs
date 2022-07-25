# Prerequisite Setup

There is a pre-defined a data stream named `neuronStream` with type attribute `neuron` in data stream engine. This data stream is all collected data from various southbound drivers. All rules would share this data stream.

## Step 1 Check over the data stream processing application node

In the commercial version, there is a default `data-stream-processing` node card in the northbound application management interface, as shown below.

![data-stream-rules-adapter](./assets/data-stream-rules-adapter.png)

## Step 2 Subscribe to southbound tag groups

Click on any blank space of the `data-stream-processing` application node to enter the interface for subscribing to the group, as shown below.

![data-stream-rules-sub](./assets/data-stream-rules-sub.png)

* Click on the `Add subscription` button in the top right corner.
* Click on the drop down box to select the southbound device, in this case, we select the modbus-plus-tcp-1 device built above.
* Select the Group you want to subscribe to in the drop-down box, in this case, we select the group-1 created above.
* Click on `Submit` button to complete the subscription.
