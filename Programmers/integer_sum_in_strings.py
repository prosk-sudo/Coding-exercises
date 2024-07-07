def solution(num_str):
    #    return sum(int(num) for num in num_str)
    return sum(map(int, num_str))


def main():
    num_str1 = "123456789"
    num_str2 = "1000000"

    print(solution(num_str1))
    print(solution(num_str2))


if __name__ == "__main__":
    main()
