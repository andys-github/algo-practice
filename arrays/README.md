# Arrays

## Array Operations

- _Adding an element at the end: **&Omicron;(1)**_
   - Element is added at the end with complexity of &Omicron;(1)
   - When the array size is full, resizing is done which takes &Omicron;(n)
   - There is a trade-off between:
     - allocating a large size in the beginning (_wastage of memory, but no worries for resizing_) and 
     - resizing whenever needed (_no wastage of memory, but resizing takes considerable linear time complexity_)

- _Inserting an element at arbitrary position: **&Omicron;(n)**_
   - First other elements are shifted to their next location, making a space for the new element
   - Then the new element is inserted.
   - This operation takes &Omicron;(n) running time.
