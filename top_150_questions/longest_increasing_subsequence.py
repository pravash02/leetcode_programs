from typing import List


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if not nums:
            return 0

        n = len(nums)
        dp = [1] * n
        print(dp)

        for i in range(1, n):
            print("i = ", i)
            for j in range(i):
                print("j = ", j)
                if nums[j] < nums[i]:
                    print("prev dp i j = ", dp[i], dp[j])
                    dp[i] = max(dp[i], dp[j] + 1)

                    print("after dp i j = ", dp[i], dp[j])
                    print("dp = ", dp)

        return max(dp)


lnlis = Solution()
print(lnlis.lengthOfLIS(nums=[10, 9, 2, 5, 3, 7, 101, 18]))
