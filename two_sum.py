# https://leetcode.com/problems/two-sum/

from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ind = []
        for i in range(len(nums)):
            for j in range(len(nums)-1, i, -1):
                if abs(nums[i] + nums[j]) == abs(target):
                    return [i, j]
                else:
                    continue

        return ind


class Solution2:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        sub_arr_sum = 0

        hash_table = {}
        for i, num in enumerate(nums):
            if target - num in hash_table:
                return [hash_table[target - num], i]

            hash_table[num] = i

        return []


if __name__ == '__main__':
    sol = Solution()
    sol2 = Solution2()
    nums = [1, 3, 4, 2]
    target = 6

    print(sol.twoSum(nums=nums, target=target))
    print(sol2.twoSum(nums=nums, target=target))
