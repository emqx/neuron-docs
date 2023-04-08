# Pluggable Modules Management

## Check Over All Available Modules

The plugin management page displays all the pluggable modules available and detailed information, including the name of the plug-in, associated node type, plug-in category, driver library name and description, as shown in the following figure.

![plugin-options](./assets/plugin-options.png)

Click the `Document` button in the upper right corner of the plugin card to jump to the documentation for the specific use and description of the driver.

The plug-in types include the following 3 modes:

* Static: cannot be deleted
* System: cannot be deleted, native
* Custom: Deletable, user-developed or custom-developed

:::tip
Users can filter out the plugins for northbound applications or southbound devices from the dropdown box.
:::

## Add A New Pluggable Module

Click on the `Add Plugin` button in the upper right corner as shown below

![plugin-add](./assets/plugin-add.png)

To add a new Pluggable module,

* Fill in the path and file name of the .so file that needs to be added.
* Click on the `Create` button to move .so file to the build directory.

:::tip
Please make sure that the plugin .so file you have written is placed under the neuron/build/plugins directory before adding it. For specific plugin development tutorials, please refer to [SDK Tutorial](../project/sdk/sdk_based-driver-development.md).
:::
