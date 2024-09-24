class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        return len(s.split()[-1])

if __name__ == "__main__":
    sol = Solution()

    print(sol.lengthOfLastWord("Hello World"))
    print(sol.lengthOfLastWord("   fly me   to   the moon  "))
    print(sol.lengthOfLastWord("luffy is still joyboy"))
