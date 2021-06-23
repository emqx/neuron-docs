# Functional Services

Neuron would provide a series of API services for IIoT platform, to query the basic information, to control gateway
behaviors or to setup the polling configuration. IIoT platform must initiate the communication by sending request
message to Neuron. By return, Neuron would send back the required information or execute the deserved action. If there
is error, a error code would be returned to tell the reason of failure.

**_MQTT Topics for Neuron_**

Subscribe: Neuron/Request /%UUID%

Publish: Neuro/Response n/%UUID%

**_MQTT Topics for IIoT platform_**

Subscribe: Neuron/Response /%UUID%

Publish: Neuron/Request /%UUID%

![](../assets/api-services-on-mqtt.png)

![](../assets/api-services-on-websockets.png)

## Function 10 Login

**_HTTP API Header_**

(GET)

Resource Path: /api/v1/funcno10

Content-Type: application/json



**_HTTP API or Websockets or MQTT Communication_**

Request body syntax

```json
{
  "func": 10,
  "wtrm": "DEMO-Neuron-1001_1532421778824_1",
  "name": "admin",
  "pass": "0000"
}
```

Response body syntax

```json
{
  "func": 10,
  "wtrm": "DEMO-Neuron-1001_1532421778824_1",
  "errc": 0,
  "tout": 15,
  "defl": -1,
  "nalw": 3,
  "alwl": [
    {
      "atxt": "VIEW",
      "anum": 0
    },
    {
      "atxt": "MANAGER",
      "anum": 1
    },
    {
      "atxt": "ALL",
      "anum": -1
    }
  ]
}
```

| Request  |                                                  |
| -------- | ------------------------------------------------ |
| **func** | Function code 10                                 |
| **wtrm** | A water mark that copied to the response message |
| **name** | Username                                         |
| **pass** | User password                                    |

| Response |                                                   |
| -------- | ------------------------------------------------- |
| **func** | Function code 10                                  |
| **wtrm** | A water mark that copied from the request message |
| **errc** | Compiler error code                               |
| **tout** | Time out                                          |
| **defl** | Default level                                     |
| **nalw** | No of allowed levels                              |
| **alwl** | Allowed level                                     |
| **atxt** | Allowed text <br>ALL -1 <br> VIEW <br> OPERATOR <br> FOREMAN <br> MAINTENANCE <br> SUPERVISOR <br> ENGINEER <br> DESIGNER <br> MANAGER 7                                         |
| **anum** | Allowed number <br>-1 <br> 0<br> 1<br> 2<br> 3<br> 4<br> 5<br> 6<br> 7 |

| Functions                     | Allowed Level   |
| ----------------------------- | --------------- |
| Exit to shell                 | 4,5,7           |
| Restart/Newrestart/Shutdown   | 2,3,4,5,6,7     |
| Login/Logout                  | 0,1,2,3,4,5,6,7 |
| New password                  | 0,1,2,3,4,5,6,7 |
| User administration           | 4,5,7           |
| Browse system ID              | 4,5,7           |
| Status control                | 2,3,4,5,7       |
| Write value to object         | 4,5,7           |
| Read instance list            | 4,5,7           |
| Setup configuration           | 4,5,7           |
| Read configuration            | 4,5,7           |
| Read global variable          | 4,5,7           |
| List all subroutine           | 4,5,7           |
| Read a subroutine             | 4,5,7           |
| Create a subroutine           | 4,5,7           |
| Delete a subroutine           | 4,5,7           |
| Compiler a subroutine         | 4,5,7           |
| Search string in a subroutine | 4,5,7           |
| Check alarm status            | 1,2,3,4,5,7     |
| Alarm acknowledge             | 2,3,4,5,7       |
| Change alarm mode             | 2,3,4,5,7       |
| Alarm Log report              | 4,5,7           |
| Read trend data               | 2,3,4,5,7       |
| Read object screen            | 2,3,4,5,7       |
| Read License Information      | 4,5,7           |

## Function 11 Logout

**_HTTP API Header_**

(GET)

Resource Path: /api/v1/funcno11

Content-Type: application/json

Authorization: Bearer \<token\>



**_HTTP API or Websockets or MQTT Communication_**

Request body syntax

```json
{
  "func": 11,
  "wtrm": "DEMO-Neuron-1001_1532419775357_240",
  "name": "admin"
}
```

Response body syntax

```json
{
  "func": 11,
  "wtrm": "DEMO-Neuron-1001_1532419775357_240",
  "errc": 0
}
```

| Request  |                                                  |
| -------- | ------------------------------------------------ |
| **func** | Function code 11                                 |
| **wtrm** | A water mark that copied to the response message |
| **name** | Username                                         |

| Response |                                                   |
| -------- | ------------------------------------------------- |
| **func** | Function code 11                                  |
| **wtrm** | A water mark that copied from the request message |
| **errc** | Compiler error code                               |

## Function 12 New Password

**_HTTP API Header_**

(POST)

Resource Path: /api/v1/funcno12

Content-Type: application/json

Authorization: Bearer \<token\>

| **HTTP status code** | **Description**      |
| -------------------- | -------------------- |
| 200                  | Successful operation |
| 400                  | Invalid Operation    |

**_HTTP API or Websockets or MQTT Communication_**

Request body syntax

```json
{
  "func": 12,
  "wtrm": "DEMO-Neuron-1001_1532419775357_240",
  "name": "admin",
  "pass": "0000",
  "npwd": "1234"
}
```

Response body syntax

```json
{
  "func": 12,
  "wtrm": "DEMO-Neuron-1001_1532419775357_240",
  "errc": 0
}
```

| Request  |                                                  |
| -------- | ------------------------------------------------ |
| **func** | Function code 12                                 |
| **wtrm** | A water mark that copied to the response message |
| **name** | Username                                         |
| **pass** | Password                                         |
| **npwd** | New Password                                     |

| Response |                                                   |
| -------- | ------------------------------------------------- |
| **func** | Function code 12                                  |
| **wtrm** | A water mark that copied from the request message |
| **errc** | Compiler error code                               |

## Function 13 Read User List

**_HTTP API Header_**

(PUT)

Resource Path: /api/v1/funcno13

Content-Type: application/json

Authorization: Bearer \<token\>

| **HTTP status code** | **Description**      |
| -------------------- | -------------------- |
| 200                  | Successful operation |
| 400                  | Invalid Operation    |

**_HTTP API or Websockets or MQTT Communication_**

Request body syntax

```json
{
  "func": 13,
  "wtrm": "DEMO-Neuron-1001_1532419775357_240"
}
```

Request body syntax

```json
{
  "func": 13,
  "wtrm": "DEMO-Neuron-1001_1532419775357_240",
  "errc": 0,
  "nusr": 3,
  "user": [
    "joey",
    "peter",
    "ruby"
  ]
}
```

| Request  |                                                  |
| -------- | ------------------------------------------------ |
| **func** | Function code 13                                 |
| **wtrm** | A water mark that copied to the response message |

| Response |                                                   |
| -------- | ------------------------------------------------- |
| **func** | Function code 13                                  |
| **wtrm** | A water mark that copied from the request message |
| **errc** | Compiler error code                               |
| **nusr** | No of users|
| **user** | A list of users name|

## Function 14 Read User Information

**_HTTP API header_**

(PUT)

Resource Path: /api/v1/funcno14

Content-Type: application/json

Authorization: Bearer \<token\>

| **HTTP status code** | **Description**      |
| -------------------- | -------------------- |
| 200                  | Successful operation |
| 400                  | Invalid Operation    |

**_HTTP API or Websockets or MQTT Communication_**

Request body syntax

```json
{
  "func": 14,
  "wtrm": "DEMO-Neuron-1001_1532421778824_1",
  "name": "joey"
}
```

Response body syntax

```json
{
  "func": 14,
  "wtrm": "DEMO-Neuron-1001_1532421778824_1",
  "errc": 0,
  "usrn": "joey",
  "tout": 15,
  "defl": -1,
  "nalw": 3,
  "alwl": [
    {
      "atxt": "VIEW",
      "anum": 0
    },
    {
      "atxt": "MANAGER",
      "anum": 1
    },
    {
      "atxt": "ALL",
      "anum": -1
    }
  ]
}
```

| Request  |                                                  |
| -------- | ------------------------------------------------ |
| **func** | Function code 14                                 |
| **wtrm** | A water mark that copied to the response message |
| **name** | Username                                         |

| Response |                                                   |
| -------- | ------------------------------------------------- |
| **func** | Function code 14                                  |
| **wtrm** | A water mark that copied from the request message |
| **errc** | Compiler error code                               |
| **usrn** | User name                                         |
| **tout** | Time out                                          |
| **defl** | Default level                                     |
| **nalw** | No of allowed levels                              |
| **alwl** | Allowed level                                     |
| **atxt** | Allowed text ALL                                   <br> VIEW                                               <br> OPERATOR                                           <br> FOREMAN                                            <br> MAINTENANCE                                        <br> SUPERVISOR                                         <br> ENGINEER                                           <br> DESIGNER                                           <br> MANAGER                                           |
| **anum** | Allowed number -1<br> 0<br> 1<br> 2<br> 3<br> 4<br> 5<br> 6<br> 7                                                 |

## Function 15 Save User Information

**_HTTP API Header_**

(POST)

Resource Path: /api/v1/funcno15

Content-Type: application/json

Authorization: Bearer \<token\>

| **HTTP status code** | **Description**      |
| -------------------- | -------------------- |
| 200                  | Successful operation |
| 400                  | Invalid Operation    |

**_HTTP API or Websockets or MQTT Communication_**

Request body syntax

```json
{
  "func": 15,
  "wtrm": "DEMO-Neuron-1001_1532419775357_240",
  "cusr": 1,
  "name": "joey",
  "pass": "0000",
  "tout": 15,
  "defl": 7,
  "nalw": 3,
  "alwl": [
    0,
    6,
    7
  ]
}
```

Response body syntax

```json
{
  "func": 15,
  "wtrm": "DEMO-Neuron-1001_1532419775357_240",
  "errc": 0
}
```

| Request  |                                                    |
| -------- | -------------------------------------------------- |
| **func** | Function code 15                                   |
| **wtrm** | A water mark that copied to the response message   |
| **cusr** | Check user already exist if exist, return error    |
| **name** | User name                                          |
| **pass** | New password                                       |
| **tout** | Timeout (0-999 in minutes, 0 means never time-out) |
| **defl** | Default level (0-9)                                |
| **nalw** | No of allowed level                                |
| **alwl** | Array of allowed level                             |

