"""
The algorithm used in the code is to extract the least significant bit of the input integer n and add it to the result.
The result is then left-shifted by 1 bit and the input integer n is right-shifted by 1 bit.
This process is repeated for 32 bits.
"""


class Solution:
    def reverseBits(self, n: int) -> int:
        result = 0
        for _ in range(32):
            result = result << 1

            bit = n % 2
            result = result + bit

            n = n >> 1
        return result


revb = Solution()
print(revb.reverseBits(n=0o11111111111111111111111111111101))
