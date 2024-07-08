def solution(arr, delete_list):
    return [num for num in arr if num not in set(delete_list)]


def main():
    arr1, delete_list1 = [293, 1000, 395, 678, 94], [94, 777, 104, 1000, 1, 12]
    arr2, delete_list2 = [110, 66, 439, 785, 1], [377, 823, 119, 43]

    print(solution(arr1, delete_list1))
    print(solution(arr2, delete_list2))


if __name__ == "__main__":
    main()
