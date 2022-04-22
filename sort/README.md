# Sorting Algorithms

## Bubble Sort



## Insertion Sort
> Insertion Sort performs really well 
> when we insert a new element to an already sorted array

## Selection Sort


## Comparison between the Quadratic Sorts
<table>
  <thead>
    <tr>
      <th>Sorting Algorithm</th>
      <th colspan="3">Time Complexity</th>
      <th>Space Complexity</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Bubble</td>
      <td>O(n)</td>
      <td>O(n ^ 2)</td>
      <td>O(n ^ 2)</td>
      <td>O(1)</td>
    </tr>
    <tr>
      <td>Insertion</td>
      <td>O(n)</td>
      <td>O(n ^ 2)</td>
      <td>O(n ^ 2)</td>
      <td>O(1)</td>
    </tr>
    <tr>
      <td>Selection</td>
      <td>O(n ^ 2)</td>
      <td>O(n ^ 2)</td>
      <td>O(n ^ 2)</td>
      <td>O(1)</td>
    </tr>
  </tbody>
</table>

> With nearly sorted data,
> Bubble and Insertion perform well

## Quick Sort

## Merge Sort
#### Gist: Keep halving input array, and merge all the atomic arrays
In Merge sort, we keep on halving the input array till we are left with a single element array or an empty array. Then we start merging these atomic arrays by comparing the elements within it.
<br />
Halving the array is of **O(log n)** complexity, and since we need to half it and then combine the halves, we take about **O(n) time for each half**. Thus the total time-complexity is **O(n log n)**
<br />

## Radix Sort
