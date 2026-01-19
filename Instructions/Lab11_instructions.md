# Lab 11: Dynamic Programming

## Overview
In this lab, you will implement **Dynamic Programming (DP)** algorithms from Chapter 11 of "Grokking Algorithms." DP solves complex problems by breaking them into overlapping subproblems.

## Learning Objectives
- Understand the dynamic programming approach
- Implement the 0/1 knapsack problem
- Implement longest common substring
- Implement longest common subsequence
- Build and use DP grids/tables

## Background

### What is Dynamic Programming?
DP is useful when:
1. Problem can be broken into **subproblems**
2. Subproblems **overlap** (same subproblem solved multiple times)
3. Problem has **optimal substructure** (optimal solution uses optimal sub-solutions)

DP builds a table to store solutions to subproblems, avoiding redundant computation.

### The Knapsack Problem
**Problem**: Given items with weights and values, and a knapsack with limited capacity, maximize the total value.

**DP approach**: Build a grid where `cell[i][w]` = max value using first `i` items with capacity `w`.

Formula:
- If item `i` doesn't fit: `cell[i][w] = cell[i-1][w]`
- If item `i` fits: `cell[i][w] = max(cell[i-1][w], value[i] + cell[i-1][w-weight[i]])`

### Longest Common Substring vs Subsequence
- **Substring**: Characters must be contiguous
- **Subsequence**: Characters can be non-contiguous but must maintain order

Example: "fish" and "fosh"
- Longest common substring: "sh" (length 2)
- Longest common subsequence: "fsh" (length 3)

---

## Complete Solutions

### Task 1: `knapsack()` - Complete Implementation

```python
from typing import List, Tuple

def knapsack(capacity: int, items: List[Tuple[str, int, int]]) -> Tuple[int, List[str]]:
    """
    Solve 0/1 knapsack problem using dynamic programming.
    
    From Chapter 11: Build a grid where each cell represents
    the max value for a given capacity and items considered.
    
    Args:
        capacity: Maximum weight capacity
        items: List of (name, weight, value) tuples
    
    Returns:
        Tuple of (max_value, list of item names)
    """
    n = len(items)
    
    # Create grid[n+1][capacity+1] initialized to 0
    # grid[i][w] = max value using first i items with capacity w
    grid = [[0 for _ in range(capacity + 1)] for _ in range(n + 1)]
    
    # Fill the grid
    for i in range(1, n + 1):
        name, weight, value = items[i - 1]  # items is 0-indexed
        
        for w in range(capacity + 1):
            # Option 1: Don't include this item
            without_item = grid[i - 1][w]
            
            # Option 2: Include this item (if it fits)
            if weight <= w:
                with_item = value + grid[i - 1][w - weight]
                grid[i][w] = max(without_item, with_item)
            else:
                grid[i][w] = without_item
    
    # Backtrack to find which items were selected
    selected_items = []
    w = capacity
    for i in range(n, 0, -1):
        # If value changed from previous row, this item was included
        if grid[i][w] != grid[i - 1][w]:
            name, weight, value = items[i - 1]
            selected_items.append(name)
            w -= weight  # Reduce remaining capacity
    
    # Reverse to get items in original order
    selected_items.reverse()
    
    return (grid[n][capacity], selected_items)
```

**How it works:**
1. Create a 2D grid where `grid[i][w]` = max value using first `i` items with capacity `w`
2. For each item `i` and capacity `w`:
   - Calculate value without this item: `grid[i-1][w]`
   - If item fits (`weight <= w`), calculate value with item: `value + grid[i-1][w-weight]`
   - Take the maximum
3. Backtrack from `grid[n][capacity]`:
   - If `grid[i][w] != grid[i-1][w]`, item `i` was included
   - Move to `grid[i-1][w-weight]`

---

### Task 2: `longest_common_substring()` - Complete Implementation

```python
def longest_common_substring(s1: str, s2: str) -> str:
    """
    Find longest common substring using DP.
    
    From Chapter 11: Build grid where cell[i][j] = length of
    common substring ending at s1[i] and s2[j].
    
    Formula:
    - If s1[i] == s2[j]: cell[i][j] = cell[i-1][j-1] + 1
    - Else: cell[i][j] = 0
    """
    m, n = len(s1), len(s2)
    
    # Create grid[m+1][n+1] initialized to 0
    grid = [[0 for _ in range(n + 1)] for _ in range(m + 1)]
    
    # Track the maximum length and its ending position
    max_length = 0
    max_end_i = 0
    
    # Fill the grid
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if s1[i - 1] == s2[j - 1]:  # Characters match
                grid[i][j] = grid[i - 1][j - 1] + 1
                
                # Update max if this is longer
                if grid[i][j] > max_length:
                    max_length = grid[i][j]
                    max_end_i = i
            else:
                grid[i][j] = 0  # Reset - substring must be contiguous
    
    # Extract the substring
    # It ends at index max_end_i-1 in s1 and has length max_length
    start = max_end_i - max_length
    return s1[start:max_end_i]
```

