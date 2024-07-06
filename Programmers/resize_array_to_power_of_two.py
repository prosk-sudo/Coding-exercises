def solution(arr):
    min_power_of_two = 1
    while len(arr) > min_power_of_two:
        min_power_of_two *= 2
        #    for _ in range(min_power_of_two - len(arr)):
        #        arr.append(0)
        #    return arr

    return arr + [0] * (min_power_of_two - len(arr))


def main():
    arr1 = [1, 2, 3, 4, 5, 6]
    arr2 = [58, 172, 746, 89]

    print(solution(arr1))
    print(solution(arr2))


if __name__ == "__main__":
    main()
