class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        coins.sort()
        n = len(coins)
        memo = [ [-1]*(amount+1) for _ in range(n) ]

        def dfs( i, amt ):
            if amt == 0:
                return 1
            if i >= n:
                return 0
            if memo[i][amt] != -1:
                return memo[i][amt]
            
            res = 0
            if amt >= coins[i]:
                res = dfs( i+1, amt )
                res += dfs( i, amt-coins[i])
            memo[i][amt] = res
            return res

        return dfs(0, amount)
