class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        #Can use a set and sliding window

        #Can keep incrementing and removing from set until duplicate is gone

        #-> O(n) space & O(n) time but need to increment each one again to remove dup

        #More optimized sliding winodw: 

        #Can keep a hashmap where key = s[i] and value is i
        #Once duplicate detected, end streak and start again from i + 1 of where dup
        h_map = {}
        l = 0
        res = 0
        
        #for loop
        for i in range(len(s)):
        #if in h_map move left pointer to its last location, update streak for r-l+1
            if s[i] in h_map:
                l = max(h_map[s[i]] + 1, l)
            h_map[s[i]] = i
            res = max(res, i - l + 1)
            
        return res

        
