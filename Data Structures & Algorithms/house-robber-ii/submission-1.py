class Solution:
    def rob(self, nums: List[int]) -> int:
        N = len( nums )
        if N <= 3:
            # only 1 house to rob
            return max( nums )
        
        # case 1: rob house 1
        profitA = nums[0] # max profit at the point of robbing the house 2 away
        profitB = max( nums[0], nums[1] ) # max profit at the point of robbing the previous house

        # case 2: skip both house 1 and 2
        profit1 = nums[1] # max profit at the point of robbing the house 2 away
        profit2 = max( nums[1], nums[2] ) # max profit at the point of robbing the previous house
        
        for i in range( 2, N ):
            if i < N-1:
                profitNow = max(profitA + nums[i], profitB)
                profitA = profitB
                profitB = profitNow
            if i > 2:
                profitNow_1 = max(profit1 + nums[i], profit2)
                profit1 = profit2
                profit2 = profitNow_1
        
        return max( profitB, profit2 )