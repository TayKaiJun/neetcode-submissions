class Solution:
    def numDecodings(self, s: str) -> int:
        '''
        up to index i, every possible combination (minus potential [i-1,i] combinations) will be discovered

        e.g.
        1212021
        i = 0: [1]                  1 way
        i = 1: [12, 2+i=0]          2 ways 
        i = 2: [21+i=0, 1+i=1]      3 ways
        i = 3: [12+i=1, 2+i=2]      5 ways
        i = 4: [20+i=2]             3 ways
        i = 5: [2+i=4]              3 ways
        i = 6: [21+i=4, 1+i=5]      6 ways
        '''
        if not s or s[0] == "0":
            return 0
        
        n = len(s)
        # combi_2 represents dp[i-2] (initialized for index -1)
        # combi_1 represents dp[i-1] (initialized for index 0)
        combi_2 = 1  # Base case: empty string has 1 way to decode
        combi_1 = 1  # Base case: string of length 1 (and not '0') has 1 way
        
        for i in range(1, n):
            current_ways = 0
            
            # 1. Can we take s[i] as a single digit?
            # It just needs to be anything except '0'
            if s[i] != "0":
                current_ways += combi_1
                
            # 2. Can we take s[i-1] and s[i] together as a two-digit number?
            # It must be between "10" and "26"
            together = int(s[i-1 : i+1])
            if 10 <= together <= 26:
                current_ways += combi_2
                
            # If both are impossible (e.g., "30"), current_ways becomes 0, 
            # which will make the entire string impossible to decode.
            if current_ways == 0:
                return 0
                
            # Shift our states forward for the next iteration
            combi_2 = combi_1
            combi_1 = current_ways
            
        return combi_1
