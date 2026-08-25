# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        '''
        - add all first element to a min heap
        - pop first element of the min heap, then add from the list that was popped from
        O(n log k) -> n is elements in a list, k is no. of list 
        '''
        heap = [] # need to store (node.val, node)
        counter = 0
        for head in lists:
            if head:
                heapq.heappush( heap, (head.val, counter, head) )
                counter += 1
        curr = ListNode()
        newList = curr
        while heap:
            _,_,node = heapq.heappop( heap )
            curr.next = node
            nextInList = node.next
            if nextInList:
                heapq.heappush( heap, (nextInList.val, counter, nextInList) )
                counter += 1
            curr = curr.next
        return newList.next

