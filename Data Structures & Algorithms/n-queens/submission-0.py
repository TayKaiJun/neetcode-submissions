class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        '''
        Brute force solution:
        for each (r,c) try to place a queen. append solution if successfully places all rows
        track 4 dimensions whenever trying to place a queen: row, column, diag(l-r), diag(r-l)

        algorithm to determine diag in a 4x4 square: 
        (3,0) = 0
        (3,1),(2,0) = 1
        (1,0),(2,1),(3,2) = 2
        (0,0),(1,1),(2,2),(3,3) = 3
        (0,1),(1,2),(2,3) = 4
        (1,3),(0,2) = 5
        (0,3) = 6

        D (left to right) = (N-1) + (c-r)

        (0,0) = 0
        (1,0),(0,1) = 1
        (2,0),(1,1),(0,2) = 2
        (3,0),(2,1),(1,2),(0,3) = 3
        (3,1),(2,2),(1,3) = 4
        (2,3),(3,2) = 5
        (3,3) = 6
        D (right to left) = r+c
        '''

        answer = []
        legalStart = {
            'row': [ True ] * n,
            'col': [ True ] * n,
            'diagToRight': [ True ] * ( 2 * n - 1 ),
            'diagToLeft': [ True ] * (2 * n - 1 ),
        }

        def diagIndexToRight( r,c ):
            # left to right diagonals
            return n-1 + c-r
        
        def diagIndexToLeft( r,c ):
            # right to left diagonals
            return r+c

        def checkLegal( legal, r, c ):
            return legal['row'][r] and legal['col'][c] and \
                    legal['diagToRight'][ diagIndexToRight(r,c) ] and \
                    legal['diagToLeft'][ diagIndexToLeft(r,c) ]
        
        def updateLegal( legal, r, c, val ):
            legal['row'][r] = val
            legal['col'][c] = val
            legal['diagToRight'][ diagIndexToRight(r,c) ] = val
            legal['diagToLeft'][ diagIndexToLeft(r,c) ] = val


        def dfs( legal, r, sol):
            if r == n:
                answer.append(list(sol))  # Append a copy of the solution
                return
            
            for i in range(n):
                if checkLegal(legal, r, i):
                    updateLegal(legal, r, i, False)
                    
                    # Create the row string: '.' for empty spaces, 'Q' at index i
                    row_string = '.' * i + 'Q' + '.' * (n - 1 - i)
                    sol.append(row_string)
                    
                    # Move to the next row (r + 1)
                    dfs( legal, r + 1, sol)
                    
                    # Backtrack: undo the legal state and pop the row string
                    updateLegal(legal, r, i, True)
                    sol.pop()

        dfs( legalStart, 0, [] )
        return answer