from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        dic = {}
        for i in nums:
            if i not in dic:
                dic[i] = 1
            else:
                dic[i] = dic[i] + 1

        for k, v in dic.items():
            if dic[k] == 1:
                return k

        return -1


snum = Solution()
print(snum.singleNumber(nums=[2, 2, 3, 2]))