| Response |                                                   |
| -------- | ------------------------------------------------- |
| **func** | Function code 15                                  |
| **wtrm** | A water mark that copied from the request message |
| **errc** | Compiler error code                               |

## Function 16 Remove User

**_HTTP API Header_**

(DELETE)

Resource Path: /api/v1/funcno16

Content-Type: application/json

Authorization: Bearer \<token\>

| **HTTP status code** | **Description**      |
| -------------------- | -------------------- |
| 200                  | Successful operation |
| 400                  | Invalid Operation    |

**_HTTP API or Websockets or MQTT Communication_**

Request body syntax

```json
{
  "func": 16,
  "wtrm": "DEMO-Neuron-1001_1532419775357_240",
  "name": "user"
}
```

Response body syntax

```json
{
  "func": 16,
  "wtrm": "DEMO-Neuron-1001_1532419775357_240",
  "errc": 0
}
```

| Request  |                                                  |
| -------- | ------------------------------------------------ |
| **func** | Function code 16                                 |
| **wtrm** | A water mark that copied to the response message |
| **name** | Username                                         |

| Response |                                                   |
| -------- | ------------------------------------------------- |
| **func** | Function code 16                                  |
| **wtrm** | A water mark that copied from the request message |
| **errc** | Compiler error code                               |

## Function 21 Configuration

**_HTTP API Header_**

(POST)

Resource Path: /api/v1/funcno21

Content-Type: application/json

Authorization: Bearer \<token\>

| **HTTP status code** | **Description**      |
| -------------------- | -------------------- |
| 200                  | Successful operation |
| 400                  | Invalid Operation    |

**_HTTP API or Websockets or MQTT Communication_**

Request boy syntax

```json
{
  "func": 21,
  "wtrm": "DEMO-Neuron-1001_1532419775357_240",
  "chnl": [
    {
      "chdv": "mbstcp",
      "tcph": "192.168.1.119",
      "tcpp": 502,
      "ttyc": "",
      "ttyb": 0,
      "ttyd": 0,
      "ttys": "",
      "ttyp": "N",
      "parm": [
        {
          "vars": "DLYCRESOCKAFTCLOSE",
          "pars": "300"
        },
        {
          "vars": "TORECEIVETCP",
          "pars": "300"
        },
        {
          "vars": "NAPTIMEREAD",
          "pars": "40"
        },
        {
          "vars": "NAPTIMEWRITE",
          "pars": "20"
        }
      ]
    },
    {
      "chdv": "pahomq",
      "tcph": "broker.emqx.io",
      "tcpp": 1883,
      "ttyc": "",
      "ttyb": 0,
      "ttyd": 0,
      "ttys": "",
      "ttyp": "N",
      "parm": [
        {
          "vars": "USERNAME",
          "pars": ""
        },
        {
          "vars": "PASSWORD",
          "pars": ""
        },
        {
          "vars": "CERTIFICATE",
          "pars": ""
        },
        {
          "vars": "KEYFILE",
          "pars": ""
        }
      ]
    }
  ],
  "objd": [
    {
      "objn": "Tank",
      "obsz": 3,
      "odes": [
        {
          "odix": 0,
          "otxt": "Water Tank"
        },
        {
          "odix": 1,
          "otxt": "Acid Tank"
        },
        {
          "odix": 2,
          "otxt": "Dryer Tank"
        }
      ],
      "updt": 1,
      "logt": 1,
      "oatt": [
        {
          "attn": "temperature",
          "attt": "word",
          "deci": 1,
          "attr": "R",
          "rtim": 0,
          "unit": "C",
          "aadd": [
            {
              "obix": 0,
              "desc": "1",
              "addr": "4!40200"
            },
            {
              "obix": 1,
              "desc": "2",
              "addr": "4!40201"
            },
            {
              "obix": 2,
              "desc": "3",
              "addr": "4!40202"
            }
          ]
        },
        {
          "attn": "energy",
          "attt": "word",
          "deci": 1,
          "attr": "R",
          "rtim": 0,
          "unit": "W",
          "aadd": [
            {
              "obix": 0,
              "desc": "1",
              "addr": "1!40100"
            },
            {
              "obix": 1,
              "desc": "2",
              "addr": "2!40100"
            },
            {
              "obix": 2,
              "desc": "3",
              "addr": "3!40100"
            }
          ]
        },
        {
          "attn": "switch",
          "attt": "bit",
          "deci": 0,
          "attr": "RW",
          "rtim": 0,
          "unit": "",
          "aadd": [
            {
              "obix": 0,
              "desc": "1",
              "addr": "5!00100"
            },
            {
              "obix": 1,
              "desc": "2",
              "addr": "5!00102"
            },
            {
              "obix": 2,
              "desc": "3",
              "addr": "5!00104"
            }
          ]
        },
        {
          "attn": "buzzer",
          "attt": "bit",
          "deci": 0,
          "attr": "RW",
          "rtim": 0,
          "unit": "",
          "aadd": [
            {
              "obix": 0,
              "desc": "1",
              "addr": "5!00101"
            },
            {
              "obix": 1,
              "desc": "2",
              "addr": "5!00103"
            },
            {
              "obix": 2,
              "desc": "3",
              "addr": "5!00105"
            }
          ]
        }
      ]
    },
    {
      "objn": "Temp",
      "obsz": 1,
      "odes": [
        {
          "obix": 0,
          "otxt": "Tank Temperature"
        }
      ],
      "updt": 1,
      "logt": 1,
      "oatt": [
        {
          "attn": "high",
          "attt": "word",
          "deci": 1,
          "attr": "-",
          "rtim": 0,
          "unit": "",
          "aadd": [
            {
              "obix": 0,
              "desc": "",
              "addr": "-"
            }
          ]
        },
        {
          "attn": "temp1",
          "attt": "word",
          "deci": 1,
          "attr": "R",
          "rtim": 0,
          "unit": "",
          "aadd": [
            {
              "obix": 0,
              "desc": "",
              "addr": "4!40200"
            }
          ]
        },
        {
          "attn": "temp2",
          "attt": "word",
          "deci": 1,
          "attr": "R",
          "rtim": 0,
          "unit": "",
          "aadd": [
            {
              "obix": 0,
              "desc": "",
              "addr": "4!40201"
            }
          ]
        },
        {
          "attn": "temp3",
          "attt": "word",
          "deci": 1,
          "attr": "R",
          "rtim": 0,
          "unit": "",
          "aadd": [
            {
              "obix": 0,
              "desc": "",
              "addr": "4!40202"
            }
          ]
        },
        {
          "attn": "low",
          "attt": "word",
          "deci": 1,
          "attr": "-",
          "rtim": 0,
          "unit": "",
          "aadd": [
            {
              "obix": 0,
              "desc": "",
              "addr": "-"
            }
          ]
        }
      ]
    },
    {
      "objn": "Energy",
      "obsz": 1,
      "odes": [
        {
          "obix": 0,
          "otxt": "Tank Energy"
        }
      ],
      "updt": 1,
      "logt": 1,
      "oatt": [
        {
          "attn": "energy1",
          "attt": "word",
          "deci": 1,
          "attr": "R",
          "rtim": 0,
          "unit": "",
          "aadd": [
            {
              "obix": 0,
              "desc": "",
              "addr": "1!40100"
            }
          ]
        },
        {
          "attn": "energy2",
          "attt": "word",
          "deci": 1,
          "attr": "R",
          "rtim": 0,
          "unit": "",
          "aadd": [
            {
              "obix": 0,
              "desc": "",
              "addr": "2!40100"
            }
          ]
        },
        {
          "attn": "energy3",
          "attt": "word",
          "deci": 1,
          "attr": "R",
          "rtim": 0,
          "unit": "",
          "aadd": [
            {
              "obix": 0,
              "desc": "",
              "addr": "3!40100"
            }
          ]
        }
      ]
    }
  ],
  "msgd": [
    {
      "msgt": ">",
      "sobj": "Temp[0]",
      "satt": "temp1",
      "cobj": "Temp[0]",
      "catt": "high",
      "acat": "critical",
      "dtim": 0,
      "subr": 200
    },
    {
      "msgt": "<",
      "sobj": "Temp[0]",
      "satt": "temp1",
      "cobj": "Temp[0]",
      "catt": "low",
      "acat": "alarm",
      "dtim": 0,
      "subr": 0
    },
    {
      "msgt": ">",
      "sobj": "Temp[0]",
      "satt": "temp2",
      "cobj": "Temp[0]",
      "catt": "high",
      "acat": "critical",
      "dtim": 0,
      "subr": 201
    },
    {
      "msgt": "<",
      "sobj": "Temp[0]",
      "satt": "temp2",
      "cobj": "Temp[0]",
      "catt": "low",
      "acat": "alarm",
      "dtim": 0,
      "subr": 0
    },
    {
      "msgt": ">",
      "sobj": "Temp[0]",
      "satt": "temp3",
      "cobj": "Temp[0]",
      "catt": "high",
      "acat": "critical",
      "dtim": 0,
      "subr": 202
    },
    {
      "msgt": "<",
      "sobj": "Temp[0]",
      "satt": "temp3",
      "cobj": "Temp[0]",
      "catt": "low",
      "acat": "alarm",
      "dtim": 0,
      "subr": 0
    }
  ]
}
```

Response body syntax

```json
{
  "func": 21,
  "wtrm": "DEMO-Neuron-1001_1532419775357_240",
  "errc": 0
}
```

