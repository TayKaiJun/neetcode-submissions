class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        digitMap = {
            '2':'abc',
            '3':'def',
            '4':'ghi',
            '5':'jkl',
            '6':'mno',
            '7':'pqrs',
            '8':'tuv',
            '9':'wxyz'
        }
        
        answer = []
        n = len( digits )

        def dfs( word: str, i: int ):
            if i == n:
                answer.append( word )
                return
            
            for char in digitMap[ digits[i] ]:
                dfs( word+char, i+1 )
            
        dfs( "", 0 )
        return answer
