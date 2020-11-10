# Script Expressions

An expression can be either a test expression or an action expression. An expression can occupy several rows. Several action expressions can be separated by a &quot;;&quot;.

A test expression is an expression that returns a value. It can only be used in an IF or ELSE IF statement, or in an assignment (&quot;variable = test expression&quot;). Note that an assignment can be used in an IF or ELSE IF statement, where the test will be if the value is zero (false) or non-zero (true).

Examples of test expression:

| COMMENT | call subroutine 10 if var is greater than 5 |
| ------- | ------------------------------------------- |
| IF      | var \&gt; 5                                 |
| THEN    | CALL SR10;                                  |
|         |                                             |
| COMMENT | increment loop index and compare if         |
|         | loop is finished, otherwise go back         |
| IF      | (ix = ix + 1) \&lt; 10                      |
| THEN    | GOTO POS10;                                 |
|         |                                             |
| COMMENT | check if flag variable is true              |
|         | (non-zero), then clear flag and take action |
| IF      | readyflag                                   |
| THEN    | readyflag = 0; CALL SR20;                   |

An action expression is an assignment or an instruction. Several assignments can be performed after each other.

| COMMENT | return if all is done     |
| ------- | ------------------------- |
| IF      | alldone                   |
| THEN    | RETURN;                   |
|         |                           |
| COMMENT | several assignments       |
| DO      | var1 = var2 = var3 \* 10; |
