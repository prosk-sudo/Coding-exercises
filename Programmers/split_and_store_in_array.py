def solution(my_str, n):
    return [my_str[i : i + n] for i in range(0, len(my_str), n)]


def main():
    my_str1, n1 = "abc1Addfggg4556b", 6
    my_str2, n2 = "abcdef123", 3

    print(solution(my_str1, n1))
    print(solution(my_str2, n2))


if __name__ == "__main__":
    main()
