# Connection Policy

On this page, you'll learn about client certificate and key configuration for connecting with the Neuron OPC UA module. This includes different login modes, certificate requirements, conversion and generation of certificates, and how to work with the crucial localhost.cnf file. 

## Client Login Mode

* Anonymous mode
  
    The anonymous login option must be enabled on the OPC UA server.

    The Neuron OPC UA module requires no username/password and certificate/key.

* Username/password mode

    The username and password that have access permission have been created on the OPC UA server.

    Neuron OPC UA module fills in the corresponding username/password without adding certificate/key.

* Certificate/key + anonymous mode

    OPC UA Enable appropriate security Settings on the server, add the client certificate to the trusted list, and enable anonymous login.

    Neuron OPC UA module adds the corresponding client certificate/key without filling in the username/password.

* Certificate/key + username/password mode

    On the OPC UA server, you have created a username and password with access permission, enabled appropriate security Settings, and added the client certificate to the trust list.

    Neuron OPC UA module adds the corresponding username/password and corresponding client certificate/key.

## Security Mode and Security Policy

When connecting to an OPC UA server using certificate-based authentication, you need to configure the **Security Mode** in Neuron and ensure the server has matching **Security Policies** enabled.

### Security Mode

The Security Mode determines whether OPC UA messages are cryptographically protected during transmission:

| Security Mode  | Description                                                                 |
| -------------- | --------------------------------------------------------------------------- |
| **None**       | No security applied. Messages are transmitted in plaintext.                 |
| **Sign**       | Messages are digitally signed to ensure integrity, but content is not encrypted. |
| **Sign&Encrypt** | Messages are both signed and encrypted, providing integrity and confidentiality. |

:::tip
**Sign&Encrypt** is recommended for production environments to prevent both tampering and eavesdropping. **Sign** may be used when encryption overhead is a concern and the network is already secured at the transport layer.
:::

### Security Policy

The Security Policy defines the specific cryptographic algorithms used for signing and encryption. When Neuron connects to a server with Security Mode set to **Sign** or **Sign&Encrypt**, the client and server negotiate a mutually supported Security Policy. The following policies are commonly supported:

| Security Policy           | Symmetric Encryption | Key Exchange     | Digital Signature | Status      |
| ------------------------- | -------------------- | ---------------- | ----------------- | ----------- |
| **Basic128Rsa15**         | AES-128              | RSA-15           | SHA-1             | Deprecated  |
| **Basic256**              | AES-256              | RSA-OAEP         | SHA-1             | Deprecated  |
| **Basic256Sha256**        | AES-256              | RSA-OAEP         | SHA-256           | Recommended |
| **Aes128_Sha256_RsaOaep** | AES-128              | RSA-OAEP         | SHA-256           | Recommended |

:::tip
- **Basic128Rsa15** and **Basic256** are deprecated in the OPC UA specification due to the use of SHA-1. Avoid using them in new deployments.
- **Basic256Sha256** and **Aes128_Sha256_RsaOaep** are recommended. **Basic256Sha256** provides the highest security strength with AES-256 encryption.
- The server must have at least one Security Policy enabled that matches the client's capabilities. If no common policy is found, the connection will fail.
:::

### How Security Mode and Security Policy Work Together

In Neuron, you only select the **Security Mode** (`None`/`Sign`/`Sign&Encrypt`). You do not choose a specific Security Policy — the selection is handled automatically by the OPC UA driver.

**Client-side initialization:** When Neuron starts the OPC UA connection, it registers all built-in Security Policies supported by the driver:
- None
- Basic128Rsa15
- Basic256
- Basic256Sha256
- Aes128Sha256RsaOaep
- Aes256Sha256RsaPss

The configured Security Mode (`Sign` or `Sign&Encrypt`) is then applied to the client configuration.

:::tip
If the Security Mode is set to `Sign` or `Sign&Encrypt` but no certificate and key are uploaded, Neuron uses its built-in default certificate and key.
:::

**Connection negotiation (first-match-wins):** When connecting to the server, the following steps occur:

