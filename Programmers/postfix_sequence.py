def solution(my_string):
#    answer = []
#
#    for i in range(len(my_string)):
#        answer.append(my_string[i:])
#    answer = sorted(answer)
#
#    return answer

    return sorted(my_string[i:] for i in range(len(my_string)))

def main():
    my_string_one = "banana"
    my_string_two = "programmers"

    print(solution(my_string_one))
    print(solution(my_string_two))

if __name__ == "__main__":
    main()
