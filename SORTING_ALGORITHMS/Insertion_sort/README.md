# Insertion Sort Algorithm

## Overview

Insertion Sort is a simple and intuitive sorting algorithm that builds the final sorted array one element at a time. It works similarly to how you might sort playing cards in your hands.

---

## How Insertion Sort Works

1. Start with the second element (index 1), assume the first element is already sorted.
2. Compare the current element to its predecessors.
3. Shift all larger elements one position to the right.
4. Insert the current element into the correct position.
5. Repeat until the entire array is sorted.

---

## Example

Consider the list: `[12, 11, 13, 5, 6]`

- Start with `11`: Insert it before `12` → `[11, 12, 13, 5, 6]`
- Next `13`: Already in correct position → `[11, 12, 13, 5, 6]`
- Next `5`: Insert before `11` → `[5, 11, 12, 13, 6]`
- Next `6`: Insert between `5` and `11` → `[5, 6, 11, 12, 13]`

---

## Python Implementation

```python
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

# Example usage
numbers = [12, 11, 13, 5, 6]
sorted_numbers = insertion_sort(numbers)
print("Sorted list:", sorted_numbers)
