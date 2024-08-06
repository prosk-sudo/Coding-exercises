class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        #        answer = []
        #        for i in range(len(nums)):
        #            for j in range(i+1, len(nums)):
        #                if nums[i] + nums[j] == target:
        #                    answer.append(i)
        #                    answer.append(j)
        #        return answer
        table = {}

        for i, num in enumerate(nums):
            complement = target - num
            if complement in table:
                return [table[complement], i]
            else:
                table[num] = i

if __name__ == "__main__":
    sol = Solution()

    num1 = [2, 7, 11, 15]
    target1 = 9
    print(f"Test case 1: {sol.twoSum(num1, target1)}")

    num2 = [3, 2, 4]
    target2 = 6
    print(f"Test case 2: {sol.twoSum(num2, target2)}")

    num3 = [3, 3]
    target3 = 6
    print(f"Test case 3: {sol.twoSum(num3, target3)}")
