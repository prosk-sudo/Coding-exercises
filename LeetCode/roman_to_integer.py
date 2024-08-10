class Solution:
    def romanToInt(self, s: str) -> int:
        roman_dict = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }

        total = 0
        i = 0
        while i < len(s):
            current_num = roman_dict[s[i]]
            if i + 1 < len(s):
                next_num = roman_dict[s[i + 1]]
                if current_num >= next_num:
                    total += current_num
                else:
                    total -= current_num
            else:
                total += current_num
            i += 1

        return total

if __name__ == "__main__":
    sol = Solution()

    input1 = "III"
    print(f"Test case 1: {sol.romanToInt(input1)}")

    input2 = "LVIII"  
    print(f"Test case 2: {sol.romanToInt(input2)}")

    input3 = "MCMXCIV"
    print(f"Test case 3: {sol.romanToInt(input3)}")
