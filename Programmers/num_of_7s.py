def solution(array):
    #    num_string = "".join(str(num) for num in array)
    #    return num_string.count("7")

    return str(array).count("7")


def main():
    array1 = [7, 77, 17]
    array2 = [10, 29]

    print(solution(array1))
    print(solution(array2))


if __name__ == "__main__":
    main()
