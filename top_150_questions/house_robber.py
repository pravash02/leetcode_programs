from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        dp = [0 for i in range(len(nums))]

        dp[0] = nums[0]

        for i in range(1, len(nums)):
            dp[i] = max(nums[i] + dp[i - 2], dp[i - 1])

        return max(dp)


rob = Solution()
print(rob.rob(nums=[2, 7, 9, 3, 1]))
