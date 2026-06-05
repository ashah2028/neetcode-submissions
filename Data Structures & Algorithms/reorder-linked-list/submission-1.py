# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow, fast = head, head.next


        #Find midpoint 
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        #Starting from slow (midpoint) traverse list

        curr = slow.next
        prev = slow.next = None
        while curr: 
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        
        #Now combine with first half of list
        first, curr = head, prev #otherwise null if curret
        while curr: 
            tmp1, tmp2 = first.next, curr.next
            first.next = curr
            curr.next = tmp1
            first, curr = tmp1, tmp2


