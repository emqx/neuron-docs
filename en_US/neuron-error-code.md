# Neuron 2.x ERROR CODE

This document mainly describes some errors that neuron will respond when calling http api and mqtt api.

## api request error codes

* 1001 internal error

* 1002    request body invalid
* 1003    request param invalid
* 1004    missing token
* 1005    decoding token error
* 1006    expired token
* 1007    validate token error
* 1008    invalid token
* 1009    user or password error

## add/del/update node/tag/plugin/group error codes

* 2001    node type invalid

* 2002    node exist
* 2003    node not exist
* 2004    node setting invalid
* 2005    node setting not found
* 2006    node not ready
* 2007    node is running
* 2008    node not running
* 2009    node is stopped

* 2101    group config not exist
* 2102    group config in use
* 2103    group config conflict

* 2201    tag not exist
* 2202    tag name conflict
* 2203    tag attribute not support
* 2204    tag type not support
* 2205    tag address format invalid

* 2301    library not found
* 2302    library info invalid
* 2303    library name conflict

## plugin common error codes

* 3000    plugin read failure
* 3001    plugin write failure
* 3002    plugin disconnected
* 3003    plugin tag not allow read
* 3004    plugin tag not allow write
* 3005    plugin tag not exist
* 3006    plugin group config not subscribe
