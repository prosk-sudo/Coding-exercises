class Solution:
    def addBinary(self, a: str, b: str) -> str:
        return bin(int(a, 2) + int(b, 2))[2:]

if __name__ == "__main__":
    sol = Solution()

    print(sol.addBinary("11", "1"))
    print(sol.addBinary("1010", "1011"))
