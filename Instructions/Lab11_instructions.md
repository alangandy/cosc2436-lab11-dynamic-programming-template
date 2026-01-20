# Lab 11: Dynamic Programming

## 1. Introduction and Objectives

### Overview
Implement dynamic programming solutions to solve optimization problems. Apply DP to the knapsack problem and string comparison problems using Texas city delivery scenarios.

### Learning Objectives
- Understand the dynamic programming paradigm
- Build and fill DP grids/tables
- Solve the knapsack problem
- Implement longest common substring and subsequence

### Prerequisites
- Complete Labs 1-10
- Read Chapter 11 in "Grokking Algorithms" (pages 203-228)

---

## 2. Algorithm Background

### What is Dynamic Programming?
DP solves problems by:
1. Breaking into **subproblems**
2. Solving each subproblem **once**
3. Storing results in a **grid/table**
4. Building up to the final solution

### When to Use DP
From Chapter 11:
- You're trying to **optimize** something (maximize/minimize)
- Problem can be broken into **discrete subproblems**
- Every DP solution involves a **grid**

### The Knapsack Problem
**Given:** Items with weights and values, knapsack with capacity
**Goal:** Maximize value without exceeding capacity

Key insight: For each item, you have two choices:
1. **Take it** (if it fits)
2. **Leave it**

### Longest Common Substring vs Subsequence
| Problem | Requirement | Example |
|---------|-------------|---------|
| Substring | Characters must be **consecutive** | "fish" & "hish" → "ish" |
| Subsequence | Characters in **order** but not consecutive | "fosh" & "fish" → "f", "s", "h" |

### DP Grid Formula (from Chapter 11)

**Longest Common Substring:**
```
if word_a[i] == word_b[j]:
    cell[i][j] = cell[i-1][j-1] + 1
else:
    cell[i][j] = 0
```

**Longest Common Subsequence:**
```
if word_a[i] == word_b[j]:
    cell[i][j] = cell[i-1][j-1] + 1
else:
    cell[i][j] = max(cell[i-1][j], cell[i][j-1])
```

---

## 3. Project Structure

```
lab11_dynamic_programming/
├── knapsack.py        # Knapsack problem
├── lcs.py             # Longest common substring/subsequence
├── main.py            # Main program
└── README.md          # Your lab report
```

---

## 4. Step-by-Step Implementation

### Step 1: Create `knapsack.py`

