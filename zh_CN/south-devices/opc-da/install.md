# NeuOPC 安装

本例使用 windows 7 SP1 32位系统演示

::: tip
NeuOPC 只能运行于 Windows 7 SP1 以上操作系统，并且需安装 [KB3063858](https://www.microsoft.com/zh-CN/download/details.aspx?id=47409) 和 [KB2999226](https://www.microsoft.com/zh-cn/download/details.aspx?id=49077) 两个更新程序。
:::

## NeuOPC 运行环境安装

1. 进入 NeuOPC [项目 releases 页面](https://github.com/neugates/neuopc/releases)下载最新的组件包"neuopc-package.zip"，解压后可见如下文件：

![package](./assets/package.png)

* `neuopc.exe`——运行 OPC DA 转换 OPC UA 的主程序。
* `dotnetfx-1.1`——.Net framework 1.1，安装 OPC DAAuto 需要先正确此程序。
* `OPC DA Auto 2.02 Source Code 5.30.msi` ——OPC 基金会官方组件，使用"Windows任务管理器"安装。
* `OPC Core Components Redistributable (x64) 3.00.108.msi` ——OPC 基金会官方组件，可不用安装。
* `OPC Core Components Redistributable (x86) 3.00.108.msi` ——OPC 基金会官方组件，可不用安装。

2. 检查是否已经安装过 .Net framework 1.1 ，如果没有则安装 `dotnetfx-1.1`。

3. 使用任务管理器安装 `OPC DA Auto 2.02 Source Code 5.30.msi`，打开 **Windows 任务管理器** -> **文件** -> **运行新任务**，输入MSI文件路径，勾选 `以系统管理权限创建此任务`。

![install-auto](./assets/install-auto.png)

4. 检查组件是否已安装。

* 如果是32位操作系统，则进入到 `C:\Windows\System32` 目录下，如果是64位操作系统，则进入到 `C:\Windows\SysWOW64` 目录下，检查是否有如下文件存在：

![core-components](./assets/core-components.png)

::: tip
如果文件不存在则联系销售人员进行支持。
:::

* 打开 **Windows 任务管理器** 检查 `OpcEnum` 系统服务是否在运行，如图：

![opcenum](./assets/opcenum.png)

::: tip
如果正常运行，说明 `OPC DA Auto 2.02` 已经正常安装。
:::

5. 本机安装 MatrikonOPCSimulation 模拟器程序，如果安装失败可安装KepServerEX测试。

6. 运行 neuopc.exe 程序，选择 `DA Host` 和 `DA Server` 后点击 `Connect`，设置 UA 的各项参数后点击 `Run`，运行成功，如图：

![local-neuopc](./assets/local-neuopc.png)
