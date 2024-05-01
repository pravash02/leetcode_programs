class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        # Initialize a variable 'shift' to 0.
        shift = 0

        # While the left and right limits are not equal,
        while left < right:
            # Right shift the left limit by 1 bit.
            left >>= 1

            # Right shift the right limit by 1 bit.
            right >>= 1

            # Increment the 'shift' variable by 1.
            shift += 1

            print(left, right, shift)
        # Left shift the left limit by 'shift' bits and return the result.
        return left << shift


rbit = Solution()
print(rbit.rangeBitwiseAnd(left=5, right=7))