| Request  |                                                               |
| -------- | ------------------------------------------------------------- |
| **func** | Function code 21                                              |
| **wtrm** | A water mark that copied to the response message              |
| **chnl** | Channel Details                                               |
| **chdv** | Channel driver name                                           |
| **tcph** | Hostname or IP address of PLC/hardware device                 |
| **tcpp** | Port number of a device                                       |
| **ttyc** | Linux device file name (ttyS0, ttyS1)                         |
| **ttyb** | Baud rate <br>4800 <br>9600 <br>19200 <br>38400 <br>57600 <br>115200 |
| **ttyd** | Data bit<br> 5<br> 6<br> 7<br> 8                              |
| **ttys** | Stop bit (string)<br> 1<br> 1.5<br> 2                         |
| **ttyp** | Parity bit (char)<br> E - Even<br> O - Odd<br> N - None                                                      |
| **parm** | Parameter array Details                                       |
| **vars** | Variables name                                                |
| **pars** | Parameters                                                    |
| **objd** | Object Details                                                |
| **objn** | Object name                                                   |
| **obsz** | Number of same objects                                        |
| **updt** | Time interval for data transfer to platform cloud             |
| **logt** | Time interval for data to be logged on file                   |
| **tstd** | Timestamp display<br>0 (no display)<br>1 (display)                                                   |
| **disp** | All object attributes need to be displayed<br> 0 (no display)<br> 1 (display)                                                   |
| **logs** | Need logging once connection drop<br> 0 (no need)<br> 1 (need)                                                      |
| **oatt** | Object Attribute Details                                      |
| **attn** | Attribute name                                                |
| **attt** | Attribute value type:<br> word<br> uword<br> dword<br> udword<br> float<br> double<br> bit<br> datetime                                                      |
| **deci** | No of decimal place                                           |
| **adis** | Attribute transferred to platform<br> 0 (no need)<br> 1 (need)                                                      |
| **achg** | Attribute can be changed<br> 0 (not allow)<br> 1 (allow)                                                     |
| **attr** | Attribute Read/Write indicator<br> R<br> W<br> R/W                                                           |
| **rtim** | Read time (for only attr: R)                                  |
| **aadd** | Attribute Address Details                                     |
| **obix** | Start from 0 index number                                     |
| **pref** | Object name prefix                                            |
| **suff** | Object name suffix                                            |
| **addr** | Tag address (device address) <br> Note: For internal register, both tagaddr and tagattr use "-" |
| **msgd** | Message Details                                               |
| **msgt** | Message type<br> <<br> <=<br> ><br> >=<br> ==<br> !=<br> &<br> \^<br> \|                                                            |
| **sobj** | Source object name                                            |
| **satt** | Source attribute name                                         |
| **cobj** | Compared object name                                          |
| **catt** | Compared attribute name                                       |
| **acat** | Alarm Category<br> critical<br> alarm<br> warning<br> event<br> view                                                          |
| **subr** | Subroutine number (1-999)                                     |

| Response |                                                   |
| -------- | ------------------------------------------------- |
| **func** | Function code 21                                  |
| **wtrm** | A water mark that copied from the request message |
| **errc** | Compiler error code                               |

## Function 22 Read Configuration

**_HTTP API Header_**

(PUT)

Resource Path: /api/v1/funcno22

Content-Type: application/json

Authorization: Bearer \<token\>

| **HTTP status code** | **Description**      |
| -------------------- | -------------------- |
| 200                  | Successful operation |
| 400                  | Invalid Operation    |

**_HTTP API or Websockets or MQTT Communication_**

Request body syntax

```json
{
  "func": 22,
  "wtrm": "DEMO-Neuron-1001_1532419775357_240"
}
```

Request body syntax

```json
{
  "func": 22,
  "wtrm": "DEMO-Neuron-1001_1532419775357_240",
  "errc": 0
//  The structure is same as Function 21 request message
//   Not repeat here
}
```

## Function 23 Read Drivers

**_HTTP API Header_**

(PUT)

Resource Path: /api/v1/funcno23

Content-Type: application/json

Authorization: Bearer \<token\>

| **HTTP status code** | **Description**      |
| -------------------- | -------------------- |
| 200                  | Successful operation |
| 400                  | Invalid Operation    |

**_HTTP API or Websockets or MQTT Communication_**

Request body syntax

```json
{
  "func": 23,
  "wtrm": "DEMO-Neuron-1001_1532421778824_1",
  "type": 1
}
```

Response body syntax

```json
{
  "func": 23,
  "wtrm": "DEMO-Neuron-1001_1532421778824_1",
  "errc": 0,
  "nrow": 3,
  "rows": [
    {
      "name": "mbsrtu",
      "desc": "Modbus RTU",
      "type": "tty",
      "attr": [
        "r",
        "w",
        "rw"
      ]
    },
    {
      "name": "mbstcp",
      "desc": "Modbus TCP",
      "type": "tcp",
      "attr": [
        "r",
        "w",
        "rw"
      ]
    },
    {
      "name": "mbsrot",
      "desc": "Modbus RTU over TCP",
      "type": "tcp",
      "attr": [
        "r",
        "w",
        "rw"
      ]
    },
    {
      "name": "opcua",
      "desc": "OPC UA",
      "type": "tcp",
      "attr": [
        "r",
        "w",
        "rw",
        "s",
        "sw"
      ]
    }
  ]
}
```

| Request  |                                                  |
| -------- | ------------------------------------------------ |
| **func** | Function code 23                                 |
| **wtrm** | A water mark that copied to the response message |
| **type** | 1:  Driver Channel<br>2:  Server Channel         |

| Response |                                                             |
| -------- | ----------------------------------------------------------- |
| **func** | Function code 23                                            |
| **wtrm** | A water mark that copied from the request message           |
| **errc** | Compiler error code                                         |
| **nrow** | Number of rows                                              |
| **name** | Short name of driver                                        |
| **desc** | Full description of driver                                  |
| **type** | Type of driver<br> tty Serial driver<br> tcp Network driver |
| **attr** | Attribute Read/Write indicator<br>R<br>W<br>RW<br>S<br>SW   |

## Function 24 Read Driver Parameters

**_HTTP API Header_**

(PUT)

Resource Path: /api/v1/funcno24

Content-Type: application/json

Authorization: Bearer \<token\>

| **HTTP status code** | **Description**      |
| -------------------- | -------------------- |
| 200                  | Successful operation |
| 400                  | Invalid Operation    |

**_HTTP API or Websockets or MQTT Communication_**

Request body syntax

```json
{
  "func": 24,
  "wtrm": "DEMO-Neuron-1001_1532421778824_1",
  "drvn": "i61850"
}
```

Response body syntax

```json
{
  "func": 24,
  "wtrm": "DEMO-Neuron-1001_1532421778824_1",
  "errc": 0,
  "drvn": "i61850",
  "parm": [
    {
      "vars": "DLYCRESOCKAFTCLOSE",
      "pars": "300"
    },
    {
      "vars": "TORECEIVETCP",
      "pars": "300"
    },
    {
      "vars": "NAPTIMEREAD",
      "pars": "40"
    },
    {
      "vars": "NAPTIMEWRITE",
      "pars": "20"
    },
    {
      "vars": "USERNAME",
      "pars": ""
    },
    {
      "vars": "PASSWORD",
      "pars": ""
    },
    {
      "vars": "CERTIFICATE",
      "pars": ""
    },
    {
      "vars": "KEYFILE",
      "pars": ""
    },
    {
      "vars": "ADDRSUFFIX",
      "pars": ""
    }
  ]
}
```
| Request  |                                                   |
| -------- | ------------------------------------------------- |
| **func** | Function code 24                                  |
| **wtrm** | A water mark that copied from the request message |
| **drvn** | driver name                                       |

| Response |                                                   |
| -------- | ------------------------------------------------- |
| **func** | Function code 24                                  |
| **wtrm** | A water mark that copied from the request message |
| **errc** | Compiler error code                               |
| **drvn** | driver name                                       |
| **parm** | parameter array                                   |

## Function 25 Check PLC Addresses

**_HTTP API Header_**

(PUT)

Resource Path: /api/v1/funcno25

Content-Type: application/json

Authorization: Bearer \<token\>

| **HTTP status code** | **Description**      |
| -------------------- | -------------------- |
| 200                  | Successful operation |
| 400                  | Invalid Operation    |

**_HTTP API or Websockets or MQTT Communication_**

Request body syntax

```json
{
  "func": 25,
  "wtrm": "d0fdb943-cff1-44bc-887d-0a3b3ba856b0",
  "chdv": "mbtcp",
  "attt": "word",
  "deci": 0,
  "attr": "R",
  "addr": "1!400002"
}
```

Response body syntax

```json
{
  "func": 25,
  "wtrm": "d0fdb943-cff1-44bc-887d-0a3b3ba856b0",
  "errc": 0
}
```

| Request  |                                                               |
| -------- | ------------------------------------------------------------- |
| **func** | Function code 25                                              |
| **wtrm** | A water mark that copied from the request message             |
| **chdv** | Channel driver name                                           |
| **attt** | Attribute value type, allow text:<br> word<br> uword<br> dword<br> udword<br> float<br> double<br> bit<br> datetime                                                      |
| **deci** | No of decimal place                                           |
| **attr** | Attribute Read/Write indicator, allow text:<br> R<br> W<br> R/W                                                           |
| **addr** | Tag address (device address) <br>Note: For internal register, both tagaddr and tagattr use "-" |

| Response |                                                   |
| -------- | ------------------------------------------------- |
| **func** | Function code 25                                  |
| **wtrm** | A water mark that copied from the request message |
| **errc** | Compiler error code                               |

## Function 26 Read Device List

**_HTTP API Header_**

(GET)

Resource Path: /api/v1/funcno25

Content-Type: application/json

Authorization: Bearer \<token\>



**_HTTP API or Websockets or MQTT Communication_**

**Request body syntax**

```json
{
  "func": 26,
  "wtrm": "d0fdb943-cff1-44bc-887d-0a3b3ba856b0"
}
```

**Response body syntax**
```json
{
  "func": 26,
  "wtrm": "d0fdb943-cff1-44bc-887d-0a3b3ba856b0",
  "rows": [
    {
      "name": "/dev/tty",
      "fdrw": 0
    },
    {
      "name": "/dev/ttyS0",
      "fdrw": 0
    },
    {
      "name": "/dev/ttyS1",
      "fdrw": -1
    },
    {
      "name": "/dev/ttyUSB0",
      "fdrw": -1
    }
  ],
  "errc": 0
}
```

| Request        |                                                              |
| -------------- | ------------------------------------------------------------ |
| func | Function code 26                                             |
| wtrm | A water mark that copied from the request message            |

| Response       |                                                              |
| -------------- | ------------------------------------------------------------ |
| func | Function code 26                                             |
| wtrm | A water mark that copied from the request message            |
| rows | Device list                                                  |
| name | Device name                                                  |
| fdrw | File descriptor read and write permission, <br>0: Got permission,<br>-1: No permission |
| errc | Compiler error code                                          |

## Function 30 Read Global Variable

**_HTTP API Header_**

(PUT)

Resource Path: /api/v1/funcno30

Content-Type: application/json

Authorization: Bearer \<token\>



| **HTTP status code** | **Description**      |
| -------------------- | -------------------- |
| 200                  | Successful operation |
| 400                  | Invalid Operation    |

**_HTTP API or Websockets or MQTT Communication_**

Request body syntax

```json
{
  "func": 30,
  "wtrm": "DEMO-Neuron-1001_1532421778824_1"
}
```

Response body syntax

