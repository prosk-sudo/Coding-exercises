def solution(num_list, n):
    return num_list[n-1:]

def main():
    num_list_one, n_one = [2, 1, 6], 3
    num_list_two, n_two = [5, 2, 1, 7, 5], 2

    print(solution(num_list_one, n_one))
    print(solution(num_list_two, n_two))

if __name__ == "__main__":
    main()
