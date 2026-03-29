# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        l1 = list1
        l2 = list2
        dummy = ListNode()
        p = dummy

        while l1 != None or l2 != None:
            if l1 and l2:
                if l1.val < l2.val:
                    p.next = l1
                    l1 = l1.next
                    p = p.next
                else:
                    p.next = l2
                    l2 = l2.next
                    p = p.next
            elif l1:
                p.next = l1
                l1 = l1.next
                p = p.next
            elif l2:
                p.next = l2
                l2 = l2.next
                p = p.next
        return dummy.next
