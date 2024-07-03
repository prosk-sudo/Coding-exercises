def solution(myString, pat):
    return myString[: myString.rfind(pat) + len(pat)]


def main():
    myString1, pat1 = "AbCdEFG", "dE"
    myString2, pat2 = "AAAAaaaa", "a"

    print(solution(myString1, pat1))
    print(solution(myString2, pat2))


if __name__ == "__main__":
    main()
