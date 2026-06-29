# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = head
        first, second = dummy, dummy.next

        while second != None:
            common_divisor = 1
            length = min(first.val, second.val)
            for i in range(1, length + 1):
                if not first.val % i and not second.val % i and i > common_divisor:
                    common_divisor = i
            new = ListNode(common_divisor)
            first.next = new
            new.next = second

            first = second
            second = first.next
        return dummy

        