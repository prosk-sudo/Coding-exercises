def solution(arr, k):
    answer = []
    #    seen = set()
    #    for num in arr:
    #        if num not in seen:
    #            seen.add(num)
    #            answer.append(num)
    #        if len(answer) == k:
    #            break
    #
    #    while len(answer) < k:
    #        answer.append(-1)
    #
    #    return answer

    for num in arr:
        if num not in answer:
            answer.append(num)
        if len(answer) == k:
            break

    return answer + [-1] * (k - len(answer))


def main():
    arr1, k1 = [0, 1, 1, 2, 2, 3], 3
    arr2, k2 = [0, 1, 1, 1, 1], 4

    print(solution(arr1, k1))
    print(solution(arr2, k2))


if __name__ == "__main__":
    main()
