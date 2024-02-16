from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if len(nums) == 0:
            return 0
        if target in nums:
            return nums.index(target)
        else:
            if nums[-1] < target:
                return len(nums)
            else:
                for i in nums:
                    if target < i:
                        return nums.index(i)


srchins = Solution()
print(srchins.searchInsert(nums=[1, 3, 5, 6], target=7))
