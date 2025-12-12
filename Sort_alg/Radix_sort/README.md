# Radix Sort Algorithm in Python

## Overview

**Radix Sort** is a **non-comparative sorting algorithm** that sorts integers (or fixed-length strings) **digit by digit**, starting from the **least significant digit (LSD)** and moving to the **most significant digit (MSD)**. Unlike comparison-based sorting algorithms (e.g., Quick Sort, Bubble Sort), Radix Sort does not compare elements directly. Instead, it uses **buckets** to group numbers according to each digit and reconstructs the array in order.

### Key Features:
- **Stable sorting**: preserves the relative order of numbers with the same digit.
- **Time Complexity**: O(n × k), where `n` is the number of elements and `k` is the number of digits in the largest number.
- **Space Complexity**: O(n + k), due to bucket storage.
- **Best Use Case**: Large arrays of integers or fixed-length strings, especially when the range of digits is limited.

---

## How Radix Sort Works (Algorithm)

1. **Find the Maximum Value**  
   - Determine the largest number to know the number of digits to process.

2. **Start with Least Significant Digit (LSD)**  
   - Sort numbers based on the units (ones) place.  
   - Use **buckets 0–9** to group numbers according to the current digit.

3. **Move to Next Significant Digit**  
   - Multiply the digit place by 10 (tens, hundreds, etc.) and repeat the bucket sorting.

4. **Repeat Until Most Significant Digit (MSD)**  
   - Continue until all digits of the largest number have been processed.

5. **Reconstruct Sorted Array**  
   - After processing all digits, the array becomes fully sorted.

> The key idea is to **sort the array progressively by each digit** while maintaining stability, so that the final array is sorted correctly.

---

## Python Implementation

```python
myArray = [170, 45, 75, 90, 802, 24, 2, 66]
print("Original array:", myArray)

# Initialize 10 buckets for digits 0-9
radixArray = [[] for _ in range(10)]

maxVal = max(myArray)  # Find the maximum number
exp = 1  # Start with least significant digit

while maxVal // exp > 0:
    # Distribute numbers into buckets according to current digit
    while len(myArray) > 0:
        val = myArray.pop()
        radixIndex = (val // exp) % 10
        radixArray[radixIndex].append(val)
    
    # Collect numbers back from buckets in order
    for bucket in radixArray:
        while len(bucket) > 0:
            val = bucket.pop()
            myArray.append(val)
    
    exp *= 10  # Move to next digit

print("Sorted array:", myArray)
```

## Explanation of the Code

### Initialize Buckets:
radixArray = [[] for _ in range(10)] creates 10 empty lists for digits 0–9.

### Find Maximum Value:
maxVal = max(myArray) identifies the largest number to determine the number of digits.

### Process Each Digit:

exp represents the current digit place (1 → units, 10 → tens, 100 → hundreds).

(val // exp) % 10 extracts the current digit of each number.

### Bucket Distribution:
Numbers are placed into corresponding buckets according to the current digit.

### Rebuild Array:
Numbers are collected back from the buckets in order, maintaining stability.

### Move to Next Digit:
Multiply exp by 10 to process the next more significant digit.

## Advantages

Efficient for large datasets with small key sizes.
Stable sort: useful when the relative order of elements matters.
Non-comparative → avoids repeated comparisons.

## Limitations

Works only for integers or fixed-length strings.
Requires extra space for buckets.
Becomes inefficient if numbers have many digits, as time complexity grows with k.