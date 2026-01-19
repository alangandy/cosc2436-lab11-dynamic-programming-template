"""Lab 11: Test Cases for Dynamic Programming"""
import pytest
import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from dp import knapsack, longest_common_substring, longest_common_subsequence


class TestKnapsack:
    def test_basic(self):
        items = [("guitar", 1, 1500), ("stereo", 4, 3000), ("laptop", 3, 2000)]
        value, selected = knapsack(4, items)
        assert value == 3500
        assert set(selected) == {"guitar", "laptop"}
    
    def test_exact_fit(self):
        items = [("a", 2, 10), ("b", 3, 15)]
        value, selected = knapsack(5, items)
        assert value == 25
    
    def test_empty(self):
        value, selected = knapsack(10, [])
        assert value == 0
        assert selected == []
    
    def test_no_fit(self):
        items = [("heavy", 100, 1000)]
        value, selected = knapsack(5, items)
        assert value == 0


class TestLongestCommonSubstring:
    def test_basic(self):
        assert longest_common_substring("fish", "hish") == "ish"
    
    def test_no_common(self):
        assert longest_common_substring("abc", "xyz") == ""
    
    def test_full_match(self):
        assert longest_common_substring("hello", "hello") == "hello"
    
    def test_partial(self):
        result = longest_common_substring("abcdef", "zbcdf")
        assert result == "bcd"


class TestLongestCommonSubsequence:
    def test_basic(self):
        assert longest_common_subsequence("fosh", "fish") == "fsh"
    
    def test_full_match(self):
        assert longest_common_subsequence("abc", "abc") == "abc"
    
    def test_no_common(self):
        assert longest_common_subsequence("abc", "xyz") == ""
    
    def test_longer(self):
        result = longest_common_subsequence("ABCDGH", "AEDFHR")
        assert result == "ADH"


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
