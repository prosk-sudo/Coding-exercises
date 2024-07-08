def solution(a, b):
    #    return str(int(a) + int(b))
    return str(eval(a + "+" + b))


def main():
    a1, b1 = "582", "734"
    a2, b2 = "18446744073709551615", "28734650280479981"
    a3, b3 = "0", "0"

    print(solution(a1, b1))
    print(solution(a2, b2))
    print(solution(a3, b3))


if __name__ == "__main__":
    main()
