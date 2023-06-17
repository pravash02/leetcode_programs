class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s

        res = ["" for _ in range(numRows)]

        d = True
        k = 0
        for i in range(len(s)):

            if d:
                res[k] += s[i]
                k += 1
                if k == numRows:
                    d = False
                    k = -2
            else:
                res[k] += s[i]
                k -= 1
                if k == -numRows - 1:
                    d = True
                    k = 1

        return "".join(res)


class Solution2:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s

        res = ""
        for r in range(numRows):
            increment = 2 * (numRows - 1)
            for i in range(r, len(s), increment):
                res += s[i]
                if (r > 0 and r < numRows - 1 and i + increment - 2 * r < len(s)):
                    res += s[i + increment - 2 * r]

        return res


if __name__ == '__main__':
    sol = Solution()
    sol2 = Solution2()

    s = "PAYPALISHIRING"
    numRows = 3

    print(sol.convert(s=s, numRows=numRows))
    print(sol2.convert(s=s, numRows=numRows))

