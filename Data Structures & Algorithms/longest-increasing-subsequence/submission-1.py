class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        if n==1:
            return 1

        longest = [ -1 ] * n

        def dfs( i ):
            if longest[i] != -1:
                return longest[i]
            
            currLongest = 1
            for j in range( i+1, n ):
                if nums[i] < nums[j]:
                    currLongest = max( currLongest, 1 + dfs( j ) )
            
            longest[i] = currLongest
            return currLongest

        return max( dfs(i) for i in range(n) )