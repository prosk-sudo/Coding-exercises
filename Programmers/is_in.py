def solution(myString, pat):
    #    return 1 if pat.lower() in myString.lower() else 0

    return int(pat.lower() in myString.lower())


def main():
    myString1, pat1 = "AbCdEfG", "aBc"
    myString2, pat2 = "aaAA", "aaaaa"

    print(solution(myString1, pat1))
    print(solution(myString2, pat2))


if __name__ == "__main__":
    main()
