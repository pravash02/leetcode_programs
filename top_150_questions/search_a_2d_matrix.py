from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        lst = len(matrix)

        for i in range(lst):
            if matrix[i][-1] >= target:
                if target in matrix[i]:
                    return True
        return False


srch = Solution()
print(srch.searchMatrix(matrix=[[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], target=61))
