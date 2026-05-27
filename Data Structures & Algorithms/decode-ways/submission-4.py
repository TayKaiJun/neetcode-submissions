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
        n = len(s)
        startsZero = s[0] == "0"
        if n == 1:
            return 0 if startsZero else 1
        if n == 2 and startsZero:
            return 0
        
        combi_2 = 0 if startsZero else 1
        combi_1 = 0
        if not startsZero:
            if int( s[0:2] ) <= 26:
                combi_1 += 1
            if int( s[1] ) != 0:
                combi_1 += 1
        
        for i in range( 2, n ):
            curr = int( s[i] )
            prev = int( s[i-1] )
            together = int( s[i-1:i+1] )

            # CASE 1: current char is 0
            if curr == 0:
                # check if the previous number allows a 2 digit combination
                if 1 <= prev <= 2:
                    temp = combi_2
                    combi_2 = combi_1
                    combi_1 = temp
                    continue
                # else, this 0 cannot form any legal combination. return 0
                else:
                    return 0

            temp = 0
            # CASE 2: prev char is 0
            if prev == 0:
                # not possible to form a 2 digit combination since previous char is 0
                combi_2 = combi_1
                # combi_1 is unchanged
            
            # CASE 3: prev char can form a 2 digit combination 
            elif together <= 26:
                # we can take i-1 and i-2 combinations
                temp += combi_1
                combi_1 = combi_1 + combi_2
                combi_2 = temp
            
            # CASE 4: prev char cannot form 2 digit combination, there's only 1 possible way
            else:
                combi_2 = combi_1
                # combi_1 is unchanged

        return combi_1