```json
{
  "func": 30,
  "wtrm": "DEMO-Neuron-1001_1532421778824_1",
  "errc": 0,
  "nrow": 7,
  "rows": [
    {
      "glov": "time",
      "leng": 1,
      "comt": "unix timestamp"
    },
    {
      "glov": "year",
      "leng": 1,
      "comt": "current year"
    },
    {
      "glov": "month",
      "leng": 1,
      "comt": "current month"
    },
    {
      "glov": "day",
      "leng": 1,
      "comt": "day of the month"
    },
    {
      "glov": "hour",
      "leng": 1,
      "comt": "hour of the day"
    },
    {
      "glov": "min",
      "leng": 1,
      "comt": "minute of the hour"
    },
    {
      "glov": "dayofweek",
      "leng": 1,
      "comt": "day of the week"
    }
  ]
}
```

| Request  |                                                  |
| -------- | ------------------------------------------------ |
| **func** | Function code 30                                 |
| **wtrm** | A water mark that copied to the response message |

| Response |                                                   |
| -------- | ------------------------------------------------- |
| **func** | Function code 30                                  |
| **wtrm** | A water mark that copied from the request message |
| **errc** | Compiler error code                               |
| **nrow** | Number of rows|
| **glov** | Global variable name|
| **leng** | Variable size|
| **comt** | Comments|

## Function 31 Save Global Variable

**_HTTP API Header_**

(POST)

Resource Path: /api/v1/funcno31

Content-Type: application/json

Authorization: Bearer \<token\>



| **HTTP status code** | **Description**      |
| -------------------- | -------------------- |
| 200                  | Successful operation |
| 400                  | Invalid Operation    |

**_HTTP API or Websockets or MQTT Communication_**

Request body syntax

```json
{
  "func": 31,
  "wtrm": "DEMO-Neuron-1001_1532421778824_1",
  "nrow": 7,
  "rows": [
    {
      "glov": "time",
      "leng": 1,
      "comt": "unix timestamp"
    },
    {
      "glov": "year",
      "leng": 1,
      "comt": "current year"
    },
    {
      "glov": "month",
      "leng": 1,
      "comt": "current month"
    },
    {
      "glov": "day",
      "leng": 1,
      "comt": "day of the month"
    },
    {
      "glov": "hour",
      "leng": 1,
      "comt": "hour of the day"
    },
    {
      "glov": "min",
      "leng": 1,
      "comt": "minute of the hour"
    },
    {
      "glov": "dayofweek",
      "leng": 1,
      "comt": "day of the week"
    }
  ]
}
```

Response body syntax

```json
{
  "func": 31,
  "wtrm": "DEMO-Neuron-1001_1532421778824_1",
  "errc": 0
}
```

| Request  |                                                  |
| -------- | ------------------------------------------------ |
| **func** | Function code 31                                 |
| **wtrm** | A water mark that copied to the response message |
| **nrow** | Number of rows|
| **glov** | Global variable name|
| **leng** | Variable size|
| **comt** | Comments|

| Response |                                                   |
| -------- | ------------------------------------------------- |
| **func** | Function code 31                                  |
| **wtrm** | A water mark that copied from the request message |
| **errc** | Compiler error code                               |

## Function 32 Read Subroutine List

**_HTTP API Header_**

(PUT)

Resource Path: /api/v1/funcno32

Content-Type: application/json

Authorization: Bearer \<token\>

| **HTTP status code** | **Description**      |
| -------------------- | -------------------- |
| 200                  | Successful operation |
| 400                  | Invalid Operation    |

**_HTTP API or Websockets or MQTT Communication_**

Request body syntax

```json
{
  "func": 32,
  "wtrm": "DEMO-Neuron-1001_1532421778823_1"
}
```

Response body syntax

```json
{
  "func": 32,
  "wtrm": "DEMO-Neuron-1001_1532421778823_1",
  "errc": 0,
  "nsub": 3,
  "msub": 999,
  "rows": [
    {
      "subr": 200,
      "name": "SR200 TEMPERATURE ALARM HANDLER"
    },
    {
      "subr": 201,
      "name": "SR201 TEMPERATURE ALARM HANDLER"
    },
    {
      "subr": 202,
      "name": "SR202 TEMPERATURE ALARM HANDLER"
    }
  ]
}
```

| Request  |                                                  |
| -------- | ------------------------------------------------ |
| **func** | Function code 32                                 |
| **wtrm** | A water mark that copied to the response message |

| Response |                                                   |
| -------- | ------------------------------------------------- |
| **func** | Function code 32                                  |
| **wtrm** | A water mark that copied from the request message |
| **errc** | Compiler error code                               |
|**nsub** |Number of subroutines|
|**msub** |Maximum number of subroutines|
|**subr** |Subroutine number|
|**name** |Subroutine name|

## Function 33 Read Subroutine

**_HTTP API Header_**

(PUT)

Resource Path: /api/v1/funcno33

Content-Type: application/json

Authorization: Bearer \<token\>

| **HTTP status code** | **Description**      |
| -------------------- | -------------------- |
| 200                  | Successful operation |
| 400                  | Invalid Operation    |

**_HTTP API or Websockets or MQTT Communication_**

Request body syntax

```json
{
  "func": 33,
  "wtrm": "DEMO-Neuron-1001_1532421778827_1",
  "subr": 200
}
```

Response body syntax

```json
{
  "func": 33,
  "wtrm": "DEMO-Neuron-1001_1532421778827_1",
  "errc": 0,
  "subr": 200,
  "name": "SR200 TEMPERATURE ALARM TIRGGER HANDLER",
  "nrow": 5,
  "rows": [
    {
      "stmt": "COMMENT",
      "expr": "TEMPERATURE HANDLER"
    },
    {
      "stmt": "",
      "expr": ""
    },
    {
      "stmt": "IF",
      "expr": "Tank[0].buzzer == 0"
    },
    {
      "stmt": "THEN",
      "expr": "Tank[0].buzzer = 1;"
    },
    {
      "stmt": "",
      "expr": ""
    }
  ]
}
```

| Request  |                                                  |
| -------- | ------------------------------------------------ |
| **func** | Function code 33                                 |
| **wtrm** | A water mark that copied to the response message |
| **subr** | Subroutine number                                |

| Response |                                                   |
| -------- | ------------------------------------------------- |
| **func** | Function code 33                                  |
| **wtrm** | A water mark that copied from the request message |
| **errc** | Compiler error code                               |
| **subr** | Subroutine number<br> MAIN is -10<br> MANUAL is -20<br> AUTO is -22                                       |
| **name** | Subroutine name                                   |
| **nrow** | Number of rows                                    |
| **stmt** | Statement                                         |
| **expr** | Expression                                        |

## Function 34 Save Subroutine

**_HTTP API Header_**

(POST)

Resource Path: /api/v1/funcno34

Content-Type: application/json

Authorization: Bearer \<token\>

| **HTTP status code** | **Description**      |
| -------------------- | -------------------- |
| 200                  | Successful operation |
| 400                  | Invalid Operation    |

**_HTTP API or Websockets or MQTT Communication_**

Request body syntax

```json
{
  "func": 34,
  "wtrm": "DEMO-Neuron-1001_1532421778827_1",
  "csub": 0,
  "subr": 200,
  "name": "SR200 TEMPERATURE ALARM TIRGGER HANDLER",
  "nrow": 5,
  "rows": [
    {
      "stmt": "COMMENT",
      "expr": "TEMPERATURE HANDLER"
    },
    {
      "stmt": "",
      "expr": ""
    },
    {
      "stmt": "IF",
      "expr": "Tank[0].buzzer == 0"
    },
    {
      "stmt": "THEN",
      "expr": "Tank[0].buzzer = 1;"
    },
    {
      "stmt": "",
      "expr": ""
    }
  ]
}
```

Response body syntax

```json
{
  "func": 34,
  "wtrm": "DEMO-Neuron-1001_1532421778827_1",
  "errc": 0
}
```