```python
"""
Lab 11: The Knapsack Problem
Maximize value of items that fit in a knapsack.

From Chapter 11: Every DP solution involves a GRID.
"""
from typing import List, Tuple


def knapsack(capacity: int, items: List[Tuple[str, int, int]]) -> Tuple[int, List[str]]:
    """
    Solve 0/1 Knapsack using Dynamic Programming.
    
    From Chapter 11:
    - Each cell represents a subproblem
    - cell[i][w] = max value using first i items with capacity w
    
    Args:
        capacity: Maximum weight capacity
        items: List of (name, weight, value) tuples
    
    Returns:
        Tuple of (max_value, list of selected items)
    """
    n = len(items)
    
    # Create the DP grid
    # Rows = items (0 to n)
    # Columns = capacities (0 to capacity)
    grid = [[0] * (capacity + 1) for _ in range(n + 1)]
    
    print("KNAPSACK PROBLEM - DYNAMIC PROGRAMMING")
    print("=" * 50)
    print(f"Capacity: {capacity}")
    print(f"\nItems:")
    for name, weight, value in items:
        print(f"  {name}: weight={weight}, value=${value}")
    
    # Fill the grid
    print("\nFilling the DP grid...")
    for i in range(1, n + 1):
        name, weight, value = items[i - 1]
        
        for w in range(capacity + 1):
            # Option 1: Don't take item i (use previous row's value)
            grid[i][w] = grid[i - 1][w]
            
            # Option 2: Take item i (if it fits)
            if weight <= w:
                value_with_item = value + grid[i - 1][w - weight]
                
                # Take the better option
                if value_with_item > grid[i][w]:
                    grid[i][w] = value_with_item
    
    # Print the grid
    print("\nDP Grid:")
    print("     ", end="")
    for w in range(capacity + 1):
        print(f"{w:4}", end="")
    print()
    
    for i in range(n + 1):
        if i == 0:
            print("  -- ", end="")
        else:
            name = items[i-1][0][:3]
            print(f"{name:>4} ", end="")
        for w in range(capacity + 1):
            print(f"{grid[i][w]:4}", end="")
        print()
    
    # Backtrack to find selected items
    selected = []
    w = capacity
    for i in range(n, 0, -1):
        # If value changed from previous row, item was taken
        if grid[i][w] != grid[i - 1][w]:
            name, weight, value = items[i - 1]
            selected.append(name)
            w -= weight
    
    selected.reverse()
    max_value = grid[n][capacity]
    
    print(f"\nMax value: ${max_value}")
    print(f"Selected items: {selected}")
    
    return max_value, selected


def texas_delivery_example():
    """
    Example: Delivery truck with limited capacity.
    
    Which packages should we deliver to maximize profit?
    """
    capacity = 6  # kg (keeping small for clear grid)
    
    # (name, weight, value)
    packages = [
        ("Houston", 1, 15),
        ("Dallas", 3, 20),
        ("Austin", 4, 30),
        ("San Antonio", 2, 14),
    ]
    
    return capacity, packages


def demonstrate_subproblem_building():
    """
    Show how DP builds up from subproblems.
    
    From Chapter 11: "Each cell is a subproblem"
    """
    print("\n" + "=" * 50)
    print("HOW DP BUILDS FROM SUBPROBLEMS")
    print("=" * 50)
    print("""
    The grid represents ALL subproblems:
    
    cell[i][w] = "What's the max value I can get
                  using the first i items
                  with a knapsack of capacity w?"
    
    Example grid for 3 items, capacity 4:
    
              Capacity
              0   1   2   3   4
         ┌───┬───┬───┬───┬───┬───┐
      0  │ 0 │ 0 │ 0 │ 0 │ 0 │  ← No items = $0
         ├───┼───┼───┼───┼───┼───┤
    Item1│ 0 │ ? │ ? │ ? │ ? │  ← Can use item 1
         ├───┼───┼───┼───┼───┼───┤
    Item2│ 0 │ ? │ ? │ ? │ ? │  ← Can use items 1-2
         ├───┼───┼───┼───┼───┼───┤
    Item3│ 0 │ ? │ ? │ ? │ ? │  ← Can use items 1-3
         └───┴───┴───┴───┴───┴───┘
                              ↑
                        FINAL ANSWER
    
    For each cell, we ask:
    1. What if I DON'T take this item? → Use cell above
    2. What if I DO take this item? → Item value + remaining capacity
    
    Take the MAX of these two options!
    """)
```

### Step 2: Create `lcs.py`

