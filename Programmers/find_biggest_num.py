def solution(array):
    return [max(array), array.index(max(array))]


def main():
    array1 = [1, 8, 3]
    array2 = [9, 10, 11, 8]

    print(solution(array1))
    print(solution(array2))


if __name__ == "__main__":
    main()
