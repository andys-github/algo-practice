# Arrays

## Array Operations

1. Adding an element:
   - Element is added at the end with complexity of &Omicron;(1)
   - When the array size is full, resizing is done which takes &Omicron;(n)
   - There is a trade-off between:
     - allocating a large size in the beginning __(wastage of memory, but no worries for resizing)__ and 
     - resizing whenever needed (no wastage of memory, but resizing takes considerable linear time complexity)
