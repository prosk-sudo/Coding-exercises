def solution(num_list, n):
    return num_list[::n]

def main():
    num_list_one, n_one = [4, 2, 6, 1, 7, 6], 2
    num_list_two, n_two = [4, 2, 6, 1, 7, 6], 4

    print(solution(num_list_one, n_one))
    print(solution(num_list_two, n_two))

if __name__ == "__main__":
    main()
