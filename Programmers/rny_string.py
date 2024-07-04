def solution(rny_string):
    return rny_string.replace("m", "rn")


def main():
    rny_string1 = "masterpiece"
    rny_string2 = "programmers"
    rny_string3 = "jerry"
    rny_string4 = "burn"

    print(solution(rny_string1))
    print(solution(rny_string2))
    print(solution(rny_string3))
    print(solution(rny_string4))


if __name__ == "__main__":
    main()
