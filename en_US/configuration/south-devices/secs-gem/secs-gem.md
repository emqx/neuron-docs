# SECS GEM

The SECS GEM HSMS driver supports accessing devices that comply with the SEMI E37 HSMS standard through the TCP/IP protocol. Currently, it supports passive mode for devices and acts as the active host connection.

## Parameter Configuration

| Parameter | Description                      |
| --------- | -------------------------------- |
| host      | Target Device IP address         |
| port      | Target Device port, default 5000 |
| deviceid  | Target Device ID, default 0      |

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
* bytes

## ADDRESS

> SxFy([_1][_2][_3][_4])

## Streams and Functions

SECS-II messages are referred to as Streams and Functions. Each message has a Stream value 
(Sx) and a Function value (Fy). In the case of a Stream 1 Function 1, it is written as S1F1, and 
spoken as “S1F1”. Streams are categories of messages while Functions are specific messages 
within the category. The function value is always an odd number in a primary message, and one 
greater, or even, in the associated secondary reply.

| Stream | Description                    |
| ------ | ------------------------------ |
| 1      | Equipment Status               |
| 2      | Equipment Control              |
| 3      | Material Status                |
| 4      | Material Control               |
| 5      | Alarm Handling                 |
| 6      | Data Collection                |
| 7      | Recipe Management              |
| 8      | Control Program Transfer       |
| 9      | System Errors                  |
| 10     | Terminal Services              |
| 11     | (Not Used)                     |
| 12     | Wafer Mapping                  |
| 13     | Unformatted Data Set Transfers |


**Some SxFy**

| Stream Function | Description                             |
| --------------- | --------------------------------------- |
| S1F1            | Are You There Request (R)               |
| S1F2            | On Line Data (D)                        |
| S1F3            | Selected Equipment Status Request (SSR) |
| S1F4            | Selected Equipment Status Data (SSD)    |
| S6F7            | Data Transfer Request (DDR)             |
| S6F8            | Data Transfer Data (DDD)                |
| S6F15           | Event Report Request (ERR)              |
| S6F16           | Event Report Data (ERD)                 |


## Special Type Processing

The SECS-II message definition defines the LIST type, which is also supported by the plugin through the string type. However, there is a deserialization process involved, with specific rules as follows.

| SECS-II Type | deserialization | Description                                                                                                    |
| ------------ | --------------- | -------------------------------------------------------------------------------------------------------------- |
| LIST         | `<L[n] xxx>(.)` | n is the length of the LIST, and when the LIST is empty  set n to  0. The outermost LIST includes . at the end |
| ASCII        | `<A[n] xxx>`    | n is the length of the ASCII, and when the ASCII is empty  set n to  0.                                        |
| Binary       | `<B[n] xxx>`    | n is the length of the Binary, and when the Binary is empty  set n to  0.                                      |
| Boolean      | `<Boolean x>`   |                                                                                                                |
| UINT8        | `<U1 x>`        |                                                                                                                |
| UINT16       | `<U2 x>`        |                                                                                                                |
| UINT32       | `<U4 x>`        |                                                                                                                |
| UINT64       | `<U8 x>`        |                                                                                                                |
| INT8         | `<I1 x>`        |                                                                                                                |
| INT16        | `<I2 x>`        |                                                                                                                |
| INT32        | `<I4 x>`        |                                                                                                                |
| INT64        | `<I8 x>`        |                                                                                                                |
| 32FLOAT      | `<F4 x>`        |                                                                                                                |
| 64FLOAT      | `<F8 x>`        |                                                                                                                |

The LIST type supports accessing specific elements using indices, and currently supports nesting of up to four layers of LISTs.

## Q&A
* How to fill in the Device ID?
The Device ID can usually be viewed on the SECS GEM HSMS protocol configuration page of the device.

* How to serialize ASCII type in LIST?
This plugin serializes ASCII in LIST as `<A[n] xxx>`, without quotes for the content. For example, "ABC" is serialized as `<A[3] ABC>`, not `<A[3] "ABC">`.

* How to serialize Binary type in LIST?
This plugin serializes Binary in LIST as `<B[n] xx>`, without quotes for the content. For example, 0xFF is serialized as `<B[1] FF>`, not `<B[2] "FF">`.

* What type should be selected when creating a new point for data of LIST type?
For points with device data type **LIST**, select **string** type when creating a new point.

* How to create a new point for events actively reported by the device, such as "S6F11"?
For points actively reported by the device, such as "S6F11", simply create the corresponding point.

* How to create a new point for obtaining data that requires passing parameters?
For example, "S1F3" requires passing a **LIST** type parameter, and its return value will be returned through "S1F4", which also has **LIST** type. For this point, we need to create two points, with one having address "S1F3" and property configuration **Write**, and type **string**. The other has address "S1F4" and property configuration **Read** or **Sub**, and type **string**. Use the first point to write the parameter, and the second point to obtain the return value.

* How to create a new point for obtaining data without passing parameters?
For example, "S1F1" does not require passing parameters. Simply create one point, and its return value will be displayed directly on this point.