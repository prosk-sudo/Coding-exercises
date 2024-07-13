def solution(my_string):
    return "".join(sorted(my_string.lower()))


def main():
    my_string1 = "Bcad"
    my_string2 = "heLLo"
    my_string3 = "Python"

    print(solution(my_string1))
    print(solution(my_string2))
    print(solution(my_string3))


if __name__ == "__main__":
    main()
