# https://leetcode.com/problems/median-of-two-sorted-arrays/


from typing import List, Optional


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        median = 0
        nums1.extend(nums2)
        new_arr = sorted(nums1)

        mid = len(new_arr) // 2

        if len(new_arr) % 2 == 0:
            median = (new_arr[mid - 1] + new_arr[mid]) / 2
        else:
            median = new_arr[mid]

        return median


class Solution2:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        pass


if __name__ == '__main__':
    sol = Solution()
    sol2 = Solution2()

    nums1 = [1, 3]
    nums2 = [2]

    print(sol.findMedianSortedArrays(nums1=nums1, nums2=nums2))
