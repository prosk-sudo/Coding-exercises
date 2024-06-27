def solution(arr, query):
    for i, v in enumerate(query):
        if i % 2 == 0:
            arr = arr[:v+1]
        else:
            arr = arr[v:]
    return arr

def main():
    arr_one, query_one = [0, 1, 2, 3, 4, 5], [4, 1, 2]

    print(solution(arr_one, query_one))

if __name__ == "__main__":
    main()
