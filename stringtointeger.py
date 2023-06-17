class Solution:
    def myAtoi(self, s: str) -> int:
        length, i, sign, res = len(s), 0, +1, ''

        while i < length and s[i] == ' ':
            i = i + 1

        if i < length and s[i] in ('-', '+'):
            if s[i] == '-':
                sign = -1
            else:
                sign = +1
            i = i + 1

        while i < length and s[i].isdigit():
            res, i = res + s[i], i + 1

        return max(-2 ** 31, min(sign * int(res or 0), 2 ** 31 - 1))


class Solution2:
    def myAtoi(self, s: str) -> int:
        pass


if __name__ == '__main__':
    sol = Solution()
    sol2 = Solution2()

    x = "42"

    print(sol.myAtoi(s=x))
    print(sol2.myAtoi(s=x))
