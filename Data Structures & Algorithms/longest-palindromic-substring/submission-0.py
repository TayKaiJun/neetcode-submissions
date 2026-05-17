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
        longestLength = float('-inf')
        longest = ""
        centers = {}
        
        n = len(s)
        for i in range( n ):
            # odd length palindrome
            left = i
            right = i
            while left >= 0 and right < n:
                if s[left] != s[right]:
                    break
                centers[i] = [left,right]
                left -= 1
                right +=1
            
            length = centers[i][1] - centers[i][0] + 1
            if length > longestLength:
                longestLength = length
                longest = s[ centers[i][0] : centers[i][1]+1 ]
            
            # even length palindrome
            left = i
            right = i+1
            while left >= 0 and right < n:
                if s[left] != s[right]:
                    break
                centers[i] = [left,right]
                left -= 1
                right +=1
            
            length = centers[i][1] - centers[i][0] + 1
            if length > longestLength:
                longestLength = length
                longest = s[ centers[i][0] : centers[i][1]+1 ]
        
        return longest
