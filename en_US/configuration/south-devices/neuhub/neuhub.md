# NEURON HUB

The Neuron HUB plugin accesses hosts running the NeuronHUB program via TCP protocol.

## Device Settings

| Field          | Description                        |
| -------------- | ---------------------------------- |
| host           | NeuronHUB IP address               |
| port           | NeuronHUB port (default: 17889)    |
| type           | Node type                          |
| node           | Node name                          |
| batch_size     | Command batch size (default: 50)   |
| expires        | Expiration time (default: 2000 ms) |
| sliding_window | Window size (default: 1)           |

Currently supported node types: OPCDA, SYNTEC CNC, and MITSUBISHI CNC.

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
The address format varies by node type. Refer to the corresponding device documentation for details.

## NeuronHUB Windows Program
Due to platform limitations of some protocols, an intermediate conversion program is required. The NeuronHUB program serves this purpose. Contact support to obtain the installation package.

### Installation
Double-click to install. It is recommended not to install on the system drive to avoid permission issues when modifying configuration files. The program starts automatically by default.

### Create a Node
Click the `File` menu and select the corresponding submenu item based on the device type to connect. Fill in the connection parameters on the interface and add the node.  
 ![file](./assets/file_menu.png)

### Node Operations
In the `Node Tables` interface, right-click a node to access context menu options for starting/stopping nodes, updating parameters, or deleting nodes. OPCDA nodes also support exporting points to NEURON node table files.  
 ![right](./assets/right_mouse_menu.png)

### Port Settings
The program listens on port 17889 by default. Change the port via `File->Port`.