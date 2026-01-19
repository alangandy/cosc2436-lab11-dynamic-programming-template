"""
Lab 11: Dynamic Programming
Implement DP algorithms from Chapter 11.

Chapter 11 covers:
- Knapsack problem
- Longest common substring
- Longest common subsequence
"""
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
    
    Example:
        >>> items = [("guitar", 1, 1500), ("stereo", 4, 3000), ("laptop", 3, 2000)]
        >>> knapsack(4, items)
        (3500, ['guitar', 'laptop'])
    """
    # TODO: Implement knapsack DP
    # 1. Create grid[n+1][capacity+1]
    # 2. Fill grid: for each item and capacity
    #    - If item fits: max(without item, with item)
    #    - Else: same as without item
    # 3. Backtrack to find selected items
    
    pass


def longest_common_substring(s1: str, s2: str) -> str:
    """
    Find longest common substring using DP.
    
    From Chapter 11: Build grid where cell[i][j] = length of
    common substring ending at s1[i] and s2[j].
    
    Formula:
    - If s1[i] == s2[j]: cell[i][j] = cell[i-1][j-1] + 1
    - Else: cell[i][j] = 0
    
    Example:
        >>> longest_common_substring("fish", "hish")
        'ish'
    """
    # TODO: Implement LCS (substring)
    pass


def longest_common_subsequence(s1: str, s2: str) -> str:
    """
    Find longest common subsequence using DP.
    
    From Chapter 11: Similar to substring but characters
    don't need to be contiguous.
    
    Formula:
    - If s1[i] == s2[j]: cell[i][j] = cell[i-1][j-1] + 1
    - Else: cell[i][j] = max(cell[i-1][j], cell[i][j-1])
    
    Example:
        >>> longest_common_subsequence("fosh", "fish")
        'fsh'
    """
    # TODO: Implement LCS (subsequence)
    pass
