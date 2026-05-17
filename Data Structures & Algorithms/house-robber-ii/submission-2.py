class Solution:
    def rob(self, nums: List[int]) -> int:
        N = len( nums )
        if N <= 3:
            # only 1 house to rob
            return max( nums )
        
        '''
        in 1 pass, track 2 possible profits:
        - case 1: rob the first house (this means the last house CANNOT be robbed later)
        - case 2: skip the first house (this means the last house CAN be robbed later)
        '''
        
        # case 1: rob house 1
        profitA = nums[0]
        profitB = max( nums[0], nums[1] )

        # case 2: skip house 1
        profit1 = nums[1]
        profit2 = max( nums[1], nums[2] )
        
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