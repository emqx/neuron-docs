# Log Management

## Downloading Logs

Neuron supports one-click download of all log filed on web pages in version 2.3, as shown below.

![download_log](./assets/download_log.png)

The log download function bundles the /neuron/build/logs folder into neuron_logs.tar.gz file and downloads it to a web page. The file contains all the created driver and neuron log files.Directory level examples of files are shown below.

![neuron_logs](./assets/neuron_logs.png)

## Set The Debug Log Of The Node

Neuron supports the setting of printing debug logs of a node and automatically switching back to the default log level after approximately ten minutes. The Settings for each node are independent of each other.

Each node's `more` operation button has a `DEBUG log` operation button, as shown below.

![debug_log](./assets/debug_log.png)

When you click this button, a prompt like the one below appears.

![debug_log_tip](./assets/debug_log_tip.png)

In this case, the node starts to print debug logs. You can download the logs about ten minutes later to view the logs of the node, or view the logs under /build/logs.

:::tip
When the node debug log is printed, the neuron log will also be printed, and the default log level will be automatically switched back after ten minutes.
:::