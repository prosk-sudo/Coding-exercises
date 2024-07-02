def solution(strArr):
    #    for i in range(len(strArr)):
    #        if i % 2 == 1:
    #            strArr[i] = strArr[i].upper()
    #        else:
    #            strArr[i] = strArr[i].lower()
    #
    #    return strArr

    return [v.lower() if i % 2 == 0 else v.upper() for i, v in enumerate(strArr)]


def main():
    strArr1 = ["AAA", "BBB", "CCC", "DDD"]
    strArr2 = ["aBc", "AbC"]

    print(solution(strArr1))
    print(solution(strArr2))


if __name__ == "__main__":
    main()
