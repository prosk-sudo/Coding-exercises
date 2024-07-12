def solution(A, B):
    #    for i in range(len(A)):
    #        temp = ""
    #        if temp.join(A[-i:] + A[:-i]) == B:
    #            return i
    #    return -1

    return (B * 2).find(A)


def main():
    A1, B1 = "hello", "ohell"
    A2, B2 = "apple", "elppa"
    A3, B3 = "atat", "tata"
    A4, B4 = "abc", "abc"

    print(solution(A1, B1))
    print(solution(A2, B2))
    print(solution(A3, B3))
    print(solution(A4, B4))


if __name__ == "__main__":
    main()
