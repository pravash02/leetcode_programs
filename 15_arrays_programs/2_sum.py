# https://leetcode.com/problems/two-sum/

from typing import List


def twoSum_1(nums: List[int], target: int) -> List[int]:
    ind = []
    for i in range(len(nums)):
        for j in range(len(nums)-1, i, -1):
            if abs(nums[i] + nums[j]) == abs(target):
                return [i, j]
            else:
                continue

    return ind


def twoSum(nums: List[int], target: int) -> List[int]:
    sub_arr_sum = 0

    hash_table = {}
    for i, num in enumerate(nums):
        if target - num in hash_table:
            return [hash_table[target - num], i]

        hash_table[num] = i

    return []


nums = [1, 3, 4, 2]
target = 6

print(twoSum_1(nums=nums, target=target))
print(twoSum(nums=nums, target=target))
