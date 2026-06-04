class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        # Initialize the global maximum, and local tracking variables
        global_max = nums[0]
        curr_max = nums[0]
        curr_min = nums[0]
        
        for i in range(1, len(nums)):
            val = nums[i]
            
            # CRITICAL TRICK: If the value is negative, multiplying by it 
            # will make the max smaller and the min bigger. So swap them!
            if val < 0:
                curr_max, curr_min = curr_min, curr_max
            
            # Local optimization: do we extend the existing subarray or start fresh?
            curr_max = max(val, curr_max * val)
            curr_min = min(val, curr_min * val)
            
            # Update the best we've seen anywhere in the array so far
            global_max = max(global_max, curr_max)
            
        return global_max