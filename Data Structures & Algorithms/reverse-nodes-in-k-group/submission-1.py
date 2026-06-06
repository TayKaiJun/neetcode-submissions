# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode( next=head )

        def getKthNode( curr ):
            for _ in range(k):
                if not curr:
                    return None
                curr = curr.next
            return curr
        
        groupPrev = dummy

        while True:
            kthNode = getKthNode(groupPrev)
            if not kthNode:
                break
            
            groupNext = kthNode.next
            prev, curr = groupNext, groupPrev.next
            while curr != groupNext:
                nextNode = curr.next
                curr.next = prev
                prev = curr
                curr = nextNode
            
            temp = groupPrev.next
            groupPrev.next = kthNode
            groupPrev = temp

        return dummy.next
