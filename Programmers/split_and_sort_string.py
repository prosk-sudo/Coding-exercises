def solution(myString):
    return sorted([s for s in myString.split("x") if s])


def main():
    myString1 = "axbxcxdx"
    myString2 = "dxccxbbbxaaaa"

    print(solution(myString1))
    print(solution(myString2))


if __name__ == "__main__":
    main()
