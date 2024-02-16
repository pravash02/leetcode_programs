from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]):
        nums1.extend(nums2)
        nums1.sort()
        if len(nums1) % 2 != 0:
            return nums1[len(nums1) // 2]
        n = (nums1[len(nums1) // 2 - 1] + nums1[len(nums1) // 2]) / 2
        return n


med = Solution()
print(med.findMedianSortedArrays(nums1=[1, 3], nums2=[2]))
