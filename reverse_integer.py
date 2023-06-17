class Solution:
    def reverse(self, x: int) -> int:
        rev_num = 0
        quotient = 0
        flag = False

        if x < 0:
            flag = True
            x = abs(x)

        while len(str(x)) > 1:
            remainder = x % 10

            quotient = x // 10

            rev_num = rev_num * 10 + remainder

            x = quotient

        if len(str(quotient)) > 0 and quotient != 0:
            remainder = x % 10
            rev_num = rev_num * 10 + remainder

        if flag:
            return -rev_num

        return rev_num


class Solution2:
    def reverse(self, x: int) -> int:
        if x not in range(-9, 9):
            x = int(str(x)[::-1].lstrip('0')) if x >= 0 else int(f"-{str(x)[:0:-1]}".lstrip('0'))
        return x if (x < 2 ** 31 - 1 and x > -2 ** 31) else 0


if __name__ == '__main__':
    sol = Solution()
    sol2 = Solution2()

    x = 123

    print(sol.reverse(x=x))
    print(sol2.reverse(x=x))
