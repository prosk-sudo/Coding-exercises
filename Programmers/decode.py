def solution(cipher, code):
    return cipher[code - 1 :: code]


def main():
    cipher1, code1 = "dfjardstddetckdaccccdegk", 4
    cipher2, code2 = "pfqallllabwaoclk", 2

    print(solution(cipher1, code1))
    print(solution(cipher2, code2))


if __name__ == "__main__":
    main()
