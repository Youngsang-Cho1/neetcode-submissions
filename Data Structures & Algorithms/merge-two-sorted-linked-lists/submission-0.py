# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        combined_node = dummy
        curr1, curr2 = list1, list2
        while curr1 and curr2:
            if curr1.val < curr2.val:
                combined_node.next = curr1
                curr1 = curr1.next
            else:
                combined_node.next = curr2
                curr2 = curr2.next
            combined_node = combined_node.next
        
        while curr1:
            combined_node.next = curr1
            curr1 = curr1.next
            combined_node = combined_node.next
        
        while curr2:
            combined_node.next = curr2
            curr2 = curr2.next
            combined_node = combined_node.next
        
        return dummy.next



