#!/usr/bin/env python3
"""
Lab 11: Dynamic Programming - Interactive Tutorial
===================================================

🎯 GOAL: Implement DP algorithms in dp.py

📚 DYNAMIC PROGRAMMING (Chapter 11):
------------------------------------
DP solves problems by breaking them into overlapping subproblems,
solving each subproblem once, and storing the results.

KEY DIFFERENCE FROM DIVIDE & CONQUER:
- D&C: Subproblems are independent (quicksort)
- DP: Subproblems overlap (we reuse solutions)

DP APPROACH:
1. Define subproblems
2. Find recurrence relation (how subproblems relate)
3. Build solution bottom-up using a table/grid

HOW TO RUN:
-----------
    python main.py           # Run this tutorial
    python -m pytest tests/ -v   # Run the grading tests
"""

from dp import knapsack, longest_common_substring, longest_common_subsequence


def print_header(title: str) -> None:
    """Print a formatted section header."""
    print("\n" + "=" * 60)
    print(f"  {title}")
    print("=" * 60)


def dp_concept() -> None:
    """Explain the DP concept."""
    print_header("DYNAMIC PROGRAMMING CONCEPT")
    
    print("""
    WHEN TO USE DP:
    1. Problem can be broken into subproblems
    2. Subproblems OVERLAP (same subproblem solved multiple times)
    3. Optimal solution uses optimal solutions to subproblems
    
    EXAMPLE: Fibonacci
    
    Naive recursion (exponential!):
        fib(5) = fib(4) + fib(3)
        fib(4) = fib(3) + fib(2)  ← fib(3) calculated twice!
        fib(3) = fib(2) + fib(1)  ← fib(2) calculated multiple times!
    
    DP approach (linear!):
        Store results in a table, reuse them.
        fib = [0, 1, 1, 2, 3, 5]
        
    TWO DP APPROACHES:
    
    1. TOP-DOWN (Memoization):
       - Start with the big problem
       - Recursively solve subproblems
       - Cache results to avoid recomputation
    
    2. BOTTOM-UP (Tabulation):
       - Start with smallest subproblems
       - Build up to the solution
       - Use a table/grid to store results
    
    Chapter 11 uses BOTTOM-UP with grids!
    """)


def python_2d_arrays() -> None:
    """Explain 2D arrays in Python."""
    print_header("2D ARRAYS (GRIDS) IN PYTHON")
    
    print("""
    DP often uses 2D grids to store subproblem solutions.
    
    C++:   int grid[rows][cols];
    Java:  int[][] grid = new int[rows][cols];
    Python: List of lists
    
    CREATING A 2D GRID:
    -------------------
    # WRONG WAY (creates shared references!):
    grid = [[0] * cols] * rows  # DON'T DO THIS!
    
    # RIGHT WAY (list comprehension):
    grid = [[0 for _ in range(cols)] for _ in range(rows)]
    
    # Or using nested loops:
    grid = []
    for i in range(rows):
        grid.append([0] * cols)
    
    ACCESSING ELEMENTS:
    -------------------
    grid[row][col] = value
    value = grid[row][col]
    """)
    
    # Live demo
    print("LIVE DEMO:")
    rows, cols = 3, 4
    grid = [[0 for _ in range(cols)] for _ in range(rows)]
    print(f"    grid = [[0 for _ in range({cols})] for _ in range({rows})]")
    print(f"    grid = {grid}")
    grid[1][2] = 5
    print(f"    grid[1][2] = 5")
    print(f"    grid = {grid}")


def demo_knapsack() -> None:
    """Demonstrate the knapsack problem."""
    print_header("0/1 KNAPSACK PROBLEM")
    
    print("""
    PROBLEM: You have a knapsack with limited capacity.
    Items have weights and values. Maximize total value!
    
    "0/1" means: each item is either taken (1) or not (0).
    No fractions allowed!
    
    EXAMPLE:
    Capacity: 4 kg
    Items: guitar (1kg, $1500), stereo (4kg, $3000), laptop (3kg, $2000)
    
    DP GRID:
    Each cell[i][w] = max value using first i items with capacity w
    
              0    1    2    3    4   (capacity)
    ----------------------------------------
    0 (none)  0    0    0    0    0
    1 (guitar)0  1500 1500 1500 1500
    2 (stereo)0  1500 1500 1500 3000
    3 (laptop)0  1500 1500 2000 3500  ← Answer!
    
    RECURRENCE:
    For each item i with weight w_i and value v_i:
    
    If w_i > current_capacity:
        cell[i][w] = cell[i-1][w]  (can't fit, skip item)
    Else:
        cell[i][w] = max(
            cell[i-1][w],              # Don't take item
            cell[i-1][w-w_i] + v_i     # Take item
        )
    """)
    
    items = [("guitar", 1, 1500), ("stereo", 4, 3000), ("laptop", 3, 2000)]
    capacity = 4
    
    print(f"\nItems (name, weight, value): {items}")
    print(f"Capacity: {capacity}")
    
    print("\nTesting knapsack():")
    try:
        result = knapsack(capacity, items)
        
        if result is None:
            print("    ❌ Returned None")
        else:
            max_value, selected = result
            print(f"    Max value: ${max_value}")
            print(f"    Selected items: {selected}")
            
            if max_value == 3500 and set(selected) == {"guitar", "laptop"}:
                print("    ✅ Correct!")
            elif max_value == 3500:
                print("    ✅ Value correct!")
            else:
                print(f"    Expected: $3500, ['guitar', 'laptop']")
                
    except Exception as e:
        print(f"    ❌ Error: {e}")


def demo_lcs_substring() -> None:
    """Demonstrate longest common substring."""
    print_header("LONGEST COMMON SUBSTRING")
    
    print("""
    PROBLEM: Find the longest substring that appears in both strings.
    Substring = contiguous characters
    
    EXAMPLE: "fish" and "hish"
    Common substrings: "ish" (length 3), "h", "i", "s"
    Longest: "ish"
    
    DP GRID:
    cell[i][j] = length of common substring ending at s1[i] and s2[j]
    
              h    i    s    h
         0    0    0    0    0
    f    0    0    0    0    0
    i    0    0    1    0    0
    s    0    0    0    2    0
    h    0    1    0    0    3  ← Max = 3
    
    RECURRENCE:
    If s1[i] == s2[j]:
        cell[i][j] = cell[i-1][j-1] + 1
    Else:
        cell[i][j] = 0  (substring must be contiguous!)
    """)
    
    test_cases = [
        ("fish", "hish", "ish"),
        ("abc", "abc", "abc"),
        ("abc", "def", ""),
    ]
    
    print("\nTesting longest_common_substring():")
    for s1, s2, expected in test_cases:
        try:
            result = longest_common_substring(s1, s2)
            status = "✅" if result == expected else "❌"
            print(f"    lcs_substring('{s1}', '{s2}') = '{result}' {status}")
            if result != expected and result is not None:
                print(f"        Expected: '{expected}'")
        except Exception as e:
            print(f"    lcs_substring('{s1}', '{s2}') ❌ Error: {e}")


def demo_lcs_subsequence() -> None:
    """Demonstrate longest common subsequence."""
    print_header("LONGEST COMMON SUBSEQUENCE")
    
    print("""
    PROBLEM: Find the longest subsequence that appears in both strings.
    Subsequence = characters in order, but NOT necessarily contiguous
    
    EXAMPLE: "fosh" and "fish"
    Common subsequences: "fsh" (length 3), "fs", "fh", "sh", etc.
    Longest: "fsh"
    
    KEY DIFFERENCE FROM SUBSTRING:
    - Substring: characters must be adjacent
    - Subsequence: characters can have gaps
    
    DP GRID:
    cell[i][j] = length of LCS of s1[0:i] and s2[0:j]
    
              f    i    s    h
         0    0    0    0    0
    f    0    1    1    1    1
    o    0    1    1    1    1
    s    0    1    1    2    2
    h    0    1    1    2    3  ← Answer = 3
    
    RECURRENCE:
    If s1[i] == s2[j]:
        cell[i][j] = cell[i-1][j-1] + 1
    Else:
        cell[i][j] = max(cell[i-1][j], cell[i][j-1])
    """)
    
    test_cases = [
        ("fosh", "fish", "fsh"),
        ("abcde", "ace", "ace"),
        ("abc", "def", ""),
    ]
    
    print("\nTesting longest_common_subsequence():")
    for s1, s2, expected in test_cases:
        try:
            result = longest_common_subsequence(s1, s2)
            status = "✅" if result == expected else "❌"
            print(f"    lcs_subsequence('{s1}', '{s2}') = '{result}' {status}")
            if result != expected and result is not None:
                print(f"        Expected: '{expected}'")
        except Exception as e:
            print(f"    lcs_subsequence('{s1}', '{s2}') ❌ Error: {e}")


def dp_tips() -> None:
    """Tips for implementing DP solutions."""
    print_header("DP IMPLEMENTATION TIPS")
    
    print("""
    STEP-BY-STEP APPROACH:
    
    1. UNDERSTAND THE PROBLEM
       - What are we optimizing?
       - What are the constraints?
    
    2. DEFINE SUBPROBLEMS
       - What does cell[i][j] represent?
       - Write it down clearly!
    
    3. FIND THE RECURRENCE
       - How does cell[i][j] relate to smaller cells?
       - What are the base cases (first row/column)?
    
    4. FILL THE GRID
       - Usually left-to-right, top-to-bottom
       - Initialize base cases first
    
    5. EXTRACT THE ANSWER
       - Often in cell[n][m] (bottom-right)
       - May need to backtrack to find actual solution
    
    DEBUGGING TIP:
    Print the grid to visualize what's happening!
    
        for row in grid:
            print(row)
    """)


def main():
    """Main entry point."""
    print("\n" + "📊" * 30)
    print("   LAB 11: DYNAMIC PROGRAMMING")
    print("   Solve Once, Reuse Many Times!")
    print("📊" * 30)
    
    print("""
    📋 YOUR TASKS:
    1. Open dp.py
    2. Implement these functions:
       - knapsack()
       - longest_common_substring()
       - longest_common_subsequence()
    3. Run this file to test: python main.py
    4. Run pytest when ready: python -m pytest tests/ -v
    """)
    
    dp_concept()
    python_2d_arrays()
    demo_knapsack()
    demo_lcs_substring()
    demo_lcs_subsequence()
    dp_tips()
    
    print_header("NEXT STEPS")
    print("""
    When all tests pass, run: python -m pytest tests/ -v
    Then complete the Lab Report in README.md
    """)


if __name__ == "__main__":
    main()
