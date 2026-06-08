# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        carry = 0
        
        curr = dummy
        while l1:
            val = l1.val + carry
            if l2:
                val += l2.val
            carry = val // 10 # if sum is > 10, carry will be 1
            digit = val % 10
            newNode = ListNode(val=digit)
            curr.next = newNode
            curr = curr.next
            l1 = l1.next
            if l2:
                l2 = l2.next
            if not l1:
                l1 = l2 # we're always keeping l1 as the longer list.
                l2 = None
        
        if carry != 0:
            newNode = ListNode(val=carry)
            curr.next = newNode

        return dummy.next