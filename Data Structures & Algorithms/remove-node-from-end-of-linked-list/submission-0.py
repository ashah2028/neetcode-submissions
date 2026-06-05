# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        count = 0
        curr = head
        #Find how long linked list is
        while curr:
            count += 1
            curr = curr.next
        #Difference from the front 
        index = count - n
        if index == 0:
            return head.next
        curr = head
        #Remove that node 
        while index > 1:
            curr = curr.next
            index -= 1
        curr.next = curr.next.next
        return head
    
            

        


        