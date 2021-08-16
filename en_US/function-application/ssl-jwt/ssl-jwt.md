# SSL and JWT Settings

Neuron provides SSL authentication for https login. Go to neuron.ini in the bin directory in the Neuron installation package to configure SSL, as shown in the following figure：

![commands](./assets/commands.png)

![ssl](./assets/ssl.png)

ENABLE_SSL set to`true`，SSL_CERT_FILEPATH fill in the certificate file path，SSL_PRIVATE_KEY_FILEPATH fill in the path of the private key file。The result is shown in the following figure：

![https](./assets/https.png)
