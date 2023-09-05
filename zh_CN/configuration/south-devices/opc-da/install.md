# 安装 NeuOPC

本例使用 windows 7 SP1 32位系统演示。

## 前置准备

- Windows 7 SP1 以上操作系统
- 安装 [KB3063858](https://www.microsoft.com/zh-CN/download/details.aspx?id=47409) 以及 [KB2999226](https://www.microsoft.com/zh-cn/download/details.aspx?id=49077) 更新程序。

## 安装 NeuOPC

1. 从 Neuron 技术支持人员处获取程序包，或者进入 NeuOPC [项目页面](https://github.com/neugates/neuopc)下载源码后使用Visual Studio 2022编译。

   ![package](./assets/package.png)

   其中：

   * `neuopc.exe`——运行 OPC DA 转换 OPC UA 的主程序。
   * `OPC Core Components Redistributable (x64) 3.00.108.msi` ——OPC 基金会官方组件，64 位操作系统安装。
   * `OPC Core Components Redistributable (x86) 3.00.108.msi` ——OPC 基金会官方组件，32 位操作系统安装。

2. 安装对应版本的 OPC Core Components Redistributable (x86) 3.00.108 组件。

3. 双击 neuopc.exe 启动 NeuOPC 主程序。![local-neuopc](./assets/local-neuopc1.png) ![local-neuopc](./assets/local-neuopc2.png) 

4. 参考 **NeuOPC 远程访问** 第二节 **本地主机 DCOM 设置**，可实现对本地模拟器的访问。



