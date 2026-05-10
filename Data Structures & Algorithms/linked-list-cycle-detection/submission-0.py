# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # empty list
        if not head:
            return False
        # only 1 node and not pointing to itself
        if not head.next:
            return False

        slow, fast = head, head.next
        while slow != fast:
            slow = slow.next
            # if fast's nextPtr is null, we know we reached the end so no cycle
            if not fast or (fast and not fast.next):
                return False
            fast = fast.next.next
        
        # fast caught up with slow, so a cycle was found
        return True
        
