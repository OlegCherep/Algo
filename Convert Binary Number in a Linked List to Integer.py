# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        cur = head
        lst = []
        while cur != None:
            lst.append(str(cur.val))
            cur = cur.next
        return str(int("".join(lst), 2))