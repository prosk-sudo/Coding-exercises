def solution(arr, queries):
    for i in range(len(queries)):
        temp = arr[queries[i][0]]
        arr[queries[i][0]] = arr[queries[i][1]]
        arr[queries[i][1]] = temp
    return arr

def main():
    arr = [0, 1, 2, 3, 4]
    queries = [[0, 3], [1, 2], [1, 4]]
    print(solution(arr, queries))

if __name__ == "__main__":
    main()

# result = [3, 4, 1, 0, 2]
