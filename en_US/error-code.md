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

* 2101    group already subscribed
* 2102    group not subscribe
* 2103    group not allow
* 2104    group exist
* 2105    group parameter invalid
* 2106    group not exist
* 2017    group name too long

* 2201    tag not exist
* 2202    tag name conflict
* 2203    tag attribute not support
* 2204    tag type not support
* 2205    tag address format invalid
* 2206    tag name too long
* 2207    tag address too long
* 2208    tag description too long

* 2301    library not found
* 2302    library info invalid
* 2303    library name conflict
* 2304    library failed to open
* 2305    libraray module invalid
* 2306    library system not allow del

* 2400    license not found
* 2401    license invalid
* 2402    license expired
* 2403    plugin disabled by license
* 2404    reach licensed max number of nodes
* 2405    reach licensed max number of tags per node

## plugin common error codes

* 3000    plugin read failure
* 3001    plugin write failure
* 3002    plugin disconnected
* 3003    plugin tag not allow read
* 3004    plugin tag not allow write
* 3007    plugin tag type mismatch
* 3008    plugin tag expired
