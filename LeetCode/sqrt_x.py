class Solution:
    def mySqrt(self, x: int) -> int:
        r = z = x
        while z and int(abs((r := (z + x / z) / 2) - z)):
            z = r
        return int(r) 

if __name__ == "__main__":
    sol = Solution()

    print(sol.mySqrt(4))
    print(sol.mySqrt(8))
