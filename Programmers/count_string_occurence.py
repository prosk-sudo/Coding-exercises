def solution(myString, pat):
    #    answer = 0
    #
    #    for i in range(len(myString) - len(pat) + 1):
    #        sub_count = 0
    #        for j in range(len(pat)):
    #            if myString[i + j] == pat[j]:
    #                sub_count += 1
    #            else:
    #                break
    #        if sub_count == len(pat):
    #            answer += 1
    #    return answer

    answer = 0

    for i in range(len(myString)):
        if myString[i:].startswith(pat):
            answer += 1
    return answer


def main():
    myString1, pat1 = "banana", "ana"
    myString2, pat2 = "aaaa", "aa"

    print(solution(myString1, pat1))
    print(solution(myString2, pat2))


if __name__ == "__main__":
    main()
