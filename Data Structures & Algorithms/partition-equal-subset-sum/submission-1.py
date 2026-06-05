class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        '''
        brute force: O(2^n) for every n, try either subset
        
        DP: Notice that to achieve 2 equal subsets, total must be divisible by 2,
        and if we are able to achieve target=total/2 using a set of numbers, it's given
        that the remaining set of numbers will also form total/2.

        Thus, the dp question to ask is that at a given index i, will the rest of the
        numbers be able to form the target sum? Memoize by storing whether we've attempted
        to resolve sum at index i before. (top down DP) O(n * target)

        (bottom up DP - improves space complexity) to O(target)
        '''
        total = sum(nums)
        if total % 2 == 1:
            # we can't split sums evenly if the total is odd
            return False
        target = total // 2

        n = len(nums)
        values = [False] * (target + 1)
        values[0] = True

        for num in nums:
            for i in range(target, num-1, -1):
                if values[i - num]:
                    values[i] = True
            if values[target]:
                return True

        return False