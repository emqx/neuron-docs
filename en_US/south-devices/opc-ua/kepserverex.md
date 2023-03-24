# Connect to KEPServerEX

## Username/Password Login

1. Right-click on the KEPServerEX icon in the system tray, select "Settings" in the menu, open "KEPServerEX Settings", switch to the "User Manager" card, create a new user under the Administrators group and set the Username/Password.
![](./assets/kepware-1_en.jpg)

2. Double click on the KEPServerEX icon in the system tray, open the "Property Editor" of the "Project" in the main screen and set OPC UA - "Allow anonymous login" to "No".
![](./assets/kepware-2_en.jpg)

3. Right-click on the KEPServerEX icon in the system tray, select "OPC UA Configuration" in the menu, switch to "Server Endpoints", double-click on the endpoint entry and check all security policies.
![](./assets/kepware-3_en.jpg)

4. Right-click on the KEPServerEX icon in the system tray and select "Reinitialize" in the menu.

5. Neuron adds a new southbound OPC UA device, opens "Device Configuration", fills in the "Endpoint URL" of the target Server, fills in the user name/password, no need to add certificate/key, and starts the device connection.

6. Right-click on the KEPServerEX icon in the system tray, select "OPC UA Configuration" in the menu, switch to "Trusted Clients" and set the NeuronClient certificate as trusted.
![](./assets/kepware-4_en.jpg)

7. Right-click on the KEPServerEX icon in the system tray and select "Reinitialize" in the menu.

## Certificate/key + username/password login

1. Set the username/password as above.

2. Refer to [Connection policy](./policy.md) to generate or convert a certificate/key.

3. Right-click on the KEPServerEX icon in the system tray, select "OPC UA Configuration" in the menu, switch to "Trusted Clients" and import the client certificate in DER format into the list.

4. Right-click on the KEPServerEX icon in the system tray and select "Reinitialize" in the menu.

5. Neuron adds a new southbound OPC UA device, opens "Device Configuration", fills in the "Endpoint URL" of the target Server, fills in the user name/password, adds the certificate/key, and starts the device connection.

## Test Data List

|  Name    |  Address                                      | Attribute       | Data type   |
| -------- | ------------------------------------------ | ---------- | ------ |
| BuildDate | 0!2266 | Read | UINT32 |
| BuildNumber | 0!2265 | Read | STRING |
| ManufacturerName | 0!2263 | Read | STRING |
| ProductName | 0!2261 | Read | STRING |
| ProductUri | 0!2262 | Read | STRING |
| SoftwareVersion | 0!2264 | Read | STRING |

