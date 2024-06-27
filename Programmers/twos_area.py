import time
start_time = time.time()

def solution(arr):
    #    try:
    #        min_idx = min(loc for loc, val in enumerate(arr) if val == 2)
    #        max_idx = max(loc for loc, val in enumerate(arr) if val == 2)
    #        return arr[min_idx:max_idx+1]
    #    except ValueError:
    #        return [-1]
    #    min_idx, max_idx = -1, -1

    min_idx, max_idx = -1, -1

    for i, val in enumerate(arr):
        if val == 2:
            if min_idx == -1:
                min_idx = i
            max_idx = i

    if min_idx == -1:
        return [-1]
    else:
        return arr[min_idx:max_idx + 1]

def main():
    arr_one = [1, 2, 1, 4, 5, 2, 9]
    arr_two = [1, 2, 1]
    arr_three = [1, 1, 1]
    arr_four = [1, 2, 1, 2, 1, 10, 2, 1]

    print(solution(arr_one))
    print(solution(arr_two))
    print(solution(arr_three))
    print(solution(arr_four))
    
    print("--- %s seconds ---" % (time.time() - start_time))

if __name__ == "__main__":
    main()

