# 点位配置

## 乘系数用法

设备值 * 乘系数 = 显示值

在点位配置乘系数时，写属性支持乘系数的写入，例如。

![tag_decimal](./assets/tag_decimal.png)

点位乘系数值为 0.1，在页面写入显示值，例如 23.4，则页面显示值为 23.4，写入到设备中的值则为 234，如下图所示。

![write_value](./assets/write_value.png)

![monitor_decimal](./assets/monitor_decimal.png)

* tag1 为配置乘系数 0.1 的显示值；
* tag2 为未配置乘系数的显示值（即设备值）；

:::tip
若配置的乘系数为 0.1，输入值超过一位小数，则自动取舍。例如，输入 23.56，则显示 23.6，写入设备值为 236。
:::