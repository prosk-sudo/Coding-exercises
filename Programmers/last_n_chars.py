def solution(my_string, n):
    return my_string[-n:]

def main():
    my_string_one = "ProgrammerS123"
    n_one = 11
    my_string_two = "He110W0r1d"
    n_two = 5

    print(solution(my_string_one, n_one))
    print(solution(my_string_two, n_two))

if __name__ == "__main__":
    main()
