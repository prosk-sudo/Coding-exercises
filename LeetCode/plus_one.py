class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        num = int(''.join(str(digit) for digit in digits)) + 1
        return [int(digit) for digit in str(num)]

if __name__ == "__main__":
    sol = Solution()

    print(sol.plusOne([1,2,3]))
    print(sol.plusOne([4,3,2,1]))
    print(sol.plusOne([9]))
