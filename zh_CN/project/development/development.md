# 开始开发

## 分支

本项目有一个主分支，即 ```master```，请确保 ```master``` 在任一时刻都是可编译可使用的。同时本项目还有不同版本对应的分支，您可以自行选择分支进行开发。

## 修改代码

请注意代码的可读性。
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
 1. 先 Fork 本项目，创建自己的 github.com/your/neuron 仓库；
 2. 克隆自己的 neuron 仓库到本地：```git clone https://github.com/your/neuron.git```；
 3. 例如基于 ```master``` 分支创建新的分支；
 4. 在新创建的分支上作修改并提交修改；
 5. 在推送修改完成的分支到自己的仓库前，先切换到 ```master``` 分支，运行```git pull https://github.com/emqx/neuron.git```拉取最新的远端代码；
 6. 如果上一步拉取得到了新的远端代码，则切换到之前自己创建的分支，运行```git rebase master```执行分支合并操作。如遇到文件冲突，则需要解决冲突；
 7. 上一步处理完毕后，就可以把自己创建的分支推送到自己的仓库：```git push origin master```;
 8. 最后，把自己仓库的新推送的分支往emqx/neuron对应的分支发 PR 即可；
* 请在 PR 的标题和正文中，完整表述此次 PR 解决的问题/新增的功能/代码所做的修改的用意等；
* 请耐心等待开发者的回应，我们将很快进行回复。