class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        val = [0] * (amount+1)
        val[amount] = 1 # 1 way to start, which is to pick 0 coins
        # issue with this now is that it doesn't tell distinct combinations
        for coin in coins:
            for curr in range(amount,-1,-1):
                if curr+coin > amount:
                    continue
                val[curr] += val[curr+coin]
        
        return val[0]
