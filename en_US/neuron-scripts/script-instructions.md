# Script Instructions

Following instructions can be used in expressions.

| Instruction | Description                                                                                                                                                                                                                                                           |
| ----------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| RETURN      | This instruction returns from the Neuron program to its calling program. The following part of this program is not executed. RETURN must be the last instruction in an expression.                                                                                    |
| GOTO POSxxx | This instruction continues the execution from the statement that contain the declaration of the label xxx (1-999). GOTO POSxxx must be the last instruction in an expression.                                                                                         |
| CALL SRxxx  | This instruction calls the subroutine xxx (1-999) and executes the program in that subroutine. After completed the program in the subroutine, or executed a RETURN instruction, the execution continues with the instruction / statement that follows the CALL SRxxx. |
| AUTO        | This instruction is to change machine mode from manual mode or service mode to auto mode. Then, it runs auto routine.                                                                                                                                                 |
| MANU        | This instruction is to change machine mode from auto mode or service mode to manual mode. Then, it runs manu routine.                                                                                                                                                 |
| SERV        | This instruction is to change machine mode from auto mode or manu mode to service mode. Then, it runs manu routine.                                                                                                                                                   |
