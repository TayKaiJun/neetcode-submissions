class Node:
    def __init__(self, key=0, val=0, next=None, prev=None):
        self.key = key # Added key so dropTail knows what to delete from dict
        self.val = val
        self.next = next
        self.prev = prev

class LRUCache:
        
    def __init__(self, capacity: int):
        '''
        use a doubly linked list for easy swapping of order in the cache queue 
            any new hits of an old entry can get swapped to list head
            capcity > maxCapcity means we drop the tail
        use a dict to store values->linkedList nodes
        '''
        self.head = None
        self.tail = None
        self.capacity = 0
        self.maxCapacity = capacity
        self.values = {} # stores key -> Node
    
    def debug( self ):
        curr = self.head
        print( 'debugging')
        output = []
        print( self.head, self.tail )
        while curr:
            output.append( [ curr.prev.val if curr.prev else None,
                             curr.val,
                             curr.next.val if curr.next else None ] )
            curr = curr.next
        print( output , '\n')

    def updateHead( self, node: Node ):
        '''helper function to move Node to the top'''        
        # first node in the list, so head & tail
        if not self.head and not self.tail:
            self.head = node
            self.tail = node 
            # print( 'new list' )
            # self.debug()
            return

        if node == self.head:
            # already at the top, do nothing
            # print( 'node is head already' )
            return
        
        # Pluck the node out of its current position
        prev_node = node.prev
        next_node = node.next

        if prev_node:
            prev_node.next = next_node

        if next_node:
            next_node.prev = prev_node
        else:
            # If there is no 'next', this node WAS the tail.
            # We must update self.tail to the previous node.
            if prev_node: 
                self.tail = prev_node

        # Move to front
        self.head.prev = node
        node.next = self.head
        node.prev = None
        self.head = node
        # self.debug()
    
    def dropTail( self ):
        '''helper function to drop the tail'''
        # Use node.key to find the dictionary entry to delete
        key_to_del = self.tail.key 
        del self.values[ key_to_del ]

        if self.head == self.tail:
            self.head = None
            self.tail = None
        else:
            prev_node = self.tail.prev
            prev_node.next = None
            self.tail = prev_node

        self.capacity -= 1

    def get(self, key: int) -> int:
        if key in self.values:
            node = self.values[ key ]
            self.updateHead( node )
            return node.val
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        '''use get() first, if get returns -1, add new val'''
        if self.get( key ) != -1:
            # calling get() will update head already
            self.head.val = value
            return
        
        # Pass both key and value to the Node
        newNode = Node( key, value, None, None )
        self.values[ key ] = newNode

        self.updateHead( newNode )
        self.capacity += 1
        if self.capacity > self.maxCapacity:
            self.dropTail()
        return