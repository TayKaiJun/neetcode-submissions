'''
Optimized O(n) solution: Manacher's Algorithm
makes use of palindrome symmetric property to reduce expansion space
- expansion space is whatever's outside the sliding window of current longest palindrome
- amortized by storing the known radius of the mirrorer character within a longer palindrome
deals with ONLY ODD palindrom case by using separators -> palindromes can be centered at a separator
'''

class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s:
            return ""
        
        # transform string so all palindromes become odd length
        # example:
        # "abba" -> "#a#b#b#a#"
        transformed = "#" + "#".join(s) + "#"
        n = len(transformed)
        
        # stores the radii of a given center at index i
        radii = [0] * n

        # stores the center and rightmost boundary of current known palindrome
        center = 0
        right = 0

        # stores the center and radius of longest known palindrome
        longestCenter = 0
        longestRadius = 0

        for i in range(n):

            # find mirrored position of current char in the current known palindrome
            mirror = 2 * center - i

            if i < right:
                # we're still within an already established palindrome
                # update current radii with min() as we cannot safely establish chars outside the 
                # current rightmost boundary is part of the palindrome as it has not been explored yet
                radii[i] = min(right - i, radii[mirror])
            
            # attempt to expand palindrome centered at i
            while (
                i - radii[i] - 1 >= 0 and
                i + radii[i] + 1 < n and
                transformed[i - radii[i] - 1] == transformed[i + radii[i] + 1]
            ):
                radii[i] += 1
            
            # if our expansion explored past rightmost boundary, update
            if i + radii[i] > right:
                center = i
                right = i + radii[i]

            # update longest known palindrome
            if radii[i] > longestRadius:
                longestRadius = radii[i]
                longestCenter = i
        
        # map transformed indices back to original string indices
        start = (longestCenter - longestRadius) // 2
        return s[start : start + longestRadius]
