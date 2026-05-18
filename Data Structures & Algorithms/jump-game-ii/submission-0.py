class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return 0

        # track max reachable and no. of jumps taken at step i
        stepsTaken = [ 0 ] * n
        # have a pointer to the furthest reachable.
        furthest = 0

        for i in range( n-1 ):
            if i + nums[i] > furthest:
                # taking the current step can potentially bring us further
                stepsTaken[i] += 1
                if i + nums[i] >= n-1:
                    return stepsTaken[i]
                for j in range( furthest+1, i + nums[i] + 1 ):
                    if j < n:
                        stepsTaken[j] = stepsTaken[i]
                    else:
                        break
                furthest = i + nums[i]
            # print( f'i={i}, furthest={furthest}')
            # print( stepsTaken )
            
        return stepsTaken[-1]
