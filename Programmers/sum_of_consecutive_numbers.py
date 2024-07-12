def solution(num, total):
    #    answer = []
    #    if num % 2 == 1:
    #        for i in range((total // num) - (num // 2), (total // num) - (num // 2) + num):
    #            answer.append(i)
    #    else:
    #        for i in range(
    #            (total // num) - (num // 2) + 1, (total // num) - (num // 2) + num + 1
    #        ):
    #            answer.append(i)
    #    return answer

    return [(total - (num * (num - 1) // 2)) // num + i for i in range(num)]


def main():
    num1, total1 = 3, 12
    num2, total2 = 5, 15
    num3, total3 = 4, 14
    num4, total4 = 5, 5

    print(solution(num1, total1))
    print(solution(num2, total2))
    print(solution(num3, total3))
    print(solution(num4, total4))


if __name__ == "__main__":
    main()
