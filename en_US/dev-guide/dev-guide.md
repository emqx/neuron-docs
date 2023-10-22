# Development Guide

## Code Structure

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

## Coding Guide

Neuron code follows the principle of high readability and has the following specification requirements:

* Macros are all uppercase, except for macros, which are all lowercase.
* Variables, functions, structures, and other names are meaningful English words separated by underscores.
* Maintain a good naming style, and be able to make naming a comment without adding invalid comments.
* Each C file should be the smallest set of strongly related functions.
* Only functions and variables that need to be exported externally are added to the header file.
* Neuron uses clang format for code formatting, and the clang format file is located in the Neuron root directory.
* Functions should be as short as possible. Each function only implements one function. The logic of the function is clear (it can be easily understood by looking at previously written code after a period of time), and the maximum length of the function should not exceed 80 lines.

## Branch

This project has a main branch, `main`. Please ensure that `main` is compiled and usable at any time. At the same time, there are branches corresponding to different versions of this project, and you can choose your own branches for development.

## Modify Code

For functional issues, please submit at least one test case to verify changes to existing functionality; For performance related issues, please submit necessary test data to prove the performance defects of existing code or the performance improvement of new code.
Please perform tests before each push.

### Unit testing

Run all unit tests

```shell
$ cd build
$ ctest --output-on-failure
```

### Functional testing

Run all functional tests

```shell
$ sudo apt-get install -y mosquitto
$ mosquitto -v &
$ python3 -m pip install -U pip
$ python3 -m pip install -r ft/requirements.txt
$ python3 -m robot --maxerroelines=600 -P ft/ -d ft/reports ft
```

## Pull Request

* A PR only does one thing. If there are multiple bug fixes, please submit a PR for each bug;
* The PR process is as follows:

  * First, fork this project and create your own github.com/your/neuron warehouse;
  * Clone your own Neuron warehouse to the local location:
  ```bash
  $ git clone https://github.com/your/neuron.git 
  ```
  * For example, create a new branch based on the `main` branch;
  * Make changes on the newly created branch and submit the changes;
  * Before pushing the modified branch to your own warehouse, switch to the `main` branch and run the following command to pull the latest remote code:
  ```bash
  $ git pull https://github.com/emqx/neuron.git
  ``` 
  * If the new remote code is retrieved in the previous step, switch to the previously created branch and run branch merge operation.
  ```bash
  $ git rebase main
  ```
  If you encounter a file conflict, you need to resolve the conflict;
  * After the previous step is completed, you can push the branch you created to your own warehouse:
  ```bash
  $ git push origin main
  ```
  * Finally, send a PR to the corresponding branch of emqx/neuron from the newly pushed branch of your warehouse;

* Provide a complete description of the problems solved/new features added/the intent of the modifications made to the code in the title and text of the PR;
* Wait patiently for the developer's response, and we will respond soon.

## Debugging

1. Use logs to print relevant debugging information.
2. Because Neuron is a multithreaded asynchronous concurrent program, it is not recommended to use GDB for breakpoint debugging, etc.
3. Combining libasan runtime memory analysis, most memory issues can be resolved.

:::tip
Libasan refers to the Address Sanitizer (ASan) library, which is a memory error detection tool used to help detect memory errors during program execution, such as buffer overflows, using freed memory, and using uninitialized memory.<br>
ASan detects memory errors by injecting additional code while the program is running. It uses a red and black tree data structure to track the allocation of memory blocks, and uses shadow memory to detect read and write access to unallocated memory. When a memory error is detected, ASan prints relevant information, such as the location and type of the error.<br>
Libasan is a runtime library for ASan that can be used with compilers, such as Clang, GCC, and so on. It provides the necessary functions and data structures to detect and report memory errors during program execution.
:::