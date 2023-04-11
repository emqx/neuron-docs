# KNXnet/IP

## Parameter Configuration

| Parameter | Description                               |
| --------- | ----------------------------------------- |
| **host**  | KNXnet/IP device ip, default 224.0.23.12  |
| **port**  | KNXnet/IP device port, default 3671       |

Note that setting with the multicast address *224.0.23.12* normally requires that the
KNXnet/IP device and Neuron are in the same sub network.

Due to the way how KNXnet/IP protocol works, the KNX plugin may not be able to work correctly
if Neuron is installed using some virtualisation technology such as virtual machines or docker.
In a Linux host with docker, using the docker option `--net=host` is required. In other cases,
we recommend that you install Neuron using binary packages.

## Support Data Type

* bit
* bool
* int8
* uint8
* int16
* uint16
* float

## Usage of Address Format

### Address Format

* > GROUP_ADDRESS,INDIVIDUAL_ADDRESS</span>

Represents a KNX individual address that is a member of the group address.
When reading the KNX plugin sends a `GroupValueRead` tunnelling request using
the specified group address, and updates the tag value upon receiving a `GroupValueResp`
matching the specified individual address.
When writing the KNX plugin sends a `GroupValueWrite` tunnelling request using
the specified group address.

*Example:*

`0/0/1,1.1.1` represents a KNX individual address `1.1.1` that is a member
  of the group address `0/0/1`.

* > GROUP_ADDRESS,INDIVIDUAL_ADDRESS,BIT</span>

Same as above, but for `uint8` values with fewer than 8 bits, such as KNX data point
types `B2` and `B1U3`, etc. *BIT* represents the number of bits.

*Example:*

`0/0/1,1.1.1,2` represents a KNX individual address `1.1.1` that is a member
  of the group address `0/0/1`, the data is of 2 bit.