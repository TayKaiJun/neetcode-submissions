class Solution:
    def countSubstrings(self, s: str) -> int:
        '''
        abbbbcb -> 14
        a b b b b c b
        bb bb bb
        bbb bbb
        bbbb
        bcb
        
        Brute force: O(n^2) - for every char, see if we can make a palindrome by expanding left and right

        Memoize: store a length array for each char. 
            - At each char, when we expand, we can store the max palindrome radius centered at that char
            - At subsequent chars, if they're part of the previous palindrome, we dont need to explore up to the previous radius, and add radius-index to the count

        '''
        n = len(s)
        if len(s) == 1:
            return 1
        
        count = 0

        for i in range(n):
            # odd palindromes
            left = i
            right = i
            while left >= 0 and right < n and s[left] == s[right]:
                count += 1
                left += -1
                right += 1
        
            # even palindromes
            left = i
            right = i+1
            while left >= 0 and right < n and s[left] == s[right]:
                count += 1
                left += -1
                right += 1
            
        return count
