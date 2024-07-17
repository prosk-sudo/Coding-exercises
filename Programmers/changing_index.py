def solution(my_string, num1, num2):
    #    answer = ""
    #    for i in range(len(my_string)):
    #        if i == num1:
    #            answer += my_string[num2]
    #        elif i == num2:
    #            answer += my_string[num1]
    #        else:
    #            answer += my_string[i]
    #    return answer

    s = list(my_string)
    s[num1], s[num2] = s[num2], s[num1]

    return "".join(s)


def main():
    my_string1_1, num1_1, num2_1 = "hello", 1, 2
    my_string1_2, num1_2, num2_2 = "I love you", 3, 6

    print(solution(my_string1_1, num1_1, num2_1))
    print(solution(my_string1_2, num1_2, num2_2))


if __name__ == "__main__":
    main()
