from collections import Counter

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            # strings of different lengths cannot be anagrams
            return False

        countS = Counter(s)
        countT = Counter(t)
        return countS == countT
        