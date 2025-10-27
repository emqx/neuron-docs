# OPC UA Server

OPC UA (OPC Unified Architecture) is a platform-independent, vendor-neutral industrial communication standard designed for reliable and secure data exchange in automation systems. OPC UA supports data modeling, events, historical data access, and method invocation, making it suitable for distributed scenarios from edge devices to the cloud.

Neuron supports using OPC UA Server as a northbound application, allowing southbound device data to be exposed to upper-level systems or third-party clients via OPC UA services. Through the OPC UA Server, external systems can subscribe to data changes, read real-time points, and send control commands.

## Add Application

In **Data Collection -> North Apps**, click **Add Application** and select **OPC UA Server** to create an OPC UA Server node.

## Application Configuration

When creating an OPC UA Server application, you can configure the following parameters:

| Parameter                                | Description                                                                                                                   |
| ---------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------- |
| **Host**                                 | The computer running the OPC UA server, default is 127.0.0.1.                                                                 |
| **Port**                                 | The port the server binds to, default is 4840.                                                                                |
| **Security Policy**                      | Supported security policies, including None, Basic256Sha256, Basic256, Basic256Rsa15, Aes128_Sha256_RsaOaep. Default is None. |
| **Username and Password Authentication** | Enable username and password authentication, supports adding users, updating passwords, and deleting users.                   |
| **Server Certificate**                   | Certificate and key (PEM) used by the server.                                                                                 |
| **Trusted Certificate Authority**        | Upload trusted CA certificates(PEM).                                                                                          |
| **Trusted Client Certificate**           | Upload client-generated certificates(PEM).                                                                                    |

### Security and Certificates

OPC UA strongly recommends enabling security policies and message encryption to prevent man-in-the-middle attacks and eavesdropping. Key points:

- Use strong security policies (such as Basic256Sha256) and enable SignAndEncrypt mode on the client.
- Add client certificates to the **Trusted Client Certificates** list to enable mutual TLS.
- Enable username/password authentication.

When Neuron starts the OPC UA Server for the first time, a self-signed certificate is generated. External clients may need to manually trust this certificate (e.g., import it into the trusted list in the UA client). Uploaded client certificates are trusted by default. Unknown client connections will have their certificates added to the untrusted list and require manual trust in the UI.

### Naming and Mapping Rules

Neuron maps tags (points) from southbound devices to OPC UA nodes. Mapping rules:

- Each southbound node (e.g., modbus1) corresponds to an OPC UA Object node.
- Groups are organized as child objects under the southbound node.
- Tags are mapped to Variable nodes, with DataType mapped from Neuron's type to OPC UA types (Double, Int32, Boolean, String, etc.).

All southbound nodes are under the NeuronEX node. NodeId follows the format `ns=1;s=[device].[group].[tag]`, e.g., `ns=1;s=modbus-tcp-1.group-1.temperature`, where ns=1 is the NeuronEX namespace.

## Data Type Mapping

| NeuronEX     | OPC UA        |
| ------------ | ------------- |
| INT8/UINT8   | Sbyte/Byte    |
| INT16/UINT   | Int16/UInt16  |
| INT32/UINT32 | Int32/UInt32  |
| INT64/UINT64 | Int64/UInt64  |
| FLOAT        | Float         |
| DOUBLE       | Double        |
| BIT/BOOL     | Boolean       |
| STRING       | String        |
| BYTES        | ByteString    |
| ARRAY_INT8   | Array Sbyte   |
| ARRAY_UINT8  | Array Byte    |
| ARRAY_INT16  | Array Int16   |
| ARRAY_UINT16 | Array Uint16  |
| ARRAY_INT32  | Array Int32   |
| ARRAY_UINT32 | Array Uint32  |
| ARRAY_INT64  | Array Int64   |
| ARRAY_UINT64 | Array Uint64  |
| ARRAY_FLOAT  | Array Float   |
| ARRAY_DOUBLE | Array Double  |
| ARRAY_BOOL   | Array Boolean |
| Json         | String        |
