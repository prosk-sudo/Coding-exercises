class Solution:
    def isPalindrome(self, s: str) -> bool:
        string = ''.join(i.lower() for i in s if i.isalnum())
        return string == string[::-1]

if __name__ == "__main__":
    sol = Solution()

    print(sol.isPalindrome("A man, a plan, a canal: Panama"))
    print(sol.isPalindrome("race a car"))
    print(sol.isPalindrome(" "))