| Request  |                                                         |
| -------- | ------------------------------------------------------- |
| **func** | Function code 34                                        |
| **wtrm** | A string that copied to the response message            |
| **csub** | Check Subroutine Exist before save (0 -- don't check, 1 -- check) |
| **subr** | Routine Number<br> MAIN is -10<br> MANUAL is -20<br> AUTO is -22<br> Or any number (1-999) for subroutine                    |
| **name** | Subroutine Name                                         |
| **line** | No of Lines                                             |
| **stmt** | Statement                                               |
| **expr** | Expression                                              |

| Response |                                                   |
| -------- | ------------------------------------------------- |
| **func** | Function code 34                                  |
| **wtrm** | A water mark that copied from the request message |
| **errc** | Compiler error code                               |

## Function 35 Remove Subroutine

**_HTTP API Header_**

(DELETE)

Resource Path: /api/v1/funcno35

Content-Type: application/json

Authorization: Bearer \<token\>

| **HTTP status code** | **Description**      |
| -------------------- | -------------------- |
| 200                  | Successful operation |
| 400                  | Invalid Operation    |

**_HTTP API or Websockets or MQTT Communication_**

Request body syntax

```json
{
  "func": 35,
  "wtrm": "DEMO-Neuron-1001_1532421778827_1",
  "subr": 200
}
```

Response body syntax

```json
{
  "func": 35,
  "wtrm": "DEMO-Neuron-1001_1532421778827_1",
  "errc": 0
}
```

| Request  |                                                  |
| -------- | ------------------------------------------------ |
| **func** | Function code 35                                 |
| **wtrm** | A water mark that copied to the response message |
| **subr** | Subroutine Number                                |

| Response |                                                   |
| -------- | ------------------------------------------------- |
| **func** | Function code 35                                  |
| **wtrm** | A water mark that copied from the request message |
| **errc** | Compiler error code                               |

## Function 36 Test Subroutine

**_HTTP API Header_**

(POST)

Resource Path: /api/v1/funcno36

Content-Type: application/json

Authorization: Bearer \<token\>

| **HTTP status code** | **Description**      |
| -------------------- | -------------------- |
| 200                  | Successful operation |
| 400                  | Invalid Operation    |

**_HTTP API or Websockets or MQTT Communication_**

Request body syntax

```json
{
  "func": 36,
  "wtrm": "DEMO-Neuron-1001_1532421778827_1",
  "nrow": 5,
  "rows": [
    {
      "stmt": "COMMENT",
      "expr": "TEMPERATURE HANDLER"
    },
    {
      "stmt": "",
      "expr": ""
    },
    {
      "stmt": "IF",
      "expr": "Tank[0].buzzer == 0"
    },
    {
      "stmt": "THEN",
      "expr": "Tank[0].buzzer = 1;"
    },
    {
      "stmt": "",
      "expr": ""
    }
  ]
}
```

Response body syntax

```json
{
  "func": 36,
  "wtrm": "DEMO-Neuron-1001_1532421778827_1",
  "errc": 0
}
```

| Request  |                                                  |
| -------- | ------------------------------------------------ |
| **func** | Function code 36                                 |
| **wtrm** | A water mark that copied to the response message |
| **subr** | Subroutine Number                                |
| **line** | No of Lines                                      |
| **stmt** | Statement                                        |
| **expr** | Expression                                       |

| Response |                                                   |
| -------- | ------------------------------------------------- |
| **func** | Function code 36                                  |
| **wtrm** | A water mark that copied from the request message |
| **errc** | Compiler error code                               |

## Function 37 Search in Subroutine

**_HTTP API Header_**

(PUT)

Resource Path: /api/v1/funcno37

Content-Type: application/json

Authorization: Bearer \<token\>

| **HTTP status code** | **Description**      |
| -------------------- | -------------------- |
| 200                  | Successful operation |
| 400                  | Invalid Operation    |

**_HTTP API or Websockets or MQTT Communication_**

Request body syntax

```json
{
  "func": 37,
  "wtrm": "DEMO-Neuron-1001_1532421778827_1",
  "srhm": "main",
  "upca": 0,
  "wwrd": 0,
  "srhs": "temperature"
}
```

Response body syntax

```json
{
  "func": 37,
  "wtrm": "DEMO-Neuron-1001_1532421778827_1",
  "errc": 0,
  "rows": [
    {
      "modu": "main",
      "line": 1,
      "chnu": 8,
      "desc": "COMMENT MAIN - TEMPERATURE CONTROL"
    },
    {
      "modu": "main",
      "line": 7,
      "chnu": 9,
      "desc": "IF Tank[i].temperature > Temp[0].high && Tank[i].switch == 1"
    },
    {
      "modu": "main",
      "line": 9,
      "chnu": 9,
      "desc": "ELSE IF Tank[i].temperature < Temp[0].low && Tank[i].switch == 0"
    }
  ]
}
```

| Request  |                                                  |
| -------- | ------------------------------------------------ |
| **func** | Function code 37                                 |
| **wtrm** | A water mark that copied to the response message |
| **srhm** | Search mode globalvar<br> main<br> man<br> auto<br> subroutine                                       |
| **upca** | Match upper lower case (1 match, 0 no need)      |
| **wwrd** | Match whole word (1 match whole, 0 match part)   |
| **srhs** | Search string                                    |

| Response |                                                   |
| -------- | ------------------------------------------------- |
| **func** | Function code 37                                  |
| **wtrm** | A water mark that copied from the request message |
| **errc** | Compiler error code                               |
| **rows** | Row number index                                  |
| **modu** | Module globalvar<br> main<br> man<br> auto<br> subroutine                                        |
| **subr** | Subroutine number                                 |
| **line** | Line number                                       |
| **chnu** | Start at character position                       |
| **desc** | Description                                       |

## Function 38 Execute Script

**_HTTP API Header_**

(PUT)

Resource Path: /api/v1/funcno38

Content-Type: application/json

Authorization: Bearer \<token\>

| **HTTP status code** | **Description**      |
| -------------------- | -------------------- |
| 200                  | Successful operation |
| 400                  | Invalid Operation    |

**_HTTP API or Websockets or MQTT Communication_**

Request body syntax

```json
{
  "func": 38,
  "wtrm": "d0fdb943-cff1-44bc-887d-0a3b3ba856b0",
  "subr": 200
}
```

Response body syntax

```json
{
  "func": 38,
  "wtrm": "d0fdb943-cff1-44bc-887d-0a3b3ba856b0",
  "errc": 0
}
```

| Request  |                                                   |
| -------- | ------------------------------------------------- |
| **func** | Function code 38                                  |
| **wtrm** | A water mark that copied from the request message |
| **subr** | Subroutine number (1-999)

| Response |                                                   |
| -------- | ------------------------------------------------- |
| **func** | Function code 38                                  |
| **wtrm** | A water mark that copied from the request message |
| **errc** | Compiler error code                               |

## Function 50 Read Register

**_HTTP API Header_**

(PUT)

Resource Path: /api/v1/funcno50

Content-Type: application/json

Authorization: Bearer \<token\>

| **HTTP status code** | **Description**      |
| -------------------- | -------------------- |
| 200                  | Successful operation |
| 400                  | Invalid Operation    |

**_HTTP API or Websockets or MQTT Communication_**

Request body syntax

```json
{	
	"func": 50,
	"wtrm": "DEMO-Neuron-1001_1532421778827_1",
	"srcn": "Tank[0]"
} 
```

Request body syntax

```json
{
  "func": 50,
  "wtrm": "DEMO-Neuron-1001_1532421778827_1",
  "errc": 0,
  "tele": [
    {
      "objn": "Tank_1",
      "tstp": 1552532233,
      "temperature": 81.2,
      "energy": 2181.8,
      "switch": 1,
      "buzzer": 0
    },
    {
      "objn": "Tank_2",
      "tstp": 1552532233,
      "temperature": 79.1,
      "energy": 3176.2,
      "switch": 1,
      "buzzer": 0
    },
    {
      "objn": "Tank_3",
      "tstp": 1552532233,
      "temperature": 86.4,
      "energy": 1146.3,
      "switch": 0,
      "buzzer": 1
    }
  ]
}
```

| Request  |                                                  |
| -------- | ------------------------------------------------ |
| **func** | Function code 50                                 |
| **wtrm** | A water mark that copied to the response message |

| Response |                                                   |
| -------- | ------------------------------------------------- |
| **func** | Function code 50                                  |
| **wtrm** | A water mark that copied from the request message |
| **errc** | Error code                                        |
| **tele** |Telemetry Array|
| **objn** |Object Name|
| **tstp** |TimeStamp|

## Function 51 Write Register

**_HTTP API Header_**

(POST)

Resource Path: /api/v1/funcno51

Content-Type: application/json

Authorization: Bearer \<token\>

| **HTTP status code** | **Description**      |
| -------------------- | -------------------- |
| 200                  | Successful operation |
| 400                  | Invalid Operation    |

**_HTTP API or Websockets or MQTT Communication_**

Request body syntax

```json
{
  "func": 51,
  "wtrm": "DEMO-Neuron-1001_1532421778827_1",
  "srcn": "Temp",
  "attn": "high",
  "valn": 860
}
```

Request body syntax

```json
{
  "func": 51,
  "wtrm": "DEMO-Neuron-1001_1532421778827_1",
  "errc": 0
}
```

| Request  |                                                  |
| -------- | ------------------------------------------------ |
| **func** | Function code 51                                 |
| **wtrm** | A water mark that copied to the response message |
| **srcn** | Object Name with prefix and suffix|
| **attn** | Attribute Name|
| **valn** | Value|

| Response |                                                   |
| -------- | ------------------------------------------------- |
| **func** | Function code 51                                  |
| **wtrm** | A water mark that copied from the request message |
| **errc** | Compiler error code                               |

## Function 60 Object Screen

**_HTTP API Header_**

(PUT)

Resource Path: /api/v1/funcno60

Content-Type: application/json

Authorization: Bearer \<token\>

| **HTTP status code** | **Description**      |
| -------------------- | -------------------- |
| 200                  | Successful operation |
| 400                  | Invalid Operation    |

**_HTTP API or Websockets or MQTT Communication_**

Request body syntax

```json
{
  "func": 60,
  "wtrm": "DEMO-Neuron-1001_1532421778827_1"
}
```

Response body syntax

```json
{
  "func": 60,
  "wtrm": "DEMO-Neuron-1001_1532421778827_1",
  "errc": 0,
  "tele": [
    {
      "objn": "Tank_1",
      "logs": 0,
      "temperature": 0,
      "energy": 0,
      "switch": 1,
      "buzzer": 1
    },
    {
      "objn": "Tank_2",
      "logs": 0,
      "temperature": 0,
      "energy": 0,
      "switch": 1,
      "buzzer": 1
    },
    {
      "objn": "Tank_3",
      "logs": 0,
      "temperature": 0,
      "energy": 0,
      "switch": 1,
      "buzzer": 1
    },
    {
      "objn": "Temp",
      "logs": 1,
      "high": 1,
      "temp1": 0,
      "temp2": 0,
      "temp3": 0,
      "low": 1
    },
    {
      "objn": "Energy",
      "logs": 1,
      "energy1": 0,
      "energy2": 0,
      "energy3": 0
    }
  ]
}
```

| Request  |                                                  |
| -------- | ------------------------------------------------ |
| **func** | Function code 60                                 |
| **wtrm** | A water mark that copied to the response message |

| Response |                                                   |
| -------- | ------------------------------------------------- |
| **func** | Function code 60                                  |
| **wtrm** | A water mark that copied from the request message |
| **errc** | Error code                                        |
| **tele** | Telemetry object screen description|
| **objn** | Object name|
| **logs** | Logging (Y/N)|

## Function 61 System Status

**_HTTP API Header_**

(PUT)

Resource Path: /api/v1/funcno61

Content-Type: application/json

Authorization: Bearer \<token\>

| **HTTP status code** | **Description**      |
| -------------------- | -------------------- |
| 200                  | Successful operation |
| 400                  | Invalid Operation    |

**_HTTP API or Websockets or MQTT Communication_**

Request body syntax

```json
{
  "func": 61,
  "wtrm": "DEMO-Neuron-1001_1532421778827_1",
  "actn": "act_en"
}
```

Response body syntax

```json
{
  "func": 61,
  "wtrm": "DEMO-Neuron-1001_1532421778827_1",
  "errc": 0,
  "tstp": 1581515618,
  "comm": "UP",
  "mach": "MANU",
  "mode": "ACTIVE",
  "mqcn": "MQCONNECT",
  "dalm": "NON-EXIST",
  "galm": "UNACKNOWLEDGE",
  "ngal": 4,
  "grow": [
    {
      "acat": "alarm",
      "astt": "OFF",
      "amod": "UNACKALARM",
      "atim": 1581513580,
      "alid": 1,
      "comt": "temp1@Temp (812) < low@Temp (800)"
    },
    {
      "acat": "alarm",
      "astt": "ON",
      "amod": "UNACKALARM",
      "atim": 1581515415,
      "alid": 3,
      "comt": "temp2@Temp (791) < low@Temp (800)"
    },
    {
      "acat": "critical",
      "astt": "ON",
      "amod": "UNACKALARM",
      "atim": 1581515415,
      "alid": 4,
      "comt": "temp3@Temp (864) > high@Temp (850)"
    },
    {
      "acat": "alarm",
      "astt": "OFF",
      "amod": "UNACKALARM",
      "atim": 1581513592,
      "alid": 5,
      "comt": "temp3@Temp (864) < low@Temp (800)"
    }
  ]
}
```

| Request  |                                                  |
| -------- | ------------------------------------------------ |
| **func** | Function code 61                                 |
| **wtrm** | A water mark that copied to the response message |
| **actn** | Action can be anyone of following<br> act_en Active enabled alarms<br> act_unack Active Unack alarms<br> act_all Active all alarms<br> all_alm All alarms<br> all_en All enabled alarms<br> all_dis All disabled alarms                      |

| Response |                                                          |
| -------- | -------------------------------------------------------- |
| **func** | Function code 61                                         |
| **wtrm** | A water mark that copied from the request message        |
| **errc** | Error code                                               |
| **tstp** | TimeStamp                                                |
| **comm** | PLC or hardware communication status<br> UP<br> DOWN                                                     |
| **mach** | Machine Mode<br> AUTO<br> MANU<br> SERV |
| **mode** | Please refer to Status Mode section.<br> Inactive Mode<br> Standby Mode / Semi-Standby Mode<br> Active Mode / Semi-Active Mode                           |
| **mqcn** | MQ broker connection status<br> MQCONNECT<br> MQDISCONNECT                                             |
| **dalm** | Device Alarm which specify which device has <br> communication problem.                                   |
| **ndal** | Number of device alarms                                  |
| **drow** | Device alarm rows                                        |
| **chnl** | Channel number of devices                                |
| **addr** | Address of devices                                       |
| **galm** | General Alarm which user define their own alarms and <br> triggers                                                 |
| **ngal** | Number of general alarms                                 |
| **grow** | General alarm rows                                       |
| **acat** | Alarm Category<br> critical<br> alarm<br> warning<br> event<br> view                                                     |
| **astt** | Alarm Status<br> ON<br> OFF                                                      |
| **amod** | Alarm Mode<br> UNACKALARM<br> DISABLE                                                  |
| **atim** | Alarm TimeStamp                                          |
| **alid** | Alarm ID<br> must be copied this ID when user acknowledge function 80 |
| **comt** | Alarm Comments                                           |

## Function 62 Ping

**_HTTP API Header_**

(GET)

Resource Path: /api/v1/funcno62

Content-Type: application/json

Authorization: Bearer \<token\>

## Function 70 Gateway Control

**_HTTP API header_**

(POST)

Resource Path: /api/v1/funcno70

Content-Type: application/json

Authorization: Bearer \<token\>

| **HTTP status code** | **Description**      |
| -------------------- | -------------------- |
| 200                  | Successful operation |
| 400                  | Invalid Operation    |

**_HTTP API or Websockets or MQTT Communication_**

Request body syntax

```json
{
  "func": 70,
  "wtrm": "DEMO-Neuron-1001_1532419775357_240",
  "acts": "restartnew"
}
```

Response body syntax

```json
{
  "func": 70,
  "wtrm": "DEMO-Neuron-1001_1532419775357_240",
  "errc": 0
}
```

| Request  |                                                     |
| -------- | --------------------------------------------------- |
| **func** | Function code 70                                    |
| **wtrm** | A water mark that copied to the response message    |
| **acts** | Request action<br> restart - restart gateway<br> restartnew - restart gateway with new configuration<br> shutdown - shutdown gateway                         |

| Response |                                                   |
| -------- | ------------------------------------------------- |
| **func** | Function code 70                                  |
| **wtrm** | A water mark that copied from the request message |
| **errc** | Compiler error code                               |

## Function 71 Status Control

**_HTTP API Header_**

(POST)

Resource Path: /api/v1/funcno71

Content-Type: application/json

Authorization: Bearer \<token\>

| **HTTP status code** | **Description**      |
| -------------------- | -------------------- |
| 200                  | Successful operation |
| 400                  | Invalid Operation    |

**_HTTP API or Websockets or MQTT Communication_**

Request body syntax

```json
{
  "func": 71,
  "wtrm": "DEMO-Neuron-1001_1532419775357_240",
  "stat": "standby"
}
```

Response body syntax

```json
{
  "func": 71,
  "wtrm": "DEMO-Neuron-1001_1532419775357_240",
  "errc": 0
}
```

| Request  |                                                  |
| -------- | ------------------------------------------------ |
| **func** | Function code 71                                 |
| **wtrm** | A water mark that copied to the response message |
| **stat** | Request action<br> standby - standby mode (telemetry will stop)<br> active - active mode                             |

| Response |                                                   |
| -------- | ------------------------------------------------- |
| **func** | Function code 71                                  |
| **wtrm** | A water mark that copied from the request message |
| **errc** | Compiler error code                               |

## Function 73 Instance Information

**_HTTP API Header_**

(PUT)

Resource Path: /api/v1/funcno73

Content-Type: application/json

Authorization: Bearer \<token\>

| **HTTP status code** | **Description**      |
| -------------------- | -------------------- |
| 200                  | Successful operation |
| 400                  | Invalid Operation    |

**_HTTP API or Websockets or MQTT Communication_**

Request body syntax

```json
{
  "func": 73,
  "wtrm": "DEMO-Neuron-1001_1532419775357_240"
}
```

Response body syntax

```json
{
  "func": 73,
  "wtrm": "DEMO-Neuron-1001_1532419775357_240",
  "errc": 0,
  "agts": [
    {
      "uuid": "16538d28-4592-11e9-a787-00e067109f12",
      "time": "2019/11/10 13:42:17",
      "expd": "2070/01/01 08:00:00",
      "rest": "00:00:00:00",
      "data": "2.113112",
      "natt": "34",
      "nalr": "10",
      "tatt": "50",
      "talr": "102",
      "tusg": "10.3426",
      "matt": "100",
      "malr": "500",
      "musg": "1000",
      "self": "Y"
    },
    {
      "uuid": "87244d28-4592-11e9-a787-00e097109f12",
      "time": "2019/11/10 13:42:17",
      "expd": "2070/01/01 08:00:00",
      "rest": "00:00:00:00",
      "data": "0.1276532",
      "natt": "19",
      "nalr": "13",
      "tatt": "50",
      "talr": "102",
      "tusg": "10.3426",
      "matt": "100",
      "malr": "500",
      "musg": "1000",
      "self": "N"
    },
    {
      "uuid": "11133d28-4592-11e9-a787-00e077109f12",
      "time": "2019/11/10 13:42:17",
      "expd": "2070/01/01 08:00:00",
      "rest": "00:00:00:00",
      "data": "1.2367209",
      "natt": "21",
      "nalr": "8",
      "tatt": "50",
      "talr": "102",
      "tusg": "10.3426",
      "matt": "100",
      "malr": "500",
      "musg": "1000",
      "self": "N"
    }
  ]
}
```

| Request  |                                                  |
| -------- | ------------------------------------------------ |
| **func** | Function code 73                                 |
| **wtrm** | A water mark that copied to the response message |

| Response |                                                   |
| -------- | ------------------------------------------------- |
| **func** | Function code 73                                  |
| **wtrm** | A water mark that copied from the request message |
| **errc** | Compiler error code                               |
| **nagt** | Number of instances                               |
| **agts** | Neuron instance list                              |
| **uuid** | UUID                                              |
| **time** | Last information update time                      |
| **expd** | System expired date                               |
| **rest** | Time left for the system inactive                 |
| **data** | Data usage                                        |
| **natt** | No of attributes                                  |
| **nalr** | No of alarm points                                |
| **tatt** | Total no. of attributes                           |
| **talr** | Total no. of alarm points                         |
| **tusg** | Total data usage amount                           |
| **matt** | Maximum no. of attributes                         |
| **malr** | Maximum no. of alarm points                       |
| **tusg** | Maximum data usage amount                         |
| **self** | Self Flag (Y/N)                                   |

## Function 74 About Information

**_HTTP API Header_**

(PUT)

Resource Path: /api/v1/funcno74

Content-Type: application/json

Authorization: Bearer \<token\>

| **HTTP status code** | **Description**      |
| -------------------- | -------------------- |
| 200                  | Successful operation |
| 400                  | Invalid Operation    |

**_HTTP API or Websockets or MQTT Communication_**

Request body syntax

```json
{
  "func": 74,
  "wtrm": "DEMO-Neuron-1001_1532419775357_240"
}
```

Response body syntax

```json
{
  "func": 74,
  "wtrm": "DEMO-Neuron-1001_1532419775357_240",
  "errc": 0,
  "sysn": "NEURON SYSTEM v1.1.1",
  "cpyr": "Copyright (C) 2020, EMQ Technologies Co., Ltd. All rights<br>reserved.",
  "modl": "ENT-x86_64-1-0101",
  "srno": "SN010101200227",
  "bver": " 1.1.1",
  "pver": 1,
  "host": "Instance 0",
  "expd": "2020/12/30 11:59:00",
  "rest": "306:23:03:07",
  "tatt": 2,
  "matt": 10000,
  "talr": 2,
  "malr": 1600,
  "tusg": 0.00010799,
  "musg": 100000000,
  "cont": "Joey Cheung (joey@emqx.io)",
  "uuid": "16538d28-4592-11e9-a787-00e067109f12"
}
```

| Request  |                                                  |
| -------- | ------------------------------------------------ |
| **func** | Function code 74                                 |
| **wtrm** | A water mark that copied to the response message |

| Response |                                                   |
| -------- | ------------------------------------------------- |
| **func** | Function code 74                                  |
| **wtrm** | A water mark that copied from the request message |
| **errc** | Compiler error code                               |
| **sysn** | System Name                                       |
| **cpyr** | Copyright message                                 |
| **modl** | System model number                               |
| **modl** | System serial number                              |
| **bver** | Software build version                            |
| **pver** | Protocol number                                   |
| **tatt** | Total no. of attributes in use                    |
| **matt** | Max no. of attributes allowed                     |
| **talr** | Total no. of alarms in use                        |
| **malr** | Max no. of alarms allowed                         |
| **tusg** | Total data usage                                  |
| **tusg** | Max data usage                                    |
| **cont** | Contact information                               |
| **uuid** | UUID                                              |

## Function 79 Show Alarms

**_HTTP API Header_**

(PUT)

Resource Path: /api/v1/funcno79

Content-Type: application/json

Authorization: Bearer \<token\>

| **HTTP status code** | **Description**      |
| -------------------- | -------------------- |
| 200                  | Successful operation |
| 400                  | Invalid Operation    |

**_HTTP API or Websockets or MQTT Communication_**

Request body syntax

```json
{
  "func": 79,
  "wtrm": "DEMO-Neuron-1001_1532421778827_1",
  "actn": "act_en"
}
```

Response body syntax

```json
{
  "func": 79,
  "wtrm": "DEMO-Neuron-1001_1532421778827_1",
  "errc": 0
}
```

| Request  |                                                  |
| -------- | ------------------------------------------------ |
| **func** | Function code 79                                 |
| **wtrm** | A water mark that copied to the response message |
| **actn** | Action can be anyone of following<br> act_en Active enabled alarms<br> act_unack Active Unack alarms<br> act_all Active all alarms<br> all_alm All alarms<br> all_en All enabled alarms<br> all_dis All disabled alarms                      |

| Response |                                                   |
| -------- | ------------------------------------------------- |
| **func** | Function code 79                                  |
| **wtrm** | A water mark that copied from the request message |
| **errc** | Compiler error code                               |

## Function 80 Alarm Acknowledge

**_HTTP API Header_**

(POST)

Resource Path: /api/v1/funcno80

Content-Type: application/json

Authorization: Bearer \<token\>

| **HTTP status code** | **Description**      |
| -------------------- | -------------------- |
| 200                  | Successful operation |
| 400                  | Invalid Operation    |

**_HTTP API or Websockets or MQTT Communication_**

Request body syntax

```json
{
  "func": 80,
  "wtrm": "DEMO-Neuron-1001_1532421778827_1",
  "alid": 0,
  "actn": "acknowledge"
}
```

Response body syntax

```json
{
  "func": 80,
  "wtrm": "DEMO-Neuron-1001_1532421778827_1",
  "errc": 0
}
```

| Request  |                                                                                                        |
| -------- | ------------------------------------------------------------------------------------------------------ |
| **func** | Function code 80                                                                                       |
| **wtrm** | A water mark that copied to the response message                                                       |
| **alid** | This ID is given out by the gateway in the heartbeat message. Copy the one which is being acknowledge. |
| **actn** | Action can be anyone of following<br> acknowledge<br> enable<br> disable                                                                                                |

| Response |                                                   |
| -------- | ------------------------------------------------- |
| **func** | Function code 80                                  |
| **wtrm** | A water mark that copied from the request message |
| **errc** | Compiler error code                               |

## Function 81 Read Historical Alarm

**_HTTP API Header_**

(PUT)

Resource Path: /api/v1/funcno81

Content-Type: application/json

Authorization: Bearer \<token\>

| **HTTP status code** | **Description**      |
| -------------------- | -------------------- |
| 200                  | Successful operation |
| 400                  | Invalid Operation    |

**_HTTP API or Websockets or MQTT Communication_**

Request body syntax

```json
{
  "func": 81,
  "wtrm": "DEMO-Neuron-1001_1532421778827_1",
  "srch": "FromFirst",
  "sett": "",
  "tokn": "",
  "ofst": 0,
  "frti": 1607335939,
  "toti": 1607335950,
  "cate": "alarm",
  "patn": "Temp"
}
```

Response body syntax

```json
{
  "func": 81,
  "wtrm": "DEMO-Neuron-1001_1532421778827_1",
  "errc": 0,
  "frti": 1577930400,
  "toti": 1582552859,
  "nalm": 10,
  "ordr": "ascending",
  "rows": [
    {
      "anum": 1,
      "tstp": 1581482963,
      "uack": "",
      "cate": "alarm",
      "stat": "on",
      "comt": "temp2@Temp (791) < low@Temp (800)"
    },
    {
      "anum": 2,
      "tstp": 1581484493,
      "uack": "",
      "cate": "alarm",
      "stat": "off",
      "comt": "temp2@Temp (0) < low@Temp (0)"
    },
    {
      "anum": 3,
      "tstp": 1581485070,
      "uack": "",
      "cate": "alarm",
      "stat": "ack",
      "comt": "temp2@Temp (791) < low@Temp (790)"
    },
    {
      "anum": 4,
      "tstp": 1581513521,
      "uack": "",
      "cate": "alarm",
      "stat": "on",
      "comt": "temp1@Temp (0) < low@Temp (790)"
    },
    {
      "anum": 5,
      "tstp": 1581513521,
      "uack": "",
      "cate": "alarm",
      "stat": "on",
      "comt": "temp2@Temp (0) < low@Temp (790)"
    },
    {
      "anum": 6,
      "tstp": 1581513521,
      "uack": "",
      "cate": "alarm",
      "stat": "on",
      "comt": "temp3@Temp (0) < low@Temp (790)"
    },
    {
      "anum": 7,
      "tstp": 1581513580,
      "uack": "",
      "cate": "alarm",
      "stat": "off",
      "comt": "temp1@Temp (0) < low@Temp (0)"
    },
    {
      "anum": 8,
      "tstp": 1581513584,
      "uack": "",
      "cate": "alarm",
      "stat": "off",
      "comt": "temp2@Temp (0) < low@Temp (0)"
    },
    {
      "anum": 9,
      "tstp": 1581513592,
      "uack": "",
      "cate": "alarm",
      "stat": "off",
      "comt": "temp3@Temp (0) < low@Temp (0)"
    },
    {
      "anum": 10,
      "tstp": 1581515415,
      "uack": "",
      "cate": "alarm",
      "stat": "on",
      "comt": "temp2@Temp (791) < low@Temp (800)"
    }
  ],
  "tokn": "5e44029700000003"
}
```

| Request  |                                                        |
| -------- | ------------------------------------------------------ |
| **func** | Function code 81                                       |
| **wtrm** | A string that copied to the response message           |
| **srch** | Search Method                                          |
|          | FromFirst -- means forwards                            |
|          | FromLast -- means backwards                            |
|          | UseID -- use for consecutive search                    |
|          | Blank -- means use FromYear                            |
| **sett** | Today<br> Yesterday<br> ThisWeek<br> LastWeek<br> ThisMonth<br> LastMonth<br> Blank if using FromYear or ToYear below, can only be<br> combined with UseID or blank for first in SearchMethod<br> above                                                  |
| **tokn** | ID string from previous request for next search. (only<br> together with UseID above)                             |
| **ofst** | Offset for next search. positive or negative, only<br> together with UseID above, still using the search<br> pattern below                                          |
| **frti** | From Datetime (timestamp)  |
| **toti** | To Datetime (timestamp)    |
| **cate** | Alarm Category                                         |
| **patn** | Search Pattern - check matching string anywhere in the<br> alarm text.|

| Response |                                               |
| -------- | --------------------------------------------- |
| **func** | Function code 81                              |
| **wtrm** | A string that copied from the request message |
| **errc** | Compiler error code                           |
| **frti** | From Datetime (timestamp)                     |
| **toti** | To Datetime (timestamp)                       |
| **nalm** | Total number of alarms found                  |
| **ordr** | Order <br> ascending <br> descending                                    |
| **anum** | Alarm index number                            |
| **tstp** | Alarm happening time                          |
| **uack** | User who acknowledge this alarm               |
| **cate** | Alarm Category                                |
| **stat** | Status<br> on -- alarm on time<br> off -- alarm off time<br> ack -- alarm ack time                         |
| **comt** | Alarm message                                 |
| **tokn** | ID string for next search                     |

## Function 82 Read Historical Trend

**_HTTP API Header_**

(PUT)

Resource Path: /api/v1/funcno82

Content-Type: application/json

Authorization: Bearer \<token\>

| **HTTP status code** | **Description**      |
| -------------------- | -------------------- |
| 200                  | Successful operation |
| 400                  | Invalid Operation    |

**_HTTP API or Websockets or MQTT Communication_**

Request body syntax

```json
{
  "func": 82,
  "wtrm": "DEMO-Neuron-1001_1532421778827_1",
  "objn": "Temp",
  "obix": 0,
  "attn": [
    "temp1",
    "temp2",
    "temp3",
    "low"
  ],
  "fend": 0,
  "tokn": -1,
  "frti": 1607335939,
  "toti": 1607335950
}
```

Response body syntax

```json
{
  "func": 82,
  "wtrm": "DEMO-Neuron-1001_1532421778827_1",
  "errc": 0,
  "frti": 1519437600,
  "toti": 1582552859,
  "npts": 500,
  "itvl": 1,
  "tele": [
    {
      "tstp": 1581480345,
      "temp1": 0,
      "temp2": 0,
      "temp3": 0,
      "low": 0
    },
    {
      "tstp": 1581480346,
      "temp1": 0,
      "temp2": 0,
      "temp3": 0,
      "low": 0
    },
    {
      "tstp": 1581480347,
      "temp1": 0,
      "temp2": 0,
      "temp3": 0,
      "low": 0
    },
    {
      "tstp": 1581480348,
      "temp1": 0,
      "temp2": 0,
      "temp3": 0,
      "low": 0
    }
  ],
  "tokn": 3636
}
```

| Request  |                                                  |
| -------- | ------------------------------------------------ |
| **func** | Function code 82                                 |
| **wtrm** | A water mark that copied to the response message |
| **srcn** | Object name with prefix and suffix               |
| **attn** | Attribute name (empty means all attributes)      |
| **fend** | Include the last point<br> 1 -- include<br> 0 -- not include                                 |
| **tokn** | File index number for next search                |
| **frti** |From Datetime (timestamp)|
| **toti** |To Datetime (timestamp)|

| Response |                                                   |
| -------- | ------------------------------------------------- |
| **func** | Function code 82                                  |
| **wtrm** | A water mark that copied from the request message |
| **errc** | Compiler error code                               |
| **frti** | From Datetime (timestamp)                         |
| **toti** | To Datetime (timestamp)                           |
| **npts** | Number of trend points found                      |
| **itvl** | Time Interval between trend points                |
| **tele** | Telemetry array                                   |
| **objn** | Object name                                       |
| **tstp** | TimeStamp                                         |
| **tokn** | Token to implement next search                    |

## Function 83 Read Log

**_HTTP API Header_**

(PUT)

Resource Path: /api/v1/funcno83

Content-Type: application/json

Authorization: Bearer \<token\>

**_HTTP API or Websockets or MQTT Communication_**

Request body syntax

```json
{
  "func": 83,
  "wtrm": "DEMO-Neuron-1001_1532419775357_240",
  "logl": "all",
  "srtt": 1604311512,
  "stpt": 1604311517,
  "srtl": 0,
  "proc": "all"
}
```

Response body syntax

```json
{
  "func": 83,
  "wtrm": "DEMO-Neuron-1001_1532419775357_240",
  "nrow": 500,
  "rows": [
    {
      "tstp": 1532419775,
      "logl": "warning",
      "proc": "CORE",
      "data": "extractlicense: loading certificate into memory"
    },
    {
      "tstp": 1532419775,
      "logl": "debug",
      "proc": "DRVR",
      "data": "debuglog: Cannot connect"
    },
    {
      "tstp": 1532419775,
      "logl": "err",
      "proc": "SERV",
      "data": "serverdisconnect: send disconnection request failed return code -3"
    },
    {
      "tstp": 1532419775,
      "logl": "warning",
      "proc": "CORE",
      "data": "update_process: process /home/neuron/ /bin/neuron_o_mbstcp was killed by uncaught signal 9 "
    }
  ],
  "last": 400,
  "errc": 0
}
```

| Request  |                                                         |
| -------- | ------------------------------------------------------- |
| **func** | Function code 83                                        |
| **wtrm** | A water mark that copied to the response message        |
| **logl** | Log level,<br> allow text :<br> all,<br> debug,<br> info,<br> warning,<br> err                                                     |
| **srtt** | Sart timestamp(s), default none                         |
| **stpt** | End timestamp(s), default none, must with a nonempty <br> "srtt" if set value for "stpt"                          |
| **srtl** | Start line number of the log file, also can be got from <br> "last" of response message,default 0                    |

| Response |                                                   |
| -------- | ------------------------------------------------- |
| **func** | Function code 83                                  |
| **wtrm** | A water mark that copied from the request message |
| **nrow** | Number of rows, <= 500                            |
| **rows** | Rows of Log content, json array                   |
| **tstp** | log timestamp (s)                                 |
| **logl** | Log level                                         |
| **data** | Log string data                                   |
| **last** | Last line number , useful for "strl" of request message                                           |
| **errc** | Compiler error code                               |

## Function 84 Log Switch

**_Websockets or MQTT Communication_**

**Request body syntax**

```json
{
  "func": 84,
  "wtrm": "DEMO-Neuron-1002_1532419775357_240",
  "logn": "SCRIPTLOG",
  "vars": 100
} 
```

**Response body syntax**
```json
{
  "func": 84,
  "wtrm": "DEMO-Neuron-1002_1532419775357_240",
  "errc": 0
}
```

| Request        |                                                   |
| -------------- | ------------------------------------------------- |
| **func** | Function code 84                                  |
| **wtrm** | A water mark that copied to the response message  |
| **logn** | Log name:<br>SCRIPTLOG<br>DRIVERLOG<br>SERVICELOG             |
| **vars** | Variable for maximum of log lines can be reported |

| Response       |                                                   |
| -------------- | ------------------------------------------------- |
| **func** | Function code 84                                  |
| **wtrm** | A water mark that copied from the request message |
| **errc** | Compiler error code                               |

## License Update HTTP API only

(POST)

Resource Path: /api/v1/license

Content-Type: multipart/form-data

Authorization: Bearer \<token\>

| **HTTP status code** | **Description**      |
| -------------------- | -------------------- |
| 200                  | Successful operation |
| 400                  | Invalid Operation    |

## Error Response

The above gateway responses are assumed the request function are
successfully handled. In case of failure to process the request, the
gateway will return the following error message to the response topic.

**_Error response body syntax_**

```json
{
  "func": 14,
  "wtrm": "DEMO-Neuron-1001_1532419203896_239",
  "errc": 1001,
  "emsg": " Statement expected for this row "
}
```

| Response Compiler Error |                                                               |
| ----------------------- | ------------------------------------------------------------- |
| **func**                | Function code                                                 |
| **wtrm**                | A string that copied from the request message                 |
| **errc**                | Compiler error code                                           |
| **emsg**                | Error code Error text <br>0 , "No Error"<br>2 , "Function no has not found!"<br>3 , "Missing JSON item"<br>4 , "Invalid JSON structure"<br>10 , "Object locked"<br>11 , "Object not found"<br>12 , "Attribute locked"<br>13 , "Attribute not found"<br>14 , "Object number invalid"<br>15 , "Modification not allowed"<br>16 , "Attribute type invalid"<br>20 , "Operation not allowed"<br>21 , "Wrong password"<br>22 , "Wrong user name"<br>23 , "Not super user account"<br>24 , "System function error"<br>25 , "User not found"<br>26 , "Time out"<br>27 , "Default level"<br>28 , "Wrong number of levels"<br>29 , "User already exist"<br>30 , "Too many users"<br>40 , "Alarm not found"<br>41 , "Report empty"<br>42 , "Data format error"<br>43 , "Wrong revision"<br>44 , "Need rebuild file"<br>50 , "Too many global variables"<br>51 , "Global variable name length exceed"<br>52 , "Duplicated Global variables found"<br>53 , "Subroutine number not found"<br>54 , "Subroutine already exist"<br>55 , "No disk space for subroutine"<br>56 , "Search program number error"<br>57 , "No search string"<br>70 , "Wrong status change request"<br>71 , "Wrong gateway control request"<br>72 , "Wrong key"<br>73 , "Function not allowed in SEMI mode"<br>80 , "Attribute read only"<br>81 , "Object name error"<br>82 , "Data range error"<br>502 , "Too many channels"<br>503 , "Channel driver length size exceed maximum"<br>504 , "Channel driver invalid"<br>505 , "Channel driver type invalid"<br>506 , "Too many dummy variables"<br>507 , "Hostname length exceed maximum"<br>508 , "Port number is invalid"<br>509 , "Device file length too long"<br>510 , "Baud rate number is invalid"<br>511 , "Data bit invalid"<br>512 , "Stop bit invalid"<br>513 , "Parity bit invalid"<br>514 , "Too many objects"<br>515 , "Object ID length exceed maximum"<br>516 , "Object name length exceed maximum"<br>517 , "Duplicated object ID found"<br>518 , "Duplicated object name found"<br>519 , "Object size incorrect"<br>520 , "Update time incorrect"<br>521 , "Logging time incorrect"<br>522 , "Object status invalid"<br>523 , "Too many attributes"<br>524 , "Attribute status invalid"<br>525 , "Attribute type incorrect"<br>526 , "Attribute ID length exceed maximum"<br>527 , "Attribute name length exceed maximum"<br>528 , "Duplicated attribute ID found"<br>529 , "Duplicated attribute name found"<br>530 , "Decimal value invalid"<br>531 , "Attribute R/W length exceed maximum"<br>532 , "Attribute object number is not  match"<br>533 , "Attribute object index is not  match"<br>534 , "Prefix length exceed maximum"<br>535 , "Suffix length exceed maximum"<br>536 , "Prefix and Suffix string empty"<br>537 , "Tag address length exceed maximum"<br>538 , "Tag address invalid"<br>539 , "Tag address delimiter invalid"<br>540 , "Dummy sign invalid"<br>541 , "Tag address overlap"<br>542 , "Tag RW direction invalid"<br>543 , "Tag attribute is not match"<br>544 , "Tag bit type is not match"<br>545 , "Tag bit type error"<br>546 , "Tag ix exceed limit"<br>547 , "Tag array member invalid"<br>548 , "Alarm object name length exceed"<br>549 , "Alarm attribute name length  exceed"<br>550 , "Alarm subroutine number not  found"<br>551 , "Alarm category not found"<br>552 , "Alarm attribute not match"<br>553 , "Alarm ID not found"<br>554 , "Alarm type not found"<br>555 , "Alarm object name not found"<br>556 , "Tag name length exceed maximum"<br>557 , "Tag name invalid"<br>558 , "Duplicated tag name found"<br>559 , "Attribute tag length exceed"<br>560 , "Attribute tag not found"<br>561 , "Attribute tag index invalid"<br>562 , "Tag array invalid"<br>563 , "Tag type invalid"<br>564 , "Tag R/W direction invalid"<br>1001, "Statement expected for this row"<br>1002, "Statement does not exist"<br>1003, "INIT follows a normal statement (except REM, INIT)"<br>1004, "THEN expected after test statement"<br>1005, "Unexpected THEN, not a test above"<br>1006, "Unexpected ELIF/ELSE, not a THEN above"<br>1007, "Unknown statement"<br>1008, "GOTO undefined position (POSxxx)"<br>1009, "Error in POSxxx statement"<br>1010, "FATAL! Cannot solve all jump instruction"<br>2001, "Too many local variables in one file"<br>2002, "Syntax error in INIT (only assign local vars)"<br>2003, "INIT: assign (=) expected"<br>2004, "INIT: assign value expected"<br>2005, "INIT: expression delimiter (;) expected"<br>2006, "Syntax error in token"<br>2007, "Too long local variable name"<br>2008, "Syntax error in local variable"<br>2009, "Syntax error in constant"<br>2010, "Too long DB variable name"<br>2011, "Syntax error in [..] construction"<br>2012, "Syntax error in DB variable"<br>2013, "Syntax error in object variable"<br>2014, "Illegal label number"<br>2015, "Illegal subroutine number"<br>2016, "Too long global variable name"<br>2017, "Syntax error in global variable"<br>2018, "Syntax error in [index] construction"<br>2019, "Too long [index] name"<br>2020, "Syntax error in GOTO POSxxx instruction"<br>2021, "Syntax error in CALL SRxxx instruction"<br>2023, "Declaring a control variable"<br>2024, "Declaring too many local variables"<br>2025, "Local variable not declared/not a control variable"<br>2029, "Too long object name"<br>2030, "Too long field name"<br>2101, "Not an executable instruction/variable"<br>2102, "; expected after instruction"<br>2103, "No statement should follow RETURN/GOTO"<br>2104, "= expected after variable for assign"<br>2105, "; not allowed in test or inside parenthesis"<br>2106, "Instruction not allowed in test or inside parenthesis"<br>2107, "Operand expected"<br>2108, "Instruction should be first token in expression"<br>2109, "Operand/expression not expected"<br>2110, "Assign not allowed after test"<br>2111, "Assign variable is read-only"<br>2112, ") unexpected"<br>2113, "Object variable does not exist"<br>2114, "Index of Object variable not inside array"<br>2115, "Tag variable does not exist"<br>2116, "Index of Tag variable not inside array"<br>2117, "Unary used twice on same operand"<br>2118, "Unrecognized operator"<br>2119, "Application part for station does not exist"<br>2120, "Global variable does not exist"<br>2121, "Index of global variable not inside array"<br>2122, ", expected after variable declaration"<br>2123, "Index must be used on variable array"<br>2124, "Index cannot be used on single variable"<br>2125, "Operator is not allowed in double calculation"<br>2132, "Local variable as index is not used before"<br>2201, "Expression not completed"<br>2202, "Expression ended before resolving last parenthesis"<br>2300, "Global variable name too long"<br>2301, "Global variable name have capital letter"<br>2302, "Global variable length too large < 1000"<br>2303, "Global variable comment too long"|