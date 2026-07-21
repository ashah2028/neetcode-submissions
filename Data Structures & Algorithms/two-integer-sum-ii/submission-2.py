class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        #two pointer and sorted so just increment left or right based off what total is
        l, r = 0, len(numbers) - 1

        while l < r:
            sum = numbers[l] + numbers[r]
            if sum < target:
                l += 1
            elif sum > target:
                r -= 1
            else:
                return [l + 1, r + 1]
        

    