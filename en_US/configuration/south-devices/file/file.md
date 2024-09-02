# File Storage

## Module Description

File plugin is used to read or write files.

## Parameter Configuration

| Parameter   | Description                                           |
| ----------- | ----------------------------------------------------- |
| file_length | Set the character length for reading or writing file |

## Support Data Type

* STRING

## Usage of Address Format

### Address Format

> FILE PATH

### Address Example

| Address                  | Data Type | Description              |
| ------------------------ | --------- | ----------------------------------------------- |
| /home/root/test/test.txt | string    | Read or write the contents of the test.txt file |

:::tip
The address needs to fill in the GetFullPath.

When writing, the written content will overwrite the previous file content.
:::
