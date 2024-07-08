def solution(my_string, target):
    return int(target in my_string)


def main():
    my_string1, target1 = "banana", "ana"
    my_string2, target2 = "banana", "wxyz"

    print(solution(my_string1, target1))
    print(solution(my_string2, target2))


if __name__ == "__main__":
    main()
