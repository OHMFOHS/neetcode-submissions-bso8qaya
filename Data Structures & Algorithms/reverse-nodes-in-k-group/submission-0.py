# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        def reverse_list(root, k):
            prev = None
            cur = root
            for _ in range(k):
                next = cur.next
                cur.next = prev
                prev = cur
                cur = next
            return prev, cur

        length = 0
        p = head
        while p:
            length += 1
            p = p.next
        
        if length // k == 0:
            return head

        dummy = ListNode()
        dummy.next = head

        p0 = dummy

        for _ in range(length // k):
            prev, cur = reverse_list(p0.next, k)
            p0.next.next = cur
            p0.next = prev
            for _ in range(k):
                p0 = p0.next
        return dummy.next


            

            
                