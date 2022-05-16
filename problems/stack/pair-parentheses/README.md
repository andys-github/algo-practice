# pair parentheses

Write a function, paired_parentheses, that takes in a string as an argument. The function should return a boolean indicating whether or not the string has well-formed parentheses.

You may assume the string contains only alphabetic characters, '(', or ')'.

test_00:
```py
paired_parentheses("(david)((abby))") # -> True
```

test_01:
```py
paired_parentheses("()rose(jeff") # -> False
```

test_02:
```py
paired_parentheses(")(") # -> False
```

test_03:
```py
paired_parentheses("()") # -> True
```

test_04:
```py
paired_parentheses("(((potato())))") # -> True
```

test_05:
```py
paired_parentheses("(())(water)()") # -> True
```

test_06:
```py
paired_parentheses("(())(water()()") # -> False
```

test_07:
```py
paired_parentheses("") # -> True
```

test_08:
```py
pairedParentheses("))()") # False
```