```python
"""
Lab 11: Longest Common Substring and Subsequence
String comparison using Dynamic Programming.

From Chapter 11: Used for spell-check, DNA comparison, diff tools.
"""
from typing import Tuple


def longest_common_substring(s1: str, s2: str) -> Tuple[int, str]:
    """
    Find longest common SUBSTRING (consecutive characters).
    
    From Chapter 11:
    - If letters match: cell[i][j] = cell[i-1][j-1] + 1
    - If letters don't match: cell[i][j] = 0
    
    The answer is the LARGEST number in the grid (not necessarily last cell!)
    """
    m, n = len(s1), len(s2)
    
    # Create DP grid
    grid = [[0] * (n + 1) for _ in range(m + 1)]
    
    max_length = 0
    end_pos = 0
    
    print("LONGEST COMMON SUBSTRING")
    print("=" * 50)
    print(f"String 1: '{s1}'")
    print(f"String 2: '{s2}'")
    
    # Fill the grid
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if s1[i - 1] == s2[j - 1]:
                # Characters match - extend the substring
                grid[i][j] = grid[i - 1][j - 1] + 1
                
                if grid[i][j] > max_length:
                    max_length = grid[i][j]
                    end_pos = i
            else:
                # Characters don't match - reset to 0
                grid[i][j] = 0
    
    # Print the grid
    print("\nDP Grid:")
    print("     ", end="")
    for j, c in enumerate(s2):
        print(f"  {c}", end="")
    print()
    
    for i in range(m + 1):
        if i == 0:
            print("   ", end="")
        else:
            print(f" {s1[i-1]} ", end="")
        for j in range(n + 1):
            print(f"{grid[i][j]:3}", end="")
        print()
    
    # Extract the substring
    substring = s1[end_pos - max_length:end_pos]
    
    print(f"\nLongest common substring: '{substring}'")
    print(f"Length: {max_length}")
    
    return max_length, substring


def longest_common_subsequence(s1: str, s2: str) -> Tuple[int, str]:
    """
    Find longest common SUBSEQUENCE (not necessarily consecutive).
    
    From Chapter 11:
    - If letters match: cell[i][j] = cell[i-1][j-1] + 1
    - If letters don't match: cell[i][j] = max(cell[i-1][j], cell[i][j-1])
    
    The answer IS in the last cell!
    """
    m, n = len(s1), len(s2)
    
    # Create DP grid
    grid = [[0] * (n + 1) for _ in range(m + 1)]
    
    print("\nLONGEST COMMON SUBSEQUENCE")
    print("=" * 50)
    print(f"String 1: '{s1}'")
    print(f"String 2: '{s2}'")
    
    # Fill the grid
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if s1[i - 1] == s2[j - 1]:
                # Characters match - extend the subsequence
                grid[i][j] = grid[i - 1][j - 1] + 1
            else:
                # Characters don't match - take the max of neighbors
                grid[i][j] = max(grid[i - 1][j], grid[i][j - 1])
    
    # Print the grid
    print("\nDP Grid:")
    print("     ", end="")
    for j, c in enumerate(s2):
        print(f"  {c}", end="")
    print()
    
    for i in range(m + 1):
        if i == 0:
            print("   ", end="")
        else:
            print(f" {s1[i-1]} ", end="")
        for j in range(n + 1):
            print(f"{grid[i][j]:3}", end="")
        print()
    
    # Backtrack to find the subsequence
    subsequence = []
    i, j = m, n
    while i > 0 and j > 0:
        if s1[i - 1] == s2[j - 1]:
            subsequence.append(s1[i - 1])
            i -= 1
            j -= 1
        elif grid[i - 1][j] > grid[i][j - 1]:
            i -= 1
        else:
            j -= 1
    
    subsequence.reverse()
    lcs = ''.join(subsequence)
    
    print(f"\nLongest common subsequence: '{lcs}'")
    print(f"Length: {grid[m][n]}")
    
    return grid[m][n], lcs


def compare_substring_vs_subsequence():
    """
    Show the difference between substring and subsequence.
    
    From Chapter 11: "fosh" vs "fish" example.
    """
    print("\n" + "=" * 50)
    print("SUBSTRING vs SUBSEQUENCE")
    print("=" * 50)
    print("""
    SUBSTRING: Characters must be CONSECUTIVE
    SUBSEQUENCE: Characters in ORDER but not consecutive
    
    Example from Chapter 11:
    
    Comparing "hish" with "fish":
    - Longest common SUBSTRING: "ish" (length 3)
    
    Comparing "fosh" with "fish":
    - Longest common SUBSTRING: "sh" (length 2)
    - Longest common SUBSEQUENCE: "fsh" (length 3)
    
    For spell-check, SUBSEQUENCE is often more useful!
    "fosh" is closer to "fish" than to "fort" because
    it shares more letters in the same order.
    """)


def city_route_comparison():
    """
    Compare delivery routes using LCS.
    
    Which routes are most similar?
    """
    print("\n" + "=" * 50)
    print("CITY ROUTE COMPARISON")
    print("=" * 50)
    
    route1 = "HDASA"  # Houston, Dallas, Austin, San Antonio, Amarillo
    route2 = "HDALA"  # Houston, Dallas, Austin, Laredo, Amarillo
    
    print("Route 1: H-D-A-S-A (Houston→Dallas→Austin→SanAntonio→Amarillo)")
    print("Route 2: H-D-A-L-A (Houston→Dallas→Austin→Laredo→Amarillo)")
    
    longest_common_subsequence(route1, route2)
```

### Step 3: Create `main.py`

