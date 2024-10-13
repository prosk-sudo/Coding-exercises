class Solution:
    def hammingWeight(self, n: int) -> int:
        return bin(n)[2:].count('1')

if __name__ == "__main__":
    sol = Solution()

    print(sol.hammingWeight(11))
    print(sol.hammingWeight(128))
    print(sol.hammingWeight(2147483645))
