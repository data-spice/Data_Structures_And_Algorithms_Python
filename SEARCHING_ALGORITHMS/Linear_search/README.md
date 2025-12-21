# Linear Search Algorithm

## What is Linear Search?

Linear Search is a straightforward algorithm that checks each element of a list one by one until it finds the target value or reaches the end of the list.

- Works on both sorted and unsorted lists.
- Time complexity is **O(n)**, where *n* is the number of elements.
- Simple to implement but less efficient on large lists compared to other search algorithms.

---

## How This Code Works

```python
def linear(arr, element):
    n = len(arr)
    found = []
    for index, x in enumerate(arr):
        if x == element:
            found.append(index)
            status = 1
    if status == 1:
        return f"{element} found at the following indexes {found}"
    else:
        return f"{element} was not found."

arr = list(map(int, filter(None, input("Enter the values separated with a comma:").split(","))))
element = int(input("Enter the value you want to look for: "))

print(linear(arr, element))
