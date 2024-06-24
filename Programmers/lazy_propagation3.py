def solution(arr, queries):
    for query in queries:
        s, e, k = query
        first = (s + k - 1) // k**2
        for j in range(first, e + 1, k):
            arr[j] += 1
    return arr

def main():
    arr = [0, 1, 2, 4, 3]
    queries = [[0, 4, 1], [0, 3, 2], [0, 3, 3]]
    print(solution(arr, queries))   # [3, 2, 4, 6, 4]

if __name__ == "__main__":
    main()
