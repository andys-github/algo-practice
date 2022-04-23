# Arrays

## Array Operations

1. Adding an element at the end: **&Omicron;(1)**
   - Element is added at the end with complexity of &Omicron;(1)
   - When the array size is full, resizing is done which takes &Omicron;(n)
   - There is a trade-off between:
     - allocating a large size in the beginning __(wastage of memory, but no worries for resizing)__ and 
     - resizing whenever needed (no wastage of memory, but resizing takes considerable linear time complexity)

1. Inserting an element at arbitrary position: **&Omicron;(n)**
   - First other elements are shifted to their next location, making a space for the new element
   - Then the new element is inserted.
   - This operation takes &Omicron;(n) running time.
