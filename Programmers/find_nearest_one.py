def solution(arr, idx):
#    for i in range(idx, len(arr)):
#        if arr[i] == 1:
#            return i
#    return -1

    return next((i for i in range(idx, len(arr)) if arr[i] == 1), -1)

def main():
    arr_one, idx_one = [0, 0, 0, 1], 1
    arr_two, idx_two = [1, 0, 0, 1, 0, 0], 4
    arr_three, idx_three = [1, 1, 1, 1, 0], 3

    print(solution(arr_one, idx_one))
    print(solution(arr_two, idx_two))
    print(solution(arr_three, idx_three))

if __name__ == "__main__":
    main()
