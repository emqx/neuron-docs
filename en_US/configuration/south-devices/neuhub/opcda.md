# OPCDA

Neuron can use the Neuron HUB driver and NEURON HUB Windows program to indirectly access OPC DA servers running on Windows systems. For remote system configuration, refer to [NeuOPC Remote Access](../opc-da/remote.md).

## NEURON HUB Windows Program Parameters

| Parameter | Description                                                                                                                               |
| --------- | ----------------------------------------------------------------------------------------------------------------------------------------- |
| Node Name | Node name, must be unique to distinguish multiple nodes                                                                                   |
| Host      | Target host identifier (IP or hostname)                                                                                                   |
| UserName  | user name                                                                                                                                 |
| PassWrod  | password                                                                                                                                  |
| Domain    | domain                                                                                                                                    |
| Server    | DA server name (e.g., `opcda://192.168.10.133/Matrikon.OPC.Simulation`). After filling in Host, click the dropdown to fetch server lists. |

## Supported Data Types

* uint8  
* int8  
* uint16  
* int16  
* uint32  
* int32  
* uint64  
* int64  
* float  
* double  
* bool  
* string  
* ARRAY_INT8     
* ARRAY_UINT8    
* ARRAY_INT16    
* ARRAY_UINT16    
* ARRAY_INT32     
* ARRAY_UINT32   
* ARRAY_INT64     
* ARRAY_UINT64   
* ARRAY_FLOAT       
* ARRAY_DOUBLE    
* ARRAY_BOOL       
* ARRAY_STRING    

## Address Format
When selecting the OPCDA node type in the Neuron HUB driver, the address format matches OPCDA. Alternatively, use the `Export` function to export all point information as a table and import it directly into NEURON.