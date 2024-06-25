def solution(my_string, queries):
    for start, end in queries:
        my_string = my_string[:start] + my_string[start:end+1][::-1] + my_string[end+1:]
    return my_string

def main():
    my_string_one = "rermgorpsam"
    queries_one = [[2, 3], [0, 7], [5, 9], [6, 10]]

    print(solution(my_string_one, queries_one))     # "programmers"

if __name__ == "__main__":
    main()
