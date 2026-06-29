# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next:
            return
        # getting length of the linked list
        curr = head
        length = 1
        while curr.next:
            length+=1
            curr = curr.next
        # dividing the linked list
        curr = head
        idx = 1
        l1 = ListNode()
        l2 = ListNode()
        mid = (length + 1) // 2
        prev, curr = None, head
        for _ in range(mid):
            prev, curr = curr, curr.next
        prev.next = None
        l1, l2 = head, curr
            
        # flipping the order of l2
        prev, curr = None, l2
        
        while curr:
            next_elem = curr.next
            curr.next = prev
            prev = curr
            curr = next_elem
        l2 = prev
        # merging l1 and l2
        curr = head
        l1 = head.next
        counter = 1
        while l1 and l2:
            if counter % 2 == 1:
                curr.next = l2
                l2 = l2.next
            else:
                curr.next = l1
                l1 = l1.next
            curr = curr.next
            counter += 1
        
        if l1:
            curr.next = l1 
        else:
            curr.next = l2
        return
        


        




        

        
        


        