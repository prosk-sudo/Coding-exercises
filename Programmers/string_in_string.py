def solution(str1, str2):
    return 1 if str2 in str1 else 2


def main():
    str1_1, str2_1 = "ab6CDE443fgh22iJKlmn1o", "6CD"
    str1_2, str2_2 = "ppprrrogrammers", "pppp"
    str1_3, str2_3 = "AbcAbcA", "AAA"

    print(solution(str1_1, str2_1))
    print(solution(str1_2, str2_2))
    print(solution(str1_3, str2_3))


if __name__ == "__main__":
    main()
