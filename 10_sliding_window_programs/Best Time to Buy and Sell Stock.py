from typing import List


def maxProfit(prices: List[int]) -> int:
    res = 0

    lowest = prices[0]
    for price in prices:
        if price < lowest:
            lowest = price
        res = max(res, price - lowest)
    return res


prices = [10,1,5,6,7,1]
print(maxProfit(prices))
