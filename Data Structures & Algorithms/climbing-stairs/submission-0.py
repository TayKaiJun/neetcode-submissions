'''
Brute force:
- 2^n -> recursive DFS where every step_we have 2 decisions

1-DP (bottom up):
- At sol[i] = sol[i-1] + sol[i-2] -> calculations up to that point do not change
Base cases:
- sol[1]=1
- sol[2]=2
'''
class Solution:
    def climbStairs(self, n: int) -> int:
        step_2 = 1
        step_1 = 2
        if n == 1:
            return 1
        if n == 2:
            return 2
        
        for i in range( 3, n+1 ):
            newStep = step_2 + step_1
            step_2 = step_1
            step_1 = newStep
      
        return step_1