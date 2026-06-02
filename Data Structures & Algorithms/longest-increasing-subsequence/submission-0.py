class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        if n==1:
            return 1

        lastIndex = [[-1] * (n + 1) for _ in range(n)]

        def dfs( curr, last ):
            if curr == n:
                return 0
            if lastIndex[curr][last+1] != -1:
                return lastIndex[curr][last+1]
            
            # not include
            longest = dfs( curr+1, last )

            if last == -1 or nums[last] < nums[curr]:
                #include
                longest = max( longest, 1 + dfs( curr+1, curr ) )
            
            lastIndex[curr][last+1] = longest
            return longest

        return dfs(0,-1)