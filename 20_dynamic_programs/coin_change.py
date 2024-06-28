def coinChange(coins, amount):
    num_coins = [float('inf')] * (amount + 1)  # +1 to account for 0 sum
    num_coins[0] = 0  # no coin selection

    for target_sum in range(len(num_coins)):
        for coin in coins:
            if (target_sum - coin) < 0:
                continue

            num_coins[target_sum] = min(num_coins[target_sum],
                                        1 + num_coins[target_sum - coin]) # Is the minimum number of coins needed to make up the remaining amount.
                                                                          # adding 1, accounts for the current coin being used.

    if num_coins[-1] != float('inf'):
        return num_coins[-1]
    else:
        return -1


coins = [1, 5, 10]
amount = 12
print(coinChange(coins, amount))
