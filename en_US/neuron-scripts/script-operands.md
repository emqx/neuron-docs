# Script Operands

## Local variables

A local variable is a variable that only the current script can use and must be declared by &quot;DECLARE&quot; comment. When starting the program, the variable gets the value 0. When a Neuron script ends (returns), all local variables are disconnected, so next time this script starts again, all its local variables are 0. To save data until next execution time, global variables should be used.

A local variable is a lower-case letter name. \_ and digits (except as first characters) can also be used as a part of the name. The name can consist up to 30 characters.

## Global variables

A global variable is a variable that all Neuron scripts can use and must be defined in global variables setup environment. When starting the Neuron program, the variable gets the value 0. When the Neuron program ends, all global variables are disconnected, so next time the Neuron program starts, all its global variables are 0 again. To save data until next execution time, data base variables should be used.

A global variable starts with the upper-case letter G followed by a dot and a lower-case letter name. \_ and digits (except as first characters) can also be used as a part of the name. The name can consist up to 20 characters (except the leading G.).

Global variables can be used with an index. When declaring a global variable, also the number of words is entered. Attempt to try to address outside the array will fail.

## Object variables

An object variable is the attribute of object. It can be used thought all the Neuron subroutines. When starting the Neuron instance, the variable gets the previous value. When the Neuron instance ends, all tag variables are saved on the hard disk for next start.

An object variable consists of three elements. The first element is the object name. For example, temperature object can use &quot;SENSORA&quot; as its object name. humidity object can use &quot;SENSORB&quot; as its object name.

Second, there is a constant inside [] called object index which can be a local variable. This number represents the item index of the objects.

The last element is the attribute of the object. An object can have as many as attribute field. Each field contains one unique field name called attribute name. For example, the actual temperature of object SENSORA can use &quot;TEMPERATURE&quot; as attribute name.

Therefore, the actual temperature of temperature object would be SENSORA[ix].TEMPERATURE. This is the object variable.

## Constants

A constant is numeric value in the range -2,147,483,648 to 2,147,483,647. The constant can be a signed decimal (as above), unsigned hexadecimal in case of a leading 0x (0x0 to 0xffffffff) or unsigned octal in case of a leading 0 (0 to 037777777777). A constant with decimal place is also accepted as a double value in script. For example, pi is 3.1415. Script constant supports two value type.

## System variables

In the system, there are some system global variables that are used by the system. A system global variable is a global variable, with its syntax. The variables are prepared/used every time before starting the main program.

| Variable    | Description                                                                                                              |
| ----------- | ------------------------------------------------------------------------------------------------------------------------ |
| G.time      | This variable returns the current time. The value is the standard UNIX time (number of seconds since 00:00 Jan 1, 1970). |
| G.year      | This variable returns the current year.                                                                                  |
| G.month     | This variable returns the current month.                                                                                 |
| G.day       | This variable returns the current day of the month.                                                                      |
| G.hour      | This variable returns the current hour of the day.                                                                       |
| G.min       | This variable returns the current minute of the hour.                                                                    |
| G.dayofweek | This variable returns the current day of the week (1-7, 1 is Monday etc.).                                               |
| G.mode      | This variable returns the current machine running mode (1 – auto, 2 – manu, 3 – serv)                                    |
