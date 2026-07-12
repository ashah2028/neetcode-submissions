class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        #Go through each num, track freq, if hits majority append output space
        #Data strcut -> hashmap to keep count of freq: O(n)
        #Output array: O(n)

        counts = defaultdict(int)
        maj_val = len(nums) // 3 + 1
        res = []
        for num in nums:
            if counts[num] + 1 == maj_val and num not in res:
                res.append(num)
                counts[num] += 1
            else:
                counts[num] += 1

        return res

        #Need to recheck syntax for sets and list**
