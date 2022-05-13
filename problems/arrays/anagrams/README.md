# anagrams

Write a function, anagrams, that takes in two strings as arguments.
The function should return a boolean indicating whether or not the strings are anagrams.
Anagrams are strings that contain the same characters, but in any order.

test_00:
```py
anagrams('restful', 'fluster') # -> True
```

test_01:
```py
anagrams('cats', 'tocs') # -> False
```

test_02:
```py
anagrams('monkeyswrite', 'newyorktimes') # -> True
```

test_03:
```py
anagrams('paper', 'reapa') # -> False
```

test_04:
```py
anagrams('elbow', 'below') # -> True
```

test_05:
```py
anagrams('tax', 'taxi') # -> False
```

test_06:
```py
anagrams('taxi', 'tax') # -> False
```

test_07:
```py
anagrams('night', 'thing') # -> True
```

test_08:
```py
anagrams('abbc', 'aabc') # -> False
```
