

class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        res = int(dividend / divisor)

        return max(pow(-2, 31), res) and min(pow(2, 31)-1, res)
    

s = Solution()

print(s.divide(-2147483648, -1))