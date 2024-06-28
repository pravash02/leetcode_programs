def shortestCommonSupersequence(str1: str, str2: str):
    m, n = len(str1), len(str2)

    # Create the DP table
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    # Fill the DP table
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if str1[i - 1] == str2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    # The length of the LCS is dp[m][n]
    lcs_length = dp[m][n]
    # scs_length = m + n - lcs_length

    scs = []
    i, j = m, n
    while i > 0 and j > 0:
        if str1[i - 1] == str2[j - 1]:
            scs.append(str1[i - 1])
            i -= 1
            j -= 1
        elif dp[i - 1][j] > dp[i][j - 1]:
            scs.append(str1[i - 1])
            i -= 1
        else:
            scs.append(str2[j - 1])
            j -= 1

    # Add the remaining characters from str1 or str2
    while i > 0:
        scs.append(str1[i - 1])
        i -= 1
    while j > 0:
        scs.append(str2[j - 1])
        j -= 1

    scs.reverse()
    print(f"Length of Shortest Common Subsequence is {len(scs)}")
    print(f"Shortest Common Subsequence is '{''.join(scs)}'")


# Example usage:
str1 = "AGGTAB"
str2 = "GXTXAYB"
shortestCommonSupersequence(str1, str2)
