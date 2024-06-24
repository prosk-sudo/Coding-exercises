def solution(my_string, index_list):
    answer = ''
    return answer.join(my_string[num] for num in index_list)

def main():
    my_string_one = "cvsgiorszzzmrpaqpe"
    index_list_one = [16, 6, 5, 3, 12, 14, 11, 11, 17, 12, 7]

    my_string_two = "zpiaz"
    index_list_two = [1, 2, 0, 0, 3]

    print(solution(my_string_one, index_list_one))
    print(solution(my_string_two, index_list_two))

if __name__ == "__main__":
    main()


