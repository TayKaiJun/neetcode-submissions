from collections import defaultdict
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        '''
        board does not need to be filled or solvable = we just need to check existing numbers
        track existence according to row, column, 3x3 box
        for each number, check if it already existed in r/c/b, if not then update
        '''
        def box( row:int, col:int ) -> int:
            # helper function to convert (r,c) into box number.
            #   0,1,2
            #   3,4,5
            #   6,7,8
            return ( ( row // 3 ) * 3 + col // 3 )
        
        row = defaultdict(set)
        col = defaultdict(set)
        square = defaultdict(set)

        for r in range( 9 ):
            for c in range( 9 ):
                # print( r, c, board[ r ][ c ] )
                if board[ r ][ c ] == '.':
                    continue
                num = int( board[ r ][ c ] )
                boxCoord = box( r, c )
                if num in row[ r ] or num in col[ c ] or num in square[ boxCoord ]:
                    return False
                row[ r ].add( num )
                col[ c ].add( num )
                square[ boxCoord ].add( num )
                # print( row, col, square )
        return True

