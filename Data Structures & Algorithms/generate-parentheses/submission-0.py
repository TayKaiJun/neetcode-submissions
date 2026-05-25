class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        answer = []

        def dfs( target, unclosed, s ):
            '''
            base case: no more new pairs to make

            each decision point:
            - if there's more target, add new parenthesis
            - if there's unclosed parenthesis, add closing parenthesis
            '''
            if target == 0:
                if unclosed > 0:
                    s += ')' * unclosed
                answer.append( s )
                return
            
            dfs( target-1, unclosed+1, s+'(')
            if unclosed > 0:
                dfs( target, unclosed-1, s+')')
        
        dfs( n, 0, '' )

        return answer