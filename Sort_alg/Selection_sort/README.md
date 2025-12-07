# Selection Sort Algorithm with User Input

## Overview

This Python script implements the **Selection Sort** algorithm to sort a list of integers entered by the user. Selection Sort is a simple comparison-based sorting technique that repeatedly finds the minimum element from the unsorted portion and places it at the beginning.

---

## How Selection Sort Works

1. Start from the first element, assume it as the minimum.
2. Compare this element with the rest of the list to find the true minimum.
3. Swap the found minimum with the current element.
4. Move to the next element and repeat the process until the entire list is sorted.

---

## User Input

The script takes input values as a comma-separated string from the user, converts them into a list of integers, and then sorts them.

---

## Code

```python
# Get user input as comma-separated values
values = input("Enter the values separated by a comma: ").strip().split(",")

# Convert the input strings to integers
arr = list(map(int, values))

n = len(arr)

# Selection Sort implementation
for i in range(n - 1):
    min_index = i
    for j in range(i + 1, n):
        if arr[j] < arr[min_index]:
            min_index = j
    # Swap the minimum element with the first element
    arr[i], arr[min_index] = arr[min_index], arr[i]

print("\n\nSorted elements:", arr)
