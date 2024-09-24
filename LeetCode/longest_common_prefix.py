class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        if not strs:
            return ""
        
        min_str = min(strs, key = len)
        for i, v in enumerate(min_str):
            for string in strs:
                if string[i] != v:
                    return min_str[:i]
        return min_str

if __name__ == "__main__":
    sol = Solution()

    case1 = ["flower", "flow", "flight"]
    print(sol.longestCommonPrefix(case1)) # "fl"

    case2 = ["dog", "racecar", "car"]
    print(sol.longestCommonPrefix(case2)) # ""
