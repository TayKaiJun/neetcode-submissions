class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        '''
        brute force: backtracking O(n^n)
        - try each word in the word dict
            if works, recursively try the remaining substring and repeat
        - if nothing works, return false

        memo: at index i, we can check if up to this point whether it's
        been reached before, since we don't care what words were used
        False = unvisited, True = visited but fails (early return)
        - we dont need to store a success state since we should return directly
        '''
        n = len(s)
        # slight optimization: try with the longest words first
        wordDict.sort( key=len, reverse=True )
        memo = [ False ] * n

        def dfs( i ):
            if i == n:
                return True
            if memo[i]:
                return False

            for word in wordDict:
                w = len(word)
                if i+w > n:
                    # using this word goes beyond s
                    continue
                if word == s[i:i+w]:
                    if dfs(i+w):
                        return True
                    else:
                        memo[i] = True
            return False
        
        return dfs(0)