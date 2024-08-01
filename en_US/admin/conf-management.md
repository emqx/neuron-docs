# Configuration Management
Neuron supports modifying Neuron's configuration parameters through `command line`, `environment variables`, and `configuration files`, which can provide a more flexible way of starting and running.
If `command line`, `environment variable`, and `configuration file` are configured at the same time, the priority relationship between the three is: command line > environment variable > configuration file

## Command Line

![cli_info](./assets/cli_info.png)

## Environment Variables

Neuron supports reading environment variables during the startup process to configure startup parameters. The currently supported environment variables are as follows:


| Configuration name     | Configuration function                                                      |
| ---------------------- | --------------------------------------------------------------------------- |
| NEURON_DAEMON          | Set to 1, the Neuron daemon runs; set to 0, Neuron runs normally                             |
| NEURON_LOG             | Set to 1, Neuron Log outputs to standard output stdout; set to 0, Neuron Log does not output to standard output stdout; |
| NEURON_LOG_LEVEL       | Neuron log output level, can be set to DEBUG or NOTICE                       |
| NEURON_RESTART         | Neuron restart settings, which can be set to never, always, on-failure or NUMBER (1, 2, 3, 4)           |
| NEURON_DISABLE_AUTH    | Set to 1, Neuron turns off Token authentication and authentication; set to 0, Neuron turns on Token authentication and authentication              |
| NNEURON_CONFIG_DIR     | Neuron configuration file directory                  |
| NEURON_PLUGIN_DIR      | Neuron plug-in file directory                        |
| NEURON_SUB_FILTER_ERROR | Set to 1, the 'subscribe' attribute only detects the normal value read last time, and does not report any error codes to north apps|


## Configuration File

Neuron provides json format configuration files to configure Neuron-related personalized parameters. The configuration file path is the neuron installation directory config/neuron.json. The default configuration content is as follows:

```json
{
	"ip": "0.0.0.0",
	"port": 7000,
	"disable_auth": 0,
	"syslog_host": "",
	"syslog_port": 541,
	"sub_filter_error": 0
}
```
