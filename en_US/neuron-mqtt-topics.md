# Neuron 2.0 MQTT Topics

All topics for interaction between client and neuron with read, write command.

The xxx in all topics refers to the Client-id, which is set in the northbound application configuration in the Neuron UI.

## Read Tags

### Request

*Topic*  **neuron/xxx/read/req**

#### Body

```json
{
    "command": "",
    "uuid": "E21AEE51-1269-B228-E9E5-CD252CE10877",
    "node_id": 5,
    "group_config_name": "group-2"
}
```

### Response

*Topic*  **neuron/xxx/read/resp**

#### Body

```json
{
  "uuid": "E21AEE51-1269-B228-E9E5-CD252CE10877",
  "command": "",
  "tags": [
    {
      "value": 4,
      "id": 3,
      "error": 0
    },
    {
      "value": 5,
      "id": 4,
      "error": 0
    }
  ]
}
```

## Upload Data

### Response

*Topic* **neuron/xxx/read/resp**

#### Body

```json
{
  "node_id": 5,
  "node_name": "modbus-tcp-2",
  "group_config_name": "group-1",
  "timestamp": 1647497389075,
  "tags": [
    {
      "value": 123,
      "id": 1,
      "error": 0
    },
    {
      "value": 0,
      "id": 2,
      "error": 0
    }
  ]
}
```

**Node:**  A group sends a message.

## Write Tags

### Request

*Topic*  **neuron/xxx/write/req**

#### Body

```json
{
    "command": "",
    "uuid": "E21AEE51-1269-B228-E9E5-CD252CE10877",
    "node_id": 5,
    "group_config_name": "group-2",
    "tags": [
      {
        "value": 6,
        "id": 3
      },
      {
        "value": 6,
        "id": 4
      }
    ]
}
```

### Response

*Topic*  **neuron/xxx/write/resp**

#### Body

```json
{
  "uuid": "E21AEE51-1269-B228-E9E5-CD252CE10877",
  "command": "",
  "tags": [
    {
      "value": 6,
      "id": 3,
      "error": 0
    },
    {
      "value": 6,
      "id": 4,
      "error": 0
    }
  ]
}
```