**How it works:**
1. Create grid where `grid[i][j]` = length of common substring ending at `s1[i-1]` and `s2[j-1]`
2. If characters match: `grid[i][j] = grid[i-1][j-1] + 1` (extend the substring)
3. If characters don't match: `grid[i][j] = 0` (substring must be contiguous)
4. Track the maximum length and where it ends
5. Extract the substring from `s1`

---

### Task 3: `longest_common_subsequence()` - Complete Implementation

```python
def longest_common_subsequence(s1: str, s2: str) -> str:
    """
    Find longest common subsequence using DP.
    
    From Chapter 11: Similar to substring but characters
    don't need to be contiguous.
    
    Formula:
    - If s1[i] == s2[j]: cell[i][j] = cell[i-1][j-1] + 1
    - Else: cell[i][j] = max(cell[i-1][j], cell[i][j-1])
    """
    m, n = len(s1), len(s2)
    
    # Create grid[m+1][n+1] initialized to 0
    grid = [[0 for _ in range(n + 1)] for _ in range(m + 1)]
    
    # Fill the grid
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if s1[i - 1] == s2[j - 1]:  # Characters match
                grid[i][j] = grid[i - 1][j - 1] + 1
            else:
                # Take the best from excluding either character
                grid[i][j] = max(grid[i - 1][j], grid[i][j - 1])
    
    # Backtrack to reconstruct the subsequence
    subsequence = []
    i, j = m, n
    
    while i > 0 and j > 0:
        if s1[i - 1] == s2[j - 1]:
            # This character is part of the LCS
            subsequence.append(s1[i - 1])
            i -= 1
            j -= 1
        elif grid[i - 1][j] > grid[i][j - 1]:
            # Came from above
            i -= 1
        else:
            # Came from left
            j -= 1
    
    # Reverse since we built it backwards
    subsequence.reverse()
    return ''.join(subsequence)
```

**How it works:**
1. Create grid where `grid[i][j]` = length of LCS of `s1[0:i]` and `s2[0:j]`
2. If characters match: `grid[i][j] = grid[i-1][j-1] + 1`
3. If characters don't match: `grid[i][j] = max(grid[i-1][j], grid[i][j-1])`
4. Backtrack from `grid[m][n]`:
   - If characters match, add to result and move diagonally
   - Else, move in direction of larger value (up or left)

---

## Example Usage

```python
# Knapsack
items = [("guitar", 1, 1500), ("stereo", 4, 3000), ("laptop", 3, 2000)]
>>> knapsack(4, items)
(3500, ['guitar', 'laptop'])

# Grid visualization for knapsack:
#          0    1    2    3    4  (capacity)
#     0 [  0,   0,   0,   0,   0]
# guitar [  0, 1500, 1500, 1500, 1500]  (weight=1, value=1500)
# stereo [  0, 1500, 1500, 1500, 3000]  (weight=4, value=3000)
# laptop [  0, 1500, 1500, 2000, 3500]  (weight=3, value=2000)
#
# Max value = 3500 (guitar + laptop)


# Longest Common Substring
>>> longest_common_substring("fish", "hish")
'ish'

# Grid:
#       ""  h  i  s  h
#   ""   0  0  0  0  0
#   f    0  0  0  0  0
#   i    0  0  1  0  0
#   s    0  0  0  2  0
#   h    0  1  0  0  3  ← max=3, ends at 'h'
#
# Substring = "ish"


# Longest Common Subsequence
>>> longest_common_subsequence("fosh", "fish")
'fsh'

# Grid:
#       ""  f  i  s  h
#   ""   0  0  0  0  0
#   f    0  1  1  1  1
#   o    0  1  1  1  1
#   s    0  1  1  2  2
#   h    0  1  1  2  3  ← LCS length = 3
#
# Backtrack: h(match) → s(match) → o(up) → f(match)
# Subsequence = "fsh"
```

---

## Testing
```bash
python -m pytest tests/ -v
```

## Submission
Commit and push your completed `dp.py` file.
