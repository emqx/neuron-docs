# Script Statements {#endpoint-script-statements}

The statements are in the left column in object programming editor. Those statements perform the expression of the Neuron programs. Everything in the right column to the right of the statement (and on next row(s) if no new statement) belongs to this statement.

### COMMENT {#endpoint-comment}

This statement does not mean anything for the system. This is only comments for the operator. It can also be used to temporarily remove other statement to avoid some action.

Example:

| COMMENT | \*\*\* This is a comment to describe   |
| ------- | -------------------------------------- |
|         | \*\*\* how to use a COMMENT statement. |

### DECLARE {#endpoint-declare}

For all local variables, it should be declared before it can be used in the subroutine. All local variables are used in local script only.

### POS {#endpoint-pos}

This statement marks a label number (1-999) at this location, which can be used for a GOTO instruction (see below). There is no action taken when reaching this statement. The text in the right column is treated as a comment.

Example:

| COMMENT |                                |
| ------- | ------------------------------ |
| POS120  | \* goto here if end of routine |

### DO {#endpoint-do}

This statement executes its expressions unconditionally. The expressions are separated with &quot;;&quot;.

Example:

| COMMENT | \*\*\* call subroutine with parameters |
| ------- | -------------------------------------- |
| DO      | valuein = 12; CALL SR210;              |

### IF-THEN-ELSEIF-THEN-ELSE {#endpoint-if-then}

This statement executes its expressions conditionally. The expressions are separated with &quot;;&quot;.

The complete syntax is IF expression THEN action expression; action expression; ELSE IF expression THEN action expression; action expression; ELSE action expression; action expression;

If the IF expression is true (non-zero), the system executes the expressions after THEN and then skip the rest of the IF-THEN-ELSE statement.

If the IF expression is false (zero), the system skips the THEN statement and look for a ELSE or ELSE IF statement (if any). If next statement is ELSE IF, the system treats it as an IF statement (beginning of a IF-THEN-ELSE). If next statement is ELSE, the system executes the expressions.

Example:

| COMMENT | \*\*\* check st number 10 and 25 |
| ------- | -------------------------------- |
| IF      | st == 10                         |
| THEN    | st = 11;                         |
| ELSE IF | st == 25                         |
| THEN    | st = 26;                         |
