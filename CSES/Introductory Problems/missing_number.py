def main():
    upper_limit = int(input())
    num_set = set(range(1, upper_limit+1))
    for num in input().split():
        num_set.remove(int(num))
    print(str(num_set)[1:len(str(num_set))-1])

if __name__ == "__main__":
    main()
