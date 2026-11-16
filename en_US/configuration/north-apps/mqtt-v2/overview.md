# MQTT V2

MQTT V2 is a northbound MQTT plugin that organizes data by device. Each subscribed southbound device has its own set of topics:

- State topic: publishes a retained device state message, with the connection state, the running state and the device properties;
- Data topic: uploads the collected data, in a format given by the data template and the tag template;
- Write request and write response topics: receive tag write requests and return the write results.

The online state of the northbound application itself is also published as a retained message, with a will message registered. The cloud only needs to subscribe to the topics to get the latest state, properties and data of the devices.

MQTT V2 and the [MQTT](../mqtt/overview.md) plugin can be used at the same time, the behavior of the MQTT plugin is unaffected.

| Item | MQTT | MQTT V2 |
| --- | --- | --- |
| Topics | Write request and response topics in the application configuration, upload topic in the subscription | Generated from the topic prefix and the device name, the data topic of a group can be overridden in its subscription |
| Data format | values-format, tags-format, ECP-format or custom format | Data template plus tag template, with built-in variables |
| Device state | Periodic report of the states of all southbound drivers | One retained state message per device, published on changes only |
| Online state | None | Retained online state message, plus a will message |
| Device properties | None, subscription static tags can be used instead | Supported, properties are included in the state messages and usable in templates |

::: tip
The **Client ID** of each northbound application must be unique. Connections with the same client ID take over each other, and the broker may publish the will, turning the online state to offline.
The plugin subscribes to its own online state topic and to the write request topic of each device. When configuring ACLs on the MQTT broker, grant the subscribe and publish permissions of these topics.
:::

## Add Application

Navigate to **Configuration -> North Apps**, click **Add Application** and select the **MQTT V2** plugin.

## Configure Application