```python
"""
Lab 11: Main Program
Demonstrates dynamic programming concepts from Chapter 11.
"""
from knapsack import knapsack, texas_delivery_example, demonstrate_subproblem_building
from lcs import (
    longest_common_substring,
    longest_common_subsequence,
    compare_substring_vs_subsequence,
    city_route_comparison
)


def main():
    # =========================================
    # PART 1: The Knapsack Problem
    # =========================================
    print("=" * 60)
    print("PART 1: THE KNAPSACK PROBLEM")
    print("=" * 60)
    
    capacity, packages = texas_delivery_example()
    max_value, selected = knapsack(capacity, packages)
    
    demonstrate_subproblem_building()
    
    # =========================================
    # PART 2: Longest Common Substring
    # =========================================
    print("\n" + "=" * 60)
    print("PART 2: LONGEST COMMON SUBSTRING")
    print("=" * 60)
    
    # Example from Chapter 11
    longest_common_substring("hish", "fish")
    
    # Another example
    longest_common_substring("houston", "austin")
    
    # =========================================
    # PART 3: Longest Common Subsequence
    # =========================================
    print("\n" + "=" * 60)
    print("PART 3: LONGEST COMMON SUBSEQUENCE")
    print("=" * 60)
    
    # Example from Chapter 11
    longest_common_subsequence("fosh", "fish")
    
    # Compare with fort
    longest_common_subsequence("fosh", "fort")
    
    # =========================================
    # PART 4: Substring vs Subsequence
    # =========================================
    compare_substring_vs_subsequence()
    
    # =========================================
    # PART 5: City Route Comparison
    # =========================================
    city_route_comparison()
    
    # =========================================
    # PART 6: Key Concepts from Chapter 11
    # =========================================
    print("\n" + "=" * 60)
    print("PART 6: KEY CONCEPTS FROM CHAPTER 11")
    print("=" * 60)
    print("""
    DYNAMIC PROGRAMMING ESSENTIALS:
    
    1. EVERY DP SOLUTION INVOLVES A GRID
       - Rows and columns represent subproblems
       - Each cell contains the answer to a subproblem
    
    2. THE VALUES IN CELLS
       - Usually what you're trying to optimize
       - Knapsack: maximum value
       - LCS: length of longest match
    
    3. EACH CELL IS A SUBPROBLEM
       - Think: "What smaller problem does this cell solve?"
       - Knapsack: "Max value with first i items, capacity w"
       - LCS: "Longest match of first i chars and first j chars"
    
    4. HOW TO DIVIDE INTO SUBPROBLEMS
       - This is the hard part!
       - No single formula - requires thinking
       - The "Feynman algorithm": Think real hard!
    
    5. BUILDING UP THE SOLUTION
       - Start with base cases (usually 0s)
       - Fill grid row by row or column by column
       - Each cell uses previously computed cells
    
    APPLICATIONS (from Chapter 11):
    - Biologists: DNA strand comparison
    - git diff: Finding differences between files
    - Spell-check: Levenshtein distance
    - Plagiarism detection
    """)


if __name__ == "__main__":
    main()
```

---

## 5. Lab Report Template

```markdown
# Lab 11: Dynamic Programming

## Student Information
- **Name:** [Your Name]
- **Date:** [Date]

## DP Concepts

### What is Dynamic Programming?
[Explain in your own words based on Chapter 11]

### The DP Grid
[Explain why every DP solution involves a grid]

## Knapsack Problem

### Problem Setup
- Capacity: [value]
- Items: [list items with weights and values]

### DP Grid
[Draw or copy your grid here]

### Solution
- Maximum value: $[value]
- Selected items: [list]

### How did you determine which items were selected?
[Explain the backtracking process]

## Longest Common Substring

### Test Case: "hish" vs "fish"
- Grid: [show grid]
- Result: [substring and length]

### Why is the answer NOT always in the last cell?
[Explain based on Chapter 11]

## Longest Common Subsequence

### Test Case: "fosh" vs "fish"
- Grid: [show grid]
- Result: [subsequence and length]

### Substring vs Subsequence Formula Difference
| Situation | Substring Formula | Subsequence Formula |
|-----------|-------------------|---------------------|
| Letters match | | |
| Letters don't match | | |

## Reflection Questions

1. Why does DP use a grid instead of just recursion?

2. In the knapsack problem, what do the rows and columns represent?

3. Why is "fosh" closer to "fish" than to "fort" using LCS?

4. What real-world applications use longest common subsequence?

5. What makes a problem suitable for dynamic programming?
```

---

## 6. Submission
Save files in `lab11_dynamic_programming/`, complete README, commit and push.
