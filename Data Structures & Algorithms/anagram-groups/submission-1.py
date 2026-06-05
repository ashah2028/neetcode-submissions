class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        output = defaultdict(list)
        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord('a')] += 1
            output[tuple(count)].append(s)
        return list(output.values())
       

       #Create hashmap for output where .values() will be taken
       #Loop throug each string in array, and each character in string
       #For each string create a new array for each char in english init 0 (26 size)
       #Determine where to add 1 for each char depenent on ord subtraction
       #Then as key the tuple of array (bc array mutable) append the string
       #Return a list of the hashmap's dict values iterable