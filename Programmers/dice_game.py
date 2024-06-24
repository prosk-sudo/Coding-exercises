def solution(a, b, c, d):
    answer = 0
    numbers_list = [a, b, c, d]
    numbers_set = {a, b, c, d}

    if len(numbers_set) == 1:
        answer += 1111*a


    elif len(numbers_set) == 4:
        answer += min(numbers_set))

    return answer

def main():
    a_1, b_1, c_1, d_1 = 2, 2, 2, 2
    a_2, b_2, c_2, d_2 = 4, 1, 4, 4
    a_3, b_3, c_3, d_3 = 6, 3, 3, 6
    a_4, b_4, c_4, d_4 = 2, 5, 2, 6
    a_5, b_5, c_5, d_5 = 6, 4, 2, 5

    print(solution(a_1, b_1, c_1, d_1))
    print(solution(a_2, b_2, c_2, d_2))
    print(solution(a_3, b_3, c_3, d_3))
    print(solution(a_4, b_4, c_4, d_4))
    print(solution(a_5, b_5, c_5, d_5))

if __name__ == "__main__":
    main()
