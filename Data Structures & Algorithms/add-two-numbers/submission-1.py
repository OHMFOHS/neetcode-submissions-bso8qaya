# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        adds = 0
        dummy = ListNode()
        p = dummy
        while l1 or l2 or adds > 0:
            num1 = l1.val if l1 else 0
            num2 = l2.val if l2 else 0
            sum = num1 + num2 + adds
            if sum >= 10:
                adds = sum // 10
                sum %= 10
            else:
                adds = 0
            new = ListNode(sum)
            p.next = new
            p = p.next
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        return dummy.next
