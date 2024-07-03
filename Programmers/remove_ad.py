def solution(strArr):
    #    for string in strArr:
    #        if "ad" in string:
    #            strArr.remove(string)
    #    return strArr

    return [string for string in strArr if "ad" not in string]


def main():
    strArr1 = ["and", "notad", "abcd"]
    strArr2 = ["there", "are", "no", "a", "ds"]

    print(solution(strArr1))
    print(solution(strArr2))


if __name__ == "__main__":
    main()
