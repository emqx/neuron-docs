# 开发指南

## 代码结构

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

其中`cmake`存放交叉编译文件，`ft`存放功能测试文件，`include`存放对外头文件，`plugins`存放南向插件，`simulator`存放 modbus 模拟器相关文件， `tests`存放单元测试文件。

## 编码规范

Neuron 代码以高可读性为原则，有以下规范要求：

  * 宏全大写，除了宏，其他均使用小写。
  * 变量，函数，结构体等名字是有用意义的英文单词，单词间用下划线隔开。
  * 保持良好的命名风格，能做到命名即注释，不添加无效的注释。
  * 每个 C 文件应该是一类强相关功能的最小集合。
  * 只有需要对外导出的函数，变量等，才添加到头文件中。
  * Neuron 使用 clang-format 进行代码格式化，clang-format 文件在 Neuron 根目录。
  * 函数尽可能的短小，一个函数只实现一个功能，函数逻辑清晰（一段时间后再去看之前写过的代码，也能很容易看懂），函数最长不超过 80 行。

## 分支

本项目有一个主分支，即 ```main```，请确保 ```main``` 在任一时刻都是可编译可使用的。同时本项目还有不同版本对应的分支，您可以自行选择分支进行开发。

## 修改代码

对于功能性问题请提交至少一个测试用例来验证对现有功能的改动；对于性能相关问题请提交必要的测试数据来证明现有代码的性能缺陷，或是新增代码的性能提升。
在每一次 push 前，请先进行测试。

### 单元测试

运行所有的单元测试

```shell
$ cd build
$ ctest --output-on-failure
```

### 功能测试

运行所有的功能测试

```shell
$ sudo apt-get install -y mosquitto
$ mosquitto -v &
$ python3 -m pip install -U pip
$ python3 -m pip install -r ft/requirements.txt
$ python3 -m robot --maxerroelines=600 -P ft/ -d ft/reports ft
```

## Pull Request

* 一个 PR 只做一件事，如果有多个 bug 的修复，请对每一个 bug 提交一个 PR；
* PR 流程如下：

    * 先 Fork 本项目，创建自己的 github.com/your/neuron 仓库；<br>
    * 克隆自己的 neuron 仓库到本地：
    ```bash
    $ git clone https://github.com/your/neuron.git
    ```
    * 例如基于 ```main``` 分支创建新的分支；<br>
    * 在新创建的分支上作修改并提交修改；<br>
    * 在推送修改完成的分支到自己的仓库前，先切换到 ```main``` 分支，运行如下指令拉取最新的远端代码：
    ```bash
    $ git pull https://github.com/emqx/neuron.git
    ```
    * 如果上一步拉取得到了新的远端代码，则切换到之前自己创建的分支，运行如下指令执行分支合并操作：
    ```bash
    $ git rebase main
    ```
    如遇到文件冲突，则需要解决冲突；<br>
    * 上一步处理完毕后，就可以把自己创建的分支推送到自己的仓库：
    ```bash
    $ git push origin main
    ```
    * 最后，把自己仓库的新推送的分支往 emqx/neuron 对应的分支发 PR 即可；

* 在 PR 的标题和正文中，完整表述此次 PR 解决的问题/新增的功能/代码所做的修改的用意等；
* 耐心等待开发者的回应，我们将很快进行回复。

## 调试

1. 使用日志，打印相关调试信息
2. 因 Neuron 是多线程异步并发的程序，不推荐使用 GDB 进行断点调试等。
3. 结合 libasan 运行时内存分析，可调式大部分内存问题。

:::tip
libasan 是指 AddressSanitizer（ASan）库，是一种内存错误检测工具，用于帮助发现程序运行时的内存错误，如缓冲区溢出、使用已释放的内存、使用未初始化的内存等。
ASan 在程序运行时，通过注入额外的代码来检测内存错误。它使用了一种红黑树数据结构来跟踪内存块的分配情况，并使用影子内存来检测对未分配内存的读写访问。当检测到内存错误时，ASan 会打印相关信息，例如出错位置、错误类型等。
libasan 是 ASan 的运行时库，可与编译器配合使用，如 Clang、GCC 等。它提供了必要的函数和数据结构，以便在程序执行期间进行内存错误检测和报告。
:::