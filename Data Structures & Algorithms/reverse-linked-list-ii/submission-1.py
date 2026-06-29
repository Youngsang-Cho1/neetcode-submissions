# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        counter = 0
        prev = dummy
        
        while counter < left - 1:
            prev = prev.next
            counter += 1
        curr = prev.next

        while counter < right - 1:
            temp = curr.next
            curr.next = temp.next
            temp.next = prev.next
            prev.next = temp
            counter += 1
        return dummy.next



        