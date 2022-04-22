# Sorting Algorithms

<!--TOC------------------------------------------------------------------------>
## Table of Contents
- [Bubble Sort](https://github.com/andys-github/algo-practice/edit/main/sort/README.md#bubble-sort)
- [Insertion Sort](https://github.com/andys-github/algo-practice/edit/main/sort/README.md#insertion-sort)
- [Selection Sort](https://github.com/andys-github/algo-practice/edit/main/sort/README.md#selection-sort)
- [Comparison of Quadratic Sorts](https://github.com/andys-github/algo-practice/edit/main/sort/README.md#comparison-between-the-quadratic-sorts)
- [Quick Sort](https://github.com/andys-github/algo-practice/edit/main/sort/README.md#quick-sort)
- [Merge Sort](https://github.com/andys-github/algo-practice/edit/main/sort/README.md#merge-sort)
- [Radix Sort](https://github.com/andys-github/algo-practice/edit/main/sort/README.md#radix-sort)

<!--TOC ends------------------------------------------------------------------->

<hr />

<!--Bubble Sort---------------------------------------------------------------->
## [Bubble Sort](https://github.com/andys-github/algo-practice/blob/sort/sort/bubble-sort.py)
> **Gist:** Compare two adjacent numbers, and swap, if needed. Do it till the end of array. Repeat 'n' times, where 'n' is number of elements.

<br />

<table>
  <thead>
    <tr>
      <th colspan="3">Time Complexity</th>
      <th colspan="1" rowspan="2">Space Complexity</th>
    </tr>
    <tr>
      <th>Best Case</th>
      <th>Avg Case</th>
      <th>Worst Case</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>&Omega;(n)</td>
      <td>&Theta;(n<sup>2</sup>)</td>
      <td>&Omicron;(n<sup>2</sup>)</td>
      <td>O(1)</td>
    </tr>
  </tbody>
</table>

<br />

In Bubble Sort:
- We start by comparing two consecutive numbers
- If first one is greater than the other (for ascending order), swap the two
- Repeat the process for 'n' times where 'n' is the number of elements in the input

Optimized Bubble Sort:
- This can be optimized further for best case scenarios where the input array is almost sorted
- In such a case, we keep track of any swaps that happened in the previous iteration
- If no, then abort the loop
- By doing this, we can achieve a &Omega;(n) time complexity

<br />

<!--Bubble Sort ends----------------------------------------------------------->

<hr />

<!--Insertion Sort------------------------------------------------------------->
## [Insertion Sort](https://github.com/andys-github/algo-practice/blob/sort/sort/insertion-sort.py)
> **Gist:** 

<br />

<table>
  <thead>
    <tr>
      <th colspan="3">Time Complexity</th>
      <th colspan="1" rowspan="2">Space Complexity</th>
    </tr>
    <tr>
      <th>Best Case</th>
      <th>Avg Case</th>
      <th>Worst Case</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>&Omega;(n)</td>
      <td>&Theta;(n<sup>2</sup>)</td>
      <td>&Omicron;(n<sup>2</sup>)</td>
      <td>O(1)</td>
    </tr>
  </tbody>
</table>

<br />

> **Note:** Insertion Sort performs really well when we insert a new element to an already sorted array

<br />

<!--Insertion Sort ends-------------------------------------------------------->

<hr />

<!--Selection Sort------------------------------------------------------------->
## [Selection Sort](https://github.com/andys-github/algo-practice/blob/main/sort/selection-sort.py)
> **Gist:** Start with an element, and run through each subsequent elements, and swap if one of them is smaller. Repeat for the next element.

<br />

<table>
  <thead>
    <tr>
      <th colspan="3">Time Complexity</th>
      <th colspan="1" rowspan="2">Space Complexity</th>
    </tr>
    <tr>
      <th>Best Case</th>
      <th>Avg Case</th>
      <th>Worst Case</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>&Omega;(n<sup>2</sup>)</td>
      <td>&Theta;(n<sup>2</sup>)</td>
      <td>&Omicron;(n<sup>2</sup>)</td>
      <td>O(1)</td>
    </tr>
  </tbody>
</table>

<br />

In Selection Sort:
- We maintain two pointers - one is fixed at an element, and the other one iterates over the remaining elements
- After every iteration, we compare the elements these two pointers points to
- If the second one is smaller than the first, we swap
- This continues till the last element

Each 'nth' element takes about (n - 1) run throughs. So the overall complexity comes around &Omicron;(n) * &Omicron;(n - 1), which becomes **&Omicron;(n<sup>2</sup>) time complexity**.
And since the swapping takes place in the input array itself, we have a **&Omicron;(1) space complexity**.

<br />

<!--Selection Sort ends-------------------------------------------------------->

<hr />

<!--Comparison between the Quadratic Sorts------------------------------------->

## Comparison of Quadratic Sorts
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
      <td>&Omega;(n)</td>
      <td>&Theta;(n<sup>2</sup>)</td>
      <td>&Omicron;(n<sup>2</sup>)</td>
      <td>&Omicron;(1)</td>
    </tr>
    <tr>
      <td>Insertion</td>
      <td>&Omega;(n)</td>
      <td>&Theta;(n<sup>2</sup>)</td>
      <td>&Omicron;(n<sup>2</sup>)</td>
      <td>&Omicron;(1)</td>
    </tr>
    <tr>
      <td>Selection</td>
      <td>&Omega;(n<sup>2</sup>)</td>
      <td>&Theta;(n<sup>2</sup>)</td>
      <td>&Omicron;(n<sup>2</sup>)</td>
      <td>&Omicron;(1)</td>
    </tr>
  </tbody>
</table>

<br />

> **Note:** With nearly sorted data, Bubble and Insertion sorts perform well

<br />

<!--Comparison between the Quadratic Sorts ends-------------------------------->

<hr />

<!--Quick Sort----------------------------------------------------------------->
## [Quick Sort](https://github.com/andys-github/algo-practice/blob/main/sort/quick-sort.py)
> **Gist:**

<br />

<table>
  <thead>
    <tr>
      <th colspan="3">Time Complexity</th>
      <th colspan="1" rowspan="2">Space Complexity</th>
    </tr>
    <tr>
      <th>Best Case</th>
      <th>Avg Case</th>
      <th>Worst Case</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>&Omega;(n log n)</td>
      <td>&Theta;(n log n)</td>
      <td>&Omicron;(n<sup>2</sup>)</td>
      <td>O(1)</td>
    </tr>
  </tbody>
</table>

<br />

<!--Quick Sort ends------------------------------------------------------------>

<hr />

<!--Merge Sort----------------------------------------------------------------->
## [Merge Sort](https://github.com/andys-github/algo-practice/blob/main/sort/merge-sort.py)
> **Gist:** Keep halving input array, and merge all the atomic arrays. 

<br />

<table>
  <thead>
    <tr>
      <th colspan="3">Time Complexity</th>
      <th colspan="1" rowspan="2">Space Complexity</th>
    </tr>
    <tr>
      <th>Best Case</th>
      <th>Avg Case</th>
      <th>Worst Case</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>&Omega;(n log n)</td>
      <td>&Theta;(n log n)</td>
      <td>&Omicron;(n log n)</td>
      <td>O(1)</td>
    </tr>
  </tbody>
</table>

<br />

In Merge sort:
- We keep on halving the input array till we are left with a single element array or an empty array
- Then we start merging these atomic arrays by comparing the elements within it.

Halving the array is of **&Omicron;(log n)** complexity, and since we need to half it and then combine the halves, we take about **&Omicron;(n) time for each half**. Thus the total time-complexity is **&Omicron;(n log n)**

<br />

<!--Merge Sort ends------------------------------------------------------------>

<hr />

<!--Radix Sort----------------------------------------------------------------->
## [Radix Sort](https://github.com/andys-github/algo-practice/blob/main/sort/radix-sort.py)
> **Gist:**

<br />

<table>
  <thead>
    <tr>
      <th colspan="3">Time Complexity</th>
      <th colspan="1" rowspan="2">Space Complexity</th>
    </tr>
    <tr>
      <th>Best Case</th>
      <th>Avg Case</th>
      <th>Worst Case</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>&Omega;(nk)</td>
      <td>&Theta;(nk)</td>
      <td>&Omicron;(nk)</td>
      <td>O(1)</td>
    </tr>
  </tbody>
</table>

<br />

<!--Radix Sort ends------------------------------------------------------------>

