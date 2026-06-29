# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        num1, num2 = '', ''
        
        while l1:
            num1 = str(l1.val) + num1
            l1 = l1.next
        while l2:
            num2 = str(l2.val) + num2
            l2 = l2.next
        two_sum = str(int(num1) + int(num2))
        # print(num1, num2, two_sum)
        
        head = ListNode(int(two_sum[-1]))
        res = head
        
        for i in range(len(two_sum) - 2, -1, -1):
            # print(i)
            curr = ListNode(int(two_sum[i]))
            head.next = curr
            head = head.next

        return res
            
            


        

        