# MTConnect

The Neuron MTConnect plugin accesses devices installed with MTConnect Agent through the HTTP protocol.

## Parameter Configuration

| Parameter | Description                      |
| --------- | -------------------------------- |
| host      | Target Device IP address         |
| port      | Target Device port, default 5000 |
| ns_prefix | namespace prefix                 |
| ns_uri    | namespace uri                    |



## Support Data Type

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

## MTConnect Agent 
For detailed information on the installation and usage of MTConnect Agent, please visit this link [cppagent](https://github.com/mtconnect/cppagent).

## ADDRESS
The plugin address is in the form of XML XPATH.

## Address Examples

| Address                                                                                                                            | Type   | Des                                     |
| ---------------------------------------------------------------------------------------------------------------------------------- | ------ | --------------------------------------- |
| //m:Angle[@dataItemId='Babs']                                                                                                      | float  | Absolute angle of rotation axis B       |
| //m:DeviceStream[@uuid='Mazak']/m:ComponentStream[@componentId='LYI1']/m:Samples/m:Position[@dataItemId='LYI1actm']                | double | Mechanical coordinates of linear axis Y |
| //m:DeviceStream[@uuid='Mazak']/m:ComponentStream[@componentId='Lct1']/m:Events/m:InputOutputSignal[@dataItemId='LPlcMonitorIO_1'] | bit    | IO signal                               |

