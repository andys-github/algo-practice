# befitting brackets

Write a function, befitting_brackets, that takes in a string as an argument. The function should return a boolean indicating whether or not the string contains correctly matched brackets.

You may assume the string contains only characters: ( ) [ ] { }

test_00:
```py
befitting_brackets('(){}[](())') # -> True
```

test_01:
```py
befitting_brackets('({[]})') # -> True
```

test_02:
```py
befitting_brackets('[][}') # -> False
```

test_03:
```py
befitting_brackets('{[]}({}') # -> False
```

test_04:
```py
befitting_brackets('[]{}(}[]') # -> False
```

test_05:
```py
befitting_brackets('[]{}()[]') # -> True
```

test_06:
```py
befitting_brackets(']{}') # -> False
```

test_07:
```py
befitting_brackets('') # -> True
```

test_08:
```py
befitting_brackets("{[(}])") # -> False
```
