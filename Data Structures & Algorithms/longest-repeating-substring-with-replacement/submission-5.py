class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        #optimization for runtine to just O(n)

        #tracking frequencies as we iterate can be done via freqmap
        #when a violation of window occurs 
        
        # num AAABBB -> map can determine at the point how many wrong characters

    #Solution: 

        #create a freqmap
        freq_map = {}
        #need result tracker
        res = 0
        #need a left pointer
        l = 0
        #keep a max_freq_char
        max_freq_char = 0
        #loop through s:
        for r in range(len(s)):
            #ad d the character into freqmap
            freq_map[s[r]] = freq_map.get(s[r], 0) + 1
            #calc max_freq_char
            max_freq_char = max(max_freq_char, freq_map[s[r]])
            #while (r-l + 1 - freq[s[r]] < k)
            while (r - l + 1 - max_freq_char > k):
                #subtract from freq[s[l]]
                freq_map[s[l]] -= 1
                #move left pointer
                l += 1
            #take the max res each time
            res = max(res, r - l + 1)
        return res