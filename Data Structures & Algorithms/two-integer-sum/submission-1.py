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
            # checks if we have already seen the complement
            if remainder in indices:
                j = indices[ remainder ][0]
                # prevents returning 2 of the same indices
                #    (e.g. 5+5=10 in [4,5,6],t=10)
                if i != j:
                    return sorted([i,j])
        return []