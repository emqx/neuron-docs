# Configure Tag

## Tag Attribute

### Static Tag

When configuring the attribute at the tags, select `Static` in the drop-down box.

Static tags are assigned at configuration time, for example.

![tag_static](./assets/tag_static.png)

Data monitoring is shown in the following figure.

![monitor_static](./assets/monitor_static.png)

### Subscribe Tag

When configuring the attribute at the tags, select `Subscribe` in the drop-down box, for example.


![tag_subscribe](./assets/tag_subscribe.png)

Selecting the `subscribe` attribute means that a message will be sent when the data changes, but no message will be sent if there is no change. 
For example, The default data is 0, but it has been changed to 2.
In MQTTX, subscribe to the topic and view it. After the data changes, only one message will be sent, as shown in the following figure.

![mqttx_subscribe](./assets/mqttx_subscribe.png)