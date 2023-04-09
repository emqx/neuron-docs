# Frequently asked questions and troubleshooting

## After compiling and starting Neuron, open page 404

### Check whether the port is open

By default, Neuron opens port 7000 and executes the following command to check the status of port 7000:
```bash
$ lsof -i:7000
```
If there is no output, it indicates that the port number is not enabled. Execute the following command to open the port:
To view firewall status:
```bash
$ firewall-cmd --state
```
If the returned message is```not running```, you must first enable the firewall:
```bash
$ systemctl start firewalld.service
```
Open the specified port:
```bash
$ firewall-cmd --zone=public --add-port=7000/tcp --permanent
```
Restart the firewall:
```bash
$ systemctl restart firewalld.service
```
Reload firewall:
```bash
$ firewall-cmd --reload
```
```Success``` indicates success. After completion, restart Neuron.

### Check whether the IP is input correctly

The neuron access format is http://x.x.x.x:7000 Where x.x.x.x represents the gateway address where Neuron is installed. Execute the following command to view the IP address:
```bash
$ ifconfig
```
Check whether the address after inet under the network card matches the entered address.