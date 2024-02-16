from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int):
        if target in nums:
            return [nums.index(target), len(nums) - 1 - nums[::-1].index(target)]
        else:
            return [-1, -1]


class Solution2:
    def searchRange(self, nums: List[int], target: int):
        def search(x):
            lo, hi = 0, len(nums)
            while lo < hi:
                mid = (lo + hi) // 2
                if nums[mid] < x:
                    lo = mid + 1
                else:
                    hi = mid
            return lo

        lo = search(target)
        hi = search(target + 1) - 1

        if lo <= hi:
            return [lo, hi]

        return [-1, -1]


med = Solution()
print(med.searchRange(nums=[5, 7, 7, 8, 8, 10], target=8))
