def solution(numbers, n):
    sum = 0
    for i in range(len(numbers)):
        sum += numbers[i]
        if sum > n:
            return sum
    return sum


def main():
    numbers1, n1 = [34, 5, 71, 29, 100, 34], 123
    numbers2, n2 = [58, 44, 27, 10, 100], 139

    print(solution(numbers1, n1))
    print(solution(numbers2, n2))


if __name__ == "__main__":
    main()
