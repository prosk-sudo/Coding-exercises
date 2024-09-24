class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        if n == 2:
            return 2
        
        num1, num2 = 1, 2

        for i in range(3, n + 1):
            tmp = num1 + num2
            num1 = num2
            num2 = tmp

        return num2

if __name__ == "__main__":
    sol = Solution()

    print(sol.climbStairs(2))
    print(sol.climbStairs(3))
    print(sol.climbStairs(44))
