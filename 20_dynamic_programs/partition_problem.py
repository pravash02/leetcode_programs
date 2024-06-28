def findPartiion(nums):
    total_sum = sum(nums)

    # If total sum is odd, cannot partition into two equal subsets
    if total_sum % 2 != 0:
        return False

    # The target sum for each subset
    target = total_sum // 2

    # DP array to track if a subset with sum `j` is possible
    dp = [False] * (target + 1)
    dp[0] = True  # Zero sum is always possible with an empty subset

    # Update the dp array based on the numbers in the array
    for num in nums:
        print(dp)
        for j in range(target, num - 1, -1):    # iterates backward from 7 -> num-1
            print(j)
            dp[j] = dp[j] or dp[j - num]
        print(dp)
        print('-----')

    return dp[target]


# Driver code
arr = [1, 3, 3, 2, 3, 2]
n = len(arr)

if findPartiion(arr) == True:
    print("Can be divided into two subsets of equal sum")
else:
    print("Can not be divided into two subsets of equal sum")