1. Neuron retrieves the list of all endpoints supported by the server, including each endpoint's Security Mode and Security Policy.
2. The client iterates through the server's endpoints in the order returned by the server.
3. For each endpoint, two conditions are checked:
   - The endpoint's `securityMode` must match the Security Mode configured in Neuron.
   - The endpoint's `securityPolicyUri` must be in the client's supported policies list.
4. The **first endpoint that satisfies both conditions is selected** and used for the connection.

This means the server's endpoint ordering effectively determines the priority. For example, if a server returns endpoints in this order:

```
Endpoint 1: None,     policy=None              → mode mismatch (None ≠ Sign&Encrypt), skipped
Endpoint 2: Sign,     policy=Basic256Sha256    → mode mismatch (Sign ≠ Sign&Encrypt), skipped
Endpoint 3: Sign&Encrypt, policy=Aes256Sha256RsaPss → matched! selected
Endpoint 4: Sign&Encrypt, policy=Aes128Sha256RsaOaep → not reached
```

:::tip
- If you need a specific Security Policy to be used, configure the server to return that endpoint first in its `GetEndpoints` response.
- If no matching endpoint is found, the connection fails. Ensure at least one server endpoint has a Security Mode matching Neuron's configuration and a Security Policy supported by the driver.
:::

## Client Certificate Requirements

OPC UA Users can log in to the OPC UA server using a self-signed Certificate. The certificate and Key must meet the following conditions:

* CERTIFICATE and KEYFILE must be set together.

* The certificate must be generated in standard X.509v3.

* The SAN field in Certificate must contain `URI:urn:xxx.xxx.xxx`, `xxx` is the custom part.

* The Certificate file and Key file must be encoded in DER format.

:::tip
The certificate file can be imported into the target server in advance and set as trusted, or it can be automatically submitted after being set by Neuron and set as trusted by the server.
:::

## Client Certificate/Key Conversion

You can use the following steps and commands to convert the PEM certificate and private key to DER format:

1. Save all contents including `-----BEGIN CERTIFICATE-----` and `-----END CERTIFICATE-----` as 1.crt; 

2. Save all contents including `-----BEGIN PRIVATE KEY-----` and `-----END PRIVATE KEY-----` as 1.key; 

3. Run the following command:

   ```sh
   $ openssl x509 -in 1.crt -outform der -out cert.der   
   $ openssl rsa -inform PEM -in 1.key -outform DER -out key.der
   ```

## Generate a Client Certificate/Key

The generation mode on Windows, Linux, and Mac OS systems is the same.

```sh
$ openssl req -config localhost.cnf -new -nodes -x509 -sha256 -newkey rsa:2048 -keyout localhost.key -days 365 -subj "/C=DE/O=neuron/CN=NeuronClient@localhost" -out localhost.crt
$ openssl x509 -in localhost.crt -outform der -out client_cert.der
openssl rsa -inform PEM -in localhost.key -outform DER -out client_key.der
$ rm localhost.crt
$ rm localhost.key
```

`-days` can set the value as desired.

The *.cnf file specified by `-config` can be modified using the file attachment `localhost.cnf` in the next section and needs to contain the following configuration section:


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

## Server-Side Configuration

When Neuron uses **Sign** or **Sign&Encrypt** mode, the OPC UA server must be configured to:
1. Enable the required Security Policies.
2. Trust the client certificate uploaded to Neuron.

The following sections provide step-by-step examples for common OPC UA servers.

### General Configuration Principles

