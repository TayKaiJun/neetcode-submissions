class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        if n == 1:
            return True
        reachable = [0] * n

        reachable[0] = nums[0]
        for i in range( n ):
            furthest = max( i + nums[i], reachable[i] )
            # print(i,furthest)
            if reachable[i] == 0:
                return False
            if furthest >= n:
                return True

            for j in range( 1, nums[i]+1 ):
                reachable[i+j] = furthest
            # print(reachable)
            
        return reachable[-1] > 0