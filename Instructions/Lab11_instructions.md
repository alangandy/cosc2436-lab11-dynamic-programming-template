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

## Your Tasks

### Task 1: Implement `knapsack()`
Solve the 0/1 knapsack problem:
1. Create grid `[n+1][capacity+1]` initialized to 0
2. For each item `i` and capacity `w`:
   - If item fits: `grid[i][w] = max(without_item, with_item)`
   - Else: `grid[i][w] = grid[i-1][w]`
3. Backtrack to find which items were selected
4. Return `(max_value, list_of_item_names)`

### Task 2: Implement `longest_common_substring()`
Find the longest common substring:
1. Create grid `[len(s1)+1][len(s2)+1]`
2. If `s1[i] == s2[j]`: `cell[i][j] = cell[i-1][j-1] + 1`
3. Else: `cell[i][j] = 0`
4. Track the maximum value and its position
5. Return the actual substring

### Task 3: Implement `longest_common_subsequence()`
Find the longest common subsequence:
1. Create grid `[len(s1)+1][len(s2)+1]`
2. If `s1[i] == s2[j]`: `cell[i][j] = cell[i-1][j-1] + 1`
3. Else: `cell[i][j] = max(cell[i-1][j], cell[i][j-1])`
4. Backtrack to reconstruct the subsequence

## Example

```python
# Knapsack
items = [("guitar", 1, 1500), ("stereo", 4, 3000), ("laptop", 3, 2000)]
>>> knapsack(4, items)
(3500, ['guitar', 'laptop'])  # guitar(1500) + laptop(2000) = 3500

# Longest Common Substring
>>> longest_common_substring("fish", "hish")
'ish'

# Longest Common Subsequence
>>> longest_common_subsequence("fosh", "fish")
'fsh'
```

## Testing
```bash
python -m pytest tests/ -v
```

## Hints

### Knapsack Backtracking
To find which items were selected:
```python
# Start from grid[n][capacity]
# If grid[i][w] != grid[i-1][w], item i was included
# Move to grid[i-1][w - weight[i]]
```

### Substring vs Subsequence
- Substring: Reset to 0 when characters don't match
- Subsequence: Take max of left or top cell when characters don't match

### Grid Indexing
- Use 1-based indexing for items/characters
- Row 0 and column 0 are base cases (empty)

## Submission
Commit and push your completed `dp.py` file.
