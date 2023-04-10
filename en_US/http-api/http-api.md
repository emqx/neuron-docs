# Usage

This document introduces how to setup parameter and data tag point information in configuration for northbound applications and southbound drivers.

::: tip
uint16 corresponds to the word type. uint32 corresponds to dword type.
:::

## File

File plugin is used to read or write files.

### Parameter Setting

| Parameter   | Description                                           |
| ----------- | ----------------------------------------------------- |
| file_length | Set the character length for reading or writing file |

### Support Data Type

* STRING

### Address Format

> FILE PATH</span>

*Example:*

| Address                  | Data Type | Description              |
| ------------------------ | --------- | ----------------------------------------------- |
| /home/root/test/test.txt | string    | Read or write the contents of the test.txt file |

:::tip
The address needs to fill in the GetFullPath.

When writing, the written content will overwrite the previous file content.
:::
