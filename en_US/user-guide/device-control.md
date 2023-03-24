# Device control

## Step 1 Change the value from the dashboard

When the tag is set with the write attribute, the Tag of the data monitoring interface will have a write operation. Click on `Write` button and input a value to control device. For example, modify the value of the 1!40001 point address with the write attribute, as shown below.

![write](./assets/write.png)

* Click on the `write` button at the end of the label to be changed;
* Select whether to input in hexadecimal format, not select;
* Enter a new value for the label, e.g. 123;
* Click on the `Submit` button to submit the new value.

::: tip
This point in the device must also have the writable attribute, otherwise it cannot be written successfully.
:::

## Step 2 Check whether the device point value is modified successfully

Check over the Modbus simulator whether the point value has changed to the same input value as above.

![monitor](./assets/monitor.png)