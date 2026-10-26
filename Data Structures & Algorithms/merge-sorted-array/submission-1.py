class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        #3 pointers 
        n1 = m - 1
        n2 = n - 1
        p3 = m + n - 1

        while n2 >= 0:
            if nums1[n1] > nums2[n2] and n1 >= 0:
                nums1[p3] = nums1[n1] 
                n1 -= 1
            else:
                nums1[p3] = nums2[n2]
                n2 -= 1
            p3 -= 1
        

        