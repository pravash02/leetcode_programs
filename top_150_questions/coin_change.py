from typing import List


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        num_coins = [float('inf')] * (amount + 1)  # +1 to account for 0 sum
        num_coins[0] = 0  # no coin selection

        for target_sum in range(len(num_coins)):
            for coin in coins:
                if (target_sum - coin) < 0:
                    continue

                num_coins[target_sum] = min(num_coins[target_sum],
                                            1 + num_coins[target_sum - coin])

        return num_coins[-1] if num_coins[-1] != float('inf') else -1


chng = Solution()
print(chng.coinChange(coins=[1, 2, 5], amount=11))
