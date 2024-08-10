class Solution:
    def isPalindrome(self, x: int) -> bool:
        #        original_num = x
        #        reversed_num = 0
        #
        #        if x < 0:
        #            return False
        #
        #        while x > 0:
        #            digit = x % 10
        #            reversed_num = reversed_num * 10 + digit
        #            x //= 10
        #
        #        return original_num == reversed_num
        if x < 0:
            return False
        return str(x) == str(x)[::-1]

if __name__ == "__main__":
    sol = Solution()

    input1 = 121
    print(f"Test case 1: {sol.isPalindrome(input1)}")

    input2 = -121
    print(f"Test case 2: {sol.isPalindrome(input2)}")

    input3 = 10
    print(f"Test case 3: {sol.isPalindrome(input3)}")
