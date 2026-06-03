class Solution:
    def countSubstrings(self, s: str) -> int:
        '''
        abbbbcb
        
        Brute force: O(n^2) - for every char, see if we can make a palindrome by expanding left and right

        Manacher's
        Memoize: store the radius for each char + store a right pointer of the explored palindrome
            - At each char, first take the min of dist to boundary and radius of the mirrored char
            - That's the count initially then we expand past that, updating R and center if R moved.

        '''
        n = len(s)
        if len(s) == 1:
            return 1
        
        t = "^#" + '#'.join(s) + "#$"
        
        counts = [0] * len(t)
        R = 0
        C = 0

        for i in range( 1, len(t)-1 ):
            mirrored = 2 * C - i

            if i < R:
                counts[i] = min( counts[mirrored], R-i )
            
            left = i - counts[i] - 1
            right = i + counts[i] + 1

            while t[left] == t[right]:
                counts[i] += 1
                left -= 1
                right += 1

            if i + counts[i] > R:
                R = i + counts[i]
                C = i
        
        total = 0
        for i in counts:
            total += (i+1) // 2
        return total
