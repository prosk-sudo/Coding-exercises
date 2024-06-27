def solution(n, slicer, num_list):
    a, b, c = slicer[0], slicer[1], slicer[2]

    if n == 1:
        return num_list[:b+1]
    elif n == 2:
        return num_list[a:]
    elif n == 3:
        return num_list[a:b+1]
    else:
        return num_list[a:b+1:c]

def main():
    n_one, slicer_one, num_list_one = 3, [1, 5, 2], [1, 2, 3, 4, 5, 6, 7, 8, 9]
    n_two, slicer_two, num_list_two = 4, [1, 5, 2], [1, 2, 3, 4, 5, 6, 7, 8, 9]

    print(solution(n_one, slicer_one, num_list_one))
    print(solution(n_two, slicer_two, num_list_two))

if __name__ == "__main__":
    main()
