def solution(arr, intervals):
    answer = []
    for interval in intervals:
        answer.extend(arr[interval[0]:interval[1]+1])
    return answer

def main():
    arr_one, intervals_one = [1, 2, 3, 4, 5], [[1, 3], [0, 4]]

    print(solution(arr_one, intervals_one))

if __name__ == "__main__":
    main()
