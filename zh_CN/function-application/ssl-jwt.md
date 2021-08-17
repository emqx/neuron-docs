# SSL和JWT的设置

Neuron提供SSL认证https的登录方式，在Neuron安装包中进入bin目录下的neuron.ini进行SSL的配置，如下图所示：

![commands](./assets/commands.png)

![ssl](./assets/ssl.png)

ENABLE_SSL设为`true`，SSL_CERT_FILEPATH填写证书文件路径，SSL_PRIVATE_KEY_FILEPATH填写私钥文件路径。结果如下图所示：

![https](./assets/https.png)
