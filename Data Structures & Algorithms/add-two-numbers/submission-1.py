# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        #need to keep track if digit >9
        #if there is leftover move to the next level 
        #now case where it goes above on the last integer 
        
        #save resulting digit after adding digit%10 into a new node
        #update the carry amount sum // 10
        #move both pointers forward
        #keep going until both lists are finished and no carry remains 
        #use dummy node to build and return final linked list
    
        d = ListNode()
        cur = d

        carry = 0
        while l1 or l2 or carry:
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0
            
            sum = v1 + v2 + carry
            carry = sum // 10
            sum = sum % 10
            cur.next = ListNode(sum)

            cur = cur.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None 
        
        return d.next
        


