# JWT

When calling APIs in Neuron, you need to first call the login API to generate a JWT, and then call other APIs for JWT verification. The default expiration time of the generated JWT is one hour, and you can generate a JWT with a custom expiration time.

## What is JWT？

JWT is an open standard (RFC 7519) for securely transmitting information. The JWT structure consists of three parts: the header, payload and signature.

Neuron first searches for the corresponding .pem or .pub file under the `/neuron/certs` directory based on the **iss** field and then verifies it based on the fields inside. The required JWT structure for Neuron is as follows:

```json
header
{
    "alg": "RS256",
    "typ": "JWT"
}

payload
{
    "iss": "username",
    "iat": "1679622798",
    "exp": "1679626398",
    "aud": "neuron",
    "bodyEncode": "0"
}
```

### Header

* typ: Using JWT
* alg: Using RS256


### Payload

* iss: Defined it according to the requirements, but ensure that it is consistent with the filename of the generated public key file. For example, if the iss is "neuron", the public key filename generated should be `neuron.pem`.
* iat: Time of issuance.
* exp: Expiration time of issuance.
* aud: `neuron`, cannot be modified.

## How to generate JWT?

Use the public and private keys to sign a JWT, and put the public key in the `/neuron/certs` directory, and Neuron will decode it according to the public key.

Generate RSA keys using OpenSSL command-line tools:

```bash
# generate private key
$ openssl genrsa -out private.key 2048
# generate public key
$ openssl rsa -in private.key -out public.pem -pubout
```