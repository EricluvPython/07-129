# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        middle = head
        cnt = 0
        while(head.next):
            head = head.next
            cnt += 1
            if cnt % 2 == 0:
                middle = middle.next
        if cnt % 2 ==1:
            middle = middle.next
        return middle
