# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        vis = []
        cur = head
        while cur != None:
            if cur not in vis:
                vis.append(cur)
            else:
                return cur
            cur = cur.next
        return None
            
