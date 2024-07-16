def solution(n):
    #    answer = []
    #    divisor_num = 1
    #    while divisor_num <= n // 2:
    #        if n % divisor_num == 0:
    #            answer.append(divisor_num)
    #        divisor_um += 1
    #    answer.append(n)
    #    return answer

    answer = [i for i in range(1, n + 1) if n % i == 0]
    return answer


def main():
    n1 = 24
    n2 = 29

    print(solution(n1))
    print(solution(n2))


if __name__ == "__main__":
    main()
