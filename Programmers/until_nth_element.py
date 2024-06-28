solution = lambda arr, n: arr[:n]

def main():
    num_list_one, n_one = [2, 1, 6], 1
    num_list_two, n_two = [5, 2, 1, 7, 5], 3

    print(solution(num_list_one, n_one))
    print(solution(num_list_two, n_two))

if __name__ == "__main__":
    main()
