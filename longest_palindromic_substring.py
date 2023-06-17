# https://leetcode.com/problems/longest-palindromic-substring/


class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        lon_pal = ""

        for i in range(n):
            for j in range(i, n):
                substring = s[i:j + 1]
                if substring == substring[::-1] and len(substring) > len(lon_pal):
                    lon_pal = substring

        return lon_pal


class Solution2:
    def longestPalindrome(self, s: str) -> str:
        lenS = len(s)
        if lenS <= 1:
            return s
        minStart, maxLen, i = 0, 1, 0

        while i < lenS:
            if lenS - i <= maxLen / 2:
                break
            j, k = i, i
            while k < lenS - 1 and s[k] == s[k + 1]:
                k += 1
            i = k + 1
            while k < lenS - 1 and j and s[k + 1] == s[j - 1]:
                k, j = k + 1, j - 1

            if k - j + 1 > maxLen:
                minStart, maxLen = j, k - j + 1
        return s[minStart: minStart + maxLen]


class Solution3:

    # iterate from the len of i to 0 reverse order..6, 5, 4, 3
    # j starts with 0 and range will increase by one for each iteration, 1, 2, 3... len(s)-i + 1
    # and inside j loop, similarly the substring is calculated, with 0-1, 0-2, 0-3... [j:j + i]

    def longestPalindrome(self, s: str) -> str:
        for i in range(len(s), 0, -1):
            for j in range(len(s) - i + 1):
                print("i,j", i, j)
                sub = s[j:j + i]
                print('sub', sub)
                if sub == sub[::-1]:
                    return sub
        return ''


if __name__ == '__main__':
    sol = Solution()
    sol2 = Solution2()
    sol3 = Solution3()

    s = "abbabb"

    # print(sol.longestPalindrome(s=s))
    # print(sol2.longestPalindrome(s=s))
    print(sol3.longestPalindrome(s=s))
