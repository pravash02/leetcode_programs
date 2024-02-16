from heapq import heapify, heappush, heappop
from typing import List


class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        heap1 = [(c, -p) for c, p in zip(capital, profits)]
        heapify(heap1)
        heap2 = []

        for i in range(k):
            while heap1 and heap1[0][0] <= w:
                heappush(heap2, heappop(heap1)[1])

            w += -heappop(heap2) if heap2 else 0

        return w


sol = Solution()
print(sol.findMaximizedCapital(k=2, w=0, profits=[1, 2, 3], capital=[0, 1, 1]))
