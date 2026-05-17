'''
0: a (0,0)
1: b (0,2)
2: a (1,3)
3: b (3,3)
4: d (4,4)

O(n^2) solution: treat each position as the center of palindrome
'''

class Solution:
    def longestPalindrome(self, s: str) -> str:
        def expand(left, right):
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return left + 1, right - 1

        best_left = 0
        best_right = 0

        for i in range(len(s)):
            l1, r1 = expand(i, i)       # odd length
            l2, r2 = expand(i, i + 1)   # even length

            if r1 - l1 > best_right - best_left:
                best_left, best_right = l1, r1

            if r2 - l2 > best_right - best_left:
                best_left, best_right = l2, r2

        return s[best_left : best_right + 1]