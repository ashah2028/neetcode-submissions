class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        #Sliding window: 
        #Data Structure:

        #Initalize: 
        max_sub = 0
        l = 0
        char_set = set()

        #loop O(N):
        for r in range(len(s)):
            while s[r] in char_set:
                char_set.remove(s[l])
                l += 1
            char_set.add(s[r])
            max_sub = max(max_sub, r - l + 1)
        return max_sub
        
        

        