class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #Base Case - if the strings are not the same size 
        if len(s) != len(t): 
            return False
        #Create 2 HashMap, one for each string, 
        #to represent the freq of each of the 26 english chars
        countS, countT = {}, {}
        #loop each element in the arrays
        for i in range(len(s)):
            countS[s[i]] = countS.get(s[i], 0) + 1
            countT[t[i]] = countT.get(t[i], 0) + 1
        if countS == countT:
            return True
        return False

        
