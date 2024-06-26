def solution(my_string, indices):
    lst = list(my_string)
    for index in indices:
        lst.pop(index)
        lst.insert(index, "")

    return ''.join(lst)

def main():
    my_string_one, indices_one = "apporoograpemmemprs", [1, 16, 6, 15, 0, 10, 11, 3]

    print(solution(my_string_one, indices_one))

if __name__ == "__main__":
    main()
