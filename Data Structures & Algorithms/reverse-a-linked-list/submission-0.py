# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev, curr = None, head

        while curr:
            temp = curr.next 
            curr.next = prev 
            prev = curr 
            curr = temp
        return prev



'''prev, curr = 0, 1 -> 1, 0
temp = curr.next -- 2
curr.next = prev -- 1 -> 0
prev = curr 
curr = temp'''
        