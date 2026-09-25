# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        first_list = []
        curr = l1
        while curr:
            first_list.append(str(curr.val))
            curr = curr.next
        
        first_num = int(''.join(first_list[::-1]))

        second_list = []
        curr = l2
        while curr:
            second_list.append(str(curr.val))
            curr = curr.next

        second_num = int(''.join(second_list[::-1]))

        total = first_num + second_num
        total_list = (str(total)[::-1])

        head = ListNode()
        curr = head
        for i in range(len(total_list)):
            next_node = ListNode()
            next_node.val = int(total_list[i])
            curr.next = next_node
            curr = curr.next
        return head.next
        
