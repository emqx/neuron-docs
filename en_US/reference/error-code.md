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

* 2101    group already subscribed
* 2102    group not subscribe
* 2103    group not allow
* 2104    group exist
* 2105    group parameter invalid
* 2106    group not exist
* 2107    group name too long

* 2201    tag not exist
* 2202    tag name conflict
* 2203    tag attribute not support
* 2204    tag type not support
* 2205    tag address format invalid
* 2206    tag name too long
* 2207    tag address too long
* 2208    tag description too long

* 2209    tag precision invalid

* 2301    library not found
* 2302    library info invalid
* 2303    library name conflict
* 2304    library failed to open
* 2305    libraray module invalid
* 2306    library system not allow del

* 2307    library not allow create instance

* 2400    license not found
* 2401    license invalid
* 2402    license expired
* 2403    plugin disabled by license
* 2404    reach licensed max number of nodes
* 2405    reach licensed max number of tags per node
* 2406    license hardware token not match
* 2407    license detect bad clock

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

## S7COMM error codes

* 10101  s7comm hardware error
* 10103  s7comm accessing the object not allowed
* 10105  s7comm invalid address
* 10106  s7comm data type not supported
* 10107  s7comm data type inconsistent
* 10110  s7comm object not exist
* 10150  s7comm cotp disconnected
* 10151  s7comm disconnected

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

## OPCUA error codes

* 10001 opcua tag does not exist
* 10002 opcua connection configuration error
* 10003 opcua access timeout
* 10004 opcua tag is not readable
* 10005 opcua tag is not writable
