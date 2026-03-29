# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        def find_mid(head):
            slow = fast = head
            while fast and fast.next:
                slow = slow.next
                fast = fast.next.next
            return slow
        def reverse_list(head):
            prev = None
            cur = head
            while cur:
                next = cur.next
                cur.next = prev
                prev = cur
                cur = next
            return prev
        mid = find_mid(head)
        h1 = head
        h2 = reverse_list(mid)
        while h2.next:
            next1 = h1.next
            next2 = h2.next
            h1.next = h2
            h2.next = next1
            h1 = next1
            h2 = next2



        