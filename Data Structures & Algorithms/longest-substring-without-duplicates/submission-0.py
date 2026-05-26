class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0

        seen = {}
        left = 0
        longest = float('-inf')

        for right in range( len(s) ):
            char = s[right]
            if char in seen:
                # move left ptr up to seen[char]+1 position
                lastSeen = seen[char]
                for i in range( left, lastSeen+1 ):
                    del seen[ s[i] ]
                left = lastSeen+1
                seen[char] = right
            else:
                # new char, extend the substring (by not moving left ptr)
                # store the char position, and check if it's longer
                seen[char] = right
                longest = max( longest, right-left+1 )

        return longest