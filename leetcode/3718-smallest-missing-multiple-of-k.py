class Solution:
    def missingMultiple(self, nums: List[int], k: int) -> int:
        nums.sort()
        leftPtr = 0
        curr = k
        while leftPtr < len(nums):
            if nums[leftPtr] < curr:
                leftPtr += 1
                continue
            if nums[leftPtr] == curr:
                curr += k
                leftPtr += 1
                continue
            if nums[leftPtr] > curr:
                return curr
        return curr

