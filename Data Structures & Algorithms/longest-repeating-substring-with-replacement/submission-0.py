class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        #Brute Force: Go through each character at every index and try 
        #every possible substring and keep track of how many times each char appears

        res = 0 #longest valid window

        count = {}

        l = 0
        maxf = 0

        for r in range(len(s)):
            count[s[r]] = 1 + count.get(s[r], 0)
            maxf = max(maxf, count[s[r]])

            while (r - l + 1) - maxf > k:
                count[s[l]] -= 1
                l += 1
            res = max(res, r - l + 1)
            
        return res
            
        

            

    
        
            



        