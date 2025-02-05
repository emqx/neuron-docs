# ERROR CODE

This document describes the errors that neuron will reply to sender when calling http api and mqtt api.

## api request error codes

* 1000 generic error

* 1001 internal error

* 1002    request body invalid
* 1003    request param invalid
* 1004    missing token
* 1005    decoding token error
* 1006    expired token
* 1007    validate token error
* 1008    invalid token
* 1009    user or password error
* 1010    is busy
* 1011    file not exist
* 1012    password length too short or too long
* 1013    duplicate password
* 1014    command execution failed
* 1015    invalid ip address
* 1016    ip address in use
* 1017    request body too large

## add/del/update node/tag/plugin/group error codes

* 2002    node exist
* 2003    node not exist
* 2004    node setting invalid
* 2005    node setting not found
* 2006    node not ready
* 2007    node is running
* 2008    node not running
* 2009    node is stopped
* 2010    node name too long
* 2011    node not allow delete
* 2012    node not allow subscribe
* 2013    node not allow update
* 2014    node not allow map
* 2015    node name is empty
* 2101    group already subscribed
* 2102    group not subscribe
* 2103    group not allow
* 2104    group exist
* 2105    group parameter invalid
* 2106    group not exist
* 2107    group name too long
* 2108    group exceeds the maximum number under the same node
* 2201    tag not exist
* 2202    tag name conflict
* 2203    tag attribute not support
* 2204    tag type not support
* 2205    tag address format invalid
* 2206    tag name too long
* 2207    tag address too long
* 2208    tag description too long
* 2209    tag precision invalid
* 2210    tag exist
* 2301    library not found
* 2302    library info invalid
* 2303    library name conflict
* 2304    library failed to open
* 2305    libraray module invalid
* 2306    system plugin cannot be deleted
* 2307    plugin not allow create instance
* 2308    plugin arch not support
* 2309    plugin in using
* 2310    plugin add faily
* 2311    plugin module already exit
* 2312    plugin module not exist
* 2313    plugin module kind no support
* 2314    plugin module version no match
* 2315    plugin name no conform
* 2316    plugin c lib no match
* 2317    plugin update failed
* 2400    license not found
* 2401    license invalid
* 2402    license expired
* 2403    plugin disabled by license
* 2404    reach licensed max number of nodes
* 2405    reach licensed max number of tags per node
* 2406    license hardware token not match
* 2407    license detect bad clock
* 2408    license module invalid
* ~~2500    template already exists (deprecated)~~
* ~~2501    template not found (deprecated)~~
* ~~2502    template name too long (deprecated)~~

## plugin common error codes

* 3000    plugin read failure
* 3001    plugin write failure
* 3002    plugin disconnected
* 3003    plugin tag not allow read
* 3004    plugin tag not allow write
* 3007    plugin tag type mismatch
* 3008    plugin tag value expired
* 3009    plugin protocol decode failure
* 3010    plugin not running
* 3011    plugin tag not ready
* 3012    plugin packet out of order
* 3013    plugin name too long
* 3014    plugin not found
* 3015    plugin device not response
* ~~3016    plugin does not support template (deprecated)~~
* 3017    plugin does not support write tags
* 3018    plugin does not support sync reading
* 3019    plugin does not support requested operation
* 3020    plugin tag value out of range or invalid
* 3021    plugin does not support scan tags
* 3022    plugin does not support test reading

## FILE error codes

* 4100  string too long
* 4101  file open failure
* 4102  file read failure
* 4103  file write failure

## OPCUA error codes

* 10001 opcua tag does not exist
* 10002 opcua connection configuration error
* 10003 opcua access timeout
* 10004 opcua tag is not readable
* 10005 opcua tag is not writable
* 10006 opcua tag is not supported
* 10007 opcua Error
* 10008 The value is bad but no specific reason is known
* 10009 There was nothing to do because the client passed a list of operations with no elements
* 10010 The request could not be processed because it specified too many operations
* 10011 User does not have permission to perform the requested operation
* 10012 The timestamps to return parameter is invalid
* 10013 Communication with the data source is defined, but not established, and there is no last known value available
* 10014 The syntax of the node id is not valid
* 10015 The node id refers to a node that does not exist in the server address space
* 10016 The attribute is not supported for the specified Node
* 10017 The syntax of the index range parameter is invalid
* 10018 No data exists within the range of indexes specified
* 10019 The data encoding is invalid
* 10020 The server does not support the requested data encoding for the node
* 10021 The access level does not allow reading or subscribing to the Node
* 10022 The access level does not allow writing to the Node
* 10023 The value was out of range
* 10024 The max age parameter is invalid
* 10025 The server does not support writing the combination of value, status and timestamps provided
* 10026 The value supplied for the attribute is not of the same type as the attribute's value
* 10027 The operation is not permitted over the current secure channel

## S7COMM error codes

* 10101  s7comm hardware error
* 10103  s7comm accessing the object not allowed
* 10105  s7comm invalid address
* 10106  s7comm data type not supported
* 10107  s7comm data type inconsistent
* 10110  s7comm object not exist
* 10150  s7comm cotp disconnected
* 10151  s7comm disconnected
* 10152  s7comm no value
* 10153  s7comm value too short

## KNX error codes

* 10200  knx no devices

## NONA11

* 10400 nona11 invalid address

## FINS error codes

* 10500    fins disconnected
* 10501    fins error
* 10502    fins local node error
* 10503    fins dest node error
* 10504    fins communication controller error
* 10505    fins not executable
* 10506    fins routing error
* 10507    fins command format error
* 10508    fins parameter error
* 10509    fins read not possible
* 10510    fins write not possible
* 10511    fins not executable in current mode
* 10512    fins no unit
* 10513    fins start/stop not possible
* 10514    fins unit error
* 10515    fins command error
* 10516    fins access error
* 10517    fins abort

## FOCAS error codes

* 10600 focas error
* 10601 focas program file not found
* 10602 focas program file transferring
* 10603 focas program file type not support
* 10604 focas program file name format error

## EtherNet/IP error codes

* 10701 - 10744 EtherNet/IP error
* 10797 EtherNet/IP no CIP connection
* 10798 EtherNet/IP data type mismatch
* 10799 EtherNet/IP no session

## Profinet IO error codes

* 10800 Profinet IO unidentified
* 10801 Profinet IO not connected
* 10802 Profinet IO not ready
* 10803 Profinet IO not param end
* 10804 Profinet IO not DWRITE
* 10805 Profinet IO wait HELLO
