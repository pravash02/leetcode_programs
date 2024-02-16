import heapq
from typing import List


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heapq.heapify(nums)
        print(heapq.nlargest(k, nums))
        return heapq.nlargest(k, nums)[-1]

    def findKthLargest_2(self, nums: List[int], k: int) -> int:
        nums.sort()
        return nums[k * -1]


sol = Solution()
print(sol.findKthLargest(nums=[3, 2, 3, 1, 2, 4, 5, 5, 6], k=4))
