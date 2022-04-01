# Neuron 2.0 MQTT Topics

All topics for interaction between client and neuron with read, write command.

The **client-id** in all topics refers to the actual MQTT client id, which is set in the northbound application configuration in the Neuron UI.

## Read Tags

### Request

*Topic*  **neuron/{client-id}/read/req**

#### Body

```json
{
    "command": "",
    "uuid": "E21AEE51-1269-B228-E9E5-CD252CE10877",
    "node_name": "modbus-tcp-1",
    "group_config_name": "group-2"
}
```

### Response

*Topic*  **neuron/{client-id}/read/resp**

#### Body

```json
{
  "uuid": "E21AEE51-1269-B228-E9E5-CD252CE10877",
  "command": "",
  "tags": [
    {
      "value": 4,
      "name": "data1",
      "error": 0
    },
    {
      "value": 5,
      "name": "data2",
      "error": 0
    }
  ]
}
```

## Upload Data

### Response

*Topic* **neuron/{client-id}/upload**

#### Body

```json
{
  "node_name": "modbus-tcp-2",
  "group_config_name": "group-1",
  "timestamp": 1647497389075,
  "tags": [
    {
      "value": 123,
      "name": "data1",
      "error": 0
    },
    {
      "value": 0,
      "name": "data2",
      "error": 0
    }
  ]
}
```

**Node:**  A group sends a message.

## Write Tags

### Request

*Topic*  **neuron/{client-id}/write/req**

#### Body

```json
{
    "command": "",
    "uuid": "E21AEE51-1269-B228-E9E5-CD252CE10877",
    "node_name": "modbus-tcp-1",
    "group_config_name": "group-2",
    "tags": [
      {
        "value": 6,
        "name": "data1"
      },
      {
        "value": 6,
        "name": "data2"
      }
    ]
}
```

### Response

*Topic*  **neuron/{client-id}/write/resp**

#### Body

```json
{
  "uuid": "E21AEE51-1269-B228-E9E5-CD252CE10877",
  "command": "",
  "tags": [
    {
      "value": 6,
      "name": "data1",
      "error": 0
    },
    {
      "value": 6,
      "name": "data2",
      "error": 0
    }
  ]
}
```
