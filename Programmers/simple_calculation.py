def solution(binomial):
    return eval(binomial)


# solution=eval


def main():
    binomial1 = "43 + 12"
    binomial2 = "0 - 7777"
    binomial3 = "40000 * 40000"

    print(solution(binomial1))
    print(solution(binomial2))
    print(solution(binomial3))


if __name__ == "__main__":
    main()
