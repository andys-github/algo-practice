# Sorting Algorithms

## Bubble Sort


<br />

## Insertion Sort
> **NOTE:**
> Insertion Sort performs really well when we insert a new element to an already sorted array

<br />

## Selection Sort

<br />

### Comparison between the Quadratic Sorts
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

<br />

> With nearly sorted data, Bubble and Insertion sorts perform well

<br />

## [Quick Sort](https://github.com/andys-github/algo-practice/blob/main/sort/quick-sort.py)


<br />

## [Merge Sort](https://github.com/andys-github/algo-practice/blob/main/sort/merge-sort.py)
> **Gist:** Keep halving input array, and merge all the atomic arrays. 
> TC: **O(n log n)** - SC: **O(n)**

In Merge sort:
- We keep on halving the input array till we are left with a single element array or an empty array
- Then we start merging these atomic arrays by comparing the elements within it.

Halving the array is of **O(log n)** complexity, and since we need to half it and then combine the halves, we take about **O(n) time for each half**. Thus the total time-complexity is **O(n log n)**


<br />

## [Radix Sort](https://github.com/andys-github/algo-practice/blob/main/sort/radix-sort.py)

<br />
