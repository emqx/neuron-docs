# 错误代码

本文档描述了 Neuron 在调用 http api 和 mqtt api 时会响应的错误码。

## api 请求错误代码

* 1000 通用错误

* 1001 内部错误

* 1002    请求 body 无效
* 1003    请求 param 无效
* 1004    缺少令牌
* 1005    解码令牌错误
* 1006    令牌过期
* 1007    验证令牌错误
* 1008    无效令牌
* 1009    用户名或密码错误
* 1010    程序繁忙

## 添加/删除/更新 node/tag/plugin/group 错误代码

* 2002    node 已存在
* 2003    node 不存在
* 2004    node 设置无效
* 2005    node 设置未找到
* 2006    node 未准备好
* 2007    node 正在运行
* 2008    node 未运行
* 2009    node 已停止
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

## license error codes

* 2400   license not found
* 2401   license invalid
* 2402   license expired
* 2403   license disabled
* 2404   license max nodes
* 2405   license max tags

## plugin common error codes

* 3000    plugin read failure
* 3001    plugin write failure
* 3002    plugin disconnected
* 3003    plugin tag not allow read
* 3004    plugin tag not allow write
* 3007    plugin tag type mismatch
* 3008    plugin tag expired
