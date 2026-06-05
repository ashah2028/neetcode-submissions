class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        #Brute Force: go through each number as the start and count 
        #length of sequence formed with starting element O(n^2)

        #To reduce complexity, of the while loop I have to find out when a sequence can start
        # if num - 1 not in the given array then start of sequeunce. Only build if start
        counter = 0
        store = set(nums)

        for num in nums:
            count = 0
            curr = num
            prev = curr - 1
            if prev not in store:
                while curr in store:
                    count += 1
                    curr += 1

            counter = max(counter, count)

        return counter
        