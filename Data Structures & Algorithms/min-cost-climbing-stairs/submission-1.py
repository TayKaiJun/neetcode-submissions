class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        costA = cost[0] # 2 steps away
        costB = cost[1] # 1 step away
        TOP = len(cost)
        for i in range(2, TOP):
            stepTaken = min(costA + cost[i], costB + cost[i])
            costA = costB
            costB = stepTaken
        return min(costA, costB)
