import math


class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        elif n == 1:
            return x
        elif n > 0:
            if n % 2 == 0:
                return self.myPow(x*x, n // 2)
            else:
                return x * self.myPow(x, n - 1)
        else:
            return 1 / self.myPow(x, -n)


assert math.isclose(Solution().myPow(2, 10),  1024.00)
assert math.isclose(Solution().myPow(2.100, 3),  9.261)
assert math.isclose(Solution().myPow(2.00, -2),  0.25)
print(Solution().myPow(34.00515, -3))
assert math.isclose(Solution().myPow(34.00515, -3),  3e-05)


