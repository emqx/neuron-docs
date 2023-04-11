# Connection policy

## Client login mode

* Anonymous mode
    
    The anonymous login option must be enabled on the OPC UA server.

    The Neuron OPC UA module requires no user name/password and certificate/key.

* User name/password mode

    The user name and password that have access permission have been created on the OPC UA server.

    Neuron OPC UA module fills in corresponding user name/password without adding certificate/key.

* Certificate/key + anonymous mode

    OPC UA Enable appropriate security Settings on the server, add the client certificate to the trusted list, and enable anonymous login.

    Neuron OPC UA module adds corresponding client certificate/key without filling in user name/password.

* Certificate/key + user name/password mode

    On the OPC UA server, you have created a user name and password with the access permission, enabled appropriate security Settings, and added the client certificate to the trust list.

    Neuron OPC UA module adds corresponding user name/password and corresponding client certificate/key.

## Client certificate requirements

OPC UA Users can log in to the OPC UA server using a self-signed Certificate. The certificate and Key must meet the following conditions:

* CERTIFICATE and KEYFILE must be set together.

* Certificate must be generated in standard X.509v3.

* The SAN field in Certficate must contain `URI:urn:xxx.xxx.xxx`，`xxx` is the custom part.

* The Certificate file and Key file must be encoded in DER format.

:::tip
The certificate file can be imported into the target server in advance and set as trusted, or it can be automatically submitted after being set by Neuron and set as trusted by the server.
:::

## Client certificate/key conversion

You can use the following steps and commands to convert the PEM certificate and private key to DER format:

1. Save all contents including `-----BEGIN CERTIFICATE-----` and `-----END CERTIFICATE-----` as 1.crt; </br>

2. Save all contents including `-----BEGIN PRIVATE KEY-----` and `-----END PRIVATE KEY-----` as 1.key; </br>

3. Run the following command:

```sh
$ openssl x509 -in 1.crt -outform der -out cert.der   
$ openssl rsa -inform PEM -in 1.key -outform DER -out key.der
```

## Generate a client certificate/key

The generation mode on Windows, Linux, and Mac OS systems is the same.

```sh
$ openssl req -config localhost.cnf -new -nodes -x509 -sha256 -newkey rsa:2048 -keyout localhost.key -days 365 -subj "/C=DE/O=neuron/CN=NeuronClient@localhost" -out localhost.crt
$ openssl x509 -in localhost.crt -outform der -out client_cert.der
openssl rsa -inform PEM -in localhost.key -outform DER -out client_key.der
$ rm localhost.crt
$ rm localhost.key
```

`-days` can set the value as desired.

The *.cnf file specified by `-config` can be modified using the [template file for openssl](https://github.com/openssl/openssl/blob/master/apps/openssl.cnf) and needs to contain the following configuration sections:


```sh
[ v3_req ]

# Extensions to add to a certificate request

basicConstraints = CA:FALSE
keyUsage = nonRepudiation, digitalSignature, keyEncipherment
subjectAltName = @alt_names

[ alt_names ]
URI.1 = urn:xxx.xxx.xxx
DNS.1 = localhost
#DNS.2 = localhost
IP.1 = 127.0.0.1
#IP.2 = 0.0.0.0
```
