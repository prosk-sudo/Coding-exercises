def solution(my_string, alp):
    return "".join(v.upper() if v == alp else v for v in my_string)


def main():
    my_string1, alp1 = "programmers", "p"
    my_string2, alp2 = "lowercase", "x"

    print(solution(my_string1, alp1))
    print(solution(my_string2, alp2))


if __name__ == "__main__":
    main()
