import heapq
from statistics import median
# from sortedcontainers import SortedList


# class MedianFinder:
#     def __init__(self):
#         self.num = SortedList()
#
#     def addNum(self, num: int) -> None:
#         self.num.add(num)
#
#     def findMedian(self) -> float:
#         print(median(self.num))
#         return median(self.num)

class MedianFinder:
    def __init__(self):
        self.small = []
        self.large = []

    def addNum(self, num: int) -> None:
        if len(self.small) == len(self.large):
            heapq.heappush(self.large, -heapq.heappushpop(self.small, -num))
        else:
            heapq.heappush(self.small, -heapq.heappushpop(self.large, num))

    def findMedian(self) -> float:
        if len(self.small) == len(self.large):
            print((self.large[0] - self.small[0]) / 2.0)
            return (self.large[0] - self.small[0]) / 2.0
        else:
            print(float(self.large[0]))
            return float(self.large[0])


obj = MedianFinder()
obj.addNum(1)       # return arr = [1]
obj.addNum(2)       # return arr = [1, 2]
obj.findMedian()    # return 1.5 (i.e., (1 + 2) / 2)
obj.addNum(3)       # return arr[1, 2, 3]
obj.findMedian()    # return return 2.0
