class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        #solution:

        #need to track max window, 

        res = 0

        #create hashset
        charSet = set(s)

        #loop through the charset
        for c in charSet:
            #track freq of char (counter)
            counter = 0
            #need pointer l
            l = 0
            #loop through the string
            for r in range(len(s)):
                #if s[i] == char, incr counter
                if s[r] == c:
                    counter += 1

                #while window r-l + 1  - counter > k, incr left pointer,
                while (r - l + 1 - counter) > k:
                    #if char from l pointer is char, deinc counter
                    if s[l] == c:
                        counter -= 1
                    l += 1
                #take res with max
                res = max(res, r - l + 1)
        #return res
        return res

