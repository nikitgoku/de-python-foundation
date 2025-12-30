# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], 
                     list2: Optional[ListNode]) -> Optional[ListNode]:
        """
        Merge two sorted linked lists into one sorted list by splicing nodes.
        
        Time: O(m + n) where m, n are lengths of input lists
        Space: O(1) - only dummy node + pointers
        """
        dummy = ListNode()  # Temporary head
        cur = dummy         # Current position to build
        
        # Merge while either list has nodes
        while list1 or list2:
            if not list1:
                cur.next = list2
                break
            if not list2:
                cur.next = list1
                break
                
            # Take smaller node
            if list1.val <= list2.val:
                cur.next = list1
                list1 = list1.next
            else:
                cur.next = list2
                list2 = list2.next
            
            cur = cur.next
        
        return dummy.next