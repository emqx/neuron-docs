# Coding specification

## Code structure

```
neuron
├── cmake
├── deploy
├── ft
├── include
├── persistence
├── plugins
├── simulator
├── src
└── tests
```

`cmake` stores cross compiled files, `ft` stores functional test files, `include` stores external header files, `plugins` stores southbound plug-ins, `simulator` stores modbus simulator related files, and `tests` stores unit test files.

## Coding specification

Neuron code follows the principle of high readability and has the following specification requirements:

* Macros are all uppercase, except for macros, which are all lowercase.
* Variables, functions, structures, and other names are meaningful English words separated by underscores.
* Maintain a good naming style, and be able to make naming a comment without adding invalid comments.
* Each C file should be the smallest set of strongly related functions.
* Only functions and variables that need to be exported externally are added to the header file.
* Neuron uses clang format for code formatting, and the clang format file is located in the Neuron root directory.
* Functions should be as short as possible. Each function only implements one function. The logic of the function is clear (it can be easily understood by looking at previously written code after a period of time), and the maximum length of the function should not exceed 80 lines.