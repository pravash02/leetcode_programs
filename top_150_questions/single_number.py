from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        dict = {}
        for i in nums:
            if i not in dict:
                dict[i] = 1
            else:
                dict.pop(i)
            print(dict)
        return int(*dict)


snum = Solution()
print(snum.singleNumber(nums=[2, 2, 1]))
