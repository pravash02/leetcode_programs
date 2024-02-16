from typing import List


class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        low = 0
        high = len(nums) - 1

        while low < high:
            mid = (low + high) // 2
            if nums[mid] < nums[mid + 1]:
                low = low + 1
            else:
                high = mid
        return low


fndpk = Solution()
print(fndpk.findPeakElement(nums=[1, 2, 3, 1]))
