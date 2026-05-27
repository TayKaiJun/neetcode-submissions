class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        '''
        First thought: greedy -> but this may leave out possible solutions

        DP approach:
        For any X_i amount, we can store the optimal calculations of X_0...i
        Then, for X_i, we can try all coins possible and get opt[ X_(i - coin) ] and store the most optimal
        '''

        opt = [ float('inf') ] * ( amount + 1 )
        opt[0] = 0 # BASE CASE: Choosing 0 coins is a valid way to make up amount 0.

        for i in range( 1, amount+1 ):
            for coin in coins:
                remainder = i-coin
                # CASE 1: using this coin makes amount goes negative, skip considerations of this coin
                if remainder < 0:
                    continue
                # CASE 2: use this coin only if it's more optimal
                # note that if opt[remainder]=inf, it means that it was impossible to reach that value
                # then inf+1 is still inf
                opt[i] = min( opt[remainder]+1, opt[i] )

        # no solution
        if opt[ amount ] == float('inf'):
            return -1

        return opt[ amount ]