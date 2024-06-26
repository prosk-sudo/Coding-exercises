def main():
    n, m = map(int, input().split())
    nr_of_solutions = 0

    for i in range(1000):
        for j in range(1000):
            if i**2 + j == n and i + j**2 == m:
                #                print(f"({i}, {j})")
                nr_of_solutions += 1
    print(nr_of_solutions)


if __name__ == "__main__":
    main()
