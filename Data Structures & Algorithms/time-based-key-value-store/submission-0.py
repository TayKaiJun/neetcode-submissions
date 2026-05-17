class Node:
    def __init__( self, time, val ):
        self.time = time
        self.val = val
        self.left = None
        self.right = None

class Bst:
    def __init__( self, time, val ):
        self.root = Node( time, val )
    
    def add( self, time, val ):
        newNode = Node( time, val )
        curr = self.root
        while curr:
            if time <= curr.time:
                if not curr.left:
                    curr.left = newNode
                    return
                else:
                    curr = curr.left
            else:
                if not curr.right:
                    curr.right = newNode
                    return
                else:
                    curr = curr.right

    def find( self, time ):
        '''
                    5
            3.            9
               4        8
        '''
        curr = self.root
        lastGreatestVal = ""
        while curr:
            if curr.time <= time:
                lastGreatestVal = curr.val
                curr = curr.right
            else:
                curr = curr.left
        
        return lastGreatestVal

class TimeMap:

    def __init__(self):
        self.timeMap = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.timeMap:
            timeBst = self.timeMap[ key ]
            timeBst.add( timestamp, value )
        else:
            newTimeBst = Bst( timestamp, value )
            self.timeMap[ key ] = newTimeBst        

    def get(self, key: str, timestamp: int) -> str:
        if key in self.timeMap:
            return self.timeMap[ key ].find( timestamp )
        else:
            return ""
        
