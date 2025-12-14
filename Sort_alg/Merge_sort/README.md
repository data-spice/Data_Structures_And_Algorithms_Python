# Merge Sort Algorithm

## What is Merge Sort?

Merge Sort is a **divide and conquer** sorting algorithm that works by recursively splitting a list into smaller sublists, sorting those sublists, and then merging them back together to form a sorted list.

It is efficient, stable, and works well on large datasets.

---

## How Merge Sort Works

1. **Divide:**  
   Split the list into two halves until each sublist has only one element (which is inherently sorted).

2. **Conquer:**  
   Merge the sorted sublists back together to produce new sorted sublists until the entire list is sorted.

---

## Time Complexity

- **Best Case:** O(n log n)  
- **Average Case:** O(n log n)  
- **Worst Case:** O(n log n)  

Merge sort always divides the list into halves, resulting in the logarithmic depth (log n) of recursive calls, and merging takes linear time (n), resulting in O(n log n).

---

## Code Explanation: Merge Sort in Python

```python
def mergesort(arr):
    if len(arr) <= 1:
        return arr
```
### Lines 1-3:
The base case: If the list contains 1 or 0 elements, it is already sorted, so return it as is.

```python

    mid = len(arr) // 2
    lefthalf = arr[:mid]
    righthalf = arr[mid:]
```
### Lines 5-7:
Split the list into two halves:

lefthalf is the left half (from start up to midpoint).

righthalf is the right half (from midpoint to end).

```python

    lefthalf = mergesort(lefthalf)
    righthalf = mergesort(righthalf)
```
### Lines 9-10:
Recursively call mergesort on each half to sort them.

```python

    return merge(lefthalf, righthalf)
```
### Line 12:
Merge the two sorted halves and return the fully sorted list.

```python

def merge(left, right):
    results = []
    i = j = 0
```
### Lines 1-4:
Initialize an empty list results to store merged output and two pointers i and j to traverse left and right lists.

```python

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            results.append(left[i])
            i += 1
        else:
            results.append(right[j])
            j += 1
```
### Lines 6-13:
Compare elements pointed by i and j in left and right. Append the smaller element to results and move the pointer forward.

``` python

    results.extend(left[i:])
    results.extend(right[j:])
```
Lines 15-16:
Once one list is exhausted, append the remaining elements of the other list to results.

```python

    return results
```
### Line 18:
Return the merged and sorted list.

## Summary
Merge Sort recursively divides the list into halves until single elements remain.

Then it merges those elements back in sorted order.

It consistently performs at O(n log n) time, making it efficient for large inputs.

## Example Usage
```python

unsorted = list(map(int, input("Enter numbers separated by commas: ").strip().split(",")))
sorted_list = mergesort(unsorted)
print("Sorted:", sorted_list)
```
Enter your list of numbers separated by commas to get them sorted using Merge Sort: