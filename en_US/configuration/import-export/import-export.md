# Batch Data Group/Tag Configuration

Neuron offers a feature that allows batch import and export of data label configuration information in Excel format. This function accelerates the data label configuration process and conveniently enables the export of created data label information to external storage.

## Import Data Tags

### Download Template

Select **South Devices -> Group List**. Hover the mouse over **Import** and the button **Download Template** will appear.

Click the **Download Template** button to download the Excel sheet.

### Configure the Template

Fill in the relevant information according to the Excel sheet format, as shown below.

![excel](./assets/excel.png)

The following items must be filled out accordingly:

* **group**: Fill in the Group name, when the name of the entered group does not exist, a new group will be created automatically with the name of this group;
* **name**: Fill in the Tag name;
* **address**: Fill in the address of the Tag;
* **attribute**: Select the attribute from the drop-down box;
* **type**: Select the data type from the drop-down box;
* **description**: Fill in the description, which can be left blank;
* **precision**: Optional, used to set the multiplier of the read value, can be empty;
* **decimal**: Optional, when the data type is float or double, it is used to set the precision.

### Import the Configured Template

Click on the **Import** button and select the Excel file to be imported.

## Export Data Tags

* Select the group to be exported, you can select all with one click;
* Click the **Export** button, and the information in the group, including the label information under the group, will be exported to an Excel table.