| Parameter | Description |
| --- | --- |
| **MQTT Version** | MQTT protocol version, 3.1.1 or 5.0, 3.1.1 by default. |
| **Client ID** | MQTT client ID, required, unique for each application. `${random_str}` in the default value is replaced by a random string when the application is created. |
| **QoS Level** | QoS of the data messages, write requests and write responses, QoS 0 by default. State messages always use QoS 1. |
| **Topic Prefix** | Prefix of all topics, `neuron/${app}` by default, `${app}` being replaced by the northbound application name. Only `${app}` is allowed, `+` and `#` are not. See [Topic Structure](#topic-structure). |
| **Data Template** | JSON template of data messages, the default template is used when left empty. See [Upstream/Downstream Data Format](./api.md#data-upload). |
| **Tag Template** | JSON structure of each tag in the data template, the default template is used when left empty. Tags that fail to be read are uploaded when the template uses `${tag.error}`. See [Upstream/Downstream Data Format](./api.md#data-upload). |
| **Broker Host** | MQTT broker address, required. |
| **Broker Port** | MQTT broker port, required. |
| **Username** | Username to connect to the broker, optional. |
| **Password** | Password to connect to the broker, optional. |
| **SSL** | Whether to enable SSL, disabled by default. |
| **CA** | Required when SSL is enabled. |
| **Client Cert** | For SSL mutual authentication. |
| **Client Private Key** | For SSL mutual authentication. |
| **Offline Cache** | Offline caching switch, disabled by default. When enabled, data messages are cached while disconnected and sent in order after reconnecting. State messages are not cached, the latest states are published again after reconnecting. |
| **Cache Memory Size (MB)** | Required with offline caching, 1–1024, not larger than the cache disk size. |
| **Cache Disk Size (MB)** | Required with offline caching, 1–10240. |
| **Cache Sync Interval (MS)** | Required with offline caching, the interval between the cached messages sent after reconnecting, 10–12000. |

## Topic Structure

Take the default prefix `neuron/${app}`, a northbound application named `mqtt-v2` and a southbound device named `modbus-1` as an example:

| Usage | Topic | Direction | Retain |
| --- | --- | --- | --- |
| Online state | `neuron/mqtt-v2/state` | Publish, also subscribed by the plugin | Yes |
| Device state | `neuron/mqtt-v2/modbus-1/state` | Publish | Yes |
| Device data | `neuron/mqtt-v2/modbus-1/data` | Publish | No |
| Write request | `neuron/mqtt-v2/modbus-1/write/request` | Subscribe | — |
| Write response | `neuron/mqtt-v2/modbus-1/write/response` | Publish | No |

- The plugin subscribes to the write request topic of a device once the device is first subscribed, and unsubscribes when all groups of the device are unsubscribed.
- `+` and `#` in names are replaced by `_` in topics, the messages keep the original names.
- After changing the topic prefix, the northbound application name or the southbound device name, all topics are updated, and the retained states under the old topics are cleared.

## Status Messages

Status messages have fixed formats, unaffected by the templates. They are all retained, with QoS 1.

### Online State

- A will message `{"online": false}` is registered when connecting to the broker.
- Once connected, the plugin publishes:

  ```json
  {"online": true, "timestamp": 1731744000123}
  ```

- When the application stops normally, the plugin publishes `{"online": false, "timestamp": ...}` before disconnecting, which does not trigger the will.
- If the topic is changed to offline while running, for example by the late will of an old connection, the plugin publishes the online state again.

### Device State

```json
{"timestamp": 1731744000123, "name": "modbus-1", "state": 1, "running": 3, "location": "Building A", "line": 3}
```

| Field | Description |
| --- | --- |
| `timestamp` | Publishing time, Unix timestamp in milliseconds. |
| `name` | Southbound device name. |
| `state` | Connection state: 0 disconnected, 1 connected. |
| `running` | Running state: 1 initializing, 2 ready, 3 running, 4 stopped. |
| Other fields | Device properties, see [Device Properties](#device-properties). |

A device state is published when:

- connecting or reconnecting to the broker, for all the subscribed devices;
- the device is first subscribed;
- the connection state or the running state of the device changes, checked every second;
- the device properties change.

An empty retained message clears the state of a device when:

- all the groups of the device subscribed in this application are unsubscribed;
- the southbound device is deleted;
- the southbound device is renamed, the state under the old name is cleared and the state under the new name is published;
- the northbound application is deleted, or the topic prefix is changed.

No status messages are published while disconnected from the broker, they are published again after reconnecting.

## Device Properties

Device properties are static key/value information of a southbound device, such as location, production line or asset number. They are configured on the southbound device and used by all the MQTT V2 applications subscribing to it.

Properties can be set through the HTTP API, for example:

```http
POST /api/v2/node/properties
```

```json
{
    "node": "modbus-1",
    "properties": [
        {"key": "location", "value": "Building A"},
        {"key": "line", "value": 3},
        {"key": "thresholds", "value": [0, 12.5]}
    ]
}
```

- **Value types**: a property value can be a string, boolean, integer or float, or a one-dimensional array of elements of the same type.
- **Operations**: the API also supports GET to query, PUT to update a single property and DELETE to delete properties.
- **Device state**: properties are flattened into the device state message automatically, which is published again once properties are added, updated or deleted. `timestamp`, `name`, `state` and `running` are fixed fields, properties of the same names are left out of the state message.
- **Data messages**: properties are not included by default. Use `${properties}` or `${properties[key]}` in the data template or the tag template to include them, see [Upstream/Downstream Data Format](./api.md#template-variables).

## Add Subscription

Click the MQTT V2 application card on the **North Apps** page, then **Add Subscription** on the **Group List** page:

- **Southbound Device**: the southbound device to subscribe to, for example modbus-1.
- **Group**: a group of the device, for example group-1.
- **Topic**: the data topic of the group, `${prefix}/${device}/data` by default, which is the device data topic.
  - Variables: `${prefix}` (topic prefix), `${app}` (northbound application name), `${device}` (southbound device name), `${group}` (group name).
  - No `+` or `#`, no leading `$` (except `${`), up to 255 characters.
  - With variables, the topic follows changes of the prefix and the names. For example, to publish each group to its own topic, use `${prefix}/${device}/${group}`.

Multiple groups of a device share the state and write request topics of the device. By default, the data of the groups is also published to the same data topic, distinguished by the `group` field of the data messages.

## Operation and Maintenance

On the application card or row, you can click the **Data Statistics** icon to review the application's operation status and track the data received and sent. For explanations on statistical fields, refer to [Create a Northbound Application](../north-apps.md).

If there are any issues, you can click the DEBUG log icon. The system prints DEBUG level logs for the node and switches back to the system default log level after ten minutes. Then click **System Information** -> **Logs** to view the logs and troubleshoot.
