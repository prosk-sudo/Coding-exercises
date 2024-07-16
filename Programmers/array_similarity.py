def solution(s1, s2):
    #    answer = 0
    #    for elem in s1:
    #        if elem in s2:
    #            answer += 1
    #    return answer

    return len(set(s1) & set(s2))


def main():
    s1_1, s2_1 = ["a", "b", "c"], ["com", "b", "d", "p", "c"]
    s1_2, s2_2 = ["n", "omg"], ["m", "dot"]

    print(solution(s1_1, s2_1))
    print(solution(s1_2, s2_2))


if __name__ == "__main__":
    main()
