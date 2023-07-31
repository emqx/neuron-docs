# Configure with Templates

In practice, Neuron users often need to create large numbers of nodes having similar configurations. This can be a time-consuming and error-prone process, especially in large-scale deployments. To streamline this process, Neuron introduces the template feature in version **2.5.0**.

The Neuron template feature allows users to create a template with the desired plugin and configurations including groups and tags. Users could then use that template as a basis to create new nodes.

By using templates, users can quickly and easily create new nodes with similar configurations, saving time and effort.

::: tip
Neuron 2.5.0 template feature only supports southbound plugins.
:::

## Create Template

### Add Template

Click **Configuration -> Template -> Add Template** to open the **Add Template** dialog.

  ![Add template dialog](./assets/template_add_dialog.png)

Fill in the template name and select the desired plugin, then click the **Create** button. If everything is successful, you should see the created template in the **Template** tab.

  ![Add template result](./assets/template_list.png)

### Add Template Group

At this point, the created template is empty without any data. Click the created template to enter the **Group List** page.

  ![Add template group](./assets/template_add_group.png)

To add a group to the template, it is pretty much the same as that in [Configure Data Groups And Tags](../groups-tags/groups-tags). Here, we add a group named *grp* with an interval of *3000*.

  ![Template group list](./assets/template_group_list.png)

### Add Template Tag

Click the created *grp* group to enter the **Tag List** page.

  ![Add template tag](./assets/template_tag_list_1.png)

Click the **Create** button to enter the **Add Tags** page.

  ![Add template tag](./assets/template_add_tag.png)

To keep things simple, we just add two tags. Click the **Create** button to finally submit the tags as shown in the **Tag List** page.

  ![Template tag list](./assets/template_tag_list_2.png)


## Configure with Template

Click **Configuration -> South Devices -> Add Device** to open the **New Device** dialog.

  ![Template instantiation](./assets/template_add_device.png)

Fill in the south device name, then select **Template** mode and the template to instantiate from. Click the **Create** button to bring up the **Device configuration** page.

  ![Template device setting](./assets/template_device_setting.png)

Fill in the settings and click **Submit**. If no errors, a new south device should be listed in the **South Devices** tab.

  ![Template device](./assets/template_device_list.png)

Click the instantiated south device to enter the **Group List** page. Clearly, the instantiated south device has a group named *grp* with interval *3000*, which is the same as that of the selected template.

  ![Template device group](./assets/template_device_group.png)

Click the *grp* group to enter the **Tag List** page. Also not surprisingly, there are two tags, which are the same as that of the template.

  ![Template device tag](./assets/template_device_tag.png)


## Export/Import Templates

### Export Template

To export a template, just click the **Export icon** on the desired template and it will export the template data to a JSON file.

  ![Template export](./assets/template_export.png)

### Import template

To import a template, click **Import Template** in the **Template** tab and provide the JSON file to import data from.

  ![Template import](./assets/template_import_1.png)

In the **Import Template** dialog, users could alter the template name to avoid name conflicts. Click the **Create** button to finish the import.

  ![Template import](./assets/template_import_2.png)

Imported templates are shown as usual in the **Template** tab.

  ![Template import result](./assets/template_import_result.png)
