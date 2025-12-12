# Quicksort Python Program

This project implements the **Quicksort algorithm** to sort a list of numbers entered by the user. Quicksort is one of the most efficient and widely used sorting algorithms, especially for large datasets. This README explains the algorithm, how the program works, and its computational complexity in detail.

---

## **Overview of Quicksort**

Quicksort is a **divide-and-conquer sorting algorithm**. It works by selecting a **pivot element** from the array and partitioning the other elements into two subarrays:

1. **Left Subarray:** Elements less than or equal to the pivot.  
2. **Right Subarray:** Elements greater than the pivot.

The pivot element is then placed in its **correct sorted position**, and the algorithm recursively applies the same process to the left and right subarrays. This recursion continues until the entire array is sorted.

The key idea behind Quicksort is **recursion and partitioning**. By dividing the problem into smaller subproblems, it efficiently reduces the overall number of comparisons needed to sort the array.

---

## **Step-by-Step Explanation of the Algorithm**

### 1. Choosing a Pivot

- The pivot can be any element in the array, but common choices include the **first element**, **last element**, or a **random element**.  
- The pivot serves as a reference point for arranging other elements.  

### 2. Partitioning the Array

- The array is scanned element by element.
- Elements less than or equal to the pivot are moved to the **left** of the pivot.  
- Elements greater than the pivot are moved to the **right** of the pivot.  
- After this step, the pivot is placed in its **final sorted position**.  

**Example:**  

For the array `[7, 2, 9, 1, 4, 10, 3, 6, 8, 5]` with pivot `5`:

- Left subarray (≤5): `[2, 1, 4, 3]`  
- Pivot: `[5]`  
- Right subarray (>5): `[7, 9, 10, 6, 8]`  

---

### 3. Recursion

- The algorithm then **recursively sorts the left subarray** and **right subarray**.
- This means applying the same process: choosing a pivot, partitioning, and placing it correctly.
- Each recursion reduces the problem size, eventually sorting the array completely.

**Example:**  

Sorting the left subarray `[2, 1, 4, 3]` with pivot `3`:

- Left ≤ pivot: `[2, 1]`  
- Pivot: `[3]`  
- Right > pivot: `[4]`  

Sorting `[2, 1]` further with pivot `1` results in `[1, 2]`. Combining with `[3, 4]` gives `[1, 2, 3, 4]`.

---

### 4. Combining Subarrays

- After each recursive call, the left subarray, pivot, and right subarray are combined.
- This combination gradually forms the fully **sorted array**.
- Using the previous example, after sorting both left and right parts of the original array, the final sorted array becomes:[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


---

## **User Input Handling**

- The program allows users to input numbers separated by commas.
- These inputs are converted into integers and stored in an array.
- This array is then passed to the Quicksort algorithm for sorting.
- After sorting, the program displays the **sorted array** in ascending order.

This makes the program interactive and flexible, as users can sort **any set of integers** they choose.

---

## **Time Complexity Analysis**

Quicksort is known for its **efficiency**, but its performance depends on pivot selection and array structure.

  Case   Complexity   Explanation  
 
  **Best Case**   O(n log n)   Pivot divides array into nearly equal halves at each step.  
  **Average Case**   O(n log n)   On average, the pivot splits arrays reasonably evenly.  
  **Worst Case**   O(n²)   Pivot is the smallest or largest element repeatedly, such as in already sorted arrays with naive pivot choice.  

- **Space Complexity:** O(log n)  
  - The algorithm sorts the array **in-place**, so no extra arrays are created.  
  - Only recursion stack space is needed.

---

## **Advantages of Quicksort**

- Very fast for **large datasets** due to its divide-and-conquer approach.
- Works **in-place**, saving memory.
- Simple and elegant recursive algorithm.
- Flexible pivot selection strategies improve performance (random pivot, median-of-three, etc.).

---

## **Disadvantages**

- Worst-case performance O(n²) if pivot choice is poor.
- Recursive calls can lead to stack overflow for **very large arrays** if not optimized.
- Not a stable sort (equal elements may change order).





