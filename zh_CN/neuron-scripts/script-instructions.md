# 脚本指令

下面的指令可以被用在表达式中。

| 指令        | 描述                                                                                                                                           |
| ----------- | ---------------------------------------------------------------------------------------------------------------------------------------------- |
| RETURN      | 该指令从 Neuron 程序返回到其调用程序。该程序的下面部分不执行。RETURN 必须是一个表达式中的最后一条指令。                                        |
| GOTO POSxxx | 该指令从包含标签 xxx（1-999）声明的语句开始继续执行。GOTO POSxxx 必须是一个表达式中的最后一条指令。                                            |
| CALL SRxxx  | 该指令调用子程序 xxx（1-999），并执行该子程序中的程序。在完成子程序中的程序，或执行了一条 RETURN 指令后，继续执行 CALL SRxxx 后面的指令/语句。 |
| AUTO        | 该指令将机器模式从手动模式或服务模式改为自动模式。然后，运行自动程序。                                                                         |
| MANU        | 该指令将机器模式从自动模式或服务模式改为手动模式。然后，运行手动程序。                                                                         |
| SERV        | 该指令将机器模式从自动模式或手动模式改为服务模式。然后，运行手动程序。                                                                         |
