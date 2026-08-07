# Mazak 设备端配置

本指南介绍如何配置 Mazak CNC 通过 UDP 发送运行数据，以便 Neuron Mazak CNC 插件采集。通信依赖于 Mazak 控制器 Windows PC 上运行的 **Mazak Fusion Client** 应用程序。

## 适用控制器

以下 Mazak 控制器类型受支持：

- **Fusion 640**（可能需要 16-bit PCMCIA 网卡）
- **Matrix**
- **Nexus**
- **Preview 3**
- **Smooth**

::: warning
**Preview G**、**Smooth G** 和 **Smart** 控制器需要使用 MTConnect 而非 Fusion Client。请联系 Mazak 购买 MTConnect 许可证。
:::

## 准备工作

开始配置前，请确保以下条件已满足：

1. **Mazak 设备要求：**
   - 带有 Windows PC 的 Mazak 控制器
   - 网络连接（以太网）
   - 已为机床分配静态 IP 地址或 DHCP 保留地址
   - Mazak Fusion Client 应用程序（版本 2.1 或以上）
2. **网络要求：**
   - Neuron 主机能够访问 Mazak CNC 的 IP 地址
   - 防火墙需放行 **UDP 端口 51001**（入站和出站）
   - Neuron 与 Mazak CNC 之间双向通信
3. **访问权限要求：**
   - Mazak 控制器 Windows PC 的管理员权限
   - 能够安装和配置 Fusion Client 应用程序

## 访问 Windows 桌面

Fusion Client 运行在 Mazak 控制器的 Windows 系统上。访问 Windows 桌面的方法因控制器类型而异。

### Nexus、Fusion 和 Matrix 控制器

1. 使用方向键或手轮将光标移动到**屏幕左下角**，尽可能移动到最远处。
2. 左键点击，从底部调出 Windows 任务栏。

### Smooth 控制器

1. 点击屏幕右上角的**齿轮图标**。
2. 选择 **Setup**，然后选择 **Show Windows**。如果没有弹出窗口，请重复此步骤——有时需要尝试两次。
3. 从屏幕右侧向内滑动，调出 Windows 菜单。

## 安装和启动 Fusion Client

### 步骤一：启动 Fusion Client

1. 在 Windows 资源管理器中进入 `C:\CPCU\fmcnc` 目录。
2. 双击 `FusionClient.exe`。
3. 应用程序将启动并出现在 Windows 系统托盘（右下角）中。

> **注意：** 如果机床设备上没有 `C:\CPCU` 文件夹，请联系 Mazak 获取 Fusion Client 应用程序。

### 步骤二：打开 Fusion Client 设置

1. 在 Windows 系统托盘中找到 Fusion Client 图标。
2. 双击 Fusion Client 图标，打开配置窗口。

## 配置连接

### 步骤一：配置连接参数

1. 在 Fusion Client 配置窗口中，点击 **Change Settings**。
2. 点击 **Add** 创建新的连接。
3. 输入以下信息：

| 参数                   | 说明                                 |
| ---------------------- | ------------------------------------ |
| **Network Name**       | 留空。                               |
| **IP Address**         | 输入 **Neuron 主机的静态 IP 地址**。 |
| **UDP Receive Port**   | 输入 `51001`。                       |
| **Host Compatibility** | 从下拉菜单中选择 **Level 4**。       |

4. 点击 **OK** 或 **Apply** 保存连接设置。

### 步骤二：配置参数选项

1. 在 Fusion Client 主菜单中，进入 **Parameter** 选项卡。
2. **取消勾选 Close Button** 复选框，防止 Fusion Client 被意外关闭。
3. 点击 **OK** 或 **Apply**。

### 步骤三：配置 Windows 防火墙

如果 Mazak CNC 的 Windows 防火墙处于启用状态，需配置防火墙放行 UDP 端口 51001。

| 设置         | 值                  |
| ------------ | ------------------- |
| **协议**     | UDP                 |
| **端口**     | 51001               |
| **方向**     | 入站和出站          |
| **源地址**   | Neuron 主机 IP 地址 |
| **目标地址** | Mazak CNC IP 地址   |

如果不需要防火墙，也可以直接禁用防火墙。

## 验证网络连通性

配置完成后：

1. 从 Neuron 主机 ping Mazak CNC 的 IP 地址，验证基本网络连通性：
   ```shell
   ping <MAZAK_CNC_IP_ADDRESS>
   ```
2. 确认 Mazak CNC 能够访问 Neuron 主机。
3. 确认两台设备之间 UDP 端口 51001 已开放。

验证通过后，在 Neuron 端配置 Mazak CNC 插件。详情请参考 [Mazak CNC](./mazak-udp.md)。

## 故障排查

### 未收到数据

**可能原因：**
- Fusion Client 未运行
- Fusion Client 中配置的 IP 地址不正确
- 防火墙阻止了连接
- Fusion Client 版本过旧

**解决方法：**
1. 确认 Fusion Client 正在运行（检查 Windows 系统托盘）。
2. 检查 Fusion Client 中配置的 IP 地址是否与 Neuron 主机 IP 地址一致。
3. 确认防火墙已放行 UDP 端口 51001 的双向通信。
4. 检查 Fusion Client 版本——2.1 以下版本可能无法正常工作。

### 任务栏中找不到 Fusion Client 图标

如果系统托盘中看不到 Fusion Client 图标：

- 进入 `C:\CPCU\fmcnc` 目录，双击 `FusionClient.exe` 启动程序。
- 如果目录或程序文件缺失，请联系 Mazak 获取 Fusion Client 应用程序。

### 设备状态显示为断开

**可能原因：**
- 网络中断
- Fusion Client 已停止运行
- IP 地址发生变更

**解决方法：**
1. 检查网络连通性。
2. 重新启动 Fusion Client 应用程序。
3. 重启机床控制器的 Windows PC。
4. 确认 Mazak CNC 已分配静态 IP 地址。
5. 检查 Neuron 主机能否访问 Mazak CNC 的 IP 地址。
