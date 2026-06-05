class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        #Look at each string during pass through.
        #Use first as example, once a single string disagree then return

        #Algo: 

        #prestr
        prestr = strs[0]
        longest_sub = ""
        for i in range(len(prestr)):
            for string in strs:
                if i > len(string) - 1 or prestr[i] != string[i]:
                    return longest_sub
            longest_sub += prestr[i]

        return longest_sub
            







        