class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        i = 0
        length = len(nums)

        while i < length:
            if nums[i] == val:
                nums.pop(i)
                length -= 1
            else:
                i += 1

        return length

if __name__ == "__main__":
    sol = Solution()

    print(sol.removeElement([3, 2, 2, 3], 3)) # 2
    print(sol.removeElement([0, 1, 2, 2, 3, 0, 4, 2], 2)) # 5
