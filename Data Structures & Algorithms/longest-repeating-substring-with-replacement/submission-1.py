class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        #Brute Force: Go through each character at every index and try 
        #every possible substring and keep track of how many times each char appears
        
        #Create a freqMap for the chars
        freqMap =defaultdict(int)
        #pointer for sliding window 
        l = 0
        #maxFreq
        maxFreq = 0
        #maxSize
        maxSize = 0

        #loop through the array
        for r in range(len(s)):
            freqMap[s[r]] += 1
            maxFreq = max(maxFreq, freqMap[s[r]])
        #update maxfreq char
            while (r - l + 1) - maxFreq > k:
                freqMap[s[l]] -= 1
                l += 1
            maxSize = max(maxSize, r - l + 1)
        return maxSize
        #use formula for while loop if too big window
        #Update maxWindowsize

            
        

            

    
        
            



        