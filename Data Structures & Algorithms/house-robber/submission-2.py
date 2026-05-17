class Solution:
    def rob(self, nums: List[int]) -> int:
        N = len(nums)
        if N == 1:
            return nums[0]
        if N == 2:
            return max( nums[0], nums[1] )
        
        profit2 = nums[0]
        profit1 = max( nums[0], nums[1] )
        
        for i in range( 2,N ):
            thisHouse = max( profit2+nums[i], profit1)
            profit2 = profit1
            profit1 = thisHouse
            print(i, thisHouse)
        
        return profit1
