class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        d = {}
        for num in nums:
            if num in d:
                d[num] += 1
            else:
                d[num] = 1
        for key, value in d.items():
            if value == 1:
                return key

if __name__ == "__main__":
    sol = Solution()

    print(sol.singleNumber([2,2,1]))
    print(sol.singleNumber([4,1,2,1,2]))
    print(sol.singleNumber([1]))