1. **Generate the client certificate** using OpenSSL and upload it to Neuron (refer to [Generate a Client Certificate/Key](#generate-a-client-certificatekey)).
2. **Enable security policies** on the target server — at minimum, enable **Basic256Sha256** or **Aes128_Sha256_RsaOaep**.
3. **Import the client certificate** (DER format) into the server's trusted client list.
4. **Restart the server** or reinitialize the OPC UA service to apply changes.

### Example: Siemens S7-1200 (TIA Portal)

Configure the S7-1200 built-in OPC UA server via TIA Portal:

1. Select the target PLC in TIA Portal, right-click and open **Properties -> General -> OPC UA -> Server**.
2. Under **Security -> Security policies available on the server**, check the required security policies:
   - Check **Basic256Sha256** (recommended) or other required policies.
3. In the **Trusted client** section, configure client certificate trust:
   - Enable **Automatically accept client certificates during runtime** (convenient for initial setup), or
   - Manually import the client certificate via the certificate manager.
4. Disable **Enable guest authentication** and enable **Enable username and password authentication** if using username/password login.
5. Compile and download the hardware configuration to the PLC.

For more details on S7-1200 configuration, refer to [Connect to Siemens S7-1200](./s71200.md).

### Example: KEPServerEX

Configure the OPC UA server in KEPServerEX:

1. Right-click on the KEPServerEX icon in the system tray, select **OPC UA Configuration -> Server Endpoints**.
2. Double-click on the endpoint entry (e.g., `opc.tcp://localhost:49320`).
3. In the **Security Policies** section, check the required policies:
   - Check **Basic256Sha256** (recommended).
4. Click **OK** to save the endpoint configuration.
5. After the client certificate is uploaded to Neuron, right-click the KEPServerEX icon and select **OPC UA Configuration -> Trusted Clients**.
6. Click **Import**, browse to the Neuron client certificate (DER format), and add it to the trusted list.
7. Right-click on the KEPServerEX icon and select **Reinitialize** to apply the changes.

For more details on KEPServerEX configuration, refer to [Connect to KEPServerEX](./kepserverex.md).

## Further Reaching: `localhost.cnf`

```sh
#
# OpenSSL example configuration file.
# This is mostly being used for generation of certificate requests.
#

# This definition stops the following lines choking if HOME isn't
# defined.
HOME			= .
RANDFILE		= $ENV::HOME/.rnd

# Extra OBJECT IDENTIFIER info:
#oid_file		= $ENV::HOME/.oid
oid_section		= new_oids

# To use this configuration file with the "-extfile" option of the
# "openssl x509" utility, name here the section containing the
# X.509v3 extensions to use:
# extensions		= 
# (Alternatively, use a configuration file that has only
# X.509v3 extensions in its main [= default] section.)

[ new_oids ]

# We can add new OIDs in here for use by 'ca', 'req' and 'ts'.
# Add a simple OID like this:
# testoid1=1.2.3.4
# Or use config file substitution like this:
# testoid2=${testoid1}.5.6

# Policies used by the TSA examples.
tsa_policy1 = 1.2.3.4.1
tsa_policy2 = 1.2.3.4.5.6
tsa_policy3 = 1.2.3.4.5.7

####################################################################
[ ca ]
default_ca	= CA_default		# The default ca section

####################################################################
[ CA_default ]

dir		= ./ca/			# Where everything is kept
certs		= $dir/certs		# Where the issued certs are kept
crl_dir		= $dir/crl		# Where the issued crl are kept
database	= $dir/database.txt	# database index file.
#unique_subject	= no			# Set to 'no' to allow creation of
					# several ctificates with same subject.
new_certs_dir	= $dir/newcerts		# default place for new certs.

certificate	= $dir/ca.crt	 	# The CA certificate
serial		= $dir/serial 		# The current serial number
crlnumber	= $dir/crlnumber	# the current crl number
					# must be commented out to leave a V1 CRL
crl		= $dir/crl.pem 		# The current CRL
private_key	= $dir/ca.key 		# The private key
RANDFILE	= $dir/.rand		# private random number file

x509_extensions	= usr_cert		# The extensions to add to the cert

# Comment out the following two lines for the "traditional"
# (and highly broken) format.
name_opt 	= ca_default		# Subject Name options
cert_opt 	= ca_default		# Certificate field options

# Extension copying option: use with caution.
# copy_extensions = copy

# Extensions to add to a CRL. Note: Netscape communicator chokes on V2 CRLs
# so this is commented out by default to leave a V1 CRL.
# crlnumber must also be commented out to leave a V1 CRL.
crl_extensions	= crl_ext

default_days	= 365			# how long to certify for
default_crl_days= 30			# how long before next CRL
default_md	= default		# use public key default MD
preserve	= no			# keep passed DN ordering

# A few difference way of specifying how similar the request should look
# For type CA, the listed attributes must be the same, and the optional
# and supplied fields are just that :-)
policy		= policy_match

# For the CA policy
[ policy_match ]
countryName		= match
stateOrProvinceName	= match
organizationName	= match
organizationalUnitName	= optional
commonName		= supplied
emailAddress		= optional

# For the 'anything' policy
# At this point in time, you must list all acceptable 'object'
# types.
[ policy_anything ]
countryName		= optional
stateOrProvinceName	= optional
localityName		= optional
organizationName	= optional
organizationalUnitName	= optional
commonName		= supplied
emailAddress		= optional

####################################################################
[ req ]
default_bits		= 2048
default_keyfile 	= privkey.pem
distinguished_name	= req_distinguished_name
attributes		= req_attributes
x509_extensions	= v3_ca	# The extensions to add to the self signed cert

# Passwords for private keys if not present they will be prompted for
# input_password = secret
# output_password = secret

# This sets a mask for permitted string types. There are several options. 
# default: PrintableString, T61String, BMPString.
# pkix	 : PrintableString, BMPString (PKIX recommendation before 2004)
# utf8only: only UTF8Strings (PKIX recommendation after 2004).
# nombstr : PrintableString, T61String (no BMPStrings or UTF8Strings).
# MASK:XXXX a literal mask value.
# WARNING: ancient versions of Netscape crash on BMPStrings or UTF8Strings.
string_mask = utf8only

req_extensions = v3_req # The extensions to add to a certificate request

[ req_distinguished_name ]
countryName			= Country Name (2 letter code)
countryName_default		= AU
countryName_min			= 2
countryName_max			= 2

stateOrProvinceName		= State or Province Name (full name)
stateOrProvinceName_default	= Some-State

localityName			= Locality Name (eg, city)

0.organizationName		= Organization Name (eg, company)
0.organizationName_default	= Internet Widgits Pty Ltd

# we can do this but it is not needed normally :-)
#1.organizationName		= Second Organization Name (eg, company)
#1.organizationName_default	= World Wide Web Pty Ltd

organizationalUnitName		= Organizational Unit Name (eg, section)
#organizationalUnitName_default	=

commonName			= Common Name (e.g. server FQDN or YOUR name)
commonName_max			= 64

emailAddress			= Email Address
emailAddress_max		= 64

# SET-ex3			= SET extension number 3

[ req_attributes ]
challengePassword		= A challenge password
challengePassword_min		= 4
challengePassword_max		= 20

unstructuredName		= An optional company name

[ usr_cert ]

# These extensions are added when 'ca' signs a request.

# This goes against PKIX guidelines but some CAs do it and some software
# requires this to avoid interpreting an end user certificate as a CA.

basicConstraints=CA:FALSE

# Here are some examples of the usage of nsCertType. If it is omitted
# the certificate can be used for anything *except* object signing.

# This is OK for an SSL server.
# nsCertType			= server

# For an object signing certificate this would be used.
# nsCertType = objsign

# For normal client use this is typical
# nsCertType = client, email

# and for everything including object signing:
# nsCertType = client, email, objsign

# This is typical in keyUsage for a client certificate.
# keyUsage = nonRepudiation, digitalSignature, keyEncipherment

# This will be displayed in Netscape's comment listbox.
nsComment			= "OpenSSL Generated Certificate"

# PKIX recommendations harmless if included in all certificates.
subjectKeyIdentifier=hash
authorityKeyIdentifier=keyid,issuer

# This stuff is for subjectAltName and issuerAltname.
# Import the email address.
# subjectAltName=email:copy
# An alternative to produce certificates that aren't
# deprecated according to PKIX.
# subjectAltName=email:move

# Copy subject details
# issuerAltName=issuer:copy

#nsCaRevocationUrl		= http://www.domain.dom/ca-crl.pem
#nsBaseUrl
#nsRevocationUrl
#nsRenewalUrl
#nsCaPolicyUrl
#nsSslServerName

# This is required for TSA certificates.
extendedKeyUsage = critical,timeStamping

[ v3_req ]

# Extensions to add to a certificate request

basicConstraints = CA:FALSE
keyUsage = nonRepudiation, digitalSignature, keyEncipherment
subjectAltName = @alt_names

[ alt_names ]
URI.1 = urn:neuron.client.application
DNS.1 = localhost
#DNS.2 = localhost
IP.1 = 127.0.0.1
#IP.2 = 0.0.0.0

[ v3_ca ]


# Extensions for a typical CA


# PKIX recommendation.

subjectKeyIdentifier=hash

authorityKeyIdentifier=keyid:always,issuer

# This is what PKIX recommends but some broken software chokes on critical
# extensions.
#basicConstraints = critical,CA:true
# So we do this instead.
basicConstraints = CA:false

# Key usage: this is typical for a CA certificate. However since it will
# prevent it being used as an test self-signed certificate it is best
# left out by default.
# keyUsage = cRLSign, keyCertSign

keyUsage = nonRepudiation, digitalSignature, keyEncipherment, dataEncipherment, keyCertSign
extendedKeyUsage = TLS Web Server Authentication, TLS Web Client Authentication

# Some might want this also
# nsCertType = sslCA, emailCA

# Include email address in subject alt name: another PKIX recommendation
# subjectAltName=email:copy
# Copy issuer details
# issuerAltName=issuer:copy

# DER hex encoding of an extension: beware experts only!
# obj=DER:02:03
# Where 'obj' is a standard or added object
# You can even override a supported extension:
# basicConstraints= critical, DER:30:03:01:01:FF

subjectAltName         = @alt_names

[ crl_ext ]

# CRL extensions.
# Only issuerAltName and authorityKeyIdentifier make any sense in a CRL.

# issuerAltName=issuer:copy
authorityKeyIdentifier=keyid:always

[ proxy_cert_ext ]
# These extensions should be added when creating a proxy certificate

# This goes against PKIX guidelines but some CAs do it and some software
# requires this to avoid interpreting an end user certificate as a CA.

basicConstraints=CA:FALSE

# Here are some examples of the usage of nsCertType. If it is omitted
# the certificate can be used for anything *except* object signing.

# This is OK for an SSL server.
# nsCertType			= server

# For an object signing certificate this would be used.
# nsCertType = objsign

# For normal client use this is typical
# nsCertType = client, email

# and for everything including object signing:
# nsCertType = client, email, objsign

# This is typical in keyUsage for a client certificate.
# keyUsage = nonRepudiation, digitalSignature, keyEncipherment

# This will be displayed in Netscape's comment listbox.
nsComment			= "OpenSSL Generated Certificate"

# PKIX recommendations harmless if included in all certificates.
subjectKeyIdentifier=hash
authorityKeyIdentifier=keyid,issuer

# This stuff is for subjectAltName and issuerAltname.
# Import the email address.
# subjectAltName=email:copy
# An alternative to produce certificates that aren't
# deprecated according to PKIX.
# subjectAltName=email:move

# Copy subject details
# issuerAltName=issuer:copy

#nsCaRevocationUrl		= http://www.domain.dom/ca-crl.pem
#nsBaseUrl
#nsRevocationUrl
#nsRenewalUrl
#nsCaPolicyUrl
#nsSslServerName

# This really needs to be in place for it to be a proxy certificate.
proxyCertInfo=critical,language:id-ppl-anyLanguage,pathlen:3,policy:foo

####################################################################
[ tsa ]

default_tsa = tsa_config1	# the default TSA section

[ tsa_config1 ]

# These are used by the TSA reply generation only.
dir		= ./demoCA		# TSA root directory
serial		= $dir/tsaserial	# The current serial number (mandatory)
crypto_device	= builtin		# OpenSSL engine to use for signing
signer_cert	= $dir/tsacert.pem 	# The TSA signing certificate
					# (optional)
certs		= $dir/cacert.pem	# Certificate chain to include in reply
					# (optional)
signer_key	= $dir/private/tsakey.pem # The TSA private key (optional)

default_policy	= tsa_policy1		# Policy if request did not specify it
					# (optional)
other_policies	= tsa_policy2, tsa_policy3	# acceptable policies (optional)
digests		= md5, sha1		# Acceptable message digests (mandatory)
accuracy	= secs:1, millisecs:500, microsecs:100	# (optional)
clock_precision_digits  = 0	# number of digits after dot. (optional)
ordering		= yes	# Is ordering defined for timestamps?
				# (optional, default: no)
tsa_name		= yes	# Must the TSA name be included in the reply?
				# (optional, default: no)
ess_cert_id_chain	= no	# Must the ESS cert id chain be included?
				# (optional, default: no)

```

