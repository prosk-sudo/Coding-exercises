def solution(str1, str2):
    return int(str1 in str2)


def main():
    str1_1, str2_1 = "abc", "aabcc"
    str1_2, str2_2 = "tbt", "tbbttb"

    print(solution(str1_1, str2_1))
    print(solution(str1_2, str2_2))


if __name__ == "__main__":
    main()
