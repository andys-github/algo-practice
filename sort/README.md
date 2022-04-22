# Sorting Algorithms

## Bubble Sort


<br />

## Insertion Sort
> **NOTE:**
> Insertion Sort performs really well when we insert a new element to an already sorted array

<br />

## [Selection Sort](https://github.com/andys-github/algo-practice/blob/main/sort/selection-sort.py)
#### TC: O(n<sup>2</sup>), SC: O(1)
> **GIST:** Start with an element, and run through each subsequent elements, and swap if one of them is smaller. Repeat for the next element.

<table>
  <thead>
    <tr>
      <th colspan="4">S E L E C T I O N &nbsp;&nbsp;&nbsp; S O R T
    </tr>
    <tr>
      <th colspan="3">Time Complexity</th>
      <th colspan="1" rowspan="2">Space Complexity</th>
    </tr>
    <tr>
      <th>Best Case</th>
      <th>Avg Case</th>
      <th>worst Case</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>O(n<sup>2</sup>)</td>
      <td>O(n<sup>2</sup>)</td>
      <td>O(n<sup>2</sup>)</td>
      <td>O(1)</td>
    </tr>
  </tbody>
</table>

In Selection Sort:
- We maintain two pointers - one is fixed at an element, and the other one moves through the remaining elements
- After every pass, we compare the elements these two pointers hold
- If the second one is smaller than the first, we swap
- This continues till the last element

Each 'nth' element takes about (n - 1) run throughs. So the overall complexity comes around O(n) * O(n - 1), which becomes **O(n^2) time complexity**.
And since the swapping takes place in the input array itself, we have a **O(1) space complexity**.

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
> TC: **O(n log n)**, SC: **O(n)**

In Merge sort:
- We keep on halving the input array till we are left with a single element array or an empty array
- Then we start merging these atomic arrays by comparing the elements within it.

Halving the array is of **O(log n)** complexity, and since we need to half it and then combine the halves, we take about **O(n) time for each half**. Thus the total time-complexity is **O(n log n)**


<br />

## [Radix Sort](https://github.com/andys-github/algo-practice/blob/main/sort/radix-sort.py)

<br />
