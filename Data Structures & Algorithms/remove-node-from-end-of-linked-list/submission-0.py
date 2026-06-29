# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
# 1 2 3 4
        curr = head
        prev = None

        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        
        
# 4 3 2 1 
        reversed_head = prev
        counter = 1
        prev = None
        curr = reversed_head

        while curr:
            if counter == n and counter == 1:
                reversed_head = curr.next
                break
            elif counter == n:
                prev.next = curr.next
                break
            prev = curr
            curr = curr.next
            counter += 1
# 4 2 1
        curr = reversed_head
        prev = None

        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        
        return prev
        
        


        
        
        

        







        