# Device Control

This rule implements +1 processing of the data collected by neuron from the device, and neuron writes the result back to the device. At this time, the tag attribute must be a write attribute, otherwise it cannot be written successfully.

## Step 1 Add a new rule

Click `New Rule` to enter the create rule interface.

## Step 2 Setup rule details

In the rule editing interface, fill in the rule information, as shown below.

![data-stream-rules-add-action-1](./assets/data-stream-rules-add-action-1.png)

* Fill in the `Rule ID` and `SQL` statement.
* Click on `Add` button to add sink action for the rule, you may add more than one sink action for each rule.
* Click on `Submit` button to complete the rule definition.

## Step 3 Setup sink details

Set sink details in the pop-up window for adding actions, as shown below.

![data-stream-rules-action-1](./assets/data-stream-rules-action-1.png)

* Drop down to select sink.
* Fill in the node name.
* Fill in the group name.
* Fill in the tag name.
* Click on `Submit` button to complete the sink action.

After the action is added, as shown below.

![data-stream-rules-1](./assets/data-stream-rules-1.png)

## Step 4 Start rule execution

Start the rules, as shown below.

![data-stream-rules-list-1](./assets/data-stream-rules-list-1.png)

## Step 5 Check over the data in Modbus simulator

Start neuron data monitoring, check data.
