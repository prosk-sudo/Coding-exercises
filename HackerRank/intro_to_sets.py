def average(array):
    return sum(array) / len(array)

if __name__ == '__main__':
    n = int(input())
    arr = list(set(map(int, input().split())))
    result = average(arr)
    print(result)