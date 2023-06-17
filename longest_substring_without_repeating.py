# https://leetcode.com/problems/longest-substring-without-repeating-characters/


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        non_repeat = set({})
        count = 0
        max_len = 0
        for i in s:
            if i in non_repeat:
                count -= 1
                continue
            else:
                count += 1
                non_repeat.add(i)

            if count > max_len:
                max_len = count

        return max_len


class Solution2:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) <= 1:
            return len(s)
        maxs = 0
        for p1 in range(len(s)):
            arrays = []
            for p2 in range(p1, len(s)):
                if s[p2] not in arrays:
                    arrays.append(s[p2])
                    maxs = max(maxs, len(arrays))
                else:
                    break
        return maxs

        # d = {}
        # start = count = 0
        # for i in range(len(s)):
        #     if s[i] in d and start <= d[s[i]]:
        #         start = d[s[i]] + 1
        #     else:
        #         count = max(count, i - start + 1)
        #     d[s[i]] = i
        # return count


class Solution3(object):
    def lengthOfLongestSubstring(self, s):
        ss = ''                             #Empty Sub String for saving Char
        max_len = 0                  # max length substring
        i = 0                              # Starting point
        while i < len(s):
            if s[i] not in ss:          # Add char is not in sub string
                ss += s[i]
            else:
                ss = ss[ss.index(s[i])+1:] + s[i]      # Take substring from last found index of char + 1
            i += 1
            max_len = max(max_len, len(ss))     # Max length of substring
        return max_len


if __name__ == '__main__':
    sol = Solution()
    sol2 = Solution2()
    sol3 = Solution3()

    s = "abcabc"

    print(sol.lengthOfLongestSubstring(s=s))
    print(sol2.lengthOfLongestSubstring(s=s))
    print(sol3.lengthOfLongestSubstring(s=s))
