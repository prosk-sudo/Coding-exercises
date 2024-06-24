def solution(arr, queries):
    answer = []
    for s, e, k in queries:
        min_value = 10**6
        for i in range(s, e+1):
            if k < arr[i] < min_value:
                min_value = arr[i]
        if min_value == 10**6:
            answer.append(-1)
        else:
            answer.append(min_value)
    return answer

def main():
    arr = [0, 1, 2, 4, 3]
    queries = [[0, 4, 2], [0, 3, 2], [0, 2, 2]]
    print(solution(arr, queries))

if __name__ == "__main__":
    main()

# result = [3, 4, -1]
