# Neuron 编码规范

## 代码结构

```
neuron
├── build
├── cmake
├── deploy
├── ft        //功能测试
├── include
├── persistence
├── plugins   //南向插件
├── simulator //modbus 模拟器
├── src
└── tests     //单元测试
```

## 编码规范

### 命名

* 文件和目录名尽量使用单个英文单词，比如 main.c；
 1. 特殊情况下目录使用连接线/文件名使用下划线连接两个或多个单词，比如 hello-world/hello_again.c；
 2. 测试代码使用 _test.cc 结尾。
* 类型命名小写，单词间使用下划线连接；
* 变量（包括函数参数）和数据成员名小写，单词之间用下划线连接；
* 常量大写，单词之间用下划线连接；
* 函数名小写，单词之间使用下划线连接；
 