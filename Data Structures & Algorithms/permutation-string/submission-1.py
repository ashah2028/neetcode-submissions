class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        #Constraints
        if len(s1) > len(s2):
            return False
        #freq array or chars (will use ord)
        s2freq, s1freq = [0] * 26,[0] * 26

        #fill freq array for both
        for i in range(len(s1)):
            s1freq[ord(s1[i]) - ord('a')] += 1
            s2freq[ord(s2[i]) - ord("a")] += 1
        
        #Want to count up to 26 matches for the indices
        matches = 0
        for i in range(26):
            matches += (1 if s1freq[i] == s2freq[i] else 0)


        #Sliding Window
        l = 0
        for i in range(len(s1), len(s2)):
            if matches == 26:
                return True
            index = ord(s2[i]) - ord("a")
            s2freq[index] += 1
            #update the matches
            if s1freq[index] == s2freq[index]:
                matches += 1
            #match broken
            elif s1freq[index] + 1 == s2freq[index]:
                matches -= 1
            
            #move window
            index = ord(s2[l]) - ord("a")
            s2freq[index] -= 1
            if s1freq[index] == s2freq[index]:
                matches += 1
            elif s1freq[index] - 1 == s2freq[index]:
                matches -= 1
            l+= 1
        return matches == 26

            

        