class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        '''
        brute force: O(2^n) for every n, try either subset
        
        DP: Notice that to achieve 2 equal subsets, total must be divisible by 2,
        and if we are able to achieve target=total/2 using a set of numbers, it's given
        that the remaining set of numbers will also form total/2.

        Thus, the dp question to ask is that at a given index i, will the rest of the
        numbers be able to form the target sum?
        '''
        total = sum(nums)
        if total % 2 == 1:
            # we can't split sums evenly if the total is odd
            return False
        target = total // 2

        n = len(nums)
        fails = set()
        def recurse( currSum, i):
            if (currSum,i) in fails:
                return False
            if currSum == target:
                return True
            if i == n:
                return False

            if not recurse( currSum + nums[i], i+1) and not recurse( currSum, i+1 ):
                fails.add( (currSum,i) )
                return False
            
            return True

        return recurse(0,0)