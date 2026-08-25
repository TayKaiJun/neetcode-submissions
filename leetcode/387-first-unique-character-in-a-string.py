from collections import Counter
class Solution:
    def firstUniqChar(self, s: str) -> int:
        count = Counter( s )
        first = float('inf')
        # Iterate through the string in order; the first character with a count of 1 wins.
        for i, char in enumerate(s):
            if count[char] == 1:
                return i
                
        return -1