class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        #Can use a hashset but that has O(n) space. 
        #Using a linked list, approach can look for a cycle
        #With fast/slow pointer each index points to next index given by val
        #IF the pointers meet, then there is cycle and then need new pointer
        #Point where they meet again is duplicate #

        slow, fast = 0, 0
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
        
        slow2 = 0
        while True:
            slow = nums[slow]
            slow2 = nums[slow2]
            if slow == slow2:
                return slow