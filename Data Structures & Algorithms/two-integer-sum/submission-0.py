class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indices = {}
        for i in range(len(nums)):
            num = nums[i]
            if num in indices:
                indices[num].append(i)
            else:
                indices[num] = [i]
            
            print(indices)
            remainder = target - num
            if remainder in indices:
                j = indices[ remainder ][0]
                if i != j:
                    return sorted([i,j])
        return []