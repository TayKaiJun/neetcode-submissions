class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(cost) > sum(gas):
            # if total cost is greater than available gas, not possible
            return -1
        '''
        brute force is to try starting from every position and
        going through the circuit (O(n^2))

        we need to start from the global minima
        '''
        minima = 0
        totalGas = 0
        minGas = float('inf')
        for i in range(len(gas)):
            diff = gas[i] - cost[i]
            totalGas += diff
            if totalGas < minGas:
                minima = i
                minGas = totalGas
        return minima+1 if minima+1<len(gas) else 0